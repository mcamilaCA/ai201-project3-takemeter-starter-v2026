# TakeMeter

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first** — setup, the
> notebook, the baseline, and what to do when something breaks.
>
> Once `python test.py` passes:
>
> ```bash
> head -5 data/practice_labels.csv     # the shape your labels.csv needs
> ```
>
> Then open `takemeter.ipynb` **in this folder** — in VS Code, or with
> `jupyter notebook` if you prefer. Pick the kernel: the `.venv` inside this
> project. Run section 1, which reports the hardware you'll be training on.
> Everything else waits until you have data.
>
> Nothing to upload, nothing to connect, no accounts and no keys. The notebook
> runs on your machine and writes next to your code.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     HOW TO USE THIS FILE

     Unit 5 asks for the first five sections. Unit 6 adds the five below them.

     Everything is pasted as TEXT. No screenshots, no images.

     ⚠️ The confusion matrix especially. The notebook prints one as a markdown
     table, ready to copy. A screenshot of a matrix earns nothing. Paste the
     table.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 5 — THE BUILD ═══════════════════════ -->

## What This Does

<!-- Your community, and what your classifier sorts posts into. Three or four
     sentences. -->



---

## Label Taxonomy

<!-- Each label: a one-sentence definition and two real examples from your
     reading. Then your decision rule for the hardest boundary.

     The decision rule is worth a point on its own and it's the thing most
     people leave out. Every taxonomy has a hardest boundary. Name yours. -->

### `template`

**Definition:**
The post is a bot output or a list of links with no human writing
**Example 1:**
> "By: Norman Mailer | 721 pages | Published: 1948 | Popular Shelves: fiction, classics, war, historical-fiction, rory-gilmore-reading-challenge | )[^(Search "The Naked and the Dead by Norman Mailer")](https://www.goodreads.com/search?q=The Naked and the Dead by Norman Mailer&search_type=books"

**Example 2:**
> "By: A.C. Grayling | ? pages | Published: 2019 | Popular Shelves: philosophy, history, non-fiction, nonfiction, owned"

### `book_centered`

**Definition:**
The text is mainly about a specific book or author, either what the post writer liked or as a recomendation
**Example 1:**
> "Just finished reading “chaos walking” and I am left in a void"

**Example 2:**
> "Paranormal Mystery Books like Ninth House by Leigh Bardugo"

### `personal`

**Definition:**
The text is mainly about the writer's situations, age or feelings, names no specific book. 

**Example 1:**
> "I am 17 and I am terrified of growing up"

**Example 2:**
> "Book suggestions for someone who has a horrible relationship with their family"

### `bare_ask`

**Definition:**
Generic request or reply with no named book, no personal story, and no bot formatting.

**Example 1:**
> "Looking for books with a chill summertime vibe"

**Example 2:**
> "Not sure what I’m looking for"

### The hardest boundary

**Which two labels:**  Book centered and Personal.
**Reason:** They are not mutually exclusive, a post can give information about the writer and to mention a book they like, identify with, or don't like. 
**Example:**  "I'm 17, I just finished Divergent, and I'm scared of growing up. What should I read next?"

**The decision rule I used every time:**
<!-- e.g. "If the post names a specific checkable fact, it's `analysis`, even
     if the tone is heated." -->
If the post mentions a specific book or author, it is book_centered, regardless of it providing personal information or not. Which is why personal is defined as The text is mainly about the writer's situations, age or feelings, names *no specific book*. 


---

## The Dataset

<!-- Where you collected from, how you labelled, your counts, and three hard
     cases. -->

**Where the posts came from:** Kaggle 

**How I labelled them:** <!-- Cold first? Pre-labelled with AI and corrected?
Say so plainly — the disclosure is required, not penalised. -->
I labeled the first 30 to 40 and then AI finished the job. 

**Counts per label:**

|      Label    | Count | Share |
|---------------|-------|-------|
| book_centered |   84  | 46.7% |
|    template   |   37  | 20.6% |
|    personal   |   34  | 18.9% |
|    bare_ask   |   25  | 13.9% |
| **Total**     |  180  |  100% |

**Three hard cases**

<!-- Any post that made you pause: what it was, which two labels it could have
     been, and what you chose. These are worth more than the easy 190. -->

**1.**
> *The post:*
>
> *Could have been:*
>
> *I chose, because:*

**2.**
> *The post:*
>
> *Could have been:*
>
> *I chose, because:*

**3.**
> *The post:*
>
> *Could have been:*
>
> *I chose, because:*

---

## The Training Run

<!-- Your starting model, your settings, and anything you changed and why. -->

**Base model:**

**Settings:** <!-- epochs, learning rate, batch size, seed -->

**Anything I changed from the defaults, and why:**

**Split sizes:** <!-- train / val / test, and per-label counts in the test
split. If a label had fewer than about 8 in test, say so — it explains a lot
of next unit's variance. -->



---

## How I Used AI

<!-- Two specific moments — what you asked, what came back, what you changed.

     ⚠️ Plus disclosure of any pre-labelling. If you had a model pre-label a
     batch and then read and corrected every one, say that. It's an allowed
     workflow and disclosing it costs you nothing. Not disclosing it is the
     problem. -->

**Moment 1**

- *What I asked for:*
- *What came back:*
- *What I changed:*

**Moment 2**

- *What I asked for:*
- *What came back:*
- *What I changed:*

**Pre-labelling disclosure:**

<!-- ═══════════════════════ UNIT 6 — THE TEST ═══════════════════════

     Don't fill these in during unit 5.
     ═══════════════════════════════════════════════════════════════════ -->

---

## Baseline vs. Trained

<!-- Both models on the same posts. `python baseline.py --trained results.json`
     prints this table for you. -->

| Measure | Baseline | Trained | Difference |
|---|---|---|---|
| Overall accuracy |  |  |  |
| Macro F1 |  |  |  |
| F1 — `label_one` |  |  |  |
| F1 — `label_two` |  |  |  |

**What I predicted before I looked:**
<!-- Milestone 1 asks you to write this BEFORE seeing the trained numbers. A
     prediction made afterwards isn't one. -->

**What the gap actually means:**
<!-- If the baseline matched your trained model, your fine-tuning added
     nothing — and that is a real finding, not a failure. Say it plainly. -->



---

## Run Log — Before

<!-- Five criteria across three seeds. The notebook's section 6 prints the
     spread table; the Target and Verdict columns are yours. -->

| Criterion | Target | Seed 42 | Seed 7 | Seed 2024 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

### Confusion matrix

<!-- ⚠️ TYPED AS A MARKDOWN TABLE. The notebook prints one ready to paste.
     An image of a matrix earns nothing. -->

| true \ predicted |  |  |  |
|---|---|---|---|
| **** |  |  |  |
| **** |  |  |  |
| **** |  |  |  |

**My biggest off-diagonal number, and what it means:**
<!-- Not "the model made mistakes" — WHICH boundary it didn't learn, and which
     direction. "7 real analysis posts were called hot_take and only 3 went the
     other way" is a direction, not just an error rate. -->



---

## Verdicts and Diagnoses

<!-- MET or MISSED against LAST UNIT's target. The target has to hold across
     all three seeds, not turn up sometimes. -->

| # | Criterion | Target | Verdict | How I decided |
|---|---|---|---|---|
| 1 |  |  |  |  |
| 2 |  |  |  |  |
| 3 |  |  |  |  |
| 4 |  |  |  |  |
| 5 |  |  |  |  |

**Diagnoses**

<!-- For each miss: the cause, and how you know. The four common causes are:
     too few examples for a label, a boundary you applied inconsistently, a
     genuinely hard label pair, and a task the model can't reach from this
     much data.

     ⚠️ Use your agreement report as evidence. It is the only instrument you
     have that can tell a LABELLING problem from a MODEL problem, and this
     section is graded on whether you used it that way. -->



---

## Agreement Report

<!-- Your rate against the staff set, and every disagreement adjudicated.

     Remember you labelled these 30 under the STAFF taxonomy in
     data/staff_taxonomy.md, not your own — so every argument below is made
     from those definitions and those decision rules. -->

**Agreement rate:** ___ / 30 = ___%

<!-- Nobody grades this number. A 60% who argues every disagreement from the
     stated rules beats a 95% who wrote "staff was right" nine times. Several
     of the 30 were chosen because they're genuinely ambiguous — you should be
     winning some of these. -->

**Disagreements**

<!-- Three lines each: the post, both labels, and who you think is right and
     why — grounded in the staff definitions you were both applying.

     Then sort each into one of three piles:
       (a) the rule covered it and I applied it loosely → a consistency problem
       (b) the rule genuinely doesn't say               → a gap in the definitions
       (c) the rule is ambiguous here and my reading is defensible → argue it.
           This is a legitimate win.

     Pile (a) is the one that matters most for your diagnosis: if you applied a
     written rule two different ways on 30 posts, that is direct evidence about
     what you did across your own 200. -->

**1.**
> *The post:*
>
> *Staff said / I said:*
>
> *My call, and why:*
>
> *Which pile:*

**2.**
> *The post:*
>
> *Staff said / I said:*
>
> *My call, and why:*
>
> *Which pile:*

**What the pattern in my disagreements tells me:**



---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Run Log — After

| Criterion | Target | Seed 42 | Seed 7 | Seed 2024 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

**Did it help, and how do I know:**

<!-- If it didn't, say so. Relabelling that didn't help is a genuinely
     interesting result and earns full credit. -->



---

## What's Still Broken

<!-- For each criterion still missed: what you'd do, and why you stopped. -->



**The gap between what I meant my labels to capture and what the model
learned:**
<!-- Two sentences. Your confusion matrix is the evidence. -->



<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 5

       [ ] criteria.md has five numbered criteria, each naming a NUMBER
       [ ] Each has a reason underneath tied to your data or taxonomy
       [ ] labels.csv: at least 150 rows, text/label/note, ONE file not split
       [ ] No label above 70%
       [ ] All five unit 5 sections have real content
       [ ] Label Taxonomy includes the decision rule for your hardest boundary
       [ ] The Dataset includes three hard cases
       [ ] results.json and test_split.csv committed (the notebook does this)
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 6

       [ ] Baseline vs. Trained table, with your prediction written beforehand
       [ ] Run Log — Before, five criteria across three seeds
       [ ] Confusion matrix TYPED AS A MARKDOWN TABLE
       [ ] A verdict on every criterion
       [ ] A diagnosis for every miss, using the agreement report as evidence
       [ ] Agreement Report with every disagreement adjudicated
       [ ] One improvement, with Run Log — After
       [ ] What's Still Broken
       [ ] results_three_seeds_before.json, results_three_seeds_after.json,
           baseline_results.json and
           agreement_results.json committed
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**

# Miscelaneous
```
AI201 environment check
------------------------------------------------------------
[PASS] Python version
         3.13.13 on Darwin
[PASS] Virtual environment
         /Users/camila/ai201-project3-takemeter-starter-v2026/.venv
[PASS] Pinned packages
         all 6 import cleanly
[PASS] Free disk space
         181.0 GB
[PASS] Memory
         16.0 GB
[PASS] PyTorch
         2.14.1, Apple Silicon GPU (MPS) — training will use it
[PASS] Training packages
         datasets and accelerate both import
[PASS] Transformers
         imports cleanly
[WARN] Baseline model
         Not downloaded yet (~1.6 GB). It downloads on your first run of
         baseline.py. Do that BEFORE the unit 6 session, not during it.
[PASS] Project files
         notebook, scripts and practice data all present
------------------------------------------------------------
```

## Hard cases (working notes)

Row numbers are the position in `labels_template.csv` (1 = first row after the header, 180 rows). Rows 1-30 are `cold`, rows 31-180 are `pre-label`. Tie-break order used throughout: `template` > `book_centered` > `personal` > `bare_ask`.

**1. Names a book AND tells a personal story** (`book_centered` vs `personal`)
- Row 70: grief after losing a baby, with favorite reads listed. Row 77: just moved to Maryland, has read *Chesapeake Requiem*.
- Chose `book_centered`: the rule is "names a specific book or author -> `book_centered`", however personal the rest is.

**2. My cold labels vs. the rule** (`book_centered` vs `personal`, `personal` vs `bare_ask`)
- Row 2, "I'm 17 and I don't want to be old": cold label `book_centered`, but it names no book, so the rule gives `personal`.
- Row 4, "chill summertime vibe... Life is Strange": cold label `personal`, but *Life is Strange* is a game and the post gives no facts about the writer, so the rule gives `bare_ask`.
- Both kept as my cold labels. Worth deciding whether the rule or the label should change.

**3. Books named only as exclusions** (`book_centered` vs `bare_ask`)
- Row 30 (early Christianity, "not looking for Augustine, Origen") and row 55 (female friendships, "except Sisterhood of the Travelling Pants").
- Chose `bare_ask`: the books are named as things the writer does not want, not as something they read or liked.

**4. A title that only shows up late in a long post** (`bare_ask` vs `book_centered`)
- Row 24 opens as a generic request for a friendship book, but the last sentence asks for something "like The People We Meet on Vacation and/or Eleanor Oliphant is Completely Fine".
- Chose `book_centered`. Reading only the start of the post would have given `bare_ask`.

**5. Movies, shows and games instead of books** (`book_centered` vs `bare_ask`)
- Rows 41 (*Body of Lies*), 51 (Rick and Morty), 88 (*Moxie*, which is also a book) and 145 (Avatar).
- Chose `bare_ask`: no book or author is named.

**6. "Help me find this book" with no title** (`bare_ask` vs `personal`)
- Rows 33 and 135 describe a half-remembered plot but give no title.
- Chose `bare_ask`.

**7. Comments about a book that is never named** (`bare_ask` vs `personal`)
- Row 95 (discussing a plot and characters, no title): `bare_ask`. Row 84 ("I've always been kind of an outsider socially"): `personal`.
- Decided by whether the writer states a fact about themselves.

**8. Lists of links with no writing** (`template` vs `book_centered`)
- Row 19 is only Amazon links. Chose `template`, as "a list of links with no human writing". Row 92, the subreddit's automatic removal message, is also `template` because it is bot output.

**9. Gift requests** (`personal` vs `bare_ask`)
- Rows 10, 16, 44 and 63 ask for a gift or a shared read and give concrete details about the other person. Chose `personal`.

**10. Taste only, no facts about the writer** (`personal` vs `bare_ask`)
- Row 26 (genres, "bored with what I'm reading") and row 98 (preference for math/science). Chose `bare_ask`.

**Label balance:** 84 `book_centered` (46.7%), 37 `template` (20.6%), 34 `personal` (18.9%), 25 `bare_ask` (13.9%). All four are inside criterion 2's 10-50% range. The 20 extra `template` rows (161-180) are Goodreads-bot comments added by `rebalance.py`, and 40 `book_centered` rows were dropped by it, so the shares reflect that rebalancing and not the raw forum.

## Labels Training:
[note] 'template' has only 6 examples in the test split.
[note] 'personal' has only 5 examples in the test split.
[note] 'bare_ask' has only 4 examples in the test split.