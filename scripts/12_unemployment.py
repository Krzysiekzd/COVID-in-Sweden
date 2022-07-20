import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv('final_data/unemployment_sweden.csv')

fig = go.Figure()

# data
minus = df.loc[df['annual_change']<0]
plus = df.loc[df['annual_change']>0]

fig.add_trace(go.Scatter(x=df['year'],y=df['unemployment_rate'],name='Unemployment Rate'))

fig.add_trace(go.Bar(x=minus['year'],y=minus['annual_change'],name='Negative annual change'))
fig.add_trace(go.Bar(x=plus['year'],y=plus['annual_change'],name='Positive annual change'))


# style
fig.update_traces(hoverinfo="y+x")
fig.update_layout(hovermode="x", height=600, width=1100, template='plotly_white',
    title = {'text': "Unemployment rate in Sweden by year"}, titlefont={"size": 25,'color':'black'},
    yaxis={'tickfont':{"size": 15}},xaxis={'tickfont':{"size": 15}},colorway=['#2c2ea3','#37bd56',"#b5342f",]
)
fig.update_xaxes(title_text = "Year", title_font = {"size": 20,'color':'black'},dtick=1)
fig.update_yaxes(title_text = "Rate in %", title_font = {"size": 20,'color':'black'})


fig.show()
#fig.write_html('unemployment.html')
