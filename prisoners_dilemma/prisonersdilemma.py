"""
Room with n boxes with numbers 1 to n

Figure out the probability of all prisoners finding their number in a
given amount of checks
"""
import random


def make_boxes(num_boxes: int) -> dict[int, int]:
    numbers = [i for i in range(0, num_boxes)]
    random.shuffle(numbers)
    return {i: numbers[i] for i in range(num_boxes)}


def prisoner_found_their_number(
    my_number: int, boxes: dict[int, int], n_box_checks: int
) -> bool:
    """Look for their number using a loop strategy"""
    current_number = my_number
    for _ in range(n_box_checks):
        new_number = boxes[current_number]
        if new_number == my_number:
            return True
        current_number = new_number
    return False


def play(n_prisoners: int, n_box_checks: int) -> bool:
    boxes = make_boxes(n_prisoners)
    for prisoner_number in range(n_prisoners):
        if not prisoner_found_their_number(prisoner_number, boxes, n_box_checks):
            return False
    return True


def wins_in_n_games(n_prisoners: int, n_box_checks: int, n_games: int) -> int:
    """Check how many times the prisoners win in n_games games"""
    wins = 0
    for _ in range(n_games):
        if play(n_prisoners, n_box_checks):
            wins += 1
    return wins


def print_results(n_prisoners: int, wins: int, games: int):
    """Output results as text to terminal"""
    print(f"With {n_prisoners} prisoners")
    print(f"Won {wins} of {games} games")
    print(f"{wins / games} chance of everyone finding their own number")


def main():
    """Run n_games games with n_prisoners prisoners and print results to terminal"""
    n_prisoners = 100
    n_games = 1000
    wins = wins_in_n_games(
        n_prisoners=n_prisoners, n_box_checks=int(n_prisoners / 2), n_games=n_games
    )
    print_results(n_prisoners, wins, n_games)


if __name__ == "__main__":
    main()
