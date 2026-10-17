"""Rebalance labels_template.csv so no label is >50% or <10%.

Adds bot-style (template) rows from the full reddit pool and drops
book_centered rows that mention a specific book title. Dry run by default;
writes data/labels_balanced.csv and never touches labels_template.csv.

    python3 rebalance.py            # preview + write data/labels_balanced.csv
    python3 rebalance.py --add 50 --drop 40 --seed 42
"""
import argparse
import pandas as pd

ap = argparse.ArgumentParser()
ap.add_argument("--add", type=int, default=50, help="template rows to add")
ap.add_argument("--drop", type=int, default=40, help="book_centered rows to drop")
ap.add_argument("--seed", type=int, default=42)
args = ap.parse_args()

df = pd.read_csv("labels_template.csv")
pool = pd.read_csv("data/reddit_booksuggestions.csv")

# --- 1. template candidates: Goodreads-bot / automod comments not already used
bot = r"^\[\*\*.+\]\(https://www\.goodreads\.com/book|^Your submission has been automatically removed"
cand = pool[pool.body.fillna("").str.strip().str.contains(bot)].copy()
cand["text"] = cand.body.str.strip()
cand = cand.drop_duplicates("text")
cand = cand[~cand.text.isin(df.text.str.strip())]
cand = cand[cand.text.str.len() >= 200]  # same length floor as data_cleaning
add = cand.sample(n=min(args.add, len(cand)), random_state=args.seed)
new = pd.DataFrame({"text": add.text, "label": "template", "note": "added-bot"})
print(f"template candidates available: {len(cand)}, adding {len(new)}")

# --- 2. book_centered rows to drop: ones that name a specific book/link
# Hand-labelled ("cold") rows are kept.
title_hint = (r"goodreads\.com|amazon\.com|\"[A-Z][^\"]{3,60}\"|“[^”]+”"
              r"|\bby [A-Z][a-z]+ [A-Z][a-z]+|\*[A-Z][^*]{3,60}\*")
bc = df[(df.label == "book_centered") & (df.note != "cold")]
hinted = bc[bc.text.str.contains(title_hint)]
rest = bc.drop(hinted.index)
print(f"book_centered with a title hint: {len(hinted)}; others: {len(rest)}")
drop_idx = hinted.sample(n=min(args.drop, len(hinted)), random_state=args.seed).index
short = args.drop - len(drop_idx)
if short > 0:  # top up with the shortest remaining (least informative)
    drop_idx = drop_idx.append(rest.assign(n=rest.text.str.len()).nsmallest(short, "n").index)
out = pd.concat([df.drop(drop_idx), new], ignore_index=True)

def report(d, name):
    s = d.label.value_counts()
    print(f"\n{name} (n={len(d)})")
    for l, c in s.items():
        flag = "" if 0.10 <= c / len(d) <= 0.50 else "  <-- OUT OF RANGE"
        print(f"  {l:14s}{c:4d}  {100*c/len(d):5.1f}%{flag}")

report(df, "before")
report(out, "after")
print("\nDropped rows (preview):")
for i in drop_idx:
    print("  -", df.text[i][:90].replace("\n", " "))
out.to_csv("data/labels.csv", index=False)
print("\nwrote data/labels.csv")
