import read_inputs as inp
import numpy as np

class City:
    """
    Stores coordinates of each city and function to compute euclidian
    distance with any other city
    """
    def __init__(self, index, x, y):
        self.index = index
        self.x = x
        self.y = y

    def distance(self, city):
        x_distance = self.x - city.x
        y_distance = self.y - city.y
        distance = np.sqrt(x_distance**2 + y_distance**2)
        return distance

    def __repr__(self):
        return f"City {self.index}: [{self.x}, {self.y}]"


def greedy(data):
    """
    Simple heuristics where closest city is the next one visited
    """
    # create list of all cities to visit
    cities = []
    for i in data:
        city = City(i[0], i[1], i[2])
        cities.append(city)
    num_cities = len(cities)

    # initialize route
    total_distance = 0
    not_visited = cities[:]
    u = not_visited.pop(0)
    route = [u.index]

    # iterate until no city remains to be visited
    while len(route) < num_cities:
        # compute distances
        dist_from_u = []
        for i in not_visited:
            # compute distance
            dist = u.distance(i)
            dist_from_u.append([i.index, dist])

        # sort cities by distance
        dist_from_u = sorted(dist_from_u, key = lambda j: j[1], reverse = False)

        # select next city
        u = cities[dist_from_u[0][0]]
        total_distance += dist_from_u[0][1]
        route.append(u.index)
        not_visited.remove(u)

    total_distance += cities[route[0]].distance(cities[route[-1]])  
    print(f'Route {route} with a distance of {total_distance}')

# run algorithm
file_name = 'tsp_5_1'        
data = inp.read_file(file_name)    
greedy(data)







