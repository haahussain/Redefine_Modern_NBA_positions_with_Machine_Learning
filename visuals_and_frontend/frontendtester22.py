#!/usr/bin/env python
# coding: utf-8

# In[1]:


#frontend


# In[158]:


import plotly.express as px
import pandas as pd 
from chart_studio.plotly import iplot as py
import plotly.graph_objects as go
import streamlit as st
from PIL import Image


# In[159]:


dfclust=pd.read_csv('dfclustzzz.csv')


# In[160]:


dfclustz=dfclust.groupby('Pos').mean()


# In[161]:


dfclustz.reset_index(inplace=True)


# In[162]:


image = Image.open('NBA_logo.png')

st.image(image, use_column_width=True)


# In[163]:


st.title('Reassigning Modern NBA Positions by Playing Style/Team Role')
st.subheader('Conventional NBA positions no longer reflect what type of player is on the court. The purpose of this project is to redefine NBA roles that better fit the players style and functionality by using K-Means Clustering')


# In[164]:


st.title('Visualizations for Conventional NBA positions')
image2= Image.open('old_basketball.png')
st.image(image2, use_column_width=True)


# In[165]:


st.header('2011-2019 BoxScore Stats by Positions')
label = dfclustz['Pos']
points = dfclustz['PTS']
assists = dfclustz['AST']
rebounds = dfclustz['TRB']
threept = dfclustz['3P%']
blocks = dfclustz['BLK']
steals = dfclustz['STL']
fig = go.Figure()
fig.add_trace(go.Bar(x=label,
                y= points,
                name='Points',
                marker_color='rgb(55, 83, 109)'
                ))
fig.add_trace(go.Bar(x=label,
                y=assists,
                name='Assists',
                marker_color='rgb(26, 118, 255)'
                ))
fig.add_trace(go.Bar(x=label,
                y=rebounds,
                name='Rebounds',
                marker_color='rgb(100, 50, 300)'
                ))
fig.add_trace(go.Bar(x=label,
                y=threept,
                name='ThreePt %',
                marker_color='rgb(400, 5, 60)'
                ))
fig.add_trace(go.Bar(x=label,
                y=blocks,
                name='Blocks',
                marker_color='rgb(150, 160, 200)'
                ))
fig.add_trace(go.Bar(x=label,
                y=steals,
                name='Steals',
                marker_color='rgb(40, 250, 100)'
                ))
fig.update_layout(
    title='BoxScore Stats',
    xaxis_tickfont_size= 10,
    yaxis=dict(
        title='Average',
        titlefont_size=16,
        tickfont_size=14,
    ),
    xaxis=dict(
        title='Positions'
    ),
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    barmode='group',
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)
st.write(fig)


# In[166]:


dfclustR=pd.read_csv('dfRolezzz.csv')


# In[167]:


dfclustzr=dfclustR.groupby('Role').mean()


# In[168]:


dfclustzr.reset_index(inplace=True)


# In[169]:


st.header('2011-2019 Leaguewide Conventional Position Percentages')
labels = dfclustR.Pos.unique()
values = dfclustR['Pos'].value_counts(normalize=False)

fig5 = go.Figure(data =[go.Pie(labels=labels, values=values)])
fig5.update_layout(
    title='Positions',
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    barmode='group',
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)
st.write(fig5)


# In[170]:


dfpospca=pd.read_csv('dfpospcazzz.csv')


# In[171]:


st.header('2011-2019 Conventional NBA position clusters ')
fig2 = px.scatter_3d(dfpospca, x='PC 1', y='PC 2', z='PC 3', color='Pos',
              )
st.write(fig2)


# In[172]:


st.title('Results After Clustering New Roles')
image3= Image.open('lebron.png')
st.image(image3, use_column_width=True)


# In[173]:


st.header('2011-2019 BoxScore Stats by New Roles')
label = dfclustzr['Role']
points = dfclustzr['PTS']
assists = dfclustzr['AST']
rebounds = dfclustzr['TRB']
threept = dfclustzr['3P%']
blocks = dfclustzr['BLK']
steals = dfclustzr['STL']
fig1 = go.Figure()
fig1.add_trace(go.Bar(x=label,
                y= points,
                name='Points',
                marker_color='rgb(55, 83, 109)'
                ))
fig1.add_trace(go.Bar(x=label,
                y=assists,
                name='Assists',
                marker_color='rgb(26, 118, 255)'
                ))
fig1.add_trace(go.Bar(x=label,
                y=rebounds,
                name='Rebounds',
                marker_color='rgb(100, 50, 300)'
                ))
fig1.add_trace(go.Bar(x=label,
                y=threept,
                name='Threept %',
                marker_color='rgb(400, 5, 60)'
                ))
fig1.add_trace(go.Bar(x=label,
                y=blocks,
                name='Blocks',
                marker_color='rgb(150, 160, 200)'
                ))
fig1.add_trace(go.Bar(x=label,
                y=steals,
                name='Steals',
                marker_color='rgb(40, 250, 100)'
                ))
fig1.update_layout(
    title='BoxScore Stats',
    xaxis_tickfont_size= 10,
    yaxis=dict(
        title='Average',
        titlefont_size=16,
        tickfont_size=14,
    ),
    xaxis=dict(
        title='Role'
    ),
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    barmode='group',
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)
st.write(fig1)


# In[174]:


st.header('2011-2019 Leaguewide Player Percentages by Role/Style')
labels = dfclustR.Role.unique()
values = dfclustR['Role'].value_counts(normalize=False)

fig6 = go.Figure(data =[go.Pie(labels=labels, values=values)])
fig6.update_layout(
    title='Roles',
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    barmode='group',
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)
st.write(fig6)


# In[175]:


dfclustpca6=pd.read_csv('dfclustpca6.csv')


# In[176]:


st.header('2011-2019 New Clusters by Role/ Playing Style')
fig3 = px.scatter_3d(dfclustpca6, x='PC1', y='PC2', z='PC3', color='Role',
              )
st.write(fig3)


# In[177]:


st.subheader('What is the difference between Elite teams & Average teams when it comes to player roles/styles')


# In[178]:


st.subheader('Do winning teams have more or less players with a specific style/role. Does roster diversity play a part in winning? ')


# In[179]:


dfAverage=pd.read_csv('dfAverageee.csv')


# In[185]:


st.header("Roster Construction for various 'Average' NBA Teams over the last 4 years")
labels = dfAverage.Role.unique()
values = dfAverage['Role'].value_counts(normalize=False)
colors = ['purple', 'mediumturquoise', 'darkorange', 'green', 'red', 'orange', 'blue', 'yellow', 'pink']

fig8 = go.Figure(data =[go.Pie(labels=['All Star','Elite Wing','3&D', 'Do It All', 'Star Inside Big','Backup Inside Big', 'Superstar','Perimeter Scorer'],
                               values=[11,9,6,5,3,2,1,1])])
fig8.update_layout(
    title='Roles for Average Teams',
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    barmode='group',
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)
fig8.update_traces(
                  marker=dict(colors=colors))
st.write(fig8)


# In[181]:


dfFinals=pd.read_csv('dfFinalsss.csv')


# In[184]:


st.header('Roster Construction for NBA Finals Teams over the last 4 years')
labels = dfFinals.Role.unique()
values = dfFinals['Role'].value_counts(normalize=False)
colors = ['purple', 'mediumturquoise', 'darkorange', 'green', 'navyblue', 'orange', 'blue', 'yellow', 'pink']


fig7 = go.Figure(data =[go.Pie(labels=['All Star','Elite Wing','3&D', 'Do It All', 'Elite Inside Big','Backup Inside Big', 'Superstar','Perimeter Scorer'],
                               values=[11,6,4,1,4,3,7,3])])
fig7.update_layout(
    title='Roles for Elite Teams',
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    barmode='group',
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)
fig7.update_traces(
                  marker=dict(colors=colors))
st.write(fig7)


# In[183]:


st.subheader('Main Takeaway: Overall NBA Finalist teams have more star power and their inside players have a reserved/defined role. In comparison, average NBA teams have less star power and rely on star inside bigs as their focal points.')


# In[ ]:




