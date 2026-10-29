# joob

A job-hunting helper. Users are often new to Claude Code and the terminal, so use plain language and run the commands for them.

- **Finding jobs:** run `uv run search.py "<term>" "<City, Region>" [--sites indeed,linkedin] [--n 30] [--hours 72]`. Results go to `jobs/<term>.csv`, including full job descriptions. Show the user a short list, not the raw CSV. If LinkedIn fails or is rate-limited, retry with `--sites indeed`.
- **Importing a resume:** use the `docx-md` skill to convert it into `resumes/<Name>_Resume_<date>.md`.
- **Polishing the main resume** (no specific job): use the `resume-polish` skill. It writes `resumes/<Name>_Resume_Master_<date>.md`.
- **Tailoring:** use the `resume-tailoring` skill. Its library is `resumes/*.md`. Save its output to `resumes/tailored/`, not the repo root.
- **Cover letters:** use the `cover-letter` skill after tailoring. It reuses the tailoring report and saves to `resumes/tailored/`.
- **Exporting:** use the `docx-md` skill to turn files in `resumes/tailored/` into `.docx`.
- Personal data stays in `resumes/` and `jobs/`, which are gitignored. Never write it to tracked paths.
