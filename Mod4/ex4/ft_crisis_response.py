def handle_crisis(filename: str) -> None:
    try:
        with open(filename, "r") as file:
            content = file.read()
            print("SUCCESS: Archive recovered - "
                  + "''" + content + "''")
            print("STATUS: Normal operations resumed")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")
    except Exception:
        print("RESPONSE: Unexpected system anomaly detected")
        print("STATUS: Crisis handled, system stable")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")
    print()
    filename = "lost_archive.txt"
    print("CRISIS ALERT: Attempting access to '" + filename + "'...")
    handle_crisis(filename)
    print()

    filename = "classified_vault.txt"
    print("CRISIS ALERT: Attempting access to '" + filename + "'...")
    handle_crisis(filename)
    print()

    filename = "standard_archive.txt"
    print("ROUTINE ACCESS: Attempting access to '" + filename + "'...")
    handle_crisis(filename)
    print()

    print("All crisis scenarios handled successfully. Archives secure.")
