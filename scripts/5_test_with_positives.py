import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv('final_data/deaths_tests_cases_scandinavian.csv')
df = df.loc[df['location']=='Sweden'] 
new_df = df[['date','positive_rate','new_tests']].copy()
new_df.dropna(inplace=True)

new_df['smoothed_tests'] = new_df['new_tests'].rolling(7).mean()
new_df['smoothed_positives'] = new_df['positive_rate'].rolling(7).mean()

new_df['positive_percent'] = new_df['smoothed_tests']*new_df['smoothed_positives']


fig = go.Figure()

# data
fig.add_trace(go.Scatter(x=new_df['date'], y=new_df['smoothed_tests'], name='Tests performed'))
fig.add_trace(go.Scatter(x=new_df['date'], y=new_df['positive_percent'], name='Positive'))

# style
fig.update_traces(hoverinfo="x+name+y")
fig.update_layout(hovermode="x", height=600, width=1000, template='none',
    title = {'text': "Tests"}, titlefont={"size": 25,'color':'black'},
    yaxis={'tickfont':{"size": 15}},xaxis={'tickfont':{"size": 15}},legend={'font':{'size':15}},
)
fig.update_xaxes(title_text = "Date", title_font = {"size": 20,'color':'black'})
fig.update_yaxes(title_text = "Number of tests", title_font = {"size": 20,'color':'black'})

#fig.show()
fig.write_html('tests.html')

