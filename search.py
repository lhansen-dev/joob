"""Search job boards with JobSpy and save results to jobs/<term>.csv.

Usage: uv run search.py "python developer" "Remote" [--sites indeed,linkedin] [--n 30] [--hours 72]
"""
import argparse
import re
from pathlib import Path

from jobspy import scrape_jobs

p = argparse.ArgumentParser()
p.add_argument("term")
p.add_argument("location")
p.add_argument("--sites", default="indeed,linkedin")  # glassdoor/zip_recruiter are flaky
p.add_argument("--n", type=int, default=30, help="results per site")
p.add_argument("--hours", type=int, default=72, help="max posting age")
a = p.parse_args()

jobs = scrape_jobs(
    site_name=a.sites.split(","),
    search_term=a.term,
    location=a.location,
    results_wanted=a.n,
    hours_old=a.hours,
    fetch_description=True,  # slower, but tailoring needs the full JD
)

out = Path("jobs") / (re.sub(r"\W+", "_", a.term).strip("_").lower() + ".csv")
out.parent.mkdir(exist_ok=True)
jobs.to_csv(out, index=False)
print(f"{len(jobs)} jobs -> {out}")
print(jobs[["site", "title", "company", "location", "job_url"]].to_string(max_colwidth=50))
