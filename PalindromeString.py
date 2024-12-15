a="abcda"
b="abcscba"
c="c"
print(a)
print(a[::-1])
print(a[3:0:-1])

#palindrome string
def isPalindrome(s:str) -> bool:
    for i in range(len(s)//2): #2
        if s[i] != s[len(s) -i -1]:
            return False
    return True

print(isPalindrome(a))
print(isPalindrome(b))
print(isPalindrome(c))

sum("9,10")