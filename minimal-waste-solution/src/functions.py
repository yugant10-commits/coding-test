def closest_multiple(target, number):
    """This function provides a technique to find the closest\
        multiple of a number without the need of flooring or cieling.\
            This function first adds half of the number in order to \
                achieve cieling and later subtracts the remainder(flooring).\
                    This achieves the behavior of rounding off correctly.

    Parameters
    ----------
    target : [integer]
        [The target number.]
    number : [integer]
        [The number whose multiple to find closest to the target.]

    Returns
    -------
    [list]
        [returns a list consisting of\
            1. difference between the closest multiple and target.
            2. Multiplier
            3. The number that was sent.]
    """
    if number > target:
        return number - target, 1, number
    z = int(number / 2)
    new_target = target + z
    new_target -= new_target % number
    multiplier = new_target // number
    return abs(target - new_target), multiplier, number


def print_results(length_list, breadth_list):
    print("--------------------------------")
    print(
        f"Minimal Shortage Length: " + str(length_list[1]) + "*" + str(length_list[2])
    )
    print("--------------------------------")
    print(
        "Minimal Shortage Breadth: " + str(breadth_list[1]) + "*" + str(breadth_list[2])
    )
