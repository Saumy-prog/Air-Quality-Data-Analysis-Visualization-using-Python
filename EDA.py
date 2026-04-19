sns.set_style("whitegrid")

df = pd.read_csv(r"D:\MAFIA\Python.py\Air_Quality.csv")

print(df.head())
print(df.info())

# DATA CLEANING
df["Start_Date"] = pd.to_datetime(df["Start_Date"], errors='coerce')
df["Data Value"] = pd.to_numeric(df["Data Value"], errors='coerce')

df = df.dropna(subset=["Data Value"])

# BASIC STATS (NumPy)
print("Mean:", np.mean(df["Data Value"]))
print("Median:", np.median(df["Data Value"]))
print("Std Dev:", np.std(df["Data Value"]))
