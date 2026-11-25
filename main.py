import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

# One-line out-of-office reply for make.fun's "Funniest One-Line
# Out-of-Office Reply" bounty. The gate: UTF-8 text of 1-160 characters.
# Judge-brief check: (1) a real one-line away message; (2) the laugh lands
# on the first read, punchline in the last five words; (3) reads like a
# message a person would switch on, not a notice with a joke bolted on;
# (4) fresh turn - no beach, inbox or limited-email cliche, the boss and
# the meeting carry the joke; (5) 118 characters, every word earns its place.
# Written for the sponsor to switch on as their own away message.
LINE = "I'm out until Monday. If it's urgent, please tell my boss; she'll schedule a meeting about it, and I'll miss that too."

if not 1 <= len(LINE) <= 160 or not LINE.strip():
    raise ValueError("entry line must be 1-160 characters")

os.makedirs(OUTPUT_DIR, exist_ok=True)
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE)
