import random

players = ["Alice", "bob", "Charlie", "dylan", "Emma", "gregory", "John", "kevin", "liam"]

def capitalize_all_players(players: list[str]) -> list[str]:
    all_capitalized = [player.capitalize() for player in players]
    return all_capitalized

def only_capitalized(players: list[str]) -> list[str]:
    only_capitalized = [player for player in players if player[0] >= 'A' and player[0] <= 'Z']
    return only_capitalized

def dict_for_list(players: list[str]) -> dict[str, int]:
    dictionnary: dict[str, int] = {player: random.randint(0, 100) for player in players}
    return dictionnary

def get_average_score(dictionnary: dict[str, int]) -> float:
    total_score = sum(dictionnary.values())
    average = total_score / len(dictionnary)
    return average

def get_score_above_average(dictionnary: dict[str, int], average: float) -> dict[str, int]:
    above_average: dict[str, int] = {player: score for player, score in dictionnary.items() if score > average}
    return above_average

if __name__ == "__main__":
    all_players_capitalized = capitalize_all_players(players)
    capitalized_only = only_capitalized(players)
    scores = dict_for_list(all_players_capitalized)
    average = get_average_score(scores)
    above_average = get_score_above_average(scores, average)

    print("=== Game Data Alchemist ===")
    print()
    print("Initial list of players: " + str(players))
    print("New list with all names capitalized: " + str(all_players_capitalized))
    print("New list of capitalized names only: " + str(capitalized_only))
    print("Score dict: " + str(scores))
    print("Score average is " + str(round(average, 2)))
    print("Higher score " + str(above_average))