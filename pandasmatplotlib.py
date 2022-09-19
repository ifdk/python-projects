import pandas as pd
from matplotlib import pyplot as plt

# Very similar to multiplot.py
# taken from https://medium.com/analytics-vidhya/visualizing-historical-stock-price-and-volume-from-scratch-46029b2c5ef9
# Read data file
columns = ["Date", "Adj Close", "Volume"]
df = pd.read_csv("MSFT.csv", usecols=columns)

# Example of getting a subset of columns
# get array of just the dates and volumes
# volume_data = df[['Date', 'Volume']]
# get array of just the dates and adjusted closing prices
# price_data = df[['Date', 'Adj Close']]

# The strategy is to use the left and right verticals as separate y axes

# first, get the subplots (without any parameters) which returns
# the y axis of the two plots; the relative heights of the 2 plots is 1:3
fig, axes = plt.subplots(2, 1, gridspec_kw={'height_ratios': [3, 1]})
fig.tight_layout(pad=3)  # padding

second_plot_axis = axes[0]
first_plot_axis = axes[1]
date_data = df["Date"]
price_data = df["Adj Close"]
volume_data = df["Volume"]

color = 'tab:red'
second_plot_axis.set_xlabel('Date')
second_plot_axis.set_ylabel('Closing Price', color=color)
# line graph
second_plot_axis.plot(date_data, price_data, color=color)
second_plot_axis.tick_params(axis='y', labelcolor=color)

color = 'tab:blue'
first_plot_axis.set_ylabel('Volume', color=color)  # we already handled the x-label with ax1
# right_axis.plot(date_data, volume_data, color=color)
# volume bars
first_plot_axis.bar(date_data, volume_data, color=color)
first_plot_axis.tick_params(axis='y', labelcolor=color)

fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.show()
