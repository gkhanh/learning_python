# def remove_non_alphabet_char(strings):
#     strings = strings.lower()
#     word_list = strings.split()
#     final_list = []
#     for word in word_list:
#         for i in word:
#             if not i.isalnum():
#                 word = word.replace(i, " ")
#         # word = ''.join(c for c in word if c.isalnum())
#         final_list.append(word)
#     return final_list

def remove_non_alphabet_char(string):
    string = string.lower()
    for i in string:
        if not i.isalnum():
            string = string.replace(i, " ")
    resultList = string.split()
    return resultList

def word_frequency(strings):
    word_list = remove_non_alphabet_char(strings)
    word_dict = {}
    for word in word_list:

        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    return word_dict


def process(strings, banned_word):
    banned = banned_word
    my_dict = word_frequency(strings)
    for word in my_dict:
        if word in banned:
            my_dict[word] = -1
    return my_dict


def largest(strings, banned_word):
    word_dict = process(strings, banned_word)
    k = list(word_dict.keys())
    val = list(word_dict.values())
    return k[val.index(max(val))]


def main():
    print(largest("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))


if __name__ == "__main__":
    main()


# class Solution:
#     def remove_non_alphabet_char(self, strings):
#         strings = strings.lower()
#         for i in strings:
#             if not i.isalnum():
#                 strings = strings.replace(i, " ")
#         resultList = strings.split()
#         return resultList
#
#     def word_frequency(self, strings):
#         word_list = self.remove_non_alphabet_char(strings)
#         word_dict = {}
#         for word in word_list:
#             if word in word_dict:
#                 word_dict[word] += 1
#             else:
#                 word_dict[word] = 1
#         return word_dict
#
#     def process(self, strings, banned_word):
#         banned = banned_word
#         my_dict = self.word_frequency(strings)
#         for word in my_dict:
#             if word in banned:
#                 my_dict[word] = -1
#         return my_dict
#
#     def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
#         word_dict = self.process(paragraph, banned)
#         k = list(word_dict.keys())
#         val = list(word_dict.values())
#         return k[val.index(max(val))]
