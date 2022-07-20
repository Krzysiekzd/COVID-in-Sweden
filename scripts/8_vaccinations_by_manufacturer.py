import plotly.graph_objects as go
# data from vaccination_by_manufacturer_final.csv, 13-05-2022

manufacturers = ['Moderna','AstraZeneca','Pfizer']
values = [3506804,1328722,14907400]

fig = go.Figure()
# data
fig.add_trace(go.Bar(
            x=values,
            y=manufacturers,
            orientation='h'))

# style
fig.update_traces(hoverinfo="x")
fig.update_layout(hovermode="y", height=600, width=1000, template='plotly_white',
    title = {'text': "Vaccinations by manufacturer in Sweden"}, titlefont={"size": 25,'color':'black'},
    yaxis={'tickfont':{"size": 15}},xaxis={'tickfont':{"size": 15}},
)
fig.update_xaxes(title_text = "Number of vaccines", title_font = {"size": 20,'color':'black'})
fig.update_yaxes(title_text = "Manufacturer", title_font = {"size": 20,'color':'black'})


#fig.show()
fig.write_html('vaccines_by_manufacturer.html')
