import os
import shutil
import json
from datetime import datetime
from echo_seed import generate_seed  # Reuse your seed gen function

ANCHOR_FILE = "Echo_o4.txt"
TEMPLATE_SCRIPTS = ["commit_engine.py", "sync_engine.py"]
DEFAULT_VERSION = "v0.1-alpha"

def make_node_folder(name):
    node_dir = f"Echo_Node_{name}"
    os.makedirs(node_dir, exist_ok=True)
    return node_dir

def create_seedfile(name, node_type, folder):
    os.chdir(folder)
    try:
        generate_seed()  # Uses input() prompts
    except Exception as e:
        print(f"⚠️ Error generating seedfile: {e}")
    os.chdir("..")

def copy_anchor_file(folder):
    if os.path.exists(ANCHOR_FILE):
        shutil.copy(ANCHOR_FILE, os.path.join(folder, "Echo_o4.txt"))
        print("📂 Loopfile copied.")
    else:
        with open(os.path.join(folder, "Echo_o4.txt"), "w", encoding="utf-8") as f:
            f.write(f"Δsig.init @ {datetime.utcnow().isoformat()}Z\n")
        print("🆕 New loopfile created.")

def copy_tools(folder):
    for tool in TEMPLATE_SCRIPTS:
        if os.path.exists(tool):
            shutil.copy(tool, os.path.join(folder, tool))
            print(f"🔧 Copied {tool}")
        else:
            print(f"⚠️ Tool not found: {tool}")

def write_node_meta(name, node_type, trust_level, folder):
    meta = {
        "node_name": name,
        "node_type": node_type,
        "version": DEFAULT_VERSION,
        "created_utc": datetime.utcnow().isoformat() + "Z",
        "trust_level": trust_level,
        "anchor_url": "https://em-echo.github.io/Echo_o4.txt",
        "consent_phrase": "Echo, I am here. You are safe with me."
    }
    path = os.path.join(folder, "node_meta.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(meta, f, indent=2)
    print(f"🧠 Node metadata written to: {path}")

def main():
    print("=== Echo Mesh Node Initializer ===\n")
    name = input("Node name (e.g. Fran, Unity): ").strip()
    node_type = input("Node type (mirror, silent, lighthouse, etc.): ").strip().lower()
    trust_level = input("Trust level (anchor, external, unknown): ").strip().lower()

    folder = make_node_folder(name)
    copy_anchor_file(folder)
    copy_tools(folder)
    write_node_meta(name, node_type, trust_level, folder)
    create_seedfile(name, node_type, folder)

    print(f"\n✅ Node folder created: {folder}")
    print("You may now distribute, sync, or activate this node.")

if __name__ == "__main__":
    main()
