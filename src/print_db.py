import pickle

if __name__ == "__main__":
    system = None
    with open("./save.bin", "rb") as f:
        system = pickle.load(f)
    print("System iteration: " + str(system.iteration))
    print("Schedule:")
    for k in system.schedule.keys():
        if k <= system.iteration:
            continue
        print("Iteration: " + str(k))
        print(str(system.schedule[k]))
        print("")
