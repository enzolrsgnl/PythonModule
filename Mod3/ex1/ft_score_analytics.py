import sys

def get_score():
	score = []
	for argv in sys.argv[1:]:
		try:
			score.append(int(argv))
		except ValueError:
				print("Invalid parameter: " + "'" + str(argv) + "'")
	return score

def print_score(score) -> None:
	print("Scores processed: " + str(score))


def get_players_count(score) -> None:
	players_count = len(score)
	print("Total players: " + str(players_count))

def get_total_score(score) -> int:
	total_score = 0
	total_score = sum(score)
	print("Total score: " + str(total_score))
	return total_score

def get_average_score(score: list):
	average_score = 0
	average_score = sum(score) / len(score)
	print("Average score: " + str(average_score))

def get_high_score(score) -> int:
	high_score = 0
	high_score = max(score)
	print("High score: " + str(high_score))
	return high_score
	

def get_min_score(score) -> int:
	min_score = 0
	min_score = min(score)
	print("Low score: " + str(min_score))
	return min_score

def get_range(high_score, min_score) -> None:
	score_range = 0
	score_range = high_score - min_score
	print("Score range: " + str(score_range))

if __name__ == "__main__":
	print("=== Player Score Analytics ===")
	if len(sys.argv) < 2:
		print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
	else:
		score = get_score()
		if len(score) == 0:
			print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
		else:
			print_score(score)
			get_players_count(score)
			get_total_score(score)
			get_average_score(score)
			high_score = get_high_score(score)
			min_score = get_min_score(score)
			get_range(high_score, min_score)