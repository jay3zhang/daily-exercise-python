# coding=utf-8

# 判断乱序字符串
# 方法2
def anagramSolution2(s1,s2):
    alist1 = list(s1)
    alist2 = list(s2)
    
    
    alist1.sort()
    alist2.sort()

    # pos = 0
    # matches = True
    matches = False

    if alist1==alist2:
        matches = True
    # while pos < len(s1) and matches:
        # if alist1[pos]==alist2[pos]:
            # pos = pos + 1
        # else:
            # matches = False

    return matches

print(anagramSolution2('this is o','o is isth'))
# print(anagramSolution2('abcde','edcba'))
# print(anagramSolution2('abcdf','edcba'))

# 方法3
def anagramSolution3(s1,s2):
    c1 = [0]*26
    c2 = [0]*26

    for i in range(len(s1)):
        pos = ord(s1[i])-ord('a')
        c1[pos] = c1[pos] + 1

    for i in range(len(s2)):
        pos = ord(s2[i])-ord('a')
        c2[pos] = c2[pos] + 1

    stillOK = False
    if c1==c2:
        stillOK = True
    # j = 0
    # stillOK = True
    # while j<26 and stillOK:
        # if c1[j]==c2[j]:
            # j = j + 1
        # else:
            # stillOK = False

    return stillOK

# print(anagramSolution3('apple','pleap'))
# print(anagramSolution3('apple','plaeap'))
# print(anagramSolution3('apple','pleaf'))

def anagramSolution4(s1,s2):    # 任意字符组成的字符串
    c1 = [0]*256
    c2 = [0]*256
    
    for i in s1:
        c1[ord(i)] += 1
    for i in s2:
        c2[ord(i)] += 1
    
    stillOK = False
    if c1==c2:
        stillOK = True
        
    return stillOK
        