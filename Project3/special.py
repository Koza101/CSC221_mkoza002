#Data for graph was pulled from Zillow.com
# It shows typical 4 bedroom home prices within the 35th to 65th percentile collected over the last ~25 years for every city in the U.S
#I am only pulling the data for Plattsburgh, NY

import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.ticker import FuncFormatter

def currency(y, pos):
    """The y argument is the axis value and pos is the tick position."""
    return '${:,.0f}'.format(y)  # Returns the y axis values with currency formatting: $xxx,xxx


data = pd.read_csv(r"C:\Users\Mason\iCloudDrive\SUNY PLATTSBURGH\Spring_24\CSC_221\Project3\Zip_zhvi_bdrmcnt_4_uc_sfrcondo_tier_0.33_0.67_sm_sa_month.csv")

row = data.iloc[3675] #specifies integer location for collected data. Row 3675 in my .csv

date_columns = row.index[10:]  #Specifies starting columb of dates in .csv
prices = row[10:].values

# Convert index to python datetime objects and reset index
# Added because dates are in horizontal array within .csv. Matplotlib expects vertical array
plot_data = pd.DataFrame({
    'Date': pd.to_datetime(date_columns, format='%Y-%m-%d'),
    'Price': prices
})

plt.style.use('seaborn-v0_8-dark')
plt.figure(figsize=(20, 10))
plt.plot(plot_data['Date'], plot_data['Price'], marker='+', linestyle='-')
plt.title('Median 4 Bedroom Home Prices Over Time for Plattsburgh, NY', fontsize=15, color="blue")
plt.xlabel('Date', fontsize=20)
plt.ylabel('Home Price', fontsize=20)
plt.gca().yaxis.set_major_formatter(FuncFormatter(currency)) #Method to call currency function
plt.grid(True)
plt.show()
