#!/usr/bin/env python
from usermodel import System
import pickle

if __name__ == "__main__":
    from os.path import exists
    system = System()
    if exists("./save.bin"):
        with open("./save.bin", "rb") as f:
            system = pickle.load(f)
    while True:
        system.do_iteration()
        with open("./save.bin", "wb") as f:
            pickle.dump(system, f)

