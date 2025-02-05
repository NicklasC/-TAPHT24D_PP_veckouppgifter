def find_2nd_max(list):
    if len(list) >= 2:
        return sorted(list)[-2]
    else:
        return None
