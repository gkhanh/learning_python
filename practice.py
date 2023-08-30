# def swapping(string1, string2):
#     # string3 = ""
#     # string3 = string2 #b
#     # string2 = string1
#     # string1 = string3
#     string1,string2 = string2,string1
#     return string1, string2

def tail_swap(strings):
    #'partA:partB', 'part1:part2'
    #todo: swap partB and part2
    string1 = strings[0]
    string2 = strings[1]
    parts_of_string1 = string1.split(':')
    #partA,partB
    parts_of_string2 = string2.split(':')
    #part1,part2

    result = []
    result.append(parts_of_string1[0]+':'+parts_of_string2[1])
    result.append(parts_of_string2[0] + ':' + parts_of_string1[1])
    return result
    pass

def main():
    print(tail_swap(['a:12345', '777:xyz']))

if __name__ == "__main__":
    main()




