# Lists are mutable, tuples are not
# Arrays and lists are both used in Python to store data, but they don't serve exactly the same purposes. They both can be used to store any data type (real numbers, strings, etc), and they both can be indexed and iterated through, but the similarities between the two don't go much further. The main difference between a list and an array is the functions that you can perform to them. For example, you can divide an array by 3, and each number in the array will be divided by 3 and the result will be printed if you request it. If you try to divide a list by 3, Python will tell you that it can't be done, and an error will be thrown.

# Lists are generally used more often between the two, which works fine most of the time. However, if you're going to perform arithmetic functions to your lists, you should really be using arrays instead. Additionally, arrays will store your data more compactly and efficiently, so if you're storing a large amount of data, you may consider using arrays as well.

def main():
    game = [ 'Rock', 'Paper', 'Scissors', 'Lizard', 'Spock' ]
    print_list(game)

def print_list(o):
    for i in o: print(i, end=' ', flush=True)
    print()

if __name__ == '__main__': main()