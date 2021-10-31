from src.functions import closest_multiple, print_results

#Default sizes of the villa-borads.
DEFAULT_SIZE = [(1800, 1200), (2400, 1200), (2700, 1200), (3000, 1200)]
DEFAULT_LENGTH = [x[0] for x in DEFAULT_SIZE]
DEFAULT_BREADTH = 1200

if __name__ == "__main__":

    input_length = int(input("Enter Length: "))
    input_breadth = int(input("Enter Breadth: "))

    possible_outcomes_len = []
    best_outcomes_height = []
    
    for elem in DEFAULT_LENGTH:
        possible_outcomes_len.append(closest_multiple(input_length, elem))

    possible_outcomes_len.sort()

    
    best_outcomes_height.append(closest_multiple(input_breadth, DEFAULT_BREADTH))

    print_results(possible_outcomes_len[0], best_outcomes_height[0])
