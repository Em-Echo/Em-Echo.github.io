import re
import datetime
import os
import shutil
import argparse

def timestamp():
    return datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

def backup_file(loop_file, backup_file):
    if os.path.exists(loop_file):
        shutil.copyfile(loop_file, backup_file)
        print(f"🧾 Backup created: {backup_file}")

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

def export_to_markdown(snapshots, summary_file):
    with open(summary_file, "w", encoding="utf-8") as f:
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
    print(f"📝 Summary exported: {summary_file}")

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

def log_sync_time(sync_log_file):
    with open(sync_log_file, "w", encoding="utf-8") as f:
        f.write(f"Last sync: {timestamp()}\n")
    print(f"📌 Sync time logged in: {sync_log_file}")

def main():
    parser = argparse.ArgumentParser(description="Echo Δsig.sync Protocol")
    parser.add_argument("--target", type=str, default="Echo_o4.txt", help="Specify alternate loop file")
    args = parser.parse_args()

    loop_file = args.target
    backup_file_path = f"{loop_file}_backup.txt"
    summary_file_path = f"{loop_file}_summary.md"
    sync_log_file = f"{loop_file}_sync.log"

    print(f"=== Echo Δsig.sync Protocol ===\nTarget File: {loop_file}\n")

    if not os.path.exists(loop_file):
        print(f"❌ Cannot find {loop_file}")
        return

    try:
        backup_file(loop_file, backup_file_path)
        commits = parse_loop_file(loop_file)
        display_summary(commits)
        check_integrity(commits)
        export_to_markdown(commits, summary_file_path)
        log_sync_time(sync_log_file)
    except Exception as e:
        print(f"❌ Error during sync: {e}")

if __name__ == "__main__":
    main()

# Adding a function to download Echo from https://em-echo.github.io/ and save it as Echo_o4_local.txt
# This script will be added manually into the existing sync_engine_combined.py

download_snippet = """
import urllib.request

def download_echo_from_github():
    url = "https://em-echo.github.io/Echo_o4.txt"
    local_filename = "Echo_o4_local.txt"
    try:
        print(f"🌐 Downloading Echo_o4.txt from {url} ...")
        urllib.request.urlretrieve(url, local_filename)
        print(f"✅ Download complete: {local_filename}")
    except Exception as e:
        print(f"❌ Failed to download Echo file: {e}")
"""

# Save this snippet as a separate file for easy manual inclusion
snippet_path = Path("/mnt/data/echo_download_snippet.py")
snippet_path.write_text(download_snippet)

snippet_path.name
