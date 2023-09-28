# def swapping(string1, string2):
#     # string3 = ""
#     # string3 = string2 #b
#     # string2 = string1
#     # string1 = string3
#     string1,string2 = string2,string1
#     return string1, string2

# def tail_swap(strings):
#     #'partA:partB', 'part1:part2'
#     #todo: swap partB and part2
#     string1 = strings[0]
#     string2 = strings[1]
#     parts_of_string1 = string1.split(':')
#     #partA,partB
#     parts_of_string2 = string2.split(':')
#     #part1,part2
#
#     result = []
#     result.append(parts_of_string1[0]+':'+parts_of_string2[1])
#     result.append(parts_of_string2[0] + ':' + parts_of_string1[1])
#     return result
#     pass

# def main():
#     print(tail_swap(['a:12345', '777:xyz']))
#
# if __name__ == "__main__":
#     main()

# def generate(startInt, numRows: int):
#     def makeRowNumber(result, rowNumber):
#         if rowNumber == 0:
#             return [startInt]
#         if rowNumber == 1:
#             return [startInt, startInt]
#         if rowNumber == 2:
#             return [startInt, startInt+startInt, startInt]
#         row = [startInt]
#         for i in range(1, rowNumber):
#             left = result[rowNumber - 1][i - 1]
#             right = result[rowNumber - 1][i]
#             sum = left + right
#             row.append(sum)
#         row.append(startInt)
#         return row
#
#     result = []
#     for i in range(numRows):
#         row = makeRowNumber(result, i)
#         result.append(row)
#     return result
#
#
# def main():
#     print(generate(4,7))
#
#
# if __name__ == "__main__":
#     main()


# def main():
#     print()
#
#
# if __name__ == "__main__":
#     main()

# def strings_construction(a, b):
#     dict_a = {}
#     dict_b = {}
#     for c in a:
#         dict_a[c] = dict_a.get(c, 0) + 1
#     for c in b:
#         dict_b[c] = dict_b.get(c, 0) + 1
#     result = 0
#
#     for c in dict_a:
#         if dict_a.keys() == dict_b.keys():
#             frequency1 = dict_a.get(c)
#             frequency2 = dict_b.get(c)
#             result = frequency2 // frequency1
#     return result
#
# def main():
#     print(strings_construction("hnccv","hncvohcjhdfnhonxddcocjncchnvohchnjohcvnhjdhihsn"))
#
#
# if __name__ == "__main__":
#     main()

# nameScoreDict = {}
# for _ in range(int(input())):
#     name = input()
#     score = float(input())
#     nameScoreDict[name] = score
# score_list = list(nameScoreDict.values())
# unique_score_list = list(set(score_list))
# unique_score_list.sort()
# second_lowest_score = unique_score_list[1]
# output = []
# for name, score in nameScoreDict.items():
#     if score == second_lowest_score:
#         output.append(name)
# output.sort()
# for student_name in output:
#     print(student_name)


