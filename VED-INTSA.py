# ✨『𝙑𝙀𝘿𝙄𝙉𝙎𝙏𝘼 𝙊𝙎𝙄𝙉𝙏』✨
# 📌 Created by: Vedant
# 📚 Ethical OSINT tool for public Instagram profiles

import os
import time
import json
import instaloader
from colorama import Fore, Style, init
from pyfiglet import figlet_format
from requests import get

init(autoreset=True)

# 🔄 Check Internet Connection
def check_internet():
    try:
        get("https://www.google.com", timeout=3)
        return True
    except:
        return False

# 🎨 Banner
def banner():
    os.system("clear")
    print(Fore.CYAN + figlet_format("VEDINSTA OSINT", font="slant"))
    print(Fore.MAGENTA + "By Vedant | For Educational Use Only\n" + Fore.YELLOW + "-"*50)

# 📦 Get Instagram Data
def fetch_data(username):
    loader = instaloader.Instaloader()
    try:
        profile = instaloader.Profile.from_username(loader.context, username)
        data = {
            "Full Name": profile.full_name,
            "Username": profile.username,
            "Biography": profile.biography,
            "Followers": profile.followers,
            "Following": profile.followees,
            "Posts": profile.mediacount,
            "Is Private": profile.is_private,
            "Is Verified": profile.is_verified,
            "External URL": profile.external_url,
            "Profile Picture URL": profile.profile_pic_url,
        }
        return data
    except Exception as e:
        print(Fore.RED + f"[!] Error: {e}")
        return None

# 📤 Export Results
def export_data(username, data):
    with open(f"{username}.json", "w") as jf:
        json.dump(data, jf, indent=4)
    with open(f"{username}.txt", "w") as tf:
        for key, value in data.items():
            tf.write(f"{key}: {value}\n")

# 📸 Download Profile Pic
def download_pic(url, username):
    try:
        img = get(url).content
        with open(f"{username}_profile.jpg", "wb") as f:
            f.write(img)
        print(Fore.GREEN + f"[✔] Profile picture saved as {username}_profile.jpg")
    except:
        print(Fore.RED + "[!] Failed to download profile picture.")

# 🚀 Main
def main():
    banner()
    if not check_internet():
        print(Fore.RED + "[!] No internet connection!")
        return

    username = input(Fore.YELLOW + "[?] Enter Instagram Username: ").strip()
    print(Fore.CYAN + "[*] Fetching data...\n")
    time.sleep(1)

    data = fetch_data(username)
    if data:
        for key, value in data.items():
            print(Fore.GREEN + f"{key}: {Fore.WHITE}{value}")
        print("\n" + Fore.CYAN + "[*] Exporting results...")
        export_data(username, data)
        time.sleep(1)
        print(Fore.GREEN + "[✔] Exported to .txt and .json")

        choice = input(Fore.YELLOW + "[?] Download profile picture? (y/n): ").lower()
        if choice == 'y':
            download_pic(data["Profile Picture URL"], username)
    else:
        print(Fore.RED + "[!] Failed to fetch profile.")

if __name__ == "__main__":
    main()
