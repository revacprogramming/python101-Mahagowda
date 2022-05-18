# Functions


def computepay(hrs,rate) :
    if hour > 40 :
        rg=rate*hrs
        ot=(hrs-40)*(rate*0.5)
        pay=rg+ot
    else:
        pay=hrs*rate
    return pay

hrs = input("Enter Hours:")
rate=input("Enter rate:")
hrs = float(hrs)
rate=float(rate)

xp = computepay(hrs,rate)

print("pay:",xp)