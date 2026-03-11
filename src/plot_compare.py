import pandas as pd
import matplotlib.pyplot as plt


def load_price_csv(path: str) -> pd.DataFrame:
    data = pd.read_csv(
        path,
        header=[0, 1],
        index_col=0
    )

    data.columns = data.columns.get_level_values(0)
    data.index = pd.to_datetime(data.index)

    return data


spy = load_price_csv("data/spy.csv")
qqq = load_price_csv("data/qqq.csv")
vti = load_price_csv("data/vti.csv")

plt.figure(figsize=(10, 5))

plt.plot(spy.index, spy["Close"], label="SPY")
plt.plot(qqq.index, qqq["Close"], label="QQQ")
plt.plot(vti.index, vti["Close"], label="VTI")

plt.title("SPY vs QQQ vs VTI")
plt.xlabel("Date")
plt.ylabel("Close Price")
plt.legend()

plt.tight_layout()
plt.savefig("charts/compare_prices.png")

print("Saved to charts/compare_prices.png")