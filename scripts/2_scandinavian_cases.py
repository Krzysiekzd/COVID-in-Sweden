import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv('final_data/cases_and_deaths_scandinavian.csv')
df.fillna(0)

df['smoothed_cases'] = df['New_cases'].rolling(7).mean()
fig = go.Figure()

# data
countries = ['Denmark','Finland','Iceland','Norway',]
populations = {'Denmark':5831,'Sweden':10350,'Finland':5531,'Iceland':366.425,'Norway':5379}

fig.add_trace(go.Scatter(x=df['Date_reported'], y=df.loc[df['Country'] == 'Sweden']['smoothed_cases']/populations['Sweden'], name='Sweden',line=dict(width=4)))

for country in countries:
    fig.add_trace(go.Scatter(x=df['Date_reported'], y=df.loc[df['Country'] == country]['smoothed_cases']/populations[country], name=country))

# style
fig.update_traces(hoverinfo="x+name+y")
fig.update_layout(hovermode="x", height=600, width=1200, template='none',
    title = {'text': "New cases of Covid per 1000 people"}, titlefont={"size": 25,'color':'black'},
    yaxis={'tickfont':{"size": 15}},xaxis={'tickfont':{"size": 15}},legend_title_text='Country',legend={'font':{'size':15}},
)
fig.update_xaxes(title_text = "Date", title_font = {"size": 20,'color':'black'})
fig.update_yaxes(title_text = "Cases", title_font = {"size": 20,'color':'black'})

fig.show()
#fig.write_html('scandinavian_cases.html')