# OBJECTIVE 7: PIE CHART
location_count = df["Geo Place Name"].value_counts().head(10)

plt.figure(figsize=(6,6))
plt.pie(location_count, labels=location_count.index, autopct="%1.1f%%")
plt.title("Top Locations Distribution")
plt.show()
