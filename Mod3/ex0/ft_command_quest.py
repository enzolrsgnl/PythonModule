import sys

def get_program_name() -> None:
	prog_name = sys.argv[0]
	print("Program name: " + prog_name)

def get_arg_count() -> None:
	arg_count = len(sys.argv) - 1
	if len(sys.argv) == 1:
		print("No arguments provided!")
	else:
		print("Arguments received: " + str(arg_count))

def print_arg() -> None:
	arg_number = 0
	for argv in sys.argv[1:]:
		arg_number += 1
		print("Argument " + str(arg_number) + ": " + argv)

def get_total_arg_count() -> None:
	total_arg_count = len(sys.argv)
	print("Total arguments: " + str(total_arg_count))


if __name__ == "__main__":
	print("=== Command Quest ===")
	get_program_name()
	get_arg_count()
	print_arg()
	get_total_arg_count()
