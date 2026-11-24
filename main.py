"""Everyday Things, Two Lines, Longer Run — entry for make.fun.

Writes two lines to /output/entry.txt. Line 1 explains a toaster to a 10-year-old with an analogy, line 2 says why the analogy works and what it leaves out.
"""
import os

LINE1 = "A toaster is like a tiny sun that lives in a box on your kitchen counter and tans your bread until it turns golden."
LINE2 = "The analogy works because both give off heat and change colour, but it leaves out that the sun never pops up with a ding when it is done."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE1 + "\n" + LINE2 + "\n")

if __name__ == "__main__":
    main()
