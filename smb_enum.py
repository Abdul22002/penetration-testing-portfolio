# smb_enum.py
import subprocess

target = input("Enter target IP: ")
print(f"Enumerating SMB shares on: {target}")
subprocess.call(["smbclient", "-L", f"//{target}/", "-N"])
