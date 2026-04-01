def read_and_print_file(filename: str) -> None:
    try:
        f = open(filename, "r")
        print("Connection to the vault established...")
        print()
        content = f.read()
        print("RECOVERED DATA: ")
        print(content)
        f.close()   # possible corruption du fichier fuite de données
        print()
        print("Data recovery complete. Storage unit disconnected.")
    except FileNotFoundError:
        print()
        print("ERROR: Storage vault not found. Run data generator first.")


if __name__ == "__main__":
    filename = "ancient_fragment.txt"
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    print()

    print("Accessing Storage Vault: " + filename)
    read_and_print_file(filename)
    print()
