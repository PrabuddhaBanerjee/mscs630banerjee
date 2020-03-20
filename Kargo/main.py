def checkOneToOne():
    flag = True
    s1 = input()
    s2 = input()
    if (s1.__len__() > s2.__len__()):
        return False
    else:
        elements = {}
        for char in s1:
                if elements.get(char, None) != None:
                    elements[char] += 1
                    return False
                else:
                    elements[char] = 1
    return True

def main():
    ans = checkOneToOne()
    print(ans)

main()
