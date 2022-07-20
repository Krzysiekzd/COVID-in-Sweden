import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv('final_data/icu_and_deaths_by_age.csv')

fig = go.Figure()

# data
fig.add_trace(go.Bar(x=df['age_group'],y=df['male_icu'],name='Males ICU'))
fig.add_trace(go.Bar(x=df['age_group'],y=df['female_icu'],name='Females ICU'))


# style
fig.update_traces(hoverinfo="y")
fig.update_layout(hovermode="x", height=600, width=850, template='plotly_white',
    title = {'text': "Demographics of Covid ICU patients in Sweden"}, titlefont={"size": 25,'color':'black'},
    yaxis={'tickfont':{"size": 15}},xaxis={'tickfont':{"size": 15}},
)
fig.update_xaxes(title_text = "Age group", title_font = {"size": 20,'color':'black'})
fig.update_yaxes(title_text = "Number of patients", title_font = {"size": 20,'color':'black'})


fig.show()
#fig.write_html('icu_demographics.html')
