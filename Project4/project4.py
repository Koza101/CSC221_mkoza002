import requests
import plotly.express as px

url = "https://api.fiscaldata.treasury.gov/services/api/fiscal_service/v1/debt"
url += "/mspd/mspd_table_1?sort=-record_date"
r = requests.get(url)

#Added a little bit of error handling in case of a bad response
if r.status_code == 200:
    response_dict = r.json()
    
    # Process the .json data
    treas_dict = response_dict['data']
    
    # A dictionary to store public debt amounts by date
    debt_by_date = {}
    
    # Iterate through each record in the data
    for data in treas_dict:
        date = data['record_date']
        debt = float(data['debt_held_public_mil_amt'])
        
        # Summing duplicate debt amounts by date
        if date in debt_by_date:
            debt_by_date[date] += debt
        else:
            debt_by_date[date] = debt
    
    # Sort dates and debt amounts for plotting
    sorted_dates = sorted(debt_by_date.keys())
    sorted_debts = [debt_by_date[date] for date in sorted_dates]
    
    #Make visualization
    title = "US Treasury Monthly Public Debt Over Time"
    labels={'x': 'Date', 'y': 'Public Debt (Millions USD)'}
    fig = px.bar(x=sorted_dates, y=sorted_debts, labels=labels, title=title)

    fig.show()

else:
    print("Failed to retrieve data", r.status_code)
    