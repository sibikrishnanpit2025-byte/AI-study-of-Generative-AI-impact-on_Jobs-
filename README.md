# Generative AI Impact on Jobs

An exploratory Python data-analysis project about how generative AI may affect work through **task exposure, worker augmentation, automation potential, and reskilling needs**.

> **Data transparency:** The included CSV is synthetic and illustrative. Its scores are not empirical findings, not sourced estimates, and not predictions of job losses. This project demonstrates a reproducible analysis workflow. Replace the demo data with cited, documented evidence before making real-world claims.

## Project goals

- Explore how the potential impact of generative AI can differ across job roles.
- Distinguish task exposure from automation and from augmentation.
- Visualize illustrative role-level scores using an interactive dashboard.
- Encourage careful interpretation and discussion of reskilling and job redesign.

## Features

- Streamlit dashboard with industry and salary filters.
- Interactive bar chart comparing a selected score across roles.
- Scatter plot comparing task exposure with augmentation potential.
- Dataset table and command-line summary.
- Clear documentation of assumptions and limitations.

## Repository structure

```text
generative_ai_impact_on_jobs/
├── app.py
├── analysis.py
├── data/
│   └── jobs_impact.csv
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
```

## Run locally

Python 3.10 or newer is recommended.

1. Clone your repository:
   ```bash
   git clone https://github.com/YOUR-USERNAME/generative-ai-impact-on-jobs.git
   cd generative-ai-impact-on-jobs
   ```
2. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv .venv
   ```
   Windows:
   ```bash
   .venv\Scripts\activate
   ```
   macOS/Linux:
   ```bash
   source .venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Launch the dashboard:
   ```bash
   streamlit run app.py
   ```
5. Optional: run the command-line analysis:
   ```bash
   python analysis.py
   ```

## Dataset dictionary

| Column | Meaning |
|---|---|
| `job_title` | Example job role |
| `industry` | Broad industry category |
| `median_annual_pay_usd` | Illustrative pay value in USD, included only to demonstrate filtering |
| `task_exposure_score` | Synthetic score from 0 to 1 for potential task exposure |
| `augmentation_potential_score` | Synthetic score from 0 to 1 for potential AI assistance |
| `automation_risk_score` | Synthetic score from 0 to 1 for hypothetical automation potential |
| `reskilling_demand_score` | Synthetic score from 0 to 1 for hypothetical reskilling needs |

The score definitions are conceptual and have not been validated. The salary values are not presented as current or country-specific salary data.

## Research questions

1. Which job roles have high potential exposure and high potential augmentation?
2. Why should exposure to AI not be treated as equivalent to a job being eliminated?
3. What skills could help workers adapt as tasks change?
4. What evidence would be needed to measure actual employment effects over time?

## Suggested methodology for a stronger research version

1. Choose a geographic scope and time period.
2. Collect reliable, cited sources on occupations, tasks, wages, and AI adoption.
3. Record source title, publisher, publication date, URL, and relevant definitions.
4. Define a transparent scoring rubric before scoring roles.
5. Separate observed evidence from expert judgment and scenario assumptions.
6. Include uncertainty, limitations, and alternative explanations.
7. Avoid causal claims unless the research design supports them.

Possible starting points for a future evidence-based edition:
- World Economic Forum — *Future of Jobs Report*: https://www.weforum.org/reports/
- International Labour Organization — research on generative AI and jobs: https://www.ilo.org/
- OECD — AI, skills, and employment research: https://www.oecd.org/
- U.S. Bureau of Labor Statistics occupational data: https://www.bls.gov/

Check each source's date, geographic coverage, methods, and reuse terms before incorporating its data.

## Example conclusion (based on project design, not empirical results)

Generative AI's impact is better studied at the task level than by assuming entire occupations will disappear. Some tasks may be automated, others may be accelerated or improved by AI, and many still require human judgment, physical work, relationships, or accountability. The real outcome depends on technology, adoption choices, business models, worker training, and public policy. This demo illustrates how to explore those questions; it does not establish which jobs will grow or decline.

## Next improvements

- Add a sourced dataset and source metadata file.
- Add country-specific labor-market context.
- Add unit tests for data validation.
- Add scenario controls and uncertainty ranges.
- Publish the dashboard with Streamlit Community Cloud.

## License

MIT — see `LICENSE`.
