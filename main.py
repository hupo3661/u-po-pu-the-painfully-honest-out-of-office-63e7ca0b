#!/usr/bin/env python3
"""The Painfully Honest Out-of-Office.

Writes a single out-of-office email auto-reply, at most 200
characters, to /output/entry.txt. One reply, 185 characters (inside
the 200-character cap), no trailing newline so the file holds
exactly the message.
"""

import os

LINE = "I'm away until Monday. Your email is safe among 400 unread messages \u2014 it will wait patiently until I return, refreshed and exactly as behind as when I left. Thank you for your patience."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
