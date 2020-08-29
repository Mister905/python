# generator solution
def even_integers_generator(n):
    for i in range(n):
        if i % 2 == 0:
            yield i


def main():
    even_nums = even_integers_generator(20)
    print(list(even_nums))
  
if __name__ == "__main__": main()