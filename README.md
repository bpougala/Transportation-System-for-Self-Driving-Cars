# Transportation System for Self-Driving cars and buses
## POUGALA Biko - November 2019 


### 1 Abstract

This project centers on shared on-demand autonomous vehicles in metropolitan areas. We’ll particularly emphasise the constraints and obstacles such systems must face in order to be practical and safe to use for users, as well as become a serious alternative to the individual car ownership model that’s still prevalent in most large metropolitan areas around the world.

### 2 Introduction/Motivation of work

There are reasons to believe that an economic model based on on-demand autonomous vehicles will be prevailing in the near-future in most large metropoli- tan areas across industrialised nations, replacing the individual car system we have today. This would entail massive new challenges for our current trans- portation infrastructure, and that for several reasons we hereby detail:

1. 68% of the world population will be living in cities by 2050 compared to 55% today, according to the UN’s Department of Economic and Social Affairs. In order to absorb that increase in transportation demand, it would entail considerably expanding urban areas’ road networks to accommodate for the millions more cars that would be needed.

2. American think-tank ReThinkX said this about the current trends in au- tonomous vehicles: 

> “We are on the cusp of the fastest, deepest, most consequential disruption of transportation in history. By 2030, within 10 years of regulatory approval of Autonomous Vehicles (AVs), 95 percent of U.S. passenger miles traveled will be served by on-demand autonomous electric vehicles owned by fleets, not individuals, ...”


### 3 Model and Problem statement

We use the San Francisco roads network developed by the University of Utah using the theoretical approach from Dr. Thomas Brinkhoff. This came under the form of unpractical `.cdege` and `.cnodes` files which I copied line by line into a `.txt` file before running a Python short scrupt to convert it into a workable CSV file. 
   I created two CSV files, one named `sf_edges_network.csv`, listing all the edges in the San Francisco road network graph, with each edge endpoint corresponding to a node ID as well as the L2 distance between the two nodes and a second file called `sf_nodes_network.csv`, listing all the nodes in the SF road network graph, where each node ID corresponding to a pair of latitude and longitude co- ordinates. For reference here is how they look: I have converted this DataFrame



