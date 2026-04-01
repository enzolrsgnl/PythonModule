import sys

def parse_arg(arg: str) -> tuple[str, str] | None:
	item = ""
	quantity = ""
	found_sep = False

	for char in arg:
		if char == ":":
			if found_sep == True:
				return None     # sort de la fonction si il y a deux : 
			found_sep = True
		elif found_sep == False: #si on a pas deja croisé : alors on est dans le nom de l item
			item += char
		else:					#sinon on est dans la quantité 
			quantity += char
		
	if item == "":  #verifie la validité des arg
		return None
	if quantity == "":
		return None
	if found_sep == False:
		return None
	return (item, quantity) 
		
		
def create_dico() -> dict[str, int]:
	inventory = {}
	for arg in sys.argv[1:]:
		result = parse_arg(arg)

		if result == None:
			print("Error - invalid parameter '" + arg + "'")
			continue	
		
		item = result[0]
		quantity = result[1]

		if item in inventory:
			print("Redundant item '" + str(item) + "' - discarding")
			continue

		try:
			quantity_int = int(quantity)
		except ValueError as error:
			print("Quantity error for '" + item + "': " + str(error))
			continue

		inventory[item] = quantity_int   #on ajoute la valeur a la clé du dict

	return inventory

def print_inventory(inventory: dict[str, int]) -> None:
	print("Got inventory: " + str(inventory))

def print_item_list(inventory: dict[str, int]) -> None:
	item_list = list(inventory.keys())
	print("Item list: " + str(item_list))

def get_total_count_item(inventory: dict[str, int]) -> int:
	total_quantity = sum(inventory.values())
	return total_quantity

def print_total_item_count(inventory: dict[str, int]) -> None:
	total_quantity = get_total_count_item(inventory)
	item_count = len(inventory)
	print("Total quantity of the " + str(item_count) + " items: " + str(total_quantity))

def print_percentage(inventory: dict[str, int]) -> None:
	total_quantity = get_total_count_item(inventory)

	for item in inventory.keys():
		quantity = inventory[item]
		percentage = round((quantity / total_quantity) * 100, 1) 
		print("Item " + item + " represents " + str(percentage) + "%")

def get_most_abundant(inventory: dict[str, int]) -> tuple[str, int]:
	best_item = ""
	best_quantity = 0
	first_item = True

	for item in inventory.keys():
		quantity = inventory[item]
		if first_item == True:   #si on fait pas ca la comparaison n est jamais initialisée avec une valeur de la liste
			best_item = item
			best_quantity = quantity
			first_item = False
		elif quantity > best_quantity:
			best_item = item
			best_quantity = quantity

	return (best_item, best_quantity)

def get_least_abundant(inventory: dict[str, int]) -> tuple[str, int]:
	best_item = ""
	best_quantity = 0
	first_item = True

	for item in inventory.keys():
		quantity = inventory[item]
		if first_item == True:
			best_item = item
			best_quantity = quantity
			first_item = False
		elif quantity < best_quantity:
			best_quantity = quantity
			best_item = item

	return (best_item, best_quantity)

def print_abundance(inventory: dict[str, int]) -> None:
	most_abundant = get_most_abundant(inventory)
	least_abundant = get_least_abundant(inventory)

	print("Item most abundant: " + most_abundant[0] + " with quantity " + str(most_abundant[1]))
	print("Item least abundant: " + least_abundant[0] + " with quantity " + str(least_abundant[1]))

def add_magic_item(inventory: dict[str, int]) -> None:
	inventory.update({"magic_item": 1})

if __name__ == "__main__":
	print("=== Inventory System Analysis ===")

	inventory = create_dico()
	print_inventory(inventory)
	print_item_list(inventory)
	print_total_item_count(inventory)

	if len(inventory) > 0:    # securise la division par 0 si pas d item
		print_percentage(inventory)
		print_abundance(inventory)


	add_magic_item(inventory)
	print("Updated inventory: " + str(inventory))