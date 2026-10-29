import pandas as pd
import plotly.express as px
import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Generative AI & Jobs", page_icon="🤖", layout="wide")
ROOT = Path(__file__).parent
DATA_PATH = ROOT / "data" / "jobs_impact.csv"

st.title("🤖 Generative AI Impact on Jobs")
st.markdown("### An exploratory, data-driven study of task exposure, augmentation, automation risk, and reskilling")
st.warning(
    "Important: the included dataset is **illustrative synthetic data**, created for a portfolio/demo project. "
    "Scores are not measured labor-market statistics and must not be interpreted as predictions about actual job losses."
)

df = pd.read_csv(DATA_PATH)
score_cols = {
    "Task exposure": "task_exposure_score",
    "Augmentation potential": "augmentation_potential_score",
    "Automation risk": "automation_risk_score",
    "Reskilling demand": "reskilling_demand_score",
}

with st.sidebar:
    st.header("Explore the dataset")
    industries = ["All"] + sorted(df["industry"].unique().tolist())
    selected_industry = st.selectbox("Industry", industries)
    metric_label = st.selectbox("Score to compare", list(score_cols.keys()))
    min_pay, max_pay = int(df.median_annual_pay_usd.min()), int(df.median_annual_pay_usd.max())
    pay_range = st.slider("Illustrative annual pay range (USD)", min_pay, max_pay, (min_pay, max_pay), step=5000)
    show_table = st.checkbox("Show data table", value=True)

filtered = df.copy()
if selected_industry != "All":
    filtered = filtered[filtered.industry == selected_industry]
filtered = filtered[filtered.median_annual_pay_usd.between(pay_range[0], pay_range[1])]
metric = score_cols[metric_label]

c1, c2, c3, c4 = st.columns(4)
c1.metric("Roles in view", f"{len(filtered)}")
c2.metric("Industries represented", f"{filtered.industry.nunique()}")
c3.metric(f"Mean {metric_label.lower()}", f"{filtered[metric].mean():.0%}" if len(filtered) else "—")
c4.metric("Dataset type", "Synthetic")

st.caption("Scores range from 0 to 1. Higher values indicate more of the named characteristic in this illustrative dataset.")
if filtered.empty:
    st.info("No roles match these filters. Adjust the industry or pay range.")
    st.stop()

left, right = st.columns(2)
with left:
    chart_df = filtered.sort_values(metric, ascending=False)
    fig = px.bar(chart_df, x=metric, y="job_title", color="industry", orientation="h",
                 title=f"{metric_label} by job role", labels={metric: metric_label, "job_title": "Job role"})
    fig.update_layout(yaxis={"categoryorder": "total ascending"}, legend_title="Industry")
    st.plotly_chart(fig, use_container_width=True)
with right:
    fig = px.scatter(filtered, x="task_exposure_score", y="augmentation_potential_score",
                     size="reskilling_demand_score", color="industry", hover_name="job_title",
                     hover_data={"automation_risk_score":":.0%", "median_annual_pay_usd":":$,.0f"},
                     title="Exposure vs. augmentation potential",
                     labels={"task_exposure_score":"Task exposure", "augmentation_potential_score":"Augmentation potential",
                             "reskilling_demand_score":"Reskilling demand"})
    st.plotly_chart(fig, use_container_width=True)

st.subheader("How to read the scores")
st.markdown("""
- **Task exposure:** how much of a role's task mix could plausibly be affected by generative AI.
- **Augmentation potential:** how much AI could assist people doing the work.
- **Automation risk:** a simplified, illustrative estimate of task automation potential—not a forecast of job elimination.
- **Reskilling demand:** a hypothetical signal of how much adaptation or new skill development may be needed.
""")

st.subheader("Key questions for the study")
st.markdown("""
1. Which roles combine high task exposure with high augmentation potential?
2. Does high exposure necessarily imply high automation risk? (It should not be assumed.)
3. Which industries may need the most worker training and transition support?
4. How can organizations redesign tasks while preserving human judgment, accountability, and service quality?
""")

if show_table:
    st.subheader("Filtered dataset")
    display = filtered.copy()
    for col in score_cols.values():
        display[col] = display[col].map(lambda x: f"{x:.0%}")
    display["median_annual_pay_usd"] = display["median_annual_pay_usd"].map(lambda x: f"${x:,.0f}")
    st.dataframe(display, use_container_width=True, hide_index=True)

st.subheader("Limitations")
st.markdown("""
This demo does not use a representative labor-force sample, observed AI adoption, or causal analysis. Job titles contain
many different tasks, and effects vary by country, company, seniority, regulation, and implementation choices. A real
study should replace this dataset with documented, cited sources and validate the scoring method with domain experts.
""")
