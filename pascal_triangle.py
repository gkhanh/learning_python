def generate(numRows: int):
    result = []
    for i in range(numRows):
        row = makeRowNumber(result, i)
        result.append(row)
    return result


def makeRowNumber(result, rowNumber):
    if rowNumber == 0:
        return [1]
    if rowNumber == 1:
        return [1, 1]
    if rowNumber == 2:
        return [1, 2, 1]
    row = [1]
    for i in range(1, rowNumber):
        left = result[rowNumber - 1][i - 1]
        right = result[rowNumber - 1][i]
        sum = left + right
        row.append(sum)
    row.append(1)
    return row
    pass


# class Solution(object):
#     def generate(self, numRows):
#         # Create an array list to store the output result...
#         output = []
#         for i in range(numRows):
#             if (i == 0):
#                 # Create a list to store the prev triangle value for further addition...
#                 # Inserting for the first row & store the prev array to the output array...
#                 prev = [1]
#                 output.append(prev)
#             else:
#                 curr = [1]
#                 j = 1
#                 # Calculate for each of the next values...
#                 while (j < i):
#                     # Inserting the addition of the prev arry two values...
#                     curr.append(prev[j - 1] + prev[j])
#                     j += 1
#                 # Store the number 1...
#                 curr.append(1)
#                 # Store the value in the Output array...
#                 output.append(curr)
#                 # Set prev is equal to curr...
#                 prev = curr
#         return output  # Return the output list of pascal values...


def main():
    print(generate(4))


if __name__ == "__main__":
    main()
