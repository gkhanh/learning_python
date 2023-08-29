# Exercise 1
def char_count_1(text):
    frequency = []  # Store number of appearance
    this_set = set()  # to store unique character appeared how many times
    this_set.update(text)  # store all the letters without duplicating letter
    for c in this_set:
        counting = text.count(c)
        frequency.append(counting)
    letter_list = list(this_set)
    print(letter_list)
    for i in range(0, len(letter_list)):
        print(f'{letter_list[i]} - {frequency[i]}')
    print(letter_list)
    print(frequency)


def char_count_2(text):
    my_dict = {}  # initialize hashmap
    for c in text:
        counting = text.count(c)
        my_dict.update({f"{c}": counting})
    print(my_dict)


def main():
    print(char_count_1("appearance"))
    print(char_count_2("appearance"))


if __name__ == "__main__":
    main()


def solve_1(startX, startY, destX, destY):
    result = abs((destX - startX)) + abs((destY - startY))
    return result


# with diagonal movement

def solve_2(startX, startY, destX, destY):
    return max(max(startX, startY), max(destX, destY))


def main():
    print(solve_1(3, 1, 0, 4))
    print(solve_2(3, 0, 1, 4))


if __name__ == "__main__":
    main()
