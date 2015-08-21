import random

def move(remaining):
    if not remaining:
        raise Exception('No more moves left')
    col = random.choice('abcdefg')
    if col in remaining:
        remaining.remove(col)
        return (col, remaining)
    else:
        return move(remaining)

def main():
    remaining = []
    for x in 'abcdefg': remaining.extend([x] * 6)
    string = ""
    for n in range(36):
        col, remaining = move(remaining)
        if (n%2 == 0):
            string += col.upper() + " "
        else:
            string += col
            string += "\n"
        n += 1
    print(string)
