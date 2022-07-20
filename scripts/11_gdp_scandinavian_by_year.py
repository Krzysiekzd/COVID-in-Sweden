import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv('final_data/gdp.csv')
fig = go.Figure()

# data
countries = ['Sweden','Denmark','Finland','Iceland','Norway',]
years_num = list(range(2011,2021))
years = [str(i) for i in years_num]

for country in countries:
    gdp = []
    data = df.loc[df['Country Name']==country]
    for year in years:
        gdp.append(data[year].tolist()[0])
    fig.add_trace(go.Scatter(x=years, y=gdp, name=country))
# style
fig.update_traces(hoverinfo="x+name+y")
fig.update_layout(hovermode="x", height=600, width=1000, template='none',
    title = {'text': "GDP by year"}, titlefont={"size": 25,'color':'black'},
    yaxis={'tickfont':{"size": 15}},xaxis={'tickfont':{"size": 15}},legend_title_text='Country',legend={'font':{'size':15}},
)
fig.update_xaxes(title_text = "Year", title_font = {"size": 20,'color':'black'})
fig.update_yaxes(title_text = "GDP", title_font = {"size": 20,'color':'black'})

fig.show()
#fig.write_html('gdp.html')

