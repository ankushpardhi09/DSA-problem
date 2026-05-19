#find the First Non-Repeating Character in a String
s = "Leetcode"

for i in range(len(s)):
    if s.index(s[i]) == s.rindex(s[i]):
        print(i)
        break

