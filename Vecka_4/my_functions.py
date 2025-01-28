def print_is_a_hacker(name):
    print(f"{name} är en riktig hacker")

def eko(what_to_echo:str):
    print(what_to_echo*2)

def eko_multiple(what_to_echo:str,number_of_times:int):
    print(what_to_echo*number_of_times)

def uppgift_3_func(number_of_times:int):
    end = number_of_times
    y = 1
    for x in range(1, 100):
        y *= 2
        if x == end:
            break
        # avsluta loopen med en if-sats här

    print(y)

def last(list:list):
    return list[-1]

def cut_edges(list:list):
    return list[1:-1]

def increase(x):
    x += 1
    return x

def average(a,b):
    return (a+b)/2

def pretty_print(list:list):
    if len(list) is 0:
        print("tom")
    else:
        print(f"Listan har {len(list)} element:")
        for item in list:
            print(item)