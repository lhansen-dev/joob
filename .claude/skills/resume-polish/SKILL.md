---
name: resume-polish
description: Use when the user wants to improve, polish, "buff" or clean up their main resume in general, with no specific job posting in mind, or says "grill me" about their resume. Audits every resume in resumes/, asks for missing facts and numbers (or, in grill mode, interviews the user in rounds), and writes one cleaned-up master resume that later tailoring builds on. For a specific job, use resume-tailoring instead.
---

# Resume Polish

**Core rule:** improve the wording and structure, never the facts. Every claim in the output must come from the user's resumes or from the user's answers in this session. If a bullet needs a number, ask for it. Never estimate one.

## 1. Gather

Read every `resumes/*.md` file (not `resumes/tailored/`). Combine them into one set of facts: roles, dates, bullets (keep the best wording of each), skills, education and contact details. Older versions often contain details the newer ones dropped, so keep those too.

## 2. Audit

Present a short report, grouped as follows and worst first:

- **Inconsistencies between versions:** dates, years of experience, titles, contact details, company names. The user has to pick the right one.
- **Weak bullets:** no result, filler ("a number of", "responsible for", "helped with"), passive voice, longer than 2 lines, or vague words like "significantly" or "improved" with no number.
- **Unsupported skills:** listed skills that no bullet shows being used.
- **ATS problems** (applicant tracking systems, the software employers use to screen resumes): tables or columns for layout, information hidden in headers or footers, unusual section names, decorative characters, spelling mistakes.
- **Missing:** a summary, dates, location, a LinkedIn URL, or a promotion story that's only implied.

## 3. Ask

Ask a single numbered list of questions, up to 8 and most valuable first. Cover:
- each inconsistency ("Your resumes say 5 and 6 years. Which is right?")
- missing numbers for the strongest bullets ("Roughly how much did support response time drop? 'From hours to minutes' is fine.")
- whether a skill has evidence ("Where have you used Azure? If nowhere, I'll drop it.")

If the user says "I don't know" or skips a question, keep the bullet without the number. Don't invent one.

### Grill mode

Use grill mode when the user says "grill me", or when you offer it and they accept. Offer it after the audit if the bullets are thin. Instead of the 8 questions above, interview the user in rounds until every bullet is backed by solid facts. Adapted from [mattpocock/skills `grilling`](https://github.com/mattpocock/skills).

**The tree:** each role branches into its bullets, and each bullet branches into what it still needs:
- **What exactly:** what did *you* personally do, and what did the team do?
- **Scale:** how much traffic, data, users, money, or how many people?
- **Result:** what changed because of it, with a number if there is one? What would have happened without it?
- **Who used it:** who relied on it, and is it still in use?

Undocumented work hangs off each role too: "What else did you ship there that isn't on the page?"

**Rounds:** ask every question you can answer *now* in one round, then wait for the answers. A question that depends on an answer still open in this round goes in a later round. For example, ask what the tool was before asking how many people used it. Answers create new branches. Keep going until every branch has been visited, then say so and move on to step 4.

Format each question like this:

```
❓ **Q1** - **<role → bullet>**: <question>

➡️ <your recommendation>
```

**Recommendations:** the user owns the facts and you own the wording. For decisions, recommend an answer, and phrase the question so that "yes" accepts it ("Drop Azure from skills since nothing shows it?"). For facts, never guess a number. Recommend how it should *read* if they confirm it, and suggest a fallback ("➡️ Even a rough before/after works, like 'hours → minutes'").

**Don't ask what you can look up:** if a fact is already in the resumes or is public (game titles, release dates, company size), look it up instead of asking.

**Push back on vagueness.** If an answer is "it helped a lot", ask what it looked like before and after. If the user truly doesn't know, drop it and move on. One honest bullet beats three padded ones.

## 4. Write the master

Save it as `resumes/<Name>_Resume_Master_<YYYY-MM-DD>.md`. Use the same layout as the existing files: `# Name`, contact line, `##` sections, `-` bullets.

- Write each bullet as **action verb + what you did + result**, with the result early, in 2 lines or fewer.
- Aim for 1 page for under 10 years of experience and at most 2 pages otherwise. Cut the weakest bullets first and mention which ones you cut.
- Use standard section names: Summary, Skills, Experience, Education.
- Use the same tense throughout: past tense for finished work, present tense only for ongoing work.
- Never delete or overwrite the user's older resumes. They are still part of the library.

## 5. Show the changes

For each bullet that changed, show it like this:

```
BEFORE: Created a number of internal tools for finding and deserializing in-flight data, significantly reducing support engineer response time
AFTER:  Built internal tools to find and decode in-flight data, cutting support response time from hours to minutes
WHY:    Removed filler; added the number you gave me
```

Then list anything you cut, and any questions that are still unanswered. Offer to export to Word with the `docx-md` skill.
