# Project 02 — Data Visualization with Matplotlib & Seaborn

## Dataset
This project uses the Seaborn **Tips** dataset, containing 244 restaurant transactions.
It includes total bill, tip, day, meal time, party size, and smoker status. Monetary values
are in US dollars (USD).

## Questions explored
1. How are restaurant bills distributed?
2. How do tip amounts differ across days?
3. Is a larger bill associated with a larger tip?
4. Which numerical variables have the strongest relationships?

## Chart takeaways

1. **Histogram — Distribution of total bills:** The distribution is right-skewed: most bills
   are in the lower-to-middle range, with fewer high-value bills. The median bill is
   $17.80; the middle 50% span $13.35 to $24.13.

2. **Box plot — Tips by day:** Tip distributions overlap across days, while their medians
   differ. The median tips are:
   Thur: $2.30, Fri: $3.00, Sat: $2.75, Sun: $3.15.
   Differences should be interpreted cautiously because the number of observations per day varies.

3. **Scatter plot — Total bill vs. tip:** There is a positive association between total bill
   and tip. The Pearson correlation is 0.68, meaning larger bills tend to be
   associated with larger tips; this does not establish causation. Meal time is shown by colour.

4. **Correlation heatmap — Relationships among numerical variables:** The strongest
   off-diagonal correlation in absolute value is between **total_bill** and
   **tip** (r = 0.68). Correlation describes linear association,
   not causation.

## Files included
- `project_02_visualization.ipynb` — executable Jupyter notebook.
- `project_02_visualization.py` — Python script version.
- `tips.csv` — dataset used by the notebook and script.
- `tips_visualization_dashboard.png` — four-chart dashboard exported at 150 DPI.
- `submission_notes.md` — this report and the chart takeaways.

## How to run
Keep the notebook/script and `tips.csv` in the same folder. Install dependencies with:

```bash
pip install pandas numpy matplotlib seaborn jupyter
```

Open the notebook in Jupyter or Google Colab. The notebook reads the included local CSV,
so it does not need to download the dataset from the internet.
