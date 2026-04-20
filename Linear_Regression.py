
# OBJECTIVE 10: LINEAR REGRESSION PREDICTION

# Convert date to numeric (ordinal format)
df = df.dropna(subset=["Start_Date"])
df["Date_Ordinal"] = df["Start_Date"].map(pd.Timestamp.toordinal)

# Define X (feature) and y (target)
X = df[["Date_Ordinal"]]
y = df["Data Value"]

# Train model
model = LinearRegression()
model.fit(X, y)

# Predict values
df["Predicted"] = model.predict(X)

# Show sample predictions
print("\nSample Predictions:")
print(df[["Start_Date", "Data Value", "Predicted"]].head())

# Plot actual vs predicted
plt.figure(figsize=(10,5))
plt.scatter(df["Start_Date"], df["Data Value"], label="Actual", alpha=0.5)
plt.plot(df["Start_Date"], df["Predicted"], color='red', label="Regression Line")
plt.title("Linear Regression Prediction")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()

# Predict future date (example)
future_date = pd.to_datetime("2026-01-01")
future_df = pd.DataFrame({
    "Date_Ordinal": [future_date.toordinal()]
})

future_prediction = model.predict(future_df)

print("\nPrediction for 2026-01-01:", future_prediction[0])
