# Acceptance criteria — TakeMeter

Five criteria that say what "working" means for this classifier, written in
unit 5 **before** anything was trained.

**All five are yours this time.** None are given. You've had two projects of
practice.

An acceptance criterion names a number. *"The model is accurate"* is an
opinion. *"Every label has an F1 of at least 0.60 on the held-out set"* is a
criterion.

Under each, write a sentence or two on **why that number**. A reason that says
something about your data or your taxonomy earns credit — *"I picked 0.60 F1
for `reaction` because it's my smallest label and I only have about 50
examples of it"*. A reason that could be attached to any project does not.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## Pick numbers you can defend

Not numbers that sound impressive. Three labels means a coin-flip guesser gets
about 33%, so a target of 0.40 is barely a target. Your number should sit
somewhere you'd honestly call useful.

**Cover at least three of these five areas.** They're here as prompts, not as a
form to fill in — a criterion that fits none of them is fine if it names a
number.

| Area | A question it could answer |
|---|---|
| Overall accuracy | How often does it need to be right to be worth using? |
| Per-label performance | Is one label allowed to be much worse than the others? |
| Balance | How lopsided can your label counts get before it's a problem? |
| Consistency | If someone else labelled the same posts, how often should you agree? |
| Confidence | Should a confident prediction be right more often than an unsure one? |

Two things worth knowing before you pick numbers, because both will affect
whether you hit them:

- **Your smallest label will have the jumpiest score.** If a label has 50
  examples, about 8 land in the test split. An F1 computed on 8 examples moves
  a lot between seeds. A target for that label should be looser than one for
  your biggest label, and saying so is a good reason.
- **Unit 6 tests across three seeds, and the target has to hold across all
  three.** A target of 0.65 against results of 0.71, 0.62, 0.68 is a **miss**.
  Pick with that in mind — it is stricter than it first sounds.

---

## 1. The F1 score of template has to be greater than 0.85, the rest's F1 should be more than 0.65

<!-- Your criterion. It must name a number. -->



**Why this target:**
Template label has a very defined and visible structure, which makes it easier to detect, while other lables (personal, book_centered, and bare_ask) rely more on a judgement call. Moreover, I am expecting about 5 test examples in smallest labels, which is why they are more lenient.


---

## 2. No label is above of 50% and no label is below 10%

<!-- Your criterion. -->



**Why this target:**
With 200 rowns, there is a possibility of the data being unbalanced, especifically a label as defined as template. I want to be able to identify if there is an overall reasonable distribution of the labels and none terribly outweights the others. 


---

## 3. Overall accuracy of 75%

<!-- Your criterion. -->



**Why this target:**

I want the model permission of being wrong to be reasonable. At first at was aiming at 90, but having in mind how some labels might not be represented with enough examples on the training set, O decided to make it so that the model is only allowed to miss 25% of the times at maximum


---

## 4.  The trained model macro F1 beats baseliones by at least 0.10 on all seeds

<!-- Your criterion. -->



**Why this target:**
I want to couble check the changes after fine tunning the model. Having 200 rows and four labels, a baseline can do a good job, and having a model that performs the same does not add up value. 


---

## 5. Template recall is al least 0.7 on every seed

<!-- Your criterion. -->



**Why this target:**
template is the rarest of the labels, and the comments are about 9% of the whole rows, and hence could be ignored by a model and still have a high accuracy even after performing poorly on tehg least represented label (in this case threshold is 75% as per criterion 3) 


---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 6 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath, like this:

         ## 2. Every label performs acceptably

         The model performs well on all labels.

         **Why this target:** ...

         > **Revised in unit 6:** Every label has an F1 of at least 0.60 on
         > the held-out set.
         >
         > **Why revised:** "performs well" gave me nothing to check. I
         > couldn't produce a verdict from it at all.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "Overall accuracy of at least 0.65" → "at least 0.55", because
            0.65 turned out to be optimistic for 200 examples.

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->
