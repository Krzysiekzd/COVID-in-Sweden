import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv('final_data/suicides_in_sweden.csv')
df1=df.loc[df['Year']<=2019]
df2=df.loc[df['Year']>2019]

fig = go.Figure()
# data
fig.add_trace(go.Bar(x=df1['Year'],y=df1['Suicide_rate'],showlegend=False))
fig.add_trace(go.Bar(x=df2['Year'],y=df2['Suicide_rate'],showlegend=False))

# style
fig.update_traces(hoverinfo="y")
fig.update_layout(hovermode="x", height=600, width=1000, template='none',
    title = {'text': "Suicide rates in Sweden"}, titlefont={"size": 25,'color':'black'},
    yaxis={'tickfont':{"size": 15}},xaxis={'tickfont':{"size": 15}},
    yaxis_range=[13,21],
)
fig.update_xaxes(title_text = "Year", title_font = {"size": 20,'color':'black'},dtick=1)
fig.update_yaxes(title_text = "Suicides per 100.000 people", title_font = {"size": 20,'color':'black'})


#fig.show()
fig.write_html('sweden_suicides.html')
