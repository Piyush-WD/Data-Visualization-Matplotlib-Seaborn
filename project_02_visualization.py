"""
Project 02: Data Visualization with Matplotlib & Seaborn
Run from the folder containing this script and tips.csv.
"""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

DATA_FILE = Path(__file__).with_name("tips.csv")
OUTPUT_FILE = Path(__file__).with_name("tips_visualization_dashboard.png")

tips = pd.read_csv(DATA_FILE)
sns.set_theme(style="whitegrid", palette="deep")

fig, axes = plt.subplots(2, 2, figsize=(12, 9), constrained_layout=True)
fig.suptitle("Restaurant Tips Dataset — Data Visualization Dashboard",
             fontsize=16, fontweight="bold")

sns.histplot(data=tips, x="total_bill", bins=20, color="#3569a8",
             edgecolor="white", ax=axes[0, 0])
axes[0, 0].set(title="Most bills are concentrated in the lower range",
               xlabel="Total bill (USD)", ylabel="Number of meals")

sns.boxplot(data=tips, x="day", y="tip", order=["Thur", "Fri", "Sat", "Sun"],
            color="#79a6d2", ax=axes[0, 1])
axes[0, 1].set(title="Tip amounts vary across days",
               xlabel="Day of week", ylabel="Tip (USD)")

sns.scatterplot(data=tips, x="total_bill", y="tip", hue="time",
                palette={"Lunch": "#2a9d8f", "Dinner": "#e76f51"},
                alpha=0.8, ax=axes[1, 0])
axes[1, 0].set(title="Larger bills generally come with larger tips",
               xlabel="Total bill (USD)", ylabel="Tip (USD)")
axes[1, 0].legend(title="Meal time")

numeric_corr = tips.select_dtypes(include="number").corr()
sns.heatmap(numeric_corr, annot=True, fmt=".2f", cmap="Blues",
            vmin=-1, vmax=1, square=True, linewidths=0.5, ax=axes[1, 1])
axes[1, 1].set_title("Correlation between numerical variables")

fig.savefig(OUTPUT_FILE, dpi=150, bbox_inches="tight")
plt.show()
print(f"Dashboard saved to: {OUTPUT_FILE}")
