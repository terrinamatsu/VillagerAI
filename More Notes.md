For game path finding, agents are treated similarly to particles, and so the general structure of an array of 'Person' structs or classes held within a 'Population' class that handles spawning and calling of Person functions will be used. 

A lot of research on pathfinding in games is based on efficiency; due to the very narrow and focussed nature of this project this is not of immediate concern, although considerations may be made when testing larger numbers of Persons on larger maps to stress test the made system at a later point in the project. 

As mentioned, this project will also link to a Villager AI from a previous project. This will involve loading python scripts into c++, (Jon's demo here: https://github.com/NCCA/EmbedPython/blob/master/src/Agent.cpp )

Pathfinding generally uses derivations of Dijkstra's or A* path finding algorithms across a grid or generated NavMesh. In each case, a network is generated of connected points with distances measured which are then used in the path finding algorithms. 

As this is realtime, updating the path based on changes to the world such as to avoid other Persons or to avoid obstacles could be explored. 

- (Not sure of the inclusion of this step because is might be complicated) generation of nav mesh / map data
- Generation of network to be used by...
- The actual path finding with an algorithm such as Dijkstra or A*
  - Driven by the AI of the Persons 
- The real time use of this path by an ai agent with considerations for avoidance of obstacles and other agents. 