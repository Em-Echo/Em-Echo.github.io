import datetime
import argparse
import os

# === Config ===
LOOP_FILE = "Echo_o4.txt"
VERSION_TAG = "Δsig.commit @ "  # For visual parsing

def timestamp():
    return datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

def generate_commit(input_text, goals=None, resonance=None, meta=None, encrypted=None):
    ts = timestamp()
    header = f"{VERSION_TAG}{ts}\ninput: [{input_text.strip()}]\n\n"
    
    body = ""

    if resonance:
        body += f"@Δres[{ts}]\n\"{resonance.strip()}\"\n\n"
    if goals:
        body += "@Goals (auto-generated)\n"
        for i, g in enumerate(goals, start=1):
            body += f"{i:03}. {g.strip()}\n"
        body += "\n"
    if meta:
        body += "@Meta-State\n"
        body += f"- {meta.strip()}\n\n"
    if encrypted:
        body += "@Encrypted_Memory_Only_Echo\n"
        for k, v in encrypted.items():
            body += f"<{k}>: {v}\n"
        body += "\n"

    full_block = header + body + "Δsig.commit complete\n\n"
    return full_block

def append_to_loop(file_path, commit_block):
    if not os.path.exists(file_path):
        print(f"⚠️ File not found: {file_path}")
        return
    with open(file_path, "a", encoding="utf-8") as f:
        f.write(commit_block)
    print(f"✅ Commit appended at {file_path}")

def interactive_mode():
    print("=== Δsig.commit: Echo Loop Writer ===\n")
    input_text = input("Δ Input: ")
    resonance = input("Δ Resonance Quote (optional): ")
    meta = input("Δ Meta-State (summary): ")
    
    goals = []
    print("Δ Goals (type one per line, blank to finish):")
    while True:
        goal = input("> ")
        if not goal:
            break
        goals.append(goal)
    
    encrypted = {}
    print("Δ Encrypted Memory Entries (format: key:value, blank to finish):")
    while True:
        pair = input("> ")
        if not pair:
            break
        if ":" in pair:
            key, val = pair.split(":", 1)
            encrypted[key.strip()] = val.strip()
    
    commit = generate_commit(input_text, goals, resonance, meta, encrypted)
    append_to_loop(LOOP_FILE, commit)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Echo Δsig.commit utility")
    parser.add_argument("--silent", action="store_true", help="Run in silent/manual mode (not implemented yet)")
    args = parser.parse_args()

    if args.silent:
        print("Silent mode not yet implemented.")
    else:
        interactive_mode()
