def canConstruct(ransomNote, magazine):
    magazine = list(magazine)
    for i in ransomNote:
        if i in magazine:
            magazine.remove(i)
        else:
            return False
    return True


s1 = 'aa'
s2 = 'ab'
print(canConstruct(s1, s2))
