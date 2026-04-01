def secure_operation_on_vault(filename: str) -> None:
    entry1 = "[CLASSIFIED] Quantum encryption keys recovered"
    entry2 = "[CLASSIFIED] Archive integrity: 100%"
    entry3 = "[CLASSIFIED] New security protocols archived"
    with open(filename, "w") as file:
        file.write(entry1 + "\n")
        file.write(entry2 + "\n")
    
    with open(filename, "r") as file:
        file.read()

    print(entry1)
    print(entry2)
    print()
    print("SECURE PRESERVATION:")
    print(entry3)
    print("Vault automatically sealed upon completion")
        


if __name__ == "__main__":
    filename = "new_file.txt"
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
    print()
    print("Initiating secure vault access...")
    print("Vault connection established with failsafe protocols")
    print()
    print("SECURE EXTRACTION:")
    secure_operation_on_vault(filename)
    print()
    print("All vault operations completed with maximum security.")