import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv('final_data/cases_and_deaths_scandinavian.csv')
df.fillna(0)
df['smoothed_cases'] = df['New_cases'].rolling(7).mean()

fig = go.Figure()
# data
fig.add_trace(go.Scatter(x=df['Date_reported'], y=df.loc[df['Country'] == 'Sweden']['smoothed_cases']))
# first wave
fig.add_shape(type="line", x0='2020-03-26', y0=0, x1='2020-03-26', y1=41000,line=dict(color="DeepSkyBlue",width=2))
fig.add_shape(type="line", x0='2020-07-24', y0=0, x1='2020-07-24', y1=41000,line=dict(color="DeepSkyBlue",width=2))
# second wave
fig.add_shape(type="line", x0='2020-10-13', y0=0, x1='2020-10-13', y1=41000,line=dict(color="Tomato",width=2))
fig.add_shape(type="line", x0='2021-02-09', y0=0, x1='2021-02-09', y1=41000,line=dict(color="Tomato",width=2))
# third wave
fig.add_shape(type="line", x0='2021-02-13', y0=0, x1='2021-02-13', y1=41000,line=dict(color="Violet",width=2))
fig.add_shape(type="line", x0='2021-06-17', y0=0, x1='2021-06-17', y1=41000,line=dict(color="Violet",width=2))
# fourth wave
fig.add_shape(type="line", x0='2021-11-20', y0=0, x1='2021-11-20', y1=41000,line=dict(color="DarkOrchid",width=2))
fig.add_shape(type="line", x0='2022-03-28', y0=0, x1='2022-03-28', y1=41000,line=dict(color="DarkOrchid",width=2))
# annotations
fig.add_annotation(x='2020-05-24', y=35000,text="First wave",showarrow=False, font={"size": 15,'color':'black'})
fig.add_annotation(x='2020-12-10', y=35000,text="Second wave",showarrow=False, font={"size": 15,'color':'black'})
fig.add_annotation(x='2021-04-12', y=35000,text="Third wave",showarrow=False, font={"size": 15,'color':'black'})
fig.add_annotation(x='2021-12-20', y=35000,text="Fourth wave",showarrow=True, arrowhead=2, ax=-90, ay=1, font={"size": 15,'color':'black'})
# style
fig.update_traces(hoverinfo="x+y", marker_color=['Red',"Red",'Red'])
fig.update_layout(hovermode="x", height=600, width=1000, template='none',
    title = {'text': "New cases of Covid in Sweden, smoothed"}, titlefont={"size": 25,'color':'black'},
    yaxis={'tickfont':{"size": 15}},xaxis={'tickfont':{"size": 15}},
)
fig.update_xaxes(title_text = "Date", title_font = {"size": 20,'color':'black'})
fig.update_yaxes(title_text = "Cases", title_font = {"size": 20,'color':'black'})

#fig.show()
fig.write_html('sweden_cases.html')
