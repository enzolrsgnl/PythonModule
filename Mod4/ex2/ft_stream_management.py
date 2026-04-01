import sys


def communication_test() -> None:
    arch_id = input("Input Stream active. Enter archivist ID: ")
    report_status = input("Input Stream active. Enter status report: ")
    print()
    print("[STANDARD] Archive status from "
          + arch_id + ": " + report_status, file=sys.stdout)
    print("[ALERT] System diagnostic: "
          "Communication channels verified", file=sys.stderr)
    print("[STANDARD] Data transmission complete", file=sys.stdout)
    print()

if __name__ == "__main__":
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")
    print()
    communication_test()
    print()
    print("Three-channel communication test successful.")
