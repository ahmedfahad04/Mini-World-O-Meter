Hex = {
    10: 'A',
    11: 'B',
    12: 'C',
    13: 'D',
    14: 'E',
    15: 'F',
}
reversehex = {
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15,
}


# all functions

def fraction2de(frac, bbb):
    fr = str(frac).lstrip("0.")
    if bbb == 16:
        res2 = 0
        for i in range(1, len(fr) + 1, 1):
            if (str(fr[i - 1]) >= 'A'):
                res2 += int(reversehex[str(fr[i - 1])]) * (bbb ** (-i))
            else:
                res2 += int(fr[i - 1]) * (bbb ** (-i))


    else:
        res = 0
        for i in range(1, len(fr) + 1, 1):
            res += int(fr[i - 1]) * (bbb ** (-i))
    if bbb == 16:
        return res2
    else:
        return res


def de2fraction(frac, bb):
    k = frac
    out = []
    hexad = []
    for i in range(0, 20, 1):
        k = k * bb
        # print(int(k))
        if (bb == 16):
            if (int(k) >= 10):

                hexad.append(Hex[int(k)])
            else:
                hexad.append(str(int(k)))

        out.append(int(k))
        k = k - int(k)
        if (k == 0):
            break

    length = len(out)
    ans = 0
    for i in out:
        ans += i * (10 ** (length - 1))
        length -= 1

    ans2 = "".join(hexad)
    if (bb == 16):
        return ans2
    else:
        return ans / (10 ** len(out))


def all2dec(numb, Base):
    return int(numb, Base)


def Decimal(n1, ba):
    fd = fraction2de(fraction, ba)
    print("Decimal of " + number + " is: ", int(int(n1, ba)) + float(fd))
    return float(int(n1, ba)) + float(fd)


def FinalResultForBinary(operator, x1, y1):
    global z, numz, fracz
    if operator == '+':
        z = str(x1 + y1)
    elif operator == '-':
        z = str(x1 - y1)
    elif operator == '*':
        z = str(x1 * y1)
    elif operator == '/':
        z = str(x1 / y1)

    resultz = z.split(".")
    if (len(resultz) == 2):
        fracz = resultz[1]
        numz = str(resultz[0])
    b = bin(all2dec(numz, 10)).lstrip("0b").rstrip("L")
    fd = fraction2de(fracz, 10)
    fm = de2fraction(float(fd), 2)

    return str(b) + str(fm).lstrip("0")  # it will be printed


def FinalResultForHexadecimal(operator, x1, y1):
    global z, numz, fracz
    if operator == '+':
        z = str(x1 + y1)
    elif operator == '-':
        z = str(x1 - y1)
    elif operator == '*':
        z = str(x1 * y1)
    elif operator == '/':
        z = str(x1 / y1)

    resultz = z.split(".")
    if (len(resultz) == 2):
        fracz = resultz[1]
        numz = str(resultz[0])
    h = hex(all2dec(numz, 10)).lstrip("0x").rstrip("L").upper()
    fd = fraction2de(fracz, 10)
    fm = de2fraction(float(fd), 16)

    return str(h) + "." + str(fm)


def FinalResultForOctal(operator, x1, y1):
    global z, numz, fracz
    if operator == '+':
        z = str(x1 + y1)
    elif operator == '-':
        z = str(x1 - y1)
    elif operator == '*':
        z = str(x1 * y1)
    elif operator == '/':
        z = str(x1 / y1)
    resultz = z.split(".")
    if (len(resultz) == 2):
        fracz = resultz[1]
        numz = str(resultz[0])
    o = oct(all2dec(numz, 10)).lstrip("0o").rstrip("L")
    fd = fraction2de(fracz, 10)
    f = de2fraction(float(fd), 8)

    return str(o) + str(f).lstrip("0")


def FinalResultForDeciaml(operator, x1, y1):
    if operator == '+':
        return x1 + y1
    elif operator == '-':
        return x1 - y1
    elif operator == '*':
        return x1 * y1
    elif operator == '/':
        return x1 / y1


# Driver program
print("Instruction\n\ttype '1' for base conversion only.\n\ttype '2' for arithmatic operation.")
option = int(input("Enter your choice: "))

if option == 1:
    # Instructions
    print("\n\ttype 'b' for Binary\n\ttype 'o' for Octal\n\ttype 'h' for Hexadecimal\n\ttype 'd' for Decimal\n")
    From = input("Covert From: ")
    To = input("Convert To: ")

    # taking number as input starts
    a = (input("Enter Number: "))
    ayhay = a.split(".")
    if (len(ayhay) == 2):
        fraction = ayhay[1]
        number = str((ayhay[0]))
    else:
        fraction = 0
        number = str((ayhay[0]))
    # taking input ends

    # Drivers operations begins
    if From == 'h':
        if To == 'd':
            Decimal(number, 16)
        elif To == 'o':
            o = oct(all2dec(number, 16)).lstrip("0o").rstrip("L")
            fd = fraction2de(fraction, 16)
            f = de2fraction(float(fd), 8)
            print("Octal of " + a + " is: ", float(o) + float(f))
        else:
            b = bin(all2dec(number, 16)).lstrip("0b").rstrip("L")
            fd = fraction2de(fraction, 16)
            fm = de2fraction(float(fd), 2)
            print("Binary of " + a + " is: ", float(b) + float(fm))

    if From == 'b':
        if To == 'd':
            Decimal(number, 2)
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
            Decimal(number, 8)
        elif To == 'h':
            h = hex(all2dec(number, 8)).lstrip("0x").rstrip("L").upper()
            fd = fraction2de(fraction, 8)
            fm = de2fraction(float(fd), 16)
            print("Hexadecimal of " + str(a) + " is: ", str(h) + "." + str(fm))
        else:
            b = bin(all2dec(number, 8)).lstrip("0b").rstrip("L")
            fd = fraction2de(fraction, 8)
            fm = de2fraction(float(fd), 2)
            print("Binary of " + str(a) + " is: ", float(b) + float(fm))

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

    # Driver operatins ends

elif option == 2:
    # Instructions
    print("\n\ttype 'b' for Binary\n\ttype 'o' for Octal\n\ttype 'h' for Hexadecimal\n\ttype 'd' for Decimal\n")
    print("Arithmetic operation on - ")
    choice = input("Enter Base name: ")

    # taking input starts
    num1 = input("Enter Number 1: ")
    problem1 = num1.split(".")
    if len(problem1) == 2:
        fracproblem1 = problem1[1]
        np1 = str(problem1[0])
    else:
        fracproblem1 = 0
        np1 = str((problem1[0]))

    num2 = input("Enter Number 2: ")
    problem2 = num2.split(".")
    if len(problem2) == 2:
        fracproblem2 = problem2[1]
        np2 = str(problem2[0])
    else:
        fracproblem2 = 0
        np2 = str((problem2[0]))

    select_operation = str(input("Enter arithmetic operators(+,-,*,/): "))
    # taking input ends

    # Driver operations starts
    if choice == 'b':
        fd = fraction2de(fracproblem1, 2)
        x = float(int(np1, 2)) + float(fd)

        fd = fraction2de(fracproblem2, 2)
        y = float(int(np2, 2)) + float(fd)

        result = FinalResultForBinary(select_operation, x, y)
        if result == ".0":
            result = "0.0"
            print("Result is: ", result)
        else:
            print("Result is: ", result)
            
    elif choice == 'h':
        fd = fraction2de(fracproblem1, 16)
        x = float(int(np1, 16)) + float(fd)

        fd = fraction2de(fracproblem2, 16)
        y = float(int(np2, 16)) + float(fd)
        result = FinalResultForHexadecimal(select_operation, x, y)
        if result == ".0":
            result = "0.0"
            print("Result is: ", result)
        else:
            print("Result is: ", result)
    elif choice == 'o':
        fd = fraction2de(fracproblem1, 8)
        x = float(int(np1, 8)) + float(fd)

        fd = fraction2de(fracproblem2, 8)
        y = float(int(np2, 8)) + float(fd)

        result = FinalResultForOctal(select_operation, x, y)
        if result == ".0":
            result = "0.0"
            print("Result is: ", result)
        else:
            print("Result is: ", result)

    else:
        result = FinalResultForDeciaml(select_operation, float(num1), float(num2))
        print("Result is: ", result)

    # Driver operations ends
