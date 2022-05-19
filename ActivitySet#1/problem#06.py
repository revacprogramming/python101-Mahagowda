# Loops & Iterators

largest=0
smallest=0
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
       num=int(num)
    except:
       print("Invalid input")
       continue
    if largest is 0:
      largest=num
    if smallest is 0:
      smallest=num
    if num>largest:
      largest=num
    if num<smallest:
      smallest=num
print("Maximum is",largest)
print("Minimum is",smallest)