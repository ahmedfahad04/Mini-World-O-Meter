def radix(string, bb):
    k = -1
    a2 = 0
    for id in range(len(string)):
        if string[id] >= 'A' and string[id] <= 'F':
            a2 += hexa[string[id]]*(int(bb)**k)
            k -= 1
        else:
            a2 += int(string[id])*(int(bb)**k)
            k -= 1

    return float(a2)


def all2dec(number, base):
    l = len(number)
    l -= 1
    ans = 0
    if base == '16':
        for i in number:
            if i >= 'A' and i <= 'F':
                ans += hexa[i]*(int(base)**l)
                l -= 1
            else:
                ans += int(i)*(int(base)**l)
                l -= 1

    else:
        ans = 0

        for i in number:

            ans += int(i)*(int(base)**l)
            l -= 1

    return int(ans)


hexa = {
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15,
}

num = input("Enter number: ")
b = input("Enter base: ")

newn = []
rad = []
k = num.find('.')
for i in range(0, len(num)):
    if i == k:
        break
    else:
        newn.append(num[i])

for x in range(k+1, len(num)):
    rad.append(num[x])


if b == '2':
    if(k != -1):
        print("Binary is: ", all2dec(newn, b) + radix(rad, b))
    else:
        print("Binary is: ", all2dec(num, b) )
elif b == '8':
    if(k != -1):
        print("Octal is: ", all2dec(newn, b) + radix(rad, b))
    else:
        print("Octal is: ", all2dec(num, b) )
elif b == '16':
    if(k != -1):
        print("Hexadecimal is: ", all2dec(newn, b) + radix(rad, b))
    else:
        print("Hexadecimal is: ", all2dec(num, b) )

# else:
#     if(k != -1):
#         print("%d Binary %d is: "%( num, all2dec(newn, 2) + radix(rad, 2)))
#         print("%d Octal %d is: "% (num ,all2dec(newn, 8) + radix(rad, 8)))
#         print("%d Hexadecimal %d is: "% (num, all2dec(newn, 16) + radix(rad, 16)))
#     else:
#         print("Binary is: ", all2dec(num, 2) )
#         print("Octal is: ", all2dec(num, 8) )
#         print("Hexadecimal is: ", all2dec(num, 16) )



