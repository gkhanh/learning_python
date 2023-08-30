def generate(numRows: int):
    result = []
    for i in range(numRows):
        row = makeRowNumber(result, i)
        result.append(row)
    return result


def makeRowNumber(result, rowNumber):
    row1 = [1]
    row2 = [1,1]
    result = []
    result.append(row1[0])
    for i in range(2,rowNumber):
        total = row2[i-2] + row2[i-1]

        result.append(total)
    result = result.append(row1[0])
    print(result)
    pass


def main():
    print(makeRowNumber([1],3))

if __name__ == "__main__":
    main()
