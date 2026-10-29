<div align="center">

# joob

**Find jobs and tailor your resume by chatting with an AI.**

You tell Claude what job you want. It searches the job boards, picks good matches, and rewrites your resume for each one without inventing anything. When you're done it hands you a Word file. You send the applications yourself.

![Python](https://img.shields.io/badge/python-3.12-3776AB?logo=python&logoColor=white)
![Claude Code](https://img.shields.io/badge/Claude_Code-skills-D97757?logo=claude&logoColor=white)
![License: MIT](https://img.shields.io/badge/license-MIT-green)

</div>

---

## What you need

- A **Claude subscription** (Pro or Max) or an Anthropic API account. Claude Code is the AI you'll be chatting with.
- About **10 minutes** for setup. You only do it once.
- Your **current resume**, as a Word file or plain text.

You won't write any code. You type everything in normal English.

## One-time setup

You'll paste a few commands into a **terminal**, the app where you type commands:

- **Mac:** open **Terminal** (press ⌘ + Space and type "Terminal").
- **Windows:** open **PowerShell** from the Start menu.
- **Linux:** you already know.

### 1. Install Claude Code

Mac / Linux:
```sh
curl -fsSL https://claude.ai/install.sh | bash
```
Windows:
```powershell
irm https://claude.ai/install.ps1 | iex
```

### 2. Install uv

uv runs the job search tool.

Mac / Linux:
```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
```
Windows:
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**Close the terminal and open a new one** so it notices the new programs.

### 3. Download joob

If you have git:
```sh
git clone https://github.com/lhansen-dev/joob
cd joob
uv sync
```

If you don't, click the green **Code** button at the top of this page, choose **Download ZIP**, and unzip it. In the terminal, type `cd ` (with a space after it), drag the unzipped folder into the window, and press Enter. Then run `uv sync`.

### 4. Start Claude

```sh
claude
```

The first time, it asks you to log in. After that you'll see a chat prompt, and everything else happens there.

## How to use it

Type these into Claude, in your own words. Claude asks permission before it runs anything, and you can say yes.

### Step 1: Give Claude your resume

> Import my resume from ~/Downloads/My_Resume.docx

Claude converts it and saves it in the `resumes/` folder. Older versions help too, because they give Claude more material to work with. Import as many as you have.

> [!TIP]
> If you don't know where the file is, drag it into the Claude window and Claude will get the path.

### Step 2: Find jobs

> Find me senior data engineer jobs in Vancouver posted this week

Claude searches Indeed and LinkedIn and shows you a list. You can then ask:

> Which of these fit my resume best?

### Step 3: Tailor your resume

> Tailor my resume for the Autodesk one

Claude will:

1. Research the company.
2. Show you how well your resume matches the posting, and what's missing.
3. **Ask you questions** about experience your resume doesn't mention. These answers make the biggest difference, so take a minute on them.
4. Write the tailored resume, plus a report explaining each change and giving tips for the interview.

It never invents jobs, skills or numbers. It only rewords and reorders what's true.

### Step 4: Get a Word file

> Export it to Word

The file goes in `resumes/tailored/`. Open it, check the formatting, and you're ready to apply.

## Other things to try

| Ask Claude... | What happens |
| --- | --- |
| *"Find remote Python jobs in Canada"* | A different search |
| *"Tailor for these 3 jobs at once"* | Answers your questions once and reuses them for all three resumes |
| *"Make it shorter"* / *"Lead with leadership"* | Revises the resume |
| *"What should I prep for the interview?"* | Gives interview tips based on the report |

## Your privacy

- Your resumes and search results stay **on your computer**, in `resumes/` and `jobs/`. Both folders are excluded from git, so they never get uploaded with the code.
- Claude reads your resume to tailor it, the same as pasting it into a chat.

## Troubleshooting

- **"command not found: claude" or "uv"**: close the terminal and open a new one. If that doesn't work, run the install command again.
- **Few or no results from LinkedIn**: LinkedIn limits how many searches you can run. Ask Claude to use Indeed only, or try again later.
- **Weird location results**: use a real city ("Austin, TX"), not just "Remote".
- **Something else**: ask Claude! For example, *"the search failed, can you fix it?"*

---

<details>
<summary><b>For developers</b></summary>

- `search.py` wraps [JobSpy](https://github.com/speedyapply/JobSpy): `uv run search.py "term" "City, ST" --sites indeed,linkedin --n 30 --hours 72`, which writes `jobs/<term>.csv`.
- `.claude/skills/resume-tailoring/` is bundled from [varunr89/resume-tailoring-skill](https://github.com/varunr89/resume-tailoring-skill) (MIT, commit `9a4a0f2`).
- `.claude/skills/docx-md/` converts between `.md` and `.docx` with pandoc (bundled by `pypandoc-binary`): `uv run .claude/skills/docx-md/convert.py IN OUT`.
- `CLAUDE.md` tells Claude how the pieces fit together.

</details>

## License

[MIT](LICENSE) © 2026 Luke Hansen
