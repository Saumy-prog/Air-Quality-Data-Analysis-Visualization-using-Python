# OBJECTIVE 5: SCATTER PLOT
plt.figure(figsize=(8,5))
sns.scatterplot(x="Indicator ID", y="Data Value", data=df)
plt.title("Indicator ID vs Data Value")
plt.show()

# OBJECTIVE 6: CORRELATION HEATMAP
plt.figure(figsize=(6,5))
corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()
