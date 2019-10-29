# Using K-means clustering Algorithm to Redefine NBA positions and Exploring Roster Construction
### Project Description and Motivation 
Conventional positions within the NBA do not accurately reflect the playing style or functional role a player provides to their team. The overall style of play has changed drastically and various era’s within the NBA indicate that. Similarly a players style of play is also reflective of this change. Currently the league is fast paced and with more floor spacing. An example that demonstrates this are Centers who shoot 3's and stretch the floor for their teamms. These centers that are multi-faceted are still grouped with traditional Centers and there is no methodology to distinguish between the two. The purpose of this project is find a better approach to define these players roles based on the value they bring to their team.   

## **Data Source** 
Information was scraped from Basketball-Reference and statistics for every player from 2011 to 2018 were collected. 2011 was used as the initial start year because it reflective of when positionless basketball started to take form (LeBron being the main facilitator in Miami and the start of the Golden State Dynasty). Approximatley 3000 observations were included in the final dataset. 
In total there were 34 features describing each player. Features include box-score metrics such as Points, Rebounds, Blocks, Steals. Advanced metrics were also used. Some examples include : USG%, PER, and Plus-Minus Score. 
All features were defined by a Per-100 possessions unit. This was done to ensure that players statistics were comparable regardless of how many minutes or games they played. 
Players who did not play more than 400 minutes were excluded because they do not have significant impact on the game.   

## **Exploratory Data Analysis**

#### Graph displaying League Average for 3 Pt % over time  

#### Graph displaying League Average for various features (Ortg, Drtg, 3P%) over time

The Above two graphs indicate that the league has changed as efficiency, scoring and amount of 3 pointers taken have increased over time. Which can also indicate player role and style has changed as the different basketball eras continue to evolve.  

#### Graph illustrating average stats for conventional positions. 

This graph cannot tell us about Power_Forwards that are also facilitators or Guards that have multi-demensional roles. 

#### Pie chart showing even distribution of conventional positions

#### Clustering visualization of conventional positions 

Players assigned to the same convetional position are scattered throughout the graph, indcating that they do not have similar playing style.

## **Data Science Methods used**
* Principal Component Analysis (PCA) was used because there are over 30 features. It is impossible to create 3D Clusters wiht so many features. PCA allows me to keep 90 % of the variation within all my features and visualize it in 3 components, hence a 3D model. PCA was used for the visualization of the conventional positions clusters and well as for the new roles after implmenting the k means clustering algorithm.    
* K-means clustering unsupervised clustering algorithm which assigns centroids (n) and then begins to cluster based off of how close the observation is to that centroid. 
* Elbow method and Silhoutte score. In order to figure out how many clusters (new roles) I should go with I used the silhoutte score, which explains the density of each cluster and the seperating from cluster to cluster. The elbow methods displays when the number of clusters increases, how much the silhoutte score is changing by. Once the rate slows down increasing the number of clusters isn't very useful. For this project I ended up with 9 clusters total.  
* Scaling features. Since k-means is using a distnace metric to evaluate and assign each observaation which cluster they belong it it is very important to scale all of the features. I also assigned weights to various features to give certain styles more emphasis. For example Assists and Turnovers can be said to represent ball handling so it was assigned a different weight when compared to the other features.  

## **Results after K-Means clustering model** 

#### Graph displaying New Roles

#### Pie chart of New Roles 

#### Clustering visual with New Roles

## **Business Insight Questions**

#### What is the difference between Elite teams  &  Average teams when it comes to player roles/styles?

#### Do winning teams have more or less players with a specific role/style. Does roster diversity play a part in winning?

#### Graph displaying Roster diversity for 'Average' NBA teams 

#### Graph disaplying Roster diversity for NBA Finalist teams 

#### Answer 
Overall NBA Final teams have more star power and their inside players have a reserved/defined role. In comparison, the ‘Average’ NBA teams have less star power and rely on star inside bigs as their focal points.


