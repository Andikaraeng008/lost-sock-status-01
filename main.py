"""Funniest Lost Sock Status Update — one-line entry.

Writes the lost sock's status update to the grader's output file.
One status update, at most 120 characters, in the sock's own voice,
with the twist in its final words. Deterministic: same line on every run.
Candidate S2 (absurd, 96 characters) — chosen by Ahmad.
"""
import os

LINE = "Day 47 behind the washing machine. I started a family with a dust bunny. The dryer took my wife."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
