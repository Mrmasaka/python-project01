import pandas as pd
import matplotlib.pyplot as plt


def load_price_csv(path):

    data = pd.read_csv(
        path,
        header=[0,1],
        index_col=0
    )

    data.columns = data.columns.get_level_values(0)
    data.index = pd.to_datetime(data.index)

    return data

spy = load_price_csv("data/spy.csv")
qqq = load_price_csv("data/qqq.csv")
vti = load_price_csv("data/vti.csv")

spy_returns = spy["Close"].pct_change()
qqq_returns = qqq["Close"].pct_change()
vti_returns = vti["Close"].pct_change()

spy_cum = (1 + spy_returns).cumprod()
qqq_cum = (1 + qqq_returns).cumprod()
vti_cum = (1 + vti_returns).cumprod()

plt.figure(figsize=(10,5))

plt.plot(spy_cum*100, label="SPY")
plt.plot(qqq_cum*100, label="QQQ")
plt.plot(vti_cum*100, label="VTI")

print("Average Daily Returns:")

returns = {
    "SPY": spy_returns.mean(),
    "QQQ": qqq_returns.mean(),
    "VTI": vti_returns.mean()
}

for ticker, r in returns.items():
    print(f"{ticker}{r*100:.3f}%")

plt.title("Cumulative Returns")
plt.xlabel("Date")
plt.ylabel("Growth")

plt.legend()

plt.savefig("charts/cumulative_returns.png")

print("Saved to charts/cumulative_returns.png")