# joob

Job hunting prep: search job boards, then tailor resumes with Claude Code. It doesn't submit applications.

## Setup

Needs [uv](https://docs.astral.sh/uv/) and [Claude Code](https://claude.com/claude-code).

```sh
git clone https://github.com/lhansen-dev/joob && cd joob
uv sync
mkdir resumes  # put your existing resumes here as markdown
```

## Search

`search.py` uses [JobSpy](https://github.com/speedyapply/JobSpy) to pull postings, including full descriptions, into `jobs/<term>.csv`.

```sh
uv run search.py "python developer" "Austin, TX" --sites indeed,linkedin --n 30 --hours 72
```

- Indeed is the most reliable site. LinkedIn starts rate-limiting at around 10 pages, so keep `--n` small.
- For LinkedIn, use a real location. "Remote" returns jobs from anywhere in the world.

## Tailor

Open Claude Code in this folder. The `resume-tailoring` skill in `.claude/skills/` loads automatically. Then ask:

> tailor my resume for row 3 in jobs/python_developer.csv

It researches the company, asks about experience your resumes don't mention, and writes a tailored resume from what's in `resumes/`.

`jobs/` and `resumes/` are gitignored.

## Credits

The `resume-tailoring` skill comes from [varunr89/resume-tailoring-skill](https://github.com/varunr89/resume-tailoring-skill) (MIT, commit `9a4a0f2`).

## License

MIT
