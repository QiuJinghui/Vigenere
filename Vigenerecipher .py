# 初始化密码盘
# Author：Jimmy
# 2020-1-16
# Version: 0.1


def initalizearray():
    # A-Z: ASCII : 65-90,0-9 : 48-57 共36个字符
    listTemp = []
    j = 48
    for i in range(1, 11):
        listTemp.append(chr(j))
        j = j + 1
    j = 65
    for i in range(11, 37):
        listTemp.append(chr(j))
        j = j + 1
    return listTemp


def initalizedisk(initaray):
    # 形成密码盘
    cipherdisk = []
    for i in range(0, 36):
        cipherdisk.append([])
        for j in range(0, 36):
            cipherdisk[i].append(initaray[j-i])
    return cipherdisk


def initalizekey(keylist, initaray):
    # 初始化密钥，将字母和数字的密钥更改为列表下标号存储
    keylist = keylist.upper()
    keylist = list(keylist)
    for i in range(len(keylist)):
        keylist[i] = initaray.index(keylist[i])
    return keylist


def getcipher(text, keylist, cipherdisk, initaray):
    # 用密码盘和密钥对明文加密，先将明文转为列表元素，再用维吉尼亚算法获取每个字符的密文
    text = text.upper()
    text = list(text)
    keylength = len(keylist)
    keyorder = 0
    for i in range(len(text)):
        row = keylist[keyorder]
        column = initaray.index(text[i])
        text[i] = cipherdisk[row][column]
        # 密钥切换到下一个字符，如果超过长度，回到起始点
        keyorder = keyorder + 1
        print(keyorder)
        if keyorder >= keylength:
            keyorder = 0
    return text


userkey = input("input a key")
userarray = initalizearray()
cleartext = input("input your cleartext")
initarray = initalizearray()
ciphertext = getcipher(cleartext, initalizekey(userkey, initarray), initalizedisk(initarray), initarray)
print(ciphertext)
