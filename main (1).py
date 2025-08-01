import PyPDF2
import os

def brute_force_pdf(pdf_path, wordlist_path):
    # Check if files exist
    if not os.path.isfile(pdf_path):
        print(f"[❌] PDF file not found: {pdf_path}")
        return
    if not os.path.isfile(wordlist_path):
        print(f"[❌] Wordlist not found: {wordlist_path}")
        return

    # Open the PDF
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)

        if not reader.is_encrypted:
            print("[✔️] PDF is not password protected.")
            return

        print(f"[🔍] Brute-force starting on: {pdf_path}")

        # Load wordlist
        with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as wlist:
            for i, password in enumerate(wlist, 1):
                password = password.strip()

                try:
                    if reader.decrypt(password):
                        print(f"\n[✅] Password found: '{password}' at line {i}")
                        return
                except Exception:
                    continue  # Skip errors silently for speed

                # Optional: Print every N attempts
                if i % 1000 == 0:
                    print(f"[...] Tried {i} passwords...")

        print("\n[❌] Password not found in wordlist.")

# Main runner
if __name__ == "__main__":
    print("=== PDF Brute Force Tool - FAST MODE ===")
    pdf_path = input("Enter path to PDF file: ").strip()
    wordlist_path = input("Enter path to password wordlist (.txt): ").strip()
    brute_force_pdf(pdf_path, wordlist_path)