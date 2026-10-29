<div align="center">

# joob

**Find jobs. Tailor resumes. Skip the grind.**

Search several job boards at once, then let Claude Code research the company and tailor a resume for the role. It stops before submitting, so you still send every application yourself.

![Python](https://img.shields.io/badge/python-3.12-3776AB?logo=python&logoColor=white)
![uv](https://img.shields.io/badge/uv-managed-DE5FE9?logo=uv&logoColor=white)
![Claude Code](https://img.shields.io/badge/Claude_Code-skill-D97757?logo=claude&logoColor=white)
![License: MIT](https://img.shields.io/badge/license-MIT-green)

</div>

---

## How it works

```
 search.py ──▶ jobs/*.csv ──▶ Claude Code + resume-tailoring skill ──▶ tailored resume
 (JobSpy)      full JDs        reads resumes/, researches the company
```

1. **Search.** [JobSpy](https://github.com/speedyapply/JobSpy) gets postings from Indeed, LinkedIn, Glassdoor and ZipRecruiter, including the full job descriptions.
2. **Tailor.** The bundled `resume-tailoring` skill compares a posting with your existing resumes and asks about experience they don't mention. It writes a tailored resume and never invents experience.

## Quick start

You need [uv](https://docs.astral.sh/uv/) and [Claude Code](https://claude.com/claude-code).

```sh
git clone https://github.com/lhansen-dev/joob && cd joob
uv sync
mkdir resumes   # put your existing resumes here as markdown
```

## Search

```sh
uv run search.py "python developer" "Austin, TX"
```

Results go to `jobs/<search_term>.csv`, and a summary table is printed.

| Flag      | Default          | What it does                                                  |
| --------- | ---------------- | ------------------------------------------------------------- |
| `--sites` | `indeed,linkedin`| Comma-separated: `indeed`, `linkedin`, `glassdoor`, `zip_recruiter` |
| `--n`     | `30`             | Results per site                                              |
| `--hours` | `72`             | Only show postings newer than this many hours                 |

> [!TIP]
> - **Indeed** is the most reliable site and doesn't rate-limit.
> - **LinkedIn** starts rate-limiting at around 10 pages, so keep `--n` small.
> - Use a real location for LinkedIn. `"Remote"` returns jobs from anywhere in the world.
> - Glassdoor and ZipRecruiter often fail.

## Tailor

Start `claude` in this folder. The skill loads automatically from `.claude/skills/`. Then ask:

> tailor my resume for row 3 in jobs/python_developer.csv

The skill will:

- research the company and the role
- pick the strongest material from every resume in `resumes/`
- ask about relevant experience your resumes don't include
- write a tailored resume, plus a report showing how it matches the posting

You can tailor for several jobs in one go:

> tailor resumes for these 3 jobs: rows 1, 4 and 7

> [!NOTE]
> Word and PDF output need a document-skills plugin. Without one, the skill writes markdown only.

## Privacy

`jobs/` and `resumes/` are gitignored, so your resumes and search results never get committed.

## Credits

- [JobSpy](https://github.com/speedyapply/JobSpy) for scraping the job boards (MIT)
- [varunr89/resume-tailoring-skill](https://github.com/varunr89/resume-tailoring-skill) for the tailoring skill (MIT, bundled from commit `9a4a0f2`)

## License

[MIT](LICENSE) © 2026 Luke Hansen
