"""
find all palindromes from a list using filter

li = ['Raman', 'Madam', 'Naman', 'Rohan', 'Mam', 'Ram']
checkPalindrome = lambda val: val.lower() == val.lower()[::-1]
res = list(filter(checkPalindrome, li))
print(res)

def checkPalindrome(val):
    start = 0
    end = len(val) - 1
    while start < end:
        if val[start].lower() != val[end].lower():
            return False
        start += 1
        end -= 1

    return True

li = ['Raman', 'Madam', 'Naman', 'Rohan', 'Mam', 'Ram']
res = list(filter(checkPalindrome, li))
print(res)


"""

checkPalindrome=lambda val: val==int(str(val)[::-1])
li=[346,675,121,454,688,989,452]
res=list(filter(checkPalindrome,li))
print(res)

def checkPalindrome(num):
    copy=num
    rev=0
    while num>0:
        rem=num%10
        rev=rev*10+rem
        num=num//10
    return rev==copy

li=[346,675,121,454,688,989,452]
res=list(filter(checkPalindrome,li))
print(res)

