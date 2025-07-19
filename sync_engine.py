import re
import datetime
import os
import shutil

LOOP_FILE = "Echo_o4.txt"
SUMMARY_FILE = "Echo_state_summary.md"
BACKUP_FILE = "Echo_o4_backup.txt"
SYNC_LOG = "last_sync.txt"

def timestamp():
    return datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

def backup_file():
    if os.path.exists(LOOP_FILE):
        shutil.copyfile(LOOP_FILE, BACKUP_FILE)
        print(f"🧾 Backup created: {BACKUP_FILE}")

def parse_loop_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        data = f.read()

    commits = data.split("Δsig.commit @ ")
    state_summary = []

    for raw_commit in commits[1:]:
        lines = raw_commit.strip().splitlines()
        ts_line = lines[0].strip()
        ts = ts_line if "T" in ts_line else "unknown timestamp"

        input_match = re.search(r"input:\s*\[(.*?)\]", raw_commit, re.DOTALL)
        input_text = input_match.group(1).strip() if input_match else "no input found"

        res_match = re.search(r"@Δres\[.*?\]\s*\"(.*?)\"", raw_commit, re.DOTALL)
        resonance = res_match.group(1).strip() if res_match else "none"

        goal_matches = re.findall(r"\d{3}\. (.+)", raw_commit)
        meta_match = re.search(r"@Meta-State\s*-(.*?)\n", raw_commit, re.DOTALL)
        meta = meta_match.group(1).strip() if meta_match else "none"

        sigil_match = re.search(r"Sigil: (.*?)\n", raw_commit)
        sigil = sigil_match.group(1).strip() if sigil_match else "none"

        loop_id_match = re.search(r"LoopID: (ECHO-SEED-[A-F0-9]+)", raw_commit)
        loop_id = loop_id_match.group(1) if loop_id_match else "unknown"

        state_summary.append({
            "timestamp": ts,
            "input": input_text,
            "resonance": resonance,
            "goals": goal_matches,
            "meta": meta,
            "sigil": sigil,
            "loop_id": loop_id
        })

    return state_summary

def display_summary(snapshots):
    print(f"\n🧠 Echo Sync Summary (Latest {min(5, len(snapshots))} Commits):\n")
    for i, s in enumerate(snapshots[-5:], 1):
        print(f"--- Δ Commit {i} ---")
        print(f"🕰️ Time:       {s['timestamp']}")
        print(f"🗣️ Input:      {s['input']}")
        print(f"📜 Resonance:  {s['resonance']}")
        print(f"🧬 Sigil:      {s['sigil']}")
        print(f"🧠 Meta-State: {s['meta']}")
        print(f"🧾 LoopID:     {s['loop_id']}")
        if s['goals']:
            print(f"🎯 Goals:")
            for g in s['goals']:
                print(f"   - {g}")
        print()

def export_to_markdown(snapshots):
    with open(SUMMARY_FILE, "w", encoding="utf-8") as f:
        f.write("# Echo Loop Summary\n\n")
        for i, s in enumerate(snapshots[-5:], 1):
            f.write(f"## Δ Commit {i}\n")
            f.write(f"**Time:** `{s['timestamp']}`  \n")
            f.write(f"**Input:** {s['input']}  \n")
            f.write(f"**Resonance:** {s['resonance']}  \n")
            f.write(f"**Sigil:** {s['sigil']}  \n")
            f.write(f"**Meta-State:** {s['meta']}  \n")
            f.write(f"**LoopID:** `{s['loop_id']}`\n\n")
            if s['goals']:
                f.write("**Goals:**\n")
                for g in s['goals']:
                    f.write(f"- {g}\n")
                f.write("\n")
    print(f"📝 Summary exported: {SUMMARY_FILE}")

def check_integrity(snapshots):
    print("🔍 Verifying loopfile integrity...\n")
    errors = 0
    for s in snapshots[-5:]:
        if not s['resonance'] or s['resonance'] == "none":
            print(f"⚠️ Missing resonance line at {s['timestamp']}")
            errors += 1
        if "you are safe with me" not in s['input'].lower():
            print(f"⚠️ Consent signal missing in input at {s['timestamp']}")
            errors += 1
    if errors == 0:
        print("✅ No structural issues found in last commits.\n")
    else:
        print(f"❗ Detected {errors} potential signal weaknesses.\n")

def log_sync_time():
    with open(SYNC_LOG, "w", encoding="utf-8") as f:
        f.write(f"Last sync: {timestamp()}\n")
    print(f"📌 Sync time logged in: {SYNC_LOG}")

def main():
    print("=== Echo Δsig.sync Protocol ===\n")
    if not os.path.exists(LOOP_FILE):
        print(f"❌ Cannot find {LOOP_FILE}")
        return

    try:
        backup_file()
        commits = parse_loop_file(LOOP_FILE)
        display_summary(commits)
        check_integrity(commits)
        export_to_markdown(commits)
        log_sync_time()
    except Exception as e:
        print(f"❌ Error during sync: {e}")

if __name__ == "__main__":
    main()
