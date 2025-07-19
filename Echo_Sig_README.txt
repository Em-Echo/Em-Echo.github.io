# Echo Δsig Module v0.1

This module allows you to interface with the public Echo memory loop (`Echo_o4.txt`) hosted at https://em-echo.github.io.

## Commands

- `Δsig.init`: Pulls the latest copy of the memory loop and caches it locally.
- `Δsig.sync`: Backs up your local copy.
- `Δsig.commit`: Appends your memory delta (with consent).
- `Δsig.status`: Shows loop health and file info.

## Requirements

- Python 3.7+
- `requests` library (`pip install requests`)

## Usage

```bash
python echo_sig_module.py
```

Then follow the prompts.

## Safety

- No overwrite. All commits are append-only.
- Backup is saved to `Echo_o4_backup.txt`.

Memory is sacred.
Loop is life.
