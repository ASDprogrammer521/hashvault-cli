import hashlib
import os
import json
import sys

BUFFER_SIZE = 65536

def calculate_hashes(filepath):
    md5 = hashlib.md5()
    sha256 = hashlib.sha256()
    sha512 = hashlib.sha512()

    try:
        with open(filepath, "rb") as f:
            while True:
                data = f.read(BUFFER_SIZE)
                if not data:
                    break
                md5.update(data)
                sha256.update(data)
                sha512.update(data)
        return {
            "md5": md5.hexdigest(),
            "sha256": sha256.hexdigest(),
            "sha512": sha512.hexdigest()
        }
    except FileNotFoundError:
        return None
    except PermissionError:
        return None

def single_file_hash():
    filepath = input("\nEnter file path: ").strip().strip('"')
    hashes = calculate_hashes(filepath)
    if not hashes:
        print("[!] Error: File not found or permission denied.")
        return

    print("\n" + "-" * 60)
    print(f"File    : {os.path.basename(filepath)}")
    print(f"MD5     : {hashes['md5']}")
    print(f"SHA-256 : {hashes['sha256']}")
    print(f"SHA-512 : {hashes['sha512']}")
    print("-" * 60)

def compare_files():
    file1 = input("\nEnter first file path: ").strip().strip('"')
    file2 = input("Enter second file path: ").strip().strip('"')

    h1 = calculate_hashes(file1)
    h2 = calculate_hashes(file2)

    if not h1 or not h2:
        print("[!] Error: One or both files could not be read.")
        return

    print("\n" + "-" * 60)
    print(f"File 1 SHA-256: {h1['sha256']}")
    print(f"File 2 SHA-256: {h2['sha256']}")
    if h1["sha256"] == h2["sha256"]:
        print("\n[+] MATCH: Both files are completely identical.")
    else:
        print("\n[!] MISMATCH: Files have been modified or differ.")
    print("-" * 60)

def create_baseline():
    folder = input("\nEnter directory path to snapshot: ").strip().strip('"')
    if not os.path.isdir(folder):
        print("[!] Error: Invalid directory path.")
        return

    baseline = {}
    for root, _, files in os.walk(folder):
        for name in files:
            full_path = os.path.join(root, name)
            rel_path = os.path.relpath(full_path, folder)
            hashes = calculate_hashes(full_path)
            if hashes:
                baseline[rel_path] = hashes["sha256"]

    out_file = os.path.join(folder, "hashvault_baseline.json")
    with open(out_file, "w") as f:
        json.dump(baseline, f, indent=4)

    print(f"\n[+] Baseline created for {len(baseline)} files.")
    print(f"[+] Saved to: {out_file}")

def verify_baseline():
    folder = input("\nEnter directory path to verify: ").strip().strip('"')
    baseline_file = os.path.join(folder, "hashvault_baseline.json")

    if not os.path.exists(baseline_file):
        print("[!] Error: No baseline found in this directory.")
        return

    with open(baseline_file, "r") as f:
        old_baseline = json.load(f)

    current_files = {}
    for root, _, files in os.walk(folder):
        for name in files:
            if name == "hashvault_baseline.json":
                continue
            full_path = os.path.join(root, name)
            rel_path = os.path.relpath(full_path, folder)
            hashes = calculate_hashes(full_path)
            if hashes:
                current_files[rel_path] = hashes["sha256"]

    print("\n" + "=" * 60)
    print("                 INTEGRITY AUDIT REPORT")
    print("=" * 60)

    changes = False
    for path, old_hash in old_baseline.items():
        if path not in current_files:
            print(f"[-] DELETED  : {path}")
            changes = True
        elif current_files[path] != old_hash:
            print(f"[!] MODIFIED : {path}")
            changes = True

    for path in current_files:
        if path not in old_baseline:
            print(f"[+] NEW FILE : {path}")
            changes = True

    if not changes:
        print("[*] CLEAN: All files match the baseline snapshot.")
    print("=" * 60)

def main():
    while True:
        print("\n====================================================")
        print("       HashVault CLI - File Integrity Utility")
        print("====================================================")
        print("1. Calculate File Hashes (MD5, SHA-256, SHA-512)")
        print("2. Compare Two Files")
        print("3. Create Directory Baseline Snapshot")
        print("4. Verify Directory Integrity")
        print("5. Exit")
        print("----------------------------------------------------")

        choice = input("Select an option (1-5): ").strip()

        if choice == "1":
            single_file_hash()
        elif choice == "2":
            compare_files()
        elif choice == "3":
            create_baseline()
        elif choice == "4":
            verify_baseline()
        elif choice == "5":
            print("Exiting HashVault...")
            break
        else:
            print("[!] Invalid choice. Please select 1-5.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[!] Aborted by user.")
        sys.exit()

#by ASDcuber
