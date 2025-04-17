import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
df = pd.read_csv("C:\\Users\\manin\\Downloads\\wb_old.csv")
print(df)
d=df.head(40)
print(d)
df.isnull().sum()
df.dropna(inplace=True)
print("Duplicate rows:", df.duplicated().sum())
df.drop_duplicates(inplace=True)
print(df.describe())
print(df.info())
df['Year_num'] = df['srcYear']
# 1. Lineplot - Average BOD trend over time (all stations)
sb.lineplot(x="Year_num", y="Min BOD", data=df, label="Min BOD")
sb.lineplot(x="Year_num", y="Max BOD", data=df, label="Max BOD")
plt.title("Trend of BOD Levels Over Years")
plt.ylabel("BOD (mg/L)")
plt.xlabel("Year")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
# 2. Barplot - Top 10 states by average Min BOD
top_states_bod = df.groupby("srcStateName")["Min BOD"].mean().nlargest(10).reset_index()
sb.barplot(x="Min BOD", y="srcStateName", data=top_states_bod,hue="srcStateName", palette="magma",legend=False)
plt.title("Top 10 States by Average Min BOD")
plt.xlabel("Avg Min BOD (mg/L)")
plt.ylabel("State")
plt.tight_layout()
plt.show()
# 3. Histogram - Distribution of Min Dissolved Oxygen
sb.histplot(df["Min dissolved oxygen"].dropna(), bins=30, kde=True, color='blue')
plt.title("Distribution of Min Dissolved Oxygen")
plt.xlabel("Dissolved Oxygen (mg/L)")
plt.tight_layout()
plt.show()
#4. pairplot
sc = ['Low pH values','High pH values','Min BOD','Max BOD']
df_selected = df[sc]
sb.set(style="whitegrid", palette="Set2")
sb.pairplot(df_selected, diag_kind="kde", corner=True,plot_kws={'alpha': 0.7, 's': 50, 'edgecolor': 'k'})
plt.suptitle("Pairplot of Selected Water Quality Parameters", y=1.02)
plt.show()
#5. heatmap
selected_cols = ['Low pH values', 'High pH values', 'Min BOD', 'Max BOD','Min dissolved oxygen', 'Max dissolved oxygen','Min conductivity ', 'Max conductivity ']
df_subset = df[selected_cols].apply(pd.to_numeric, errors='coerce').dropna()
corr_subset = df_subset.corr()
plt.figure(figsize=(10, 8))
sb.set_theme(style="white")
sb.heatmap(corr_subset,annot=True,fmt=".2f",cmap="viridis",square=True,linewidths=0.5,cbar_kws={"shrink": 0.8})
plt.title("Heatmap of Selected Water Quality Parameters", fontsize=10, fontweight='bold')
plt.tight_layout()
plt.show()
#6.pie
counts = df['Type of water body'].value_counts()
labels = [f"{k} - {v/sum(counts):.1%}" for k, v in counts.items()]
fig, ax = plt.subplots(figsize=(8, 6))
wedges, _ = ax.pie(counts, startangle=140)
ax.legend(wedges, labels, title="Type of Water Body", loc="center left", bbox_to_anchor=(1, 0.5))
plt.title("Distribution of Water Body Types")
plt.tight_layout()
plt.show()
