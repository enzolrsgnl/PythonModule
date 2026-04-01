import math

def get_player_pos() -> tuple[float, float, float]:
	while True:
		user_input = input("Enter new coordinates as floats in format 'x,y,z': ")
		parts = []
		current = ""
		for char in user_input:
			if char == ",":
				parts.append(current)
				current = ""
			else:
				current += char
		parts.append(current)

		if len(parts) != 3:
			print("Invalid syntax")
			continue

		try:
			x = float(parts[0])
		except ValueError as error:
			print("Error on parameter '" + parts[0] + "': " + str(error))
			continue
		try:
			y = float(parts[1])
		except ValueError as error:
			print("Error on parameter '" + parts[1] + "': " + str(error))
			continue
		try:
			z = float(parts[2])
		except ValueError as error:
			print("Error on parameter '" + parts[2] + "': " + str(error))
			continue

		return (x, y, z)



	
if __name__ == "__main__":
	print("=== Game Coordinate System ===")
	print()

	print("Get a first set of coordinates")
	position1 = get_player_pos()
	print("Got a first tuple: " + str(position1))
	print("It includes: X=" + str(position1[0]) + ", Y=" + str(position1[1]) + ", Z=" + str(position1[2]))
	print("Distance to center: " + str(round(math.sqrt((0 - position1[0])**2 + (0 - position1[1])**2 + (0 - position1[2])**2), 4)))
	print()

	print("Get a second set of coordinates")
	position2 = get_player_pos()
	print("Distance between the 2 sets of coordinates: " + str(round(math.sqrt((position2[0] - position1[0])**2 + (position2[1] - position1[1])**2 + (position2[2] - position1[2])**2), 4)))