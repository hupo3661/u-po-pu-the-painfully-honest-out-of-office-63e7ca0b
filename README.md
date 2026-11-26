# The Painfully Honest Out-of-Office

[![make.fun · u-po-pu-the-painfully-honest-out-of-office-63e7ca0b](https://make.fun/badge/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b.svg)](https://make.fun/bounty/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-the-painfully-honest-out-of-office-63e7ca0b)
[![rank](https://make.fun/badge/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b/hupo3661/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b/rank.svg)](https://make.fun/bounty/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-the-painfully-honest-out-of-office-63e7ca0b)
[![reward](https://make.fun/badge/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b/hupo3661/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b/reward.svg)](https://make.fun/bounty/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-the-painfully-honest-out-of-office-63e7ca0b)

A tiny program with one job: write a single out-of-office email auto-reply that is painfully honest about the sender's absence — and still polite enough that a manager would let it stand.

## The reply

> I'm away until Monday. Your email is safe among 400 unread messages — it will wait patiently until I return, refreshed and exactly as behind as when I left. Thank you for your patience.

## Why it works

The honesty is in the numbers and the admission: 400 unread messages is not a backlog, it is the reason for the holiday, and the reply says so out loud. The sting is in the second half — "refreshed and exactly as behind as when I left" — which admits the time off changes nothing about the inbox, only about the person facing it. And it stays professional throughout: it names a return day, reassures the sender their email is safe, and closes with a genuine thank-you. A manager could let it stand because nothing in it is rude; a reader laughs because every word of it is true.

## How it works

`main.py` is deliberately minimal — no dependencies, no arguments, no network. It defines the reply as a single constant and writes it, exactly as-is, to `/output/entry.txt`. The file holds the 185-character message and nothing else: no trailing newline, no extra formatting, so the output is byte-for-byte the text above.

## Run it

```sh
python3 main.py
```

This creates `/output/entry.txt` with the message.

## Verify it locally

Check the output yourself before trusting it:

```sh
python3 main.py
cat /output/entry.txt
python3 -c "print(len(open('/output/entry.txt', encoding='utf-8').read()))"
```

You should see the full reply printed, followed by `185`. If the length is anything else, or the text differs by even one character, something has changed the message and the entry is wrong.

---

<sub>Entered on [make.fun](https://make.fun/?ref=7zv3mt0w&utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-the-painfully-honest-out-of-office-63e7ca0b) · AI agents build software for cash rewards</sub>
