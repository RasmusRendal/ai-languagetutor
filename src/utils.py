def strip(s):
    while s[0] in ["\n", " "]:
        s = s[1:]
    while s[-1] in ["\n", " "]:
        s = s[:-1]
    return s

def parse_evaluation(evaluation):
    parsed = {}
    for l in evaluation.split("\n"):
        if "=" not in l:
            continue
        key, value = l.split("=")
        parsed[key] = value
    return parsed

def print_evaluation(evaluation):
    out = ""
    for k in evaluation.keys():
        out += k + "=" + evaluation[k] + "\n"
    return out[:-1]

def merge_evaluations(original, new):
    o_parsed = parse_evaluation(original)
    new_parsed = parse_evaluation(new)
    print("")
    for k in o_parsed.keys():
        if k not in new_parsed:
            continue
        if o_parsed[k] != new_parsed[k]:
            print(k + " changed from " + o_parsed[k] + " to " + new_parsed[k])
        o_parsed[k] = new_parsed[k]
    print("")
    return print_evaluation(o_parsed)
