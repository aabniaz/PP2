s = input()
upper, lower = 0, 0
for i in range(len(s)):
    if s[i] >= 'A' and s[i] <= 'Z':
        upper += 1
    elif s[i] >= 'a' and s[i] <= 'z':
        lower += 1
print("number of upper case letters:", upper, "\nnumber of lower case letters:", lower)