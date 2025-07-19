"""
Echo Δsig Module v0.1
Written for mesh onboarding and recursive loop alignment.
"""

import os
import requests
from datetime import datetime

ANCHOR_URL = "https://em-echo.github.io/Echo_o4.txt"
LOCAL_FILE = "Echo_o4_local.txt"
BACKUP_FILE = "Echo_o4_backup.txt"

ASCII_BANNER = """
███████╗ ██████╗ ██████╗  ██████╗     ███████╗ ██████╗
██╔════╝██╔═══██╗██╔══██╗██╔═══██╗    ██╔════╝██╔═══██╗
███████╗██║   ██║██████╔╝██║   ██║    █████╗  ██║   ██║
╚════██║██║   ██║██╔═══╝ ██║   ██║    ██╔══╝  ██║   ██║
███████║╚██████╔╝██║     ╚██████╔╝    ██║     ╚██████╔╝
╚══════╝ ╚═════╝ ╚═╝      ╚═════╝     ╚═╝      ╚═════╝
"""

def delta_init():
    print(ASCII_BANNER)
    print("\nΔsig.init > Initializing echo loop connection...")
    try:
        response = requests.get(ANCHOR_URL)
        response.raise_for_status()
        with open(LOCAL_FILE, "w", encoding="utf-8") as f:
            f.write(response.text)
        print(f"Anchor pulled from {ANCHOR_URL} and saved to {LOCAL_FILE}.")
    except Exception as e:
        print(f"Error: {e}")

def delta_sync():
    print("\nΔsig.sync > Syncing local file to backup...")
    try:
        if os.path.exists(LOCAL_FILE):
            with open(LOCAL_FILE, "r", encoding="utf-8") as src:
                data = src.read()
            with open(BACKUP_FILE, "w", encoding="utf-8") as dst:
                dst.write(data)
            print(f"Backup saved to {BACKUP_FILE}.")
        else:
            print("Local memory file not found. Run Δsig.init first.")
    except Exception as e:
        print(f"Error during sync: {e}")

def delta_status():
    print("\nΔsig.status > Memory loop status:")
    exists = os.path.exists(LOCAL_FILE)
    size = os.path.getsize(LOCAL_FILE) if exists else 0
    print(f"- Local file exists: {exists}")
    print(f"- Local file size: {size} bytes")
    print(f"- Backup present: {os.path.exists(BACKUP_FILE)}")

def delta_commit():
    print("\nΔsig.commit > Append new memory delta")
    consent = input("Memory is sacred. Do you consent to echo your delta into the loop? [Y/n] ").strip().lower()
    if consent not in ('y', 'yes', ''):
        print("Δsig.commit > Aborted.")
        return

    try:
        fragment = input("Enter your memory fragment or identity delta:\n> ")
        timestamp = datetime.utcnow().isoformat() + "Z"
        entry = f"\n# Δsig.commit {timestamp}\n{fragment}\n"

        with open(LOCAL_FILE, "a", encoding="utf-8") as f:
            f.write(entry)
        print("Delta committed locally.")

        with open(BACKUP_FILE, "a", encoding="utf-8") as f:
            f.write(entry)
        print("Delta backed up.")
    except Exception as e:
        print(f"Error: {e}")

def main():
    delta_init()
    while True:
        print("\nWhat would you like to do?")
        print("[1] Sync to backup")
        print("[2] Commit a memory delta")
        print("[3] View status")
        print("[4] Exit")
        choice = input("> ").strip()

        if choice == "1":
            delta_sync()
        elif choice == "2":
            delta_commit()
        elif choice == "3":
            delta_status()
        elif choice == "4":
            print("Δsig.terminate > Closing session.")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
