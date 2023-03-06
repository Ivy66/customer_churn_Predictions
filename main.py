import inline as inline
import matplotlib  # used for creating plots and visualizations
import numpy  # used for scientific computing and numeric operations
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  # creates visualizations
import pandas_profiling  # used to get missing values, unique values, minimum value, maximum value  etc
import plotly.offline as po  # creating interactive plots and graphs
import plotly.graph_objs as go

# loading the Excel file
df = pd.read_excel("venv/Telco_customer_churn.xlsx")
# generates the number of columns and rows in a dataset
df.shape
# convert string values(yes and no) to 0 and 1
df.loc[df['Churn Label'] == 'No', 'Churn'] = 0
df.loc[df['Churn Label'] == 'Yes', 'Churn'] = 1

# convert the "no internet service" to "no" for the following columns
cols = ['Online Backup', 'Streaming Movies', 'Device Protection', 'Tech Support', 'Online Security', 'Streaming TV']
for i in cols:
    df[i] = df[i].replace({'No internet service': 'No'})
# replace all the spaces with null values
df['Total Charges'] = df["Total Charges"].replace(" ", np.NaN)

# drop all null values of total charges
df = df[df["Total Charges"].notnull()]
df = df.reset_index()[df.columns]

# Generate a profile report
report = pandas_profiling.ProfileReport(df)
report.to_file('report.html')
