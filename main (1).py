import PyPDF2
import os
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

def print_banner():
    banner = f"""
{Fore.RED}╔════════════════════════════════════════════════════════════════╗
{Fore.RED}║ ██████╗ ██████╗ ███████╗    ██████╗ ██████╗ ██╗   ██╗████████╗███████╗ ║
{Fore.RED}║ ██╔══██╗██╔══██╗██╔════╝    ██╔══██╗██╔══██╗██║   ██║╚══██╔══╝██╔════╝ ║
{Fore.RED}║ ██████╔╝██████╔╝█████╗      ██████╔╝██████╔╝██║   ██║   ██║   █████╗   ║
{Fore.RED}║ ██╔═══╝ ██╔══██╗██╔══╝      ██╔══██╗██╔══██╗██║   ██║   ██║   ██╔══╝   ║
{Fore.RED}║ ██║     ██║  ██║███████╗    ██████╔╝██║  ██║╚██████╔╝   ██║   ███████╗ ║
{Fore.RED}║ ╚═╝     ╚═╝  ╚═╝╚══════╝    ╚═════╝ ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚══════╝ ║
{Fore.RED}║{Fore.YELLOW}          PDF Brute Force Attacker - FAST MODE{Fore.RED}               ║
{Fore.RED}╚════════════════════════════════════════════════════════════════╝
{Fore.RESET}"""
    print(banner)

def print_warning():
    warning = f"""
{Fore.RED}⚠ WARNING: This tool is for educational and authorized testing only. ⚠
{Fore.YELLOW}Unauthorized use against protected systems is illegal.
{Fore.RED}The developer is not responsible for misuse of this tool.
{Fore.RESET}"""
    print(warning)

def brute_force_pdf(pdf_path, wordlist_path):
    # Check if files exist
    if not os.path.isfile(pdf_path):
        print(f"{Fore.RED}[❌] PDF file not found: {pdf_path}{Fore.RESET}")
        return
    if not os.path.isfile(wordlist_path):
        print(f"{Fore.RED}[❌] Wordlist not found: {wordlist_path}{Fore.RESET}")
        return

    # Open the PDF
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)

        if not reader.is_encrypted:
            print(f"{Fore.GREEN}[✔️] PDF is not password protected.{Fore.RESET}")
            return

        print(f"{Fore.CYAN}[🔍] Brute-force starting on: {pdf_path}{Fore.RESET}")

        # Load wordlist
        with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as wlist:
            for i, password in enumerate(wlist, 1):
                password = password.strip()

                try:
                    if reader.decrypt(password):
                        print(f"\n{Fore.GREEN}[✅] {Style.BRIGHT}Password found: '{Fore.YELLOW}{password}{Fore.GREEN}' at line {i}{Fore.RESET}")
                        return
                except Exception:
                    continue  # Skip errors silently for speed

                # Optional: Print every N attempts
                if i % 1000 == 0:
                    print(f"{Fore.BLUE}[...] Tried {i} passwords...{Fore.RESET}")

        print(f"\n{Fore.RED}[❌] Password not found in wordlist.{Fore.RESET}")

# Main runner
if __name__ == "__main__":
    print_banner()
    print_warning()

    print(f"{Fore.CYAN}=== Configuration ==={Fore.RESET}")
    pdf_path = input(f"{Fore.YELLOW}[?] Enter path to PDF file: {Fore.RESET}").strip()
    wordlist_path = input(f"{Fore.YELLOW}[?] Enter path to password wordlist (.txt): {Fore.RESET}").strip()

    print(f"\n{Fore.MAGENTA}🚀 Starting attack...{Fore.RESET}")
    brute_force_pdf(pdf_path, wordlist_path)
