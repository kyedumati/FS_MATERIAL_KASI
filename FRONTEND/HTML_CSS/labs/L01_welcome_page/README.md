# Lab 01 — AcmeHR Welcome Page

**Lesson:** [Lesson 1 — How the Web Works & Your First Page](../../Lesson_01_How_the_Web_Works_and_Your_First_Page.md) · **Time:** 35 minutes

**Ticket:** ACME-101 · **Customer:** Acme HR team
**Need:** Employees open AcmeHR and land on a welcome page. It must have a correct skeleton, show the ₹ sign correctly, and pass the W3C validator.

## Part A — Fix the broken page (10 min)

Open [`broken/index.html`](broken/index.html) in the browser and in VS Code. It has **6 bugs**. Fix them all.

Hints, if you are stuck:

1. Is the first line of the file correct?
2. Which language is the page in, according to the HTML?
3. Look at the browser tab. What text does it show?
4. Look at the ₹ sign.
5. Why are the paragraphs bold and large?
6. Which `<meta>` tag do phones need?

## Part B — Build the welcome page (20 min)

Start from [`starter/index.html`](starter/index.html). Complete every `TODO`.

## Part C — Prove it works (5 min)

Serve your folder with `python3 -m http.server 8000` (or Live Server) and check every box:

- [ ] The page opens at `http://localhost:8000`, and the terminal shows **200** for it. (A 404 for `/favicon.ico` is harmless.)
- [ ] The tab reads **Home — AcmeHR**.
- [ ] The ₹ sign displays correctly.
- [ ] The W3C validator ([validator.w3.org/nu](https://validator.w3.org/nu/)) shows **0 errors**.
- [ ] The file name is lowercase with no spaces.

## Stretch

Create a second page, `about.html`, with its own title and heading. Open `http://localhost:8000/about.html` (200), then `http://localhost:8000/About.html`. What does the terminal show on your computer? Would it be the same on a Linux server?

Compare with [`solution/index.html`](solution/index.html) only after you finish.
