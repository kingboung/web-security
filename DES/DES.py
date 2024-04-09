#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 初始置换表
IP = [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7]

# 逆初始置换表
IPinv = [40, 8, 48, 16, 56, 24, 64, 32,
         39, 7, 47, 15, 55, 23, 63, 31,
         38, 6, 46, 14, 54, 22, 62, 30,
         37, 5, 45, 13, 53, 21, 61, 29,
         36, 4, 44, 12, 52, 20, 60, 28,
         35, 3, 43, 11, 51, 19, 59, 27,
         34, 2, 42, 10, 50, 18, 58, 26,
         33, 1, 41, 9, 49, 17, 57, 25]

# 置换选择1  C0表
C0 = [57, 49, 41, 33, 25, 17, 9,
      1, 58, 50, 42, 34, 26, 18,
      10, 2, 59, 51, 43, 35, 27,
      19, 11, 3, 60, 52, 44, 36]

# 置换选择1  D0表
D0 = [63, 55, 47, 39, 31, 23, 15,
      7, 62, 54, 46, 38, 30, 22,
      14, 6, 61, 53, 45, 37, 29,
      21, 13, 5, 28, 20, 12, 4]

# 轮数--左移次数
leftShitRound = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

# 置换选择2表
RStable = [14, 17, 11, 24, 1, 5, 3, 28,
           15, 6, 21, 10, 23, 19, 12, 4,
           26, 8, 16, 7, 27, 20, 13, 2,
           41, 52, 31, 37, 47, 55, 30, 40,
           51, 45, 33, 48, 44, 49, 39, 56,
           34, 53, 46, 42, 50, 36, 29, 32]

# 扩充置换表
Etable = [32, 1, 2, 3, 4, 5,
          4, 5, 6, 7, 8, 9,
          8, 9, 10, 11, 12, 13,
          12, 13, 14, 15, 16, 17,
          16, 17, 18, 19, 20, 21,
          20, 21, 22, 23, 24, 25,
          24, 25, 26, 27, 28, 29,
          28, 29, 30, 31, 32, 1]

# S盒表
Stable = [
    [
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
    ],
    [
        [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
    ],
    [
        [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
    ],
    [
        [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
    ],
    [
        [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
    ],
    [
        [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
    ],
    [
        [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
    ],
    [
        [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
    ]
]

# P表
Ptable = [16, 7, 20, 21, 29, 12, 28, 17,
          1, 15, 23, 26, 5, 18, 31, 10,
          2, 8, 24, 14, 32, 27, 3, 9,
          19, 13, 30, 6, 22, 11, 4, 25]

"""循环左移"""
def leftShit(binary):
    return binary[1:] + binary[0]

"""XOR运算"""
def XOR(L, R):
    result = ''
    for i in range(len(L)):
        if ((L[i]=='1') & (R[i]=='1')) | ((L[i]=='0') & (R[i]=='0')):
            result += '0'
        if ((L[i]=='1') & (R[i]=='0')) | ((L[i]=='0') & (R[i]=='1')):
            result += '1'
    return result

"""初始置换"""
def initSubstitution(cleartext):
    result = ''
    for i in range(64):
        result += cleartext[IP[i] - 1]
    L = result[:32]
    R = result[32:]
    return L, R

"""逆初始置换"""
def invInitSubstitution(binary):
    result = ''
    for i in range(64):
        result += binary[IPinv[i] - 1]
    return result

"""置换选择1"""
def replacementSelection1(secretkey):
    C = ''
    D = ''
    for i in range(28):
        C += secretkey[C0[i] - 1]
        D += secretkey[D0[i] - 1]
    return C, D

"""置换选择2"""
def replacementSelection2(C, D, round):
    secretKey = ''
    for i in range(round):
        C = leftShit(C)
        D = leftShit(D)
    tmp = C+D
    for i in range(48):
        secretKey += tmp[RStable[i]-1]
    return C, D, secretKey

"""扩充/置换(E)"""
def extension(R):
    result = ''
    for i in range(48):
        result += R[Etable[i]-1]
    return result

"""代换/选择（S盒）"""
def substitute(binary):
    result = ''
    for i in range(8):
        table = Stable[i]
        sixBin = binary[6*i:6*(i+1)]
        row = int(sixBin[0] + sixBin[-1], 2)
        column = int(sixBin[1:-1], 2)
        fourBin = table[row][column]
        result += bin(fourBin)[2:].zfill(4)
    return result

"""置换（P）"""
def permute(binary):
    result = ''
    for i in range(32):
        result += binary[Ptable[i] - 1]
    return result

"""生成密文"""
def generateCiphertext(cleartext, secretKey):
    L, R = initSubstitution(cleartext)
    C, D = replacementSelection1(secretKey)
    for i in range(16):
        C, D, key = replacementSelection2(C, D, leftShitRound[i])
        L, R = R, XOR(L, permute(substitute(XOR(extension(R), key))))
    return invInitSubstitution(R + L)

"""解密"""
def generateCleartext(ciphertext, secretKey):
    L, R = initSubstitution(ciphertext)
    C, D = replacementSelection1(secretKey)
    keyList = []
    for i in range(16):
        C, D, key = replacementSelection2(C, D, leftShitRound[i])
        keyList.append(key)
    for i in range(16):
        L, R = R, XOR(L, permute(substitute(XOR(extension(R), keyList[15 - i]))))
    return invInitSubstitution(R + L)

"""十进制(int)->二进制(str，64位)"""
def dec2bin(dec):
    return bin(dec)[2:].zfill(64)

"""十六进制(str)->二进制(str,64位)"""
def hex2bin(hex):
    dec = int(hex, 16)
    return bin(dec)[2:].zfill(64)

"""二进制(str)->十六进制(str)"""
def bin2hex(bin):
    dec = int(bin, 2)
    return hex(dec)[2:]



if __name__=='__main__':
    print('----------------------------------------------------------')
    print('                欢迎使用华仔DES加密解密系统                   ')
    print('----------------------------------------------------------')
    while True:
        print()
        print('请选择你的操作:1、加密      2、解密      3、退出')
        operationCode = input().strip()
        if operationCode == '1':
            cleartext = input('明文（64位二进制）：').strip()
            secretKey = input('密钥（64位二进制）：').strip()
            print('加密结果:' + generateCiphertext(cleartext, secretKey))
        if operationCode == '2':
            ciphertext = input('密文（16位十六进制）：').strip()
            secretKey = input('密钥（64位二进制）：').strip()
            print('解密结果：' + generateCleartext(ciphertext, secretKey))
        if operationCode == '3':
            print('退出成功......')
            break
