s = "abdq"
t = "ahbgdc"

def is_sequence(s, t):
    i = 0
    j = 0
    sub = ""

    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            sub += s[i]
            i += 1
            j += 1
        else:
            j += 1
    return s == sub

print(is_sequence(s, t))

