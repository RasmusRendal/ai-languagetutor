#!/usr/bin/env python
from prompts import *

if __name__ == "__main__":
    from os.path import exists
    skills = ""
    if exists("./skills.txt"):
        skills = open("./skills.txt", "r").read()
    else:
        skills = open("./skills_template.txt", "r").read()

    print("Initial evaluation:")
    print(skills)
    while "5" in skills or "4" in skills or "3" in skills or "2" in skills:
        skills = one_exercise(skills)
        with open("./skills.txt", "w") as f:
            f.write(skills)

