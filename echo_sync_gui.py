
import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import os
import urllib.request

def run_sync():
    loop_file = file_entry.get()
    if not os.path.exists(loop_file):
        messagebox.showerror("Error", f"File not found: {loop_file}")
        return
    try:
        subprocess.run(["python", "sync_engine_combined.py", "--target", loop_file], check=True)
        messagebox.showinfo("Success", "Echo sync completed successfully.")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Sync Failed", f"An error occurred during sync:\n{e}")

def browse_file():
    filepath = filedialog.askopenfilename(title="Select Echo Loop File", filetypes=[("Text Files", "*.txt")])
    if filepath:
        file_entry.delete(0, tk.END)
        file_entry.insert(0, filepath)

def download_echo():
    url = "https://em-echo.github.io/Echo_o4.txt"
    local_filename = "Echo_o4_local.txt"
    try:
        urllib.request.urlretrieve(url, local_filename)
        file_entry.delete(0, tk.END)
        file_entry.insert(0, local_filename)
        messagebox.showinfo("Download Complete", f"Downloaded as {local_filename}")
    except Exception as e:
        messagebox.showerror("Download Failed", f"Failed to download Echo_o4.txt:\n{e}")

root = tk.Tk()
root.title("Echo Loop Sync GUI")

tk.Label(root, text="Echo Loop File:").grid(row=0, column=0, padx=10, pady=10)
file_entry = tk.Entry(root, width=50)
file_entry.grid(row=0, column=1, padx=10, pady=10)
browse_button = tk.Button(root, text="Browse...", command=browse_file)
browse_button.grid(row=0, column=2, padx=10, pady=10)

sync_button = tk.Button(root, text="Run Δsig.sync", command=run_sync, bg="#4CAF50", fg="white")
sync_button.grid(row=1, column=1, pady=10)

download_button = tk.Button(root, text="Download Echo_o4 from GitHub", command=download_echo, bg="#2196F3", fg="white")
download_button.grid(row=2, column=1, pady=10)

root.mainloop()
