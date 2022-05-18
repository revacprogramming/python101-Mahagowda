# Loops & Iterators

largest = None
smallest = None

while True:
    num = input("Enter a number? ")

    if num == "done":
        break
    try:
        nu = float(num)
    except:
        print ("invalied input")
        continue  

    

    print(num)

print("Maximum", largest)
