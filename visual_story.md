# Bangladesh started behind. Now it's ahead. What can Pakistan learn?

*A briefing for the Ministry of National Health Services, Regulations & Coordination. Data: World Bank WDI, 2024.*

**The question.** A Pakistani born today can expect to live **67.8 years**, which ranks 169
out of 217 countries. In 1990, Bangladesh was 3.9 years
behind Pakistan (55.8 vs 59.7). Today it is
**7.1 years ahead** (74.9). Is that just because
Bangladesh got richer?

### 1. Income matters a lot

![Bubble chart](figures/p7_bubble.png)

Across the world, richer countries live longer: each tenfold rise in income goes with roughly **12 more
years** of life. Bangladesh is now richer per person than
Pakistan ($8,487 vs $5,502 a year, PPP),
so some of its lead is simply money.

### 2. But income only explains part of the gap

![Scatter with trend](figures/p5_scatter.png)

The dashed line shows what income alone predicts. Pakistan sits almost exactly on the trend line (-0.4 years), so it lives
about as long as its income
predicts. Bangladesh sits 4.5 years above the trend line. The income difference between them would predict about
**2.3 extra years** for Bangladesh; the real gap is 7.1 years, which leaves roughly
**4.9 years that income doesn't explain**. Of the 22 countries with an income per person within about a third of Pakistan's, **11 live longer**, up to Tonga at 73.1 years.

### 3. Among its neighbours, Pakistan is near the bottom

![Box and strip plot](figures/p6_box_strip.png)

The World Bank now files Pakistan under "Mid. East, N. Africa, Afg. & Pak.", so in this chart its ring sits among the Gulf states. The
fairer comparison is its South Asian neighbours: of these 8 countries, Pakistan comes **7th**.
Only Afghanistan ranks lower.

### 4. The gap opened slowly, over decades

![Clustered heatmap](figures/p7_heatmap_clustered.png)

Since 1990, Pakistan has gained **8 years** and Bangladesh
**19**. They still sit in the same cluster of large countries, but Bangladesh's row turns light (longer lives) much sooner.

### 5. Being lower-middle-income isn't destiny

![Choropleth](figures/p8_choropleth.png)

The lowest values cluster in Sub-Saharan Africa, but the colours don't follow wealth neatly: 17 of the
47 lower-middle-income countries already live 70 years or more.

**Takeaway.** Income accounts for about 2 of the 7 years between Bangladesh and Pakistan.
The rest comes from things a GDP figure doesn't capture, and the same data points to where to look first. A child in Pakistan is **1.8 times as likely to die before age five** as a child in Bangladesh (56 vs 30 deaths per 1,000 live births). Deaths in early childhood pull life expectancy at birth down more than deaths at any other age, so this alone covers a lot of the gap. Child survival (immunisation, care around birth, clean water) is the lever worth studying in Bangladesh's record.

---
**Methods note.** Data: World Bank World Development Indicators via the public API (v2), downloaded 2026-11-08.
Life expectancy at birth (SP.DYN.LE00.IN); GDP per person in constant PPP dollars (NY.GDP.PCAP.PP.KD); under-5
mortality (SH.DYN.MORT); population (SP.POP.TOTL). Aggregates such as "World" were removed; country names shortened;
impossible values set to missing; no gaps were filled in. Each country's value for 2024 is its most recent value
from 2022–2024. The trend line is an ordinary least-squares fit of life expectancy on log10 GDP per person
(slope 12.0 years per tenfold income); the "explained by income" part of the gap is that slope times the
difference in log10 GDP. "Peers" are countries within ±35% of Pakistan's GDP per person; "neighbours" are the eight
South Asian countries listed in the notebook. **Limitations:** life expectancy for many countries is modelled by the
UN rather than measured, so differences under a year shouldn't be over-read; PPP figures carry uncertainty; a trend line
across countries is a correlation, not proof of what causes the gap; and the regions and income groups are the World
Bank's current classification applied to every year.
