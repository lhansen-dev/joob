---
name: cover-letter
description: Use when the user wants a cover letter for a specific job. Builds on the resume-tailoring output (job posting, company research, gap notes and tailored resume) to write a short, specific letter with no invented claims. Usually runs right after a resume has been tailored.
---

# Cover Letter

**Core rule:** every claim must come from the user's resumes, the tailoring report, or the user's answers in this session. Never invent experience, numbers or reasons for wanting the job.

## 1. Gather

Use what earlier steps already produced. Only research again if something is missing:

- **Job posting:** the matching row in `jobs/*.csv` (the `description` column), or the text or URL the user gave.
- **Tailoring report:** `resumes/tailored/<Name>_<Company>_<Role>_Resume_Report.md`. It has the success profile, company research, gaps and differentiators.
- **Tailored resume:** `resumes/tailored/<Name>_<Company>_<Role>_Resume.md`.

If there's no tailored resume for this job yet, offer to run `resume-tailoring` first. Otherwise use the newest resume in `resumes/` and do a quick search on the company.

## 2. Ask (2–3 questions, at most)

Company research can't tell you why this person wants this job. Ask:

1. **Why this company or role?** For example, a product they use, the domain, the team's mission, or a person they know there. Offer 2–3 options based on your research, phrased so they can just pick one.
2. **Which story to lead with?** Recommend the bullet from the tailored resume that best matches the posting's top requirement, and ask if there's a better one.
3. **The biggest gap** from the report: address it or leave it out? Recommend one or the other.

If the user says "just write it", use your recommendations and mark the "why this company" line as `[CHECK: …]` so they confirm it.

## 3. Write

250–350 words, 3–4 paragraphs:

1. **Hook (2–3 sentences):** the specific role, plus a real reason for wanting it at *this* company. Name something concrete about them (their product, a technical challenge or a recent change). Never open with "I am writing to express my interest".
2. **Proof (1–2 short paragraphs):** one or two stories, each tied to a requirement in the posting. Use the shape *problem → what you did → result*. Don't repeat resume bullets word for word. Add the context the resume has no room for.
3. **Gap (optional, 1–2 sentences):** if you're addressing a gap, use adjacent experience to show you can pick it up quickly. Don't apologize for it.
4. **Close (1–2 sentences):** what you'd bring to the team, plus a simple call to action. No "Thank you for your time and consideration" filler.

**Style:**
- Write plainly, in the first person, the way a confident engineer would write an email, not a form letter.
- Cut words that sound AI-written: "passionate", "thrilled", "leverage", "synergy", "dynamic", "fast-paced", "I believe I would be a great fit", "delve", "tapestry".
- Use the posting's own terms where they truthfully apply.
- Address the letter to the hiring manager by name only if you found it. Otherwise use "Hi [Company] team," or "Dear Hiring Manager,".

## 4. Save and review

Save as `resumes/tailored/<Name>_<Company>_<Role>_CoverLetter.md`, next to the resume. Use the user's contact line from their resume as the header.

Then show the user:
- the letter
- a list of each claim and where it came from (which resume bullet or which of their answers)
- any `[CHECK: …]` markers still left

Offer to revise the letter and to export it to Word with the `docx-md` skill.
