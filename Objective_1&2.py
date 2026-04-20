
# OBJECTIVE 1: TREND OVER TIME
df = df.sort_values("Start_Date")

plt.figure(figsize=(10,5))
sns.lineplot(x="Start_Date", y="Data Value", data=df, marker='o')
plt.title("Air Quality Trend Over Time")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# OBJECTIVE 2: DISTRIBUTION
plt.figure(figsize=(8,5))
sns.histplot(df["Data Value"], bins=30, kde=True)
plt.title("Distribution of Data Values")
plt.show()
