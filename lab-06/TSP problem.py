import itertools

graph = {
    "1": {
        "2": 10,
        "3": 15,
        "4": 20
    },
    "2": {
        "1": 10,
        "3": 35,
        "4": 25
    },
    "3": {
        "1": 15,
        "2": 35,
        "4": 30
    },
    "4": {
        "1": 20,
        "2": 25,
        "3": 30
    }
}

# a function to calculate the distance b/w two points:


def calc_distance(tour):
    distance = 0
    for i in range(len(tour)-1):
        distance += graph[tour[i]][tour[i+1]]
    distance += graph[tour[-1]][tour[0]]
    return distance


def TSP(graph):
    # using itertool to get the permutations and return in a list
    cities = list(graph.keys())
    tours = list(itertools.permutations(cities))

    shortest_tour = None
    shortest_distance = float("inf")

    for tour in tours:
        distance = calc_distance(tour)
        if distance <= shortest_distance and tour[0] == "1":
            shortest_distance = distance
            shortest_tour = tour

    print("Shortest Distance:", shortest_distance)
    print("Shortest traveling sequence is:", shortest_tour)

# implementation
TSP(graph)
