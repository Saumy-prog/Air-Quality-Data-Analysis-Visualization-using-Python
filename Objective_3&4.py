# OBJECTIVE 3: TOP LOCATIONS
top_places = df.groupby("Geo Place Name")["Data Value"].mean().sort_values(ascending=False).head(10)

plt.figure(figsize=(10,5))
sns.barplot(x=top_places.index, y=top_places.values)
plt.title("Top 10 Locations")
plt.xticks(rotation=75)
plt.show()

# OBJECTIVE 4: BOXPLOT
plt.figure(figsize=(10,5))
sns.boxplot(x="Name", y="Data Value", data=df)
plt.title("Air Quality by Indicator")
plt.xticks(rotation=75)
plt.show()
