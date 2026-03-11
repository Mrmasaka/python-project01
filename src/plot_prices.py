import pandas as pd
import matplotlib.pyplot as plt

# 2行ヘッダーのCSVとして読む
data = pd.read_csv(
    "data/spy.csv",
    header=[0, 1],
    index_col=0
)

print("RAW DATA:")
print(data.head())
print(data.columns)

# MultiIndex の列を1階層にする
data.columns = data.columns.get_level_values(0)

# index は日付なので datetime に変換
data.index = pd.to_datetime(data.index)

print("AFTER CLEANUP:")
print(data.head())
print(data.index[:5])
print(data.columns)

plt.figure(figsize=(10, 5))
plt.plot(data.index, data["Close"])

plt.title("SPY Price")
plt.xlabel("Date")
plt.ylabel("Close")
plt.tight_layout()
plt.savefig("charts/spy_price.png")

print("Chart saved to charts/spy_price.png")