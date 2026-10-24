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

TakeMeter looks at posts from an online book-recommendation forum (a Reddit-style community where people ask for something to read next), collected from a Kaggle dataset. Each post is sorted into one of four labels based on what the writer actually gives the community to work with: `template` (bot output or a bare list of links with no human writing), `book_centered` (names a specific book or author), `personal` (shares details about the writer's life, age or feelings but names no book), and `bare_ask` (a generic request with no book, no personal story and no bot formatting). The point is to tell how much usable context a request carries, so that a moderator or recommender could separate bot noise and vague asks from posts that are easy to answer.



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

### Stretch feature: a fourth label (`bare_ask`)

The core taxonomy needs three labels (`template`, `book_centered`, `personal`). As a stretch, I added `bare_ask` as a fourth: a generic request or reply with no named book, no personal story and no bot formatting. It catches posts the other three cannot hold, such as "Looking for books with a chill summertime vibe", taste-only requests, and "help me find this book" posts with no title.

Adding it made the task harder in three ways:
- It adds boundaries with the other labels: `bare_ask` vs `personal` (gift requests count as `personal` when they give concrete details about the other person, taste alone stays `bare_ask`) and `bare_ask` vs `book_centered` (books named only as exclusions, or movies, shows and games instead of books, stay `bare_ask`).
- It is the smallest class: 25 of 180 posts (13.9%), with only 4 examples in the test split, so its scores will vary a lot between runs.
- The tie-break order for ambiguous posts is `template` > `book_centered` > `personal` > `bare_ask`, so `bare_ask` is the fallback when nothing else applies.


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
> *The post:* "Looking book I won't be able put down, during a process of grief... We lost our baby in a way that took a part of us with it. I now have a 4-6 week physical recovery time line... Some of my recent favorite reads this past year would [be] Educated, The boy who followed his father into the auschwitz, Secret sisters... I have just dove into Elenaor Oliphant is completely fine" (row 70; row 77, someone who just moved to Maryland and has read *Chesapeake Requiem*, is the same kind of case)
>
> *Could have been:* `personal` or `book_centered`
>
> *I chose `book_centered`, because:* the post names specific books, and my decision rule says that any post naming a specific book or author is `book_centered`, however personal the rest of it is.

**2.**
> *The post:* "Books on Early Christianity... I'm not looking for Augustine, Origen, or other direct sources but easy to read historical books written by modern contemporaries." (row 30; row 55, which asks for books about female friendships "except Sisterhood of the Travelling Pants", is similar)
>
> *Could have been:* `book_centered` or `bare_ask`
>
> *I chose `bare_ask`, because:* the authors are named only as things the writer does not want, not as something they read or liked, so the post is really a generic request.

**3.**
> *The post:* "I am looking for a book I read long ago that's on the tip of my tongue... a young teenage girl who works for a corporation that hunts ghost. The girl also uses a rapier... the characters go to a mansion that is haunted by a ghost, and eventually destroy him." (row 33; row 135 is similar)
>
> *Could have been:* `bare_ask` or `personal`
>
> *I chose `bare_ask`, because:* the writer gives a plot description but no title, author or facts about themselves, so the post is a request with nothing named.

---

## The Training Run

<!-- Your starting model, your settings, and anything you changed and why. -->

**Base model:** distilbert-base-uncased

**Settings:** epochs: 3, learning rate: 0.00002, batch size: 16, seed: 42

**Anything I changed from the defaults, and why:**

**Split sizes:** 70% train, 15% validation, 15% test.
Labels with less than 8 labels
- 'template' has only 6 examples in the test split.
- 'personal' has only 5 examples in the test split.
- 'bare_ask' has only 4 examples in the test split.

After adding another 30 'template' posts to complete the 50 stretch mark.

## Stretch Feature:
Added 50 posts instead of 30 of the least seen label (template)

<!-- train / val / test, and per-label counts in the test
split. If a label had fewer than about 8 in test, say so — it explains a lot
of next unit's variance. -->

### Stretch Feature: Second training with more epochs

**What changed:** I trained the model a second time (Run B) with 2 more epochs
than the original run (Run A), `EPOCHS + 2`. The seed, learning rate, batch
size, base model, and data splits were kept the same, so the number of epochs
is the only difference between the runs.

**Results on the held-out test set**

| Metric                          | Run A (3 Epochs) | Run B (5 epochs)  |
|---------------------------------|------------------|-------------------|
| Accuracy                        | 0.667            | 0.667             |
| Macro F1                        | 0.414            | 0.414             |
| Accuracy, most-confident third  | 0.900            | 0.900             |
| Accuracy, least-confident third | 0.500            | 0.300             |

**What I observed:** Accuracy, macro F1, and the accuracy on the most-confident
third did not change. The only difference was the accuracy on the
least-confident third, which dropped from 0.500 to 0.300.

**Interpretation**
- Training longer did not improve the model on the metrics I tracked. The
  extra epochs gave no gain in accuracy or macro F1.
- The model is just as reliable when it is confident (0.900 in both runs). The
  drop only affects the predictions it is least sure about.
- The test set is small, so each third contains only a few posts. A drop from
  0.500 to 0.300 is a difference of about two predictions. This is weak
  evidence, and it may be noise rather than a real effect of the extra epochs.
- A slightly worse least-sure third is consistent with the model fitting the
  training data more closely without generalizing better. I did not verify
  this, for example by comparing training and validation loss across epochs,
  so I treat it as a possible explanation only.

**Conclusion:** More epochs did not help here. The baseline (Run A) is the
better choice because it performs the same with less training and is slightly
better on the least-confident predictions. A larger test set or several seeds
would be needed to say whether the drop is real.



---

## How I Used AI

<!-- Two specific moments — what you asked, what came back, what you changed.

     ⚠️ Plus disclosure of any pre-labelling. If you had a model pre-label a
     batch and then read and corrected every one, say that. It's an allowed
     workflow and disclosing it costs you nothing. Not disclosing it is the
     problem. -->

**Moment 1**

- *What I asked for:* Feedback on my labels based on the data
- *What came back:* A structured breakdown of why some of them were good, and which sections were weak
- *What I changed:* I redefined the ones that needed more specificity, and worked on better understanding how to better tailor the labels to the test in the dataset

**Moment 2**

- *What I asked for:* Brainstorming session for the criterion based on my suggestions
- *What came back:* Feedback on why they were weak and possible redirection for those who lacked quantification or who did not make sense. It also pointed out some areas I did not consider beforehand (such as how accurance in the total model does not mean least-available label accuracy)
- *What I changed:* I deleted many criterion and ended up designing the ones in this document

**Pre-labelling disclosure:** I labeled about 30 posts manually, and AI helped label the rest following the parameters.

<!-- ═══════════════════════ UNIT 6 — THE TEST ═══════════════════════

     Don't fill these in during unit 5.
     ═══════════════════════════════════════════════════════════════════ -->

---

## Baseline vs. Trained

<!-- Both models on the same posts. `python baseline.py --trained results.json`
     prints this table for you. -->
| Measure | Baseline |
|---|---|
| Overall accuracy | 0.633 |
| Macro F1 | 0.533 |
| F1 — `bare_ask` | 0.444 |
| F1 — `book_centered` | 0.743 |
| F1 — `personal` | 0.400 |
| F1 — `template` | 0.545 |

| Measure | Baseline | Trained | Difference |
|---|---|---|---|
| Overall accuracy | 0.633 | 0.667 | +0.033 |
| Macro F1 | 0.533 | 0.432 | -0.101 |
| F1 — `bare_ask` | 0.444 | 0.000 | -0.444 |
| F1 — `book_centered` | 0.743 | 0.727 | -0.016 |
| F1 — `personal` | 0.400 | 0.000 | -0.400 |
| F1 — `template` | 0.545 | 1.000 | +0.455 |

**What I predicted before I looked:**
<!-- Milestone 1 asks you to write this BEFORE seeing the trained numbers. A
     prediction made afterwards isn't one. -->
     I believe the label that will do the best is book_centered, and the one that will do the worst is personal, due to the occurrences in the dataset. If having in mind how stiff or flexible the definitions are, I believe template will do very well since it is a well defined structured, while both bare_ask and book_centered might get confused with and book centered since they are not mutually exclusive.  

**What the gap actually means:**
<!-- If the baseline matched your trained model, your fine-tuning added
     nothing — and that is a real finding, not a failure. Say it plainly. -->
The baseline seemed to do better than the trained model. Diving deeper into each label this is what I could see:
- `bare_ask` -> did better in the baseline. The trained model has a 0 F1, which means it never predicts bare_ask
- `book_centered` -> roughly the same in baseline and trained model, baseline still outperforms trained by 0.016
- `personal` -> just like `bare_ask`, it does better in the baseline and does not get predicted at all
- `template`-> does significantly better on trained model. It went from a 0.545 in the baseline to 1.0 in training.

Overall, finetunning the way I did did not improve the model, it mainly specialized the system to be good at detecting `template`.


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

| true \ predicted | template | book_centered | personal | bare_ask |
|---|---|---|---|---|
| **template** | 7 | 0 | 0 | 0 |
| **book_centered** | 1 | 13 | 0 | 0 |
| **personal** | 0 | 4 | 0 | 0 |
| **bare_ask** | 0 | 5 | 0 | 0 |


**My biggest off-diagonal number, and what it means:**
<!-- Not "the model made mistakes" — WHICH boundary it didn't learn, and which
     direction. "7 real analysis posts were called hot_take and only 3 went the
     other way" is a direction, not just an error rate. -->
Biggest off diagonal: 5. In this case, it shows that template labels were most times confused with book_centered. Hence, the model did not learn to distinguish correctly between book centered posts and posts that act as petitions. 


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

**Agreement rate:** __24/ 30 = 80%__%

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
> "The club championship scoring changed in 2019 from top-6 to top-10. Since then our B team has finished above the A team twice. That's not depth improving, it's the scoring rewarding turnout."
> *Staff said / I said:*
> `analysis` | `hot_take` 
> *My call, and why:*
>  I said it was a hot take since I focused on the second half "that's not depth improving, it's the scoring rewarding turnout." and kidn of ignored the statistics and thought of them as "decor"
> *Which pile:*
A)

**2.**
> *The post:*
> "Everyone blames the hill at 18 miles. I split the field into people who ran the first half under 1:45 and over, and the slowdown after 18 was almost identical for both groups. If the hill were the problem the fast starters would fall apart harder."
> *Staff said / I said:*
> `analysis` | `hot_take` 
> *My call, and why:*
> Again, I focused too much on the last section in which it tried to point fingers instead of focusing on an objective statement.
> *Which pile:*
A)

**3.**
> *The post:*
> "Carbon plates aren't the whole story. My times dropped 2% in the shoes and another 2% the following year in the same pair, when the only thing that changed was going from 35 to 50 miles a week."
> *Staff said / I said:*
> `analysis` | `hot_take`
> *My call, and why:*
> I believe it was not an analysis since it is speaking of sort of a personal situation which does not mean that can apply to everyone that changes shoes. I still stand by my opinon
> *Which pile:*
C)

**4.**
> *The post:*
> "Ran the same loop in 4C and in 24C within a fortnight, same effort by heart rate. 90 seconds slower in the heat over six miles. People keep saying heat costs you 'a bit' and it's more than that."
> *Staff said / I said:*
> `analysis` | `reaction`
> *My call, and why:*
> The post talks mainly of first experience, and even though it provides a number, it is still a number based on a single person situation and their reflection afterwards, for which I consider it a reaction instead of an analysis
> *Which pile:*
C)

**5.**
> *The post:*
> "Went back through the club results going back to 2012. Every single year the number of people who enter the spring marathon and don't start it sits between 18 and 23 percent. It's not a bad-luck year, it's the base rate."
> *Staff said / I said:*
> `analysis` | `hot_take` 
> *My call, and why:*
> I did not focus on the statistic showed in the post and hence, did not classify it correctly
> *Which pile:*
C)

**6.**
> *The post:*
> "Three of us ran the same session on the same day, different shoes, within 10 seconds of each other over 5 miles. I'm not saying shoes do nothing, but whatever they do was smaller than the noise between three people."
> *Staff said / I said:*
> `analysis` | `reaction`
> *My call, and why:*
> My call is a reaction since, again, it is based on a small trial amongs maybe friens, and a conclusion which was drawn from that experience. I do not consider it to be an analysis, moreover, the conclusion is a bit personalized and tailored to the situation itself, which is why I still believe it is a reaction
> *Which pile:*
C)

**What the pattern in my disagreements tells me:**
Some of them was due to not paying close attention to the post, and some others (I believe majority) were debatable positions.. which showcase once again, that there is always space for debate in taxonomies
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

Row numbers are the position in `labels_template.csv` (1 = first row after the header, 200 rows). Rows 1-30 are `cold`, rows 31-200 are `pre-label`. Tie-break order used throughout: `template` > `book_centered` > `personal` > `bare_ask`.

**1. Names a book AND tells a personal story** (`book_centered` vs `personal`)
- Row 4: a Brazilian aspiring author asking for books like *Lolita*. Row 82: grief after losing a baby, with favorite reads listed. Row 129: a 20-year-old who has re-read *Harry Potter* five times.
- Chose `book_centered`: the rule is "names a specific book or author -> `book_centered`", however personal the rest is.

**2. A book named only to say the writer did not like it** (`book_centered` vs `bare_ask`)
- Row 5 (reading *The Terminal List* and "it is just not for me") and row 175 (trigger warning for *Body Double*, "couldn't finish the book").
- Chose `book_centered`: a named book is a named book, whether the writer liked it or not.

**3. Movies, shows and other non-books** (`book_centered` vs `bare_ask`)
- Row 21 ("Not a book, but two animated movies"), row 91 (*Attack on Titan*), row 109 (*Moxie*, which is also a book), row 155 (*Ferris Bueller*) and row 77 (James Bond / Ian Fleming, named only as inspiration).
- Chose `bare_ask`: no book the writer read or liked is named.

**4. "Help me find this book" with no title** (`bare_ask` vs `personal`)
- Rows 18, 123 and 168 describe a half-remembered plot but give no title.
- Chose `bare_ask`.

**5. Comments about a book that is never named** (`bare_ask` vs `personal`)
- Row 117 (discussing the *Ellen* plot with no title), row 12 (waiting for the second book) and row 181 (loving the hotel in the book): `bare_ask`. Row 96 ("I've always been kind of an outsider socially"): `personal`.
- Decided by whether the writer states a fact about themselves, not just an opinion about the book.

**6. Link lists and bot messages** (`template` vs `book_centered`)
- Row 19 is only Amazon links, so it is `template` ("a list of links with no human writing"). Row 113, the subreddit's automatic removal message, is `template` because it is bot output.

**7. Requests on behalf of someone else** (`personal` vs `bare_ask`)
- Rows 11 (cousin, 11th grade), 32 (10-year-old cousins), 46 (best friend's kindle) and 167 (a 50-year-old man getting back into reading) give concrete details about the other person and name no book. Chose `personal`.

**8. Interest or taste only, no facts about the writer** (`personal` vs `bare_ask`)
- Row 29 (poisons and toxins), row 92 (jellyfish) and row 94 (a beach read that is deep and sad). Chose `bare_ask`.

**9. Not really a request** (`personal` vs `bare_ask`)
- Row 33 (a Reddit book-swap announcement) and row 152 (a comment about winter weather). Neither names a book. Chose `personal` because they describe what the writer is doing or where they live.

**Label balance:** 118 `book_centered` (59.0%), 31 `bare_ask` (15.5%), 30 `personal` (15.0%), 21 `template` (10.5%). `book_centered` is above criterion 2's 50% ceiling, and `template` is just above its 10% floor.
