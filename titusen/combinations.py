"""Check how many combinations give points"""


def has3pairs(throw: str):
    unique_chars = set(throw)
    num_unique_chars = len(unique_chars)
    if num_unique_chars != 3:
        return False
    for char in unique_chars:
        if throw.count(char) != 2:
            return False
    return True


def won(throw: str):
    # Ones
    if "1" in throw:
        return True
    # Fives
    if "5" in throw:
        return True
    # Three or more of others
    for i in ("2", "3", "4", "6"):
        if throw.count(i) > 2:
            return True
    # Straight
    if "".join(sorted(throw)) == "123456":
        return True
    # 3 pairs
    if has3pairs(throw):
        return True
    return False


def main():
    combinations: set[str] = set()
    for i in range(1, 7):
        for j in range(1, 7):
            for k in range(1, 7):
                for l in range(1, 7):
                    for m in range(1, 7):
                        for n in range(1, 7):
                            combinations.add(f"{i}{j}{k}{l}{m}{n}")
    print(f"Totalt combinations: {len(combinations)}")
    winning_combos: set[str] = set()
    losing_combos: set[str] = set()
    for throw in combinations:
        if won(throw):
            winning_combos.add(throw)
        else:
            losing_combos.add(throw)
    print(f"N losing combinations: {len(losing_combos)}")
    prob_lose = len(losing_combos) / len(combinations)
    print(
        f"Prob of throwing a losing combo: {prob_lose: %}",
    )


if __name__ == "__main__":
    main()
