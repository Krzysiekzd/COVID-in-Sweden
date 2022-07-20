import pandas as pd
import scipy.stats as st
import numpy as np
import plotly.graph_objects as go


tem = pd.read_csv('final_data/stockholm_temperatures.csv')
cs = pd.read_csv('final_data/cases_and_deaths_scandinavian.csv')
cs = cs.loc[(cs['Country']=='Sweden') & (cs['New_cases']<3000) & (cs['New_cases']>0)] # 3k to look better, but 5k returns -0.47 correlation


temperatures = pd.unique(tem['homo']).tolist()
temperatures.sort()



scatter_temperatures = []
scatter_cases = []
for i in temperatures:
    days = tem.loc[tem['homo']==i]['date'].to_list()
    cases = []
    for day in days:cases.extend(cs.loc[cs['Date_reported']==day]['New_cases'].to_list())
    scatter_cases.extend(cases)
    scatter_temperatures.extend([i,]*len(cases))



fig = go.Figure()
# data
fig.add_trace(go.Scatter(x=scatter_temperatures, y=scatter_cases, mode='markers',line=dict(width=4)))
fig.update_traces(marker=dict(size=12,line=dict(width=1,color='DarkSlateGrey',)),hoverinfo="x+y")
fig.update_layout(hovermode="closest", height=600, width=850, template='none',

    title = {'text': "Temperature vs new Covid cases in Sweden"}, titlefont={"size": 25,'color':'black'},
    yaxis={'tickfont':{"size": 15}},xaxis={'tickfont':{"size": 15}},colorway=['#006699',"#c17607",]
)
fig.update_xaxes(title_text = "Temperature", title_font = {"size": 20,'color':'black'})
fig.update_yaxes(title_text = "Cases", title_font = {"size": 20,'color':'black'})

print(st.pearsonr(scatter_temperatures,scatter_cases)[0])

a,b = np.polyfit(scatter_temperatures,scatter_cases,1)
fig.add_shape(type="line", x0=scatter_temperatures[0], y0=a*scatter_temperatures[0]+b,
     x1=scatter_temperatures[-1], y1=a*scatter_temperatures[-1]+b,line=dict(color="#f90",width=4))
fig.add_annotation(x=15, y=3150,text="-0.47 Pearson correlation coefficient",showarrow=False, font={"size": 18,'color':'#c17607'})

fig.show()
#fig.write_html('sweden_temperatures.html')

        

