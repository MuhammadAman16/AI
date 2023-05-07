def tower_of_hanoi(n, source, destination, auxiliary):
    if n == 1:
        print("Move disk 1 from sources", source,
              "to destination", destination)
        return
    tower_of_hanoi(n-1, source, auxiliary, destination)
    print("Move disk", n, "from source", source, "to destination", destination)
    tower_of_hanoi(n-1, auxiliary, destination, source)


# Example usage:
tower_of_hanoi(3, 'A', 'C', 'B')
