# 🔐 Encrypted Keylogger PoC with Simulated Remote Server

**ElevateLabs Internship Project**

## 🎯 Objective

This Proof of Concept (PoC) explores keystroke logging, symmetric encryption, and simulated client-server communication in a controlled local environment.

The project demonstrates how captured input can be handled and protected using encryption and how a locally hosted Flask server can be used to simulate receiving files.

> ⚠️ This project was developed strictly for ethical, educational, and security research purposes.

---

## ⚙️ Concepts Demonstrated

- 🎹 **Keystroke Logging** — Demonstrates keyboard event capture in a controlled environment.
- 🛑 **Kill Switch** — Provides a mechanism to stop the demonstration.
- 🔐 **Symmetric Encryption** — Uses Fernet-based encryption to protect log data.
- 📡 **Client-Server Communication** — Demonstrates communication with a locally hosted Flask server.
- 🗂️ **File Handling** — Demonstrates encrypted and decrypted file processing.
- 🐍 **Python Security Programming** — Combines Python libraries for a cybersecurity-focused proof of concept.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Core application development |
| Pynput | Keyboard event handling |
| Cryptography / Fernet | Symmetric encryption |
| Flask | Local server simulation |
| Requests | HTTP communication |
| File Handling | Log and encrypted-file processing |

---

## 📂 Project Structure

```text
.
├── keylogger.py      # Main PoC application
├── server.py         # Local Flask server simulation
├── secret.key        # Generated encryption key
├── keylogs.txt       # Demonstration log data
├── encrypted_log.txt # Encrypted demonstration data
├── decrypted_log.txt # Decrypted demonstration data
└── uploads/          # Local server upload directory
