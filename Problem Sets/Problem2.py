# Simon McLain 2018-04-02
"""Write a function ispalindrome that takes a string and returns True if the string is
a palindrome and False otherwise. For example:
> ispalindrome("radar")
True
> ispalindrome("radars")
False"""

s = str(input("Enter a word to check if it is a palindrome:", ))

def ispalindrome(s):
  ans = True
  for i in range(len(s)):
    #loops over the range of s
    if s[i] != s[len(s) -i -1]:
      # check if first object in s does not equal last object
      ans = False
  return ans

print(ispalindrome(s))

