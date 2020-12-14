Hex = {
    10 : 'A',
    11 : 'B',
    12 : 'C',
    13 : 'D',
    14 : 'E',
    15 : 'F',
}
revhex = {
    'A':10,
    'B':11,
    'C':12,
    'D':13,
    'E':14,
    'F':15,
}
#all functions

def fraction2de(frac,bbb):
    fr = str(frac).lstrip("0.")
    #print(fr)
    if(bbb == 16):
        res2 = 0
        for i in range(1,len(fr)+1,1):
            if(str(fr[i-1]) >= 'A'):
                res2 += int(revhex[str(fr[i - 1])]) * (bbb ** (-i))
                #print("Value of I; ",i)
                #print("Result: ",res2)
            else:
                res2 += int(fr[i - 1]) * (bbb ** (-i))


    else:
        res = 0
        for i in range(1, len(fr)+1, 1):
            res += int(fr[i - 1]) * (bbb ** (-i))
    if(bbb == 16):
        return res2
    else:
        return res


def de2fraction(frac,bb):
    k = frac
    out = []
    hexad = []
    for i in range(0,20,1):
        k = k*bb
        #print(int(k))
        if(bb == 16):
            if(int(k) >= 10):

                hexad.append(Hex[int(k)])
            else:
                hexad.append(str(int(k)))

        out.append(int(k))
        k = k-int(k)
        if(k == 0):
            break

    length = len(out)
    ans = 0
    for i in out:
        ans += i*(10**(length-1))
        length -= 1


    ans2 = "".join(hexad)
    if(bb == 16):
        return ans2
    else:
        return ans/(10**len(out))

def all2dec(numb,Base):
    return int(numb,Base)

def Decimal(n1,ba):
    fd = fraction2de(fraction,ba)
    print("Decimal of " + number + " is: ", int(int(n1, ba))+float(fd))




# All to all
print("Instruction\n\ttype 'b' for Binary\n\ttype 'o' for Octal\n\ttype 'h' for Hexadecimal\n\ttype 'd' for Decimal\n")
From = input("Covert From: ")
To = input("Convert To: ")


#taking number as input

a = (input("Enter Number: "))
ayhay = a.split(".")
if (len(ayhay) == 2):
    fraction = ayhay[1]
    number = str((ayhay[0]))
else:
    fraction = 0
    number = str((ayhay[0]))


#distributing conversion according to choice

if From == 'h':
    if To == 'd':
        Decimal(number,16)
    elif To == 'o':
        o = oct(all2dec(number, 16)).lstrip("0o").rstrip("L")
        fd = fraction2de(fraction, 16)
        f = de2fraction(float(fd), 8)
        print("Octal of " + a + " is: ", float(o)+float(f))
    else:
        b = bin(all2dec(number, 16)).lstrip("0b").rstrip("L")
        fd = fraction2de(fraction, 16)
        fm = de2fraction(float(fd), 2)
        print("Binary of " + a + " is: ", float(b) + float(fm))

if From == 'b':
    if To == 'd':
        Decimal(number,2)
    elif To == 'o':
        o = oct(all2dec(number, 2)).lstrip("0o").rstrip("L")
        fd = fraction2de(fraction, 2)
        f = de2fraction(float(fd), 8)
        print("Octal of " + a + " is: ", float(o) + float(f))
    else:
        h = hex(all2dec(number, 2)).lstrip("0x").rstrip("L").upper()
        fd = fraction2de(fraction, 2)
        fm = de2fraction(float(fd), 16)
        print("Hexadecimal of " + str(a) + " is: ", str(h) + "." + str(fm))

if From == 'o':
    if To == 'd':
        Decimal(number,8)
    elif To == 'h':
        h = hex(all2dec(number, 8)).lstrip("0x").rstrip("L").upper()
        fd = fraction2de(fraction, 8)
        fm = de2fraction(float(fd), 16)
        print("Hexadecimal of " + str(a) + " is: ", str(h) + "." + str(fm))
    else:
        b = bin(all2dec(number, 8)).lstrip("0b").rstrip("L")
        fd = fraction2de(fraction, 8)
        fm = de2fraction(float(fd), 2)
        print("Binary of " + str(a) + " is: ",float(b) + float(fm))

if From == 'd':
    if To == 'h':
        h = hex(all2dec(number, 10)).lstrip("0x").rstrip("L").upper()
        fd = fraction2de(fraction, 10)
        fm = de2fraction(float(fd), 16)
        print("Hexadecimal of " + str(a) + " is: ", str(h) + "." + str(fm))
    elif To == 'o':
        o = oct(all2dec(number, 10)).lstrip("0o").rstrip("L")
        fd = fraction2de(fraction, 10)
        f = de2fraction(float(fd), 8)
        print("Octal of " + a + " is: ", float(o) + float(f))
    else:
        b = bin(all2dec(number, 10)).lstrip("0b").rstrip("L")
        fd = fraction2de(fraction, 10)
        fm = de2fraction(float(fd), 2)
        print("Binary of " + str(a) + " is: ", float(b) + float(fm))






