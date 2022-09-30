#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return
    best_key = []
    best_key_str = ""
    for key, val in a_dictionary.items():
        if len(best_key) == 0:
            max_val = val
            best_key.append(key)
        else:
            if val > max_val:
                max_val = val
                best_key.pop()
                best_key.append(key)
    return best_key_str.join(best_key)
