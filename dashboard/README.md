# Life expectancy explorer (dashboard)

A small Streamlit dashboard built on the same World Bank data as the notebook.

**What it does**
- Year slider, region and income-group filters, and a choice of indicator (life expectancy, internet use, CO₂, child mortality, urban share).
- **Income vs indicator**: bubble scatter (log GDP on x, circle area = population), with your chosen country highlighted.
- **Map**: choropleth in the Equal Earth projection with the cividis palette, plus a one-line text summary for readers who can't see the map.
- **Trends by region**: population-weighted regional averages over time, with the selected year marked.

**Run it locally**
```bash
# from the project folder, after running the notebook once (it writes data/processed/wdi_clean.csv)
pip install -r requirements.txt
streamlit run dashboard/app.py
```

**Deploy it (free)**
1. Push the whole project folder, including `data/processed/wdi_clean.csv`, to a public GitHub repo.
2. Go to https://share.streamlit.io, choose "New app", pick the repo and set the main file to `dashboard/app.py`.
3. Put the link it gives you in the main README.

If you'd rather not deploy, record a 1–2 minute screen capture of yourself using the filters, tabs and hover, and include it as `dashboard/demo.mp4`.

**Accessibility notes:** every control is a standard form widget, so you can Tab to it and use it from the keyboard. Colours are colour-blind-safe (Okabe-Ito for regions, cividis for the map), and regions also get different marker shapes.
