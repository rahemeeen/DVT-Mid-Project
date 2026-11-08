# Life expectancy explorer: a small Streamlit dashboard for the DSC 327 lab project.
# Run from the project folder:   streamlit run dashboard/app.py
# Needs data/processed/wdi_clean.csv, which the notebook writes in Part 1.

from pathlib import Path

import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st

DATA = Path(__file__).resolve().parent.parent / "data" / "processed" / "wdi_clean.csv"
SOURCE = "Source: World Bank, World Development Indicators"

# same colours as the notebook (Okabe-Ito, yellow swapped for dark grey)
OKABE = ["#0072B2", "#E69F00", "#009E73", "#CC79A7", "#56B4E9", "#D55E00", "#555555"]
INCOME_ORDER = ["Low income", "Lower middle income", "Upper middle income", "High income"]
LABELS = {
    "life_expectancy": "Life expectancy (years)",
    "gdp_per_capita": "GDP per person (intl $, PPP)",
    "co2_per_capita": "CO₂ per person (tonnes)",
    "internet_users_pct": "Internet users (%)",
    "under5_mortality": "Under-5 deaths per 1,000 births",
    "urban_pct": "Urban population (%)",
    "population": "Population",
}

st.set_page_config(page_title="Life expectancy explorer", layout="wide")


@st.cache_data
def load():
    df = pd.read_csv(DATA, keep_default_na=False, na_values=[""])
    return df


if not DATA.exists():
    st.error("Can't find data/processed/wdi_clean.csv. Run the notebook first (Part 1 writes it).")
    st.stop()

df = load()
regions = sorted(df.region.dropna().unique())
colours = dict(zip(regions, OKABE))

# ---- sidebar controls (all standard widgets, so they work with the keyboard too) ----
st.sidebar.header("Filters")
year = st.sidebar.slider("Year", int(df.year.min()), int(df.year.max()), int(df.year.max()))
pick_regions = st.sidebar.multiselect("Regions", regions, default=regions)
pick_income = st.sidebar.multiselect("Income groups", INCOME_ORDER + ["Not classified"],
                                     default=INCOME_ORDER + ["Not classified"])
y_var = st.sidebar.selectbox("Indicator to compare with income", [k for k in LABELS if k not in ("gdp_per_capita", "population")],
                             format_func=LABELS.get)
highlight = st.sidebar.text_input("Highlight a country", "Pakistan")

d = df[df.region.isin(pick_regions) & df.income_group.isin(pick_income)]
dy = d[d.year == year].dropna(subset=["gdp_per_capita", y_var])

st.title("Living longer, but not equally")
st.caption(f"{SOURCE}. Showing {dy.iso3.nunique()} countries in {year}.")

c1, c2, c3 = st.columns(3)
le = d[d.year == year].life_expectancy.dropna()
if len(le):
    c1.metric("Median life expectancy", f"{le.median():.1f} years")
    c2.metric("Gap: highest − lowest", f"{le.max() - le.min():.1f} years")
row = d[(d.year == year) & (d.country.str.lower() == highlight.strip().lower())]
if len(row) and pd.notna(row.life_expectancy.iloc[0]):
    c3.metric(f"{row.country.iloc[0]}", f"{row.life_expectancy.iloc[0]:.1f} years")

tab1, tab2, tab3 = st.tabs(["Income vs indicator", "Map", "Trends by region"])

with tab1:
    if dy.empty:
        st.info("No countries match these filters for this year.")
    else:
        fig = px.scatter(dy, x="gdp_per_capita", y=y_var, color="region", symbol="region", size="population",
                         size_max=45, log_x=True, hover_name="country", color_discrete_map=colours,
                         labels={**LABELS, "region": "Region"},
                         title=f"{LABELS[y_var]} vs income per person, {year}")
        fig.update_traces(marker=dict(sizemode="area", line=dict(width=0.5, color="white")))
        if len(row):
            r = row.iloc[0]
            if pd.notna(r.gdp_per_capita) and pd.notna(r[y_var]):
                fig.add_annotation(x=np.log10(r.gdp_per_capita), y=r[y_var], text=r.country, showarrow=True, arrowhead=0)
        st.plotly_chart(fig, use_container_width=True)
        st.caption("Circle area = population. Hover for details; click a region in the legend to hide it.")

with tab2:
    m = d[d.year == year].dropna(subset=[y_var])
    fig = px.choropleth(m, locations="iso3", color=y_var, hover_name="country", color_continuous_scale="cividis",
                        labels=LABELS, title=f"{LABELS[y_var]} by country, {year}")
    fig.update_geos(projection_type="equal earth", showframe=False, landcolor="#e8e8e8", showcoastlines=False)
    st.plotly_chart(fig, use_container_width=True)
    if len(m):
        lo, hi = m.nsmallest(1, y_var).iloc[0], m.nlargest(1, y_var).iloc[0]
        st.write(f"Text summary: {LABELS[y_var].lower()} ranges from {lo[y_var]:,.1f} in {lo.country} "
                 f"to {hi[y_var]:,.1f} in {hi.country}. Grey = no data.")

with tab3:
    t = d.dropna(subset=[y_var, "population"])
    t = t.assign(w=t[y_var] * t.population).groupby(["region", "year"])[["w", "population"]].sum().reset_index()
    t[y_var] = t.w / t.population
    fig = px.line(t, x="year", y=y_var, color="region", color_discrete_map=colours,
                  labels={**LABELS, "year": "Year", "region": "Region"},
                  title=f"{LABELS[y_var]}, population-weighted regional average")
    fig.add_vline(x=year, line_dash="dot", line_color="#888888")
    st.plotly_chart(fig, use_container_width=True)
