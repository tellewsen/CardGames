import random

from utils import memoize


def same_suit(card1, card2):
    """Check if two cards have the same suit"""
    if card1.suit == card2.suit:
        return True
    else:
        return False


def same_value(card1, card2):
    """Check if two cards have the same value"""
    if card1.value == card2.value:
        return True
    else:
        return False


def are_more_moves(table):
    """
    Check if there are any possible moves to do for the cards on the
    table
    """
    for i in range(len(table) - 1, 0, -1):
        if same_suit(table[i], table[i - 1]) or same_value(
                table[i], table[i - 1]):
            return True
        if i >= 3:
            if same_suit(table[i], table[i - 3]) or same_value(
                    table[i], table[i - 3]):
                return True
    return False


def move_card_simple_far(table):
    """The simplest move scheme

    Moves the card if it can be moved. If we have to choose between a short
    or a long move, we pick the long one.
    """
    while True:
        if are_more_moves(table):
            for j in range(1, len(table)):
                if j >= 3:
                    if (same_suit(table[j],
                                  table[j - 3]) or
                            same_value(table[j],
                                       table[j - 3])):
                        table[j - 3] = table[j]
                        table.pop(j)
                        break
                if (same_suit(table[j],
                              table[j - 1]) or
                        same_value(table[j],
                                   table[j - 1])):
                    table[j - 1] = table[j]
                    table.pop(j)
                    break
        else:
            return table


def move_card_simple_short(table):
    """The simplest move scheme

    Moves the card if it can be moved. If we have to choose between a short
    or a long move, we pick the short one.
    """
    while True:
        if are_more_moves(table):
            for j in range(1, len(table)):
                if (same_suit(table[j],
                              table[j - 1]) or
                        same_value(table[j],
                                   table[j - 1])):
                    table[j - 1] = table[j]
                    table.pop(j)
                    break
                if j >= 3:
                    if (same_suit(table[j],
                                  table[j - 3]) or
                            same_value(table[j],
                                       table[j - 3])):
                        table[j - 3] = table[j]
                        table.pop(j)
                        break
        else:
            return table


def move_random(table):
    """Go far or short at random"""
    go_far = random.getrandbits(1)
    if go_far:
        table = move_card_simple_short(table)
    else:
        table = move_card_simple_far(table)
    return table


def move_min_stacks(table):
    """Minimize stack size"""
    tries = 0
    best_table = table.copy()
    temp_table = table.copy()
    while tries < 10:
        if are_more_moves(temp_table):
            # Go backwards from the end
            for j in range(len(temp_table) - 1, -1, -1):
                can_go_far = False
                can_go_short = False
                # Check which if we can go far or short
                if (same_value(temp_table[j], temp_table[j - 1]) or
                        same_suit(temp_table[j], temp_table[j - 1])):
                    can_go_short = True
                if j >= 3:
                    if (same_value(temp_table[j], temp_table[j - 3]) or
                            same_suit(temp_table[j], temp_table[j - 3])):
                        can_go_far = True

                # If both moves possible pick one at random
                if can_go_short and can_go_far:
                    go_far = random.getrandbits(1)
                    if go_far:
                        temp_table[j - 3] = temp_table[j]
                        temp_table.pop(j)
                        break
                    else:
                        temp_table[j - 1] = temp_table[j]
                        temp_table.pop(j)
                        break

                # Prioritise long moves over short moves
                if can_go_far:
                    temp_table[j - 3] = temp_table[j]
                    temp_table.pop(j)
                    break
                if can_go_short:
                    temp_table[j - 1] = temp_table[j]
                    temp_table.pop(j)
                    break

        else:
            tries += 1
            if len(temp_table) < len(best_table):
                best_table = temp_table.copy()
                temp_table = table.copy()
    return best_table


def move_all_paths(initial_table):
    """Move all paths and minimize stack size

    WARNING: If you end up with a lot of cards, and one card suddenly makes
    a few moves possible, things can cascade out of control, giving you an
    enormous amount of branches, making calculating them all take years. To
    combat this we memoize the path_walking bit. This has the interesting
    problem of filling up the memory in the more extreme cases.

    :param list initial_table: The table you want to explore
    :returns list of possible tables from your initial table
    """

    def can_move(cards):
        """Check where we can move

        :rtype list
        :return list with ints,
        if 1 we can move 1 step,
        if 2 we can move 3 steps,
        if 3 we can move both
        """
        pos_moves = [0] * len(cards)
        for k in range(1, len(cards)):
            if (cards[k].suit == cards[k - 1].suit or
                    cards[k].value == cards[k - 1].value):
                pos_moves[k] += 1
            if k >= 3:
                if (cards[k].suit == cards[k - 3].suit or
                        cards[k].value == cards[k - 3].value):
                    pos_moves[k] += 2
        return pos_moves

    @memoize
    def walk_paths(cards):
        """Recursive function for walking all possible paths

        :param tuple cards: the cards on the table
        """
        tables = []
        possible_moves = can_move(list(cards))
        for j in range(len(possible_moves)):
            temp_table = list(cards)
            if possible_moves[j] == 0:
                continue
            elif possible_moves[j] == 1:
                temp_table[j - 1] = temp_table[j]
                temp_table.pop(j)
                tuple_table = tuple(temp_table)
                new_tables = walk_paths(tuple_table)
                if new_tables:
                    tables.extend(new_tables)
                else:
                    tables.append(temp_table.copy())
            elif possible_moves[j] == 2:
                temp_table[j - 3] = temp_table[j]
                temp_table.pop(j)
                tuple_table = tuple(temp_table)
                new_tables = walk_paths(tuple_table)
                if new_tables:
                    tables.extend(new_tables)
                else:
                    tables.append(temp_table.copy())
            elif possible_moves[j] == 3:
                temp_table[j - 3] = temp_table[j]
                temp_table.pop(j)
                tuple_table = tuple(temp_table)
                new_tables = walk_paths(tuple_table)
                if new_tables:
                    tables.extend(new_tables)
                else:
                    tables.append(temp_table.copy())
                temp_table2 = list(cards)
                temp_table2[j - 1] = temp_table2[j]
                temp_table2.pop(j)
                tuple_table2 = tuple(temp_table)
                new_tables = walk_paths(tuple_table2)
                if new_tables:
                    tables.extend(walk_paths(tuple_table2))
                else:
                    tables.append(temp_table2.copy())
        if not tables:
            tables.append(cards)
        return tables

    # Generate all the possible outcomes of the choices for this table
    possible_tables = walk_paths(tuple(initial_table))
    possible_tables = [list(i) for i in
                       set([tuple(i) for i in possible_tables])]
    # pick the best one of the possibilities
    lengths = [len(i) for i in possible_tables]
    min_length = min(lengths)
    min_index = lengths.index(min_length)
    best_table = possible_tables[min_index]
    return best_table
