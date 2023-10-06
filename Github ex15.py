n1=float(input("type your note1: "))
while n1<0 or n1>20:
    n1=float(input(" please type your  note1: "))
n2=float(input("type your  note2: "))
while n2<0 or n2>20:
    n2=float(input(" please type your note2: "))
n3=float(input("type your note3: "))
while n3<0 or n3>20:
    n3=float(input(" please type your note3: "))
N=(n1+n2+n3)/3
if N>=16:
    print("your note:",N,"very bien")
elif N>=14 and N<16:
    print("your note:",N,"good")
elif N>=12 and N<14:
    print("your note:",N,"quite-good")
elif N>10 and N<12:
    print("your note:",N,"passable")
else :
    print("insifficient")
