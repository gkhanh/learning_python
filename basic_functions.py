def count_positives_sum_negatives(arr):
    count_pos = 0
    result = 0
    for number in arr:
        if number >= 0:
            count_pos = count_pos + 1
        else:
            result += number

    print(count_pos)
    print(result)
    return [count_pos, result]


def reverse_words(text):
    # go for it
    words = text.split()
    new_words = []
    reversed_string = ""
    for i in words:
        word_reversed = i[::-1]
        new_words.append(word_reversed)
    reversed_string = ' '.join(new_words)
    return reversed_string


def main():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -34, -70, -120, -185]
    count_positives_sum_negatives(arr)
    print(reverse_words("This is an example!"))


if __name__ == "__main__":
    main()
