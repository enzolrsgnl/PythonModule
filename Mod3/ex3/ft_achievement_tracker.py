import random

achievements = ["Crafting Genius", "World Savior", "Master Explorer", "Collector Supreme", "Untouchable",
"Boss Slayer", "Strategist", "Treasure Hunter", "First Steps", "Sharp Mind", "Speed Runner", "Unstoppable"]

def gen_player_achievements() -> set[str]:
	k = random.randint(1, len(achievements))
	player_achievements: set[str] = set(random.sample(achievements, k))
	return player_achievements

if __name__ == "__main__":
	print("=== Achievement Tracker System ===")
	print()
	Alice: set[str] = gen_player_achievements()
	print("Player Alice: " + str(Alice))
	Bob: set[str] = gen_player_achievements()
	print("Player Bob: " + str(Bob))
	Charlie: set[str] = gen_player_achievements()
	print("Player Charlie: " + str(Charlie))
	Dylan: set[str] = gen_player_achievements()
	print("Player Dylan: " + str(Dylan))
	print()

	all_achievements: set[str] = Alice.union(Bob, Charlie, Dylan)
	print("All distinct achievements: " + str(all_achievements))
	print()

	common_achievements: set[str] = Alice.intersection(Bob, Charlie, Dylan)
	print("Common achievements: " + str(common_achievements))
	print()

	only_alice: set[str] = Alice.difference(Bob, Charlie, Dylan)
	print("Only Alice has: " + str(only_alice))
	only_bob: set[str] = Bob.difference(Alice, Charlie, Dylan)
	print("Only bob has: " + str(only_bob))
	only_charlie: set[str] = Charlie.difference(Alice, Bob, Dylan)
	print("Only Charlie has: " + str(only_charlie))
	only_Dylan: set[str] = Dylan.difference(Alice, Bob, Charlie)
	print("Only Dylan has: " + str(only_Dylan))
	print()

	all_possible_achievements: set[str] = set(achievements)

	missing_alice: set[str] = all_possible_achievements.difference(Alice)
	print("Alice is missing: " + str(missing_alice))
	missing_bob: set[str] = all_possible_achievements.difference(Bob)
	print("Bob is missing: " + str(missing_bob))
	missing_charlie: set[str] = all_possible_achievements.difference(Charlie)
	print("Charlie is missing: " + str(missing_charlie))
	missing_dylan: set[str] = all_possible_achievements.difference(Dylan)
	print("Dylan is missing: " + str(missing_dylan))