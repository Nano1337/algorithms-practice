## Traveling Salesman Problem

Traveling salesman is a O(n!) problem since it has to check every possible path. 

More formally: 
Given a list of cities and the distances between each pair of cities, what is the shortest possible route that visits each city and returns to the origin city?

We check every possible path, which leads us to n * (n-1) * (n-2) * ... * 1 = n! paths. 
Then, you take the minimum of all the paths.