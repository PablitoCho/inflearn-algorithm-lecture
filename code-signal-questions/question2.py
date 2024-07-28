# String Pattern Matching

pattern = input()
source = input()

def vowel(char):
    return char in ['a', 'e', 'i', 'o', 'u', 'y']

def checkPattern(pattern, chars):
    for p, ch in zip(pattern, chars):
        isVowel = vowel(ch)
        if int(p) == 0 and isVowel: # check vowel
            continue
        elif int(p) == 1 and not isVowel: # check consonant
            continue
        else:
            return False
    return True


answer = 0

for k in range(0, len(source) - len(pattern)):
    chars = source[k:k+len(pattern)]
    if checkPattern(pattern, chars):
        answer += 1

print(answer)