# Exercise 1
def char_count_1(text):
    frequency = []  # Store number of appearance
    this_set = set()  # to store unique character appeared how many times
    this_set.update(text)  # store all the letters without duplicating letter
    for c in this_set:
        counting = text.count(c)
        frequency.append(counting)
    letter_list = list(this_set)
    # print(letter_list)
    for i in range(0, len(letter_list)):
        print(f'{letter_list[i]} - {frequency[i]}')
    # print(letter_list)
    # print(frequency)


# def char_count_2(text):
#     my_dict = {}  # initialize hashmap
#     for c in text:
#         counting = text.count(c)
#         my_dict.update({f"{c}": counting})
#     # print(my_dict)
#     return my_dict


def main():
    char_count_1("appearance")
    # print(char_count_2("appearance"))


if __name__ == "__main__":
    main()
#
#
# def solve_1(startX, startY, destX, destY):
#     result = abs((destX - startX)) + abs((destY - startY))
#     return result
#
#
# # with diagonal movement
#
# def solve_2(startX, startY, destX, destY):
#     return max(max(startX, startY), max(destX, destY))
#
#
# def main():
#     print(solve_1(3, 1, 0, 4))
#     print(solve_2(3, 0, 1, 4))
#
#
# if __name__ == "__main__":
#     main()
#
#

# def count_sheep(n):
#     # your code
#     if n == 0:
#         return ""
#     if n == 1:
#         return "1 sheep..."
#     text = ""
#     for i in range(1, n+1):
#         text += (str(i) + " sheep...")
#
#     return text
#
#
# def main():
#     print(count_sheep(5))
#
#
# if __name__ == "__main__":
#     main()

# def make_row_number(row):
#     # result = []
#
#     if row == 0:
#         return [1]
#     if row == 1:
#         return [1, 1]
#     if row == 2:
#         return [1, 2, 1]
#     result = [1]
#     for i in range(1, row):
#         left_side = result[row-1][i - 1]
#         right_side = result[row-1][i]
#         total = left_side + right_side
#         result.append(total)
#     result.append(1)
#     return result
#
#
# def pascal_triangle(number):
#     result = []
#     for i in range(number):
#         row = make_row_number(i)
#         result.append(row)
#     return result
#
#
# def main():
#     print(pascal_triangle(4))
#
#
# if __name__ == "__main__":
#     main()


# import numpy
#
# n = int(input())
# a = []
# b = []
# for i in range(n):
#     a.append(list(map(int, input().split())))
# for i in range(n):
#     b.append(list(map(int, input().split())))
# a = numpy.array(a)
# b = numpy.array(b)
#
# print(numpy.dot(a, b))

# thickness = int(input())  # This must be an odd number
# c = 'H'
#
# # Top Cone
# for i in range(thickness):
#     print((c * i).rjust(thickness - 1) + c + (c * i).ljust(thickness - 1))
#
# # Top Pillars
# for i in range(thickness + 1):
#     print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))
#
# # Middle Belt
# for i in range((thickness + 1) // 2):
#     print((c * thickness * 5).center(thickness * 6))
#
# # Bottom Pillars
# for i in range(thickness + 1):
#     print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))
#
# # Bottom Cone for i in range(thickness): print(((c * (thickness - i - 1)).rjust(thickness) + c + (c * (thickness -
# i - 1)).ljust(thickness)).rjust(thickness * 6))
