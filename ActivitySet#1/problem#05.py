# Functions


def computepay(h, r):
    
    if h<=40:
        print(h*r)
    elif h>40:    
        pay=((40*r)+(h-40)*1.5*r)
        return pay
        
hrs = input("Enter Hours:")
rate = input('Enter Rate:')
h=float(hrs)
r=float(rate)
Pay=computepay(h,r)
print("Pay",Pay)