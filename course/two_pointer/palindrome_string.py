def is_palindrome(string):
    start = 0
    end = len(string) -1
    while start < end:
        if string[end] != string[start]:
            return False
        start += 1
        end -= 1
    return True

string = "madam"
print(is_palindrome(string))