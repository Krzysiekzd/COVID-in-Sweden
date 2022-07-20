import plotly.graph_objects as go
import pandas as pd
df = pd.read_csv('final_data/deaths_demography.csv')

y_age = df['Age']
x_M = df['Men']
x_F = df['Women'] * -1


fig = go.Figure()
  
fig.add_trace(go.Bar(y= y_age, x = x_M, name = 'Male', orientation = 'h'))
fig.add_trace(go.Bar(y = y_age, x = x_F, name = 'Female', orientation = 'h'))
  

fig.update_layout(hovermode="y", height=600, width=1000, template='plotly_white',
    title = {'text': "Demographics of Covid deaths in Sweden"}, titlefont={"size": 25,'color':'black'},
    yaxis={'tickfont':{"size": 15}},
    barmode = 'relative', bargap = 0.0, bargroupgap = 0,
    xaxis = dict(tickvals = [-2500,-2000,-1500,-1000,-500,0,500,1000,1500,2000,2500],  
        ticktext = [2500,2000,1500,1000,500,0,500,1000,1500,2000,2500],
        title_font_size = 14,tickfont={"size": 15}),xaxis_range=[-2500,2500],
)  
fig.update_xaxes(title_text = "Deaths", title_font = {"size": 20,'color':'black'},dtick=1)
fig.update_yaxes(title_text = "Age group", title_font = {"size": 20,'color':'black'})
#fig.show()
fig.write_html('deaths_pyramid.html')
