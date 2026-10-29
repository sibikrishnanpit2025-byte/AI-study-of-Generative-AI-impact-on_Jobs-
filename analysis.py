"""
Command-line summary for the Generative AI Impact on Jobs demo.
Run: python analysis.py
"""
from pathlib import Path
import pandas as pd

DATA = Path(__file__).parent / "data" / "jobs_impact.csv"
df = pd.read_csv(DATA)

score_cols = [
    "task_exposure_score",
    "augmentation_potential_score",
    "automation_risk_score",
    "reskilling_demand_score",
]

print("GENERATIVE AI IMPACT ON JOBS — EXPLORATORY SUMMARY")
print("=" * 54)
print(f"Roles: {len(df)}")
print(f"Industries: {df['industry'].nunique()}")
print("\nMean illustrative scores by industry:")
print(df.groupby("industry")[score_cols].mean().round(2).sort_values(
    "task_exposure_score", ascending=False
).to_string())

print("\nRoles with highest illustrative augmentation potential:")
print(df.nlargest(5, "augmentation_potential_score")[
    ["job_title", "industry", "augmentation_potential_score", "automation_risk_score"]
].to_string(index=False))

print("\nReminder: synthetic demo data, not real-world estimates or job-loss predictions.")
