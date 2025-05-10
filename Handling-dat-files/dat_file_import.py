import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO

# Step 1: Read the file
with open("C:/Users/sandi/Desktop/coding/python/numpy/IV trial2.txt", "r", encoding="utf-8", errors="ignore") as f:
    lines = f.readlines()

# Step 2: Filter lines that look like numeric data (tab/space separated)
numeric_lines = []
for line in lines:
    parts = line.strip().split()
    if len(parts) >= 2 and all(p.replace('.', '', 1).replace('-', '', 1).isdigit() for p in parts[:2]):
        numeric_lines.append(line.strip())   # output is like this'301.2800000000\t304.2100000000\t0.0000000000\t17.0000000000\t0.0000013810\t0.0064602254\t12.3883095000\t0.1708663750\t-0.0031798587', '301.2800000000\t304.2200000000\t0.0000000000\t17.0000000000\t0.0000014010\t0.0066176253\t12.1196605000\t0.1733854850\t-0.0092099830', '301.2800000000\t304.2500000000\t0.0000000000\t17.0000000000\t0.0000014210\t0.0067508313\t11.5270815000\t0.1759343600\t0.0084643207',

# print(numeric_lines)
# # # Step 3: Convert to DataFrame
data_str = "\n".join(numeric_lines)  #each lines in row
df = pd.read_csv(StringIO(data_str), sep="\t", header=None)  #this will make it like csv file and it is easier to deal with

# print(df)

# Step 4: Extract Temp and R columns (adjust indexes if needed)
current = df[4]  # current column
voltage = df[7]  # Resistance column

# Step 5: Plot
plt.figure(figsize=(8, 5))
plt.plot(current, voltage, marker='o', linestyle='-')
plt.xlabel("Current(A)")
plt.ylabel("Voltage(V)")
plt.title("Current vs Voltage")
plt.tight_layout()
plt.show()