import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv('final_data/deaths_tests_cases_scandinavian.csv')
df.fillna(0)

countries = ['Sweden','Denmark','Finland','Iceland','Norway',]
new_df = df.loc[(df['location']=='Sweden')|(df['location']=='Denmark')|(df['location']=='Finland')
    |(df['location']=='Iceland')|(df['location']=='Norway')][['date','location','excess_mortality']].copy()

countries = ['Sweden','Denmark','Finland','Iceland','Norway',]
fig = go.Figure()

for country in countries:
    data = new_df.loc[new_df['location']==country].copy()
    data.dropna(inplace=True)

    data['excess'] = data['excess_mortality'].rolling(7).mean()
    if country != 'Sweden':
        fig.add_trace(go.Scatter(x=data['date'], y=data['excess'], name=country))
    else: 
        fig.add_trace(go.Scatter(x=data['date'], y=data['excess'], name=country,line=dict(width=4)))



# style
fig.update_traces(hoverinfo="x+name+y")
fig.update_layout(hovermode="x", height=500, width=1000, template='plotly_white',
    title = {'text': "Smoothed excess mortality during first 3 pandemic waves"}, titlefont={"size": 25,'color':'black'},
    yaxis={'tickfont':{"size": 15}},xaxis={'tickfont':{"size": 15}},legend_title_text='Country',legend={'font':{'size':15}},
    xaxis_range = ['2020-03-15','2021-06-17']
)
fig.update_xaxes(title_text = "Date", title_font = {"size": 20,'color':'black'})
fig.update_yaxes(title_text = "Excess mortality", title_font = {"size": 20,'color':'black'})

fig.show()
#fig.write_html('excess_mortality.html')
