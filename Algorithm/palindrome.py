# Judging whether it is palindrome or not without using queues and stacks
# Make sure each letter is the same by comparing the text before and after.


def palindrome(s):
    n = len(s)
    i = 0  # first idx
    j = n - 1  # last idx
    while j // 2:
        if s[i].isalpha() is False:
            i += 1
        elif s[j].isalpha() is False:
            j -= 1
        elif s[i].lower() != s[j].lower():
            return False
        else:
            i += 1
            j -= 1
    return True


print(palindrome("God's dog"))
print(palindrome("racecar"))
print(palindrome("Madam, I'm Adam."))
print(palindrome("Modam, I am Adam."))