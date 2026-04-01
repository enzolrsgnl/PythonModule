def write_in_file(filename: str) -> None:
    entry_1: str = "[ENTRY 001] New quantum algorithm discovered"
    entry_2: str = "[ENTRY 002] Efficiency increased by 347%"
    entry_3: str = "[ENTRY 003] Archived by Data Archivist trainee"
    f = open(filename, "w")
    print("Storage unit created successfully...")
    print()
    print("Inscribing preservation data...")
    f.write(entry_1 + "\n")
    print(entry_1)
    f.write(entry_2 + "\n")
    print(entry_2)
    f.write(entry_3 + "\n")
    print(entry_3)
    print()
    f.close()
    print("Data inscription complete. Storage unit sealed.")
    print("Archive '" + filename + "' ready for long-term preservation.")


if __name__ == "__main__":
    filename = "new_discovery.txt"
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")
    print()

    print("Initializing new storage unit: " + filename)
    write_in_file(filename)
