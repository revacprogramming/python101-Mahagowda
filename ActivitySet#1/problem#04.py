# Conditional Execution

hrs = input("Enter Hours:")
rate=input("Enter rate:")
h = float(hrs)
r=float(rate)
if h > 40 :
        rg=r*h
        ot=(h-40)*(r*0.5)
        print(rg+ot)
else:
        print("Pay")
        pay=h*r
print(pay)