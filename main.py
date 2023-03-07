import inline as inline
import matplotlib
import numpy
import numpy as np
import pandas as pd
import plotly
import matplotlib.pyplot as plt
import seaborn as sns
import pandas_profiling
import plotly.graph_objs as go
from plotly.graph_objs import pie, Layout, Figure
import plotly.offline as pyo
import plotly.colors as colors

df = pd.read_excel("venv/Telco_customer_churn.xlsx")
df.shape
df.loc[df['Churn Label'] == 'No', 'Churn'] = 0
df.loc[df['Churn Label'] == 'Yes', 'Churn'] = 1

cols = ['Online Backup', 'Streaming Movies', 'Device Protection', 'Tech Support', 'Online Security', 'Streaming TV']
for i in cols:
    df[i] = df[i].replace({'No internet service': 'No'})

df['Total Charges'] = df["Total Charges"].replace(" ", np.NaN)

df = df[df["Total Charges"].notnull()]
df = df.reset_index()[df.columns]

df["Total Charges"] = df["Total Charges"].astype(float)
df["Churn"].value_counts().values

plot_by_Churn_Labels = df["Churn"].value_counts().keys().tolist()
plot_by_Churn_values = df["Churn"].value_counts().values.tolist()


# visualize the code
plot_by_Churn_Labels = df["Churn"].value_counts().keys().tolist()
plot_by_Churn_values = df["Churn"].value_counts().values.tolist()

plot_data = [go.Pie(labels=plot_by_Churn_Labels,
                    values=plot_by_Churn_values,
                    marker=dict(colors=['Magenta', 'Grey'],
                                line=dict(color="white",
                                          width=1.5)),
                    rotation=90,
                    hoverinfo="label+value+text",
                    hole=.6)
             ]
plot_layout = go.Layout(dict(title="Customer Churn ",
                             plot_bgcolor="rgb(243, 243, 243)",
                             paper_bgcolor="rgb(243, 243, 243)", ))
fig = go.Figure(data=plot_data, layout=plot_layout)
fig.show()

report = pandas_profiling.ProfileReport(df)
report.to_file('report.html')
