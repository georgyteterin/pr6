word1=input()
word2=input()
def is_anagram(word1, word2):
    return sorted(word1.replace(" ", "")) == sorted(word2.replace(" ", ""))
print(is_anagram(word1, word2))
