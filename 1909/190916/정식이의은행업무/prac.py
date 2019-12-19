def samzin(szin, x):  # 3진수 경우의 수
    global result_3
    n = len(szin)
    for i in range(n):
        for j in range(3, -1, -1):
            if szin[i] == 0:
                result_3.append(szin[0:i] + '1' + szin[i + 1:n])
                result_3.append(szin[0:i] + '2' + szin[i + 1:n])
            else:
                temp = j - int(szin[i])
                if temp >= 0:
                    result_3.append(szin[0:i] + str(temp) + szin[i+1:n])

def change(x, jinsoo):  # x진수를 10진수로
    res = 0
    for i in range(len(x)):
        if int(x[i]) != 0:
            res += int(jinsoo**(len(x)-i-1)) * int(x[i])
    return res

def eezin(ezin, x):  # 2진수 경우의 수
    global result_2
    n = len(ezin)
    for i in range(n):
        if ezin[i] == '1':
            result_2.append(ezin[0:i] + '0' + ezin[i+1:n])
        else:
            result_2.append(ezin[0:i] + '1' + ezin[i+1:n])

result_3 = []
result_2 =[]

eezin('1010', 1010)
print(result_2)
for i in result_2:
    print(change(i, 2))