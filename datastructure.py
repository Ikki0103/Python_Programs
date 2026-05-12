
# nums = {2,7,11,15}
# target =9
def two_sum(nums, target):
    for i in nums:
        need = target - i
        if need in nums and need != i:
            return (i, need)
    return None


# Example:
# print(two_sum([2, 7, 11, 15], 9))
# two_sum([1, 3, 5], 10)     → None
# print(two_sum([7, 2, 11, 15], 9))
# two_sum([1, 3, 5], 10)


def is_palindrome(text):
    palindrome_text = text.replace(" ", "").lower()
    return palindrome_text == palindrome_text[::-1]  # that is a reverse string

# print(is_palindrome("racecar"))
# print(is_palindrome("Race Car"))
# print(is_palindrome("hello"))
# print(is_palindrome("A man a plan a canal Panama"))


def most_frequent(words):
    the_dictionary = {}
    for word in words:
        if word in the_dictionary:
            the_dictionary[word] += 1
        else:
            the_dictionary[word] = 1
    return max(the_dictionary, key=the_dictionary.get)


print(most_frequent(["apple", "banana", "apple", "cherry", "banana", "apple"]))

# most_frequent(["dog", "cat", "dog", "cat"])
# → "dog" or "cat" (either is fine)
