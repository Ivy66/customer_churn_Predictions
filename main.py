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

# visualize total customer Churn
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
                             plot_bgcolor="rgb(189, 167, 242)",
                             paper_bgcolor="rgb(189, 167, 242)", ))
fig = go.Figure(data=plot_data, layout=plot_layout)
fig.show

# visualize the churn rate for male and female
plot_by_gender = df.groupby('Gender').Churn.mean().reset_index()
plot_data = [go.Bar(x=plot_by_gender['Gender'],
                    y=plot_by_gender['Churn'],
                    width=[0.4, 0.4],
                    marker=dict(color=['red', 'yellow'])
                    )
             ]
plot_layout = go.Layout(
    xaxis={"type": "category"},
    yaxis={"title": "churn Rate"},
    title='churn Rate by Gender',
    plot_bgcolor='rgb(189, 167, 242)',
    paper_bgcolor="rgb(189, 167, 242)",
)
fig = go.Figure(data=plot_data, layout=plot_layout)
fig.show()

# visualize the churn rate by internet Service
plot_by_internet_service = df.groupby('Internet Service').mean().reset_index()
plot_data = [go.Bar(x=plot_by_internet_service['Internet Service'],
                    y=plot_by_internet_service['Churn'],
                    width=[0.4, 0.4, 0.4],
                    marker=dict(color=['red', 'yellow', 'magenta'])
                    )
             ]
plot_layout = go.Layout(
    xaxis={"type": "category"},
    yaxis={"title": "churn Rate"},
    title='churn Rate by Internet Service',
    plot_bgcolor='rgb(189, 167, 242)',
    paper_bgcolor="rgb(189, 167, 242)",
)
fig = go.Figure(data=plot_data, layout=plot_layout)
fig.show()
# visualize churn rate by payment method
plot_by_payment_method = df.groupby('Payment Method').mean().reset_index()
plot_data = [go.Bar(x=plot_by_payment_method['Payment Method'],
                    y=plot_by_payment_method['Churn'],
                    width=[0.4, 0.4, 0.4],
                    marker=dict(color=['red', 'yellow', 'teal', 'blue'])
                    )
             ]
plot_layout = go.Layout(
    xaxis={"type": "category"},
    yaxis={"title": "churn Rate"},
    title='churn Rate by Payment Method',
    plot_bgcolor='rgb(189, 167, 242)',
    paper_bgcolor="rgb(189, 167, 242)",
)
fig = go.Figure(data=plot_data, layout=plot_layout)
fig.show()
# Visualization by Tech Support
plot_by_Tech_Support = df.groupby('Tech Support').mean().reset_index()
plot_data = [go.Bar(x=plot_by_Tech_Support['Tech Support'],
                    y=plot_by_Tech_Support['Churn'],
                    width=[0.4, 0.4, 0.4],
                    marker=dict(color=['teal', 'blue'])
                    )
             ]
plot_layout = go.Layout(
    xaxis={"type": "category"},
    yaxis={"title": "churn Rate"},
    title='churn Rate by Tech Support',
    plot_bgcolor='rgb(189, 167, 242)',
    paper_bgcolor="rgb(189, 167, 242)",
)
fig = go.Figure(data=plot_data, layout=plot_layout)
fig.show()

report = pandas_profiling.ProfileReport(df)
report.to_file('report.html')
