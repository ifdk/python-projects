import pandas as pd
import matplotlib.pyplot as mp

# take data
data = pd.read_csv("MSFT.csv")

data = data.head(1259)

df = pd.DataFrame(data, columns=["Date", "Adj Close"])

df.plot(x="Date", y=["Adj Close"], kind="line", figsize=(11, 8))

mp.show()
