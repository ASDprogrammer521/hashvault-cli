<div align="center">

# 🔐 HashVault CLI

**A fast, zero-dependency file integrity monitor and cryptographic hash verifier written in Python.**

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Windows%20%7C%20macOS-2EA44F?style=for-the-badge)]()
[![Dependencies](https://img.shields.io/badge/Dependencies-None-orange?style=for-the-badge)]()
[![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)](LICENSE)

</div>

---

## 📖 Overview

**HashVault CLI** is a lightweight digital forensics and cybersecurity utility built with Python's standard library. It computes multi-algorithm cryptographic checksums, verifies file authenticity, and monitors directories for unauthorized file modifications, additions, or deletions.

---

## ⚡ Key Features

- **Multi-Algorithm Hashing:** Generates `MD5`, `SHA-256`, and `SHA-512` checksums simultaneously using buffered chunk reading (handles large files efficiently).
- **Binary File Comparison:** Compares two files at the cryptographic hash level to verify exact integrity.
- **Directory Integrity Monitoring (FIM):** Creates a JSON baseline snapshot of a directory and audits it later to detect modified, deleted, or newly injected files.
- **Zero External Dependencies:** Uses only built-in Python modules (`hashlib`, `os`, `json`).

---

## 🚀 Installation & Usage

### 1. Clone the repository
```bash
git clone [https://github.com/ASDcuber/hashvault-cli.git](https://github.com/ASDcuber/hashvault-cli.git)
cd hashvault-cli
