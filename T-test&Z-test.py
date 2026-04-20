# OBJECTIVE 8: T-TEST
sample1 = df["Data Value"].sample(100)
sample2 = df["Data Value"].sample(100)

t_stat, p_val = stats.ttest_ind(sample1, sample2)

print("\nT-Test Results:")
print("T-Statistic:", t_stat)
print("P-Value:", p_val)

# OBJECTIVE 9: Z-TEST (MANUAL)
mean = np.mean(df["Data Value"])
std = np.std(df["Data Value"])
n = len(df["Data Value"])

# Assume population mean (example)
pop_mean = 50  

z_score = (mean - pop_mean) / (std / np.sqrt(n))

print("\nZ-Test Results:")
print("Z-Score:", z_score)
