def read_int(prompt, min, max):
    ok = False
    while not ok:
        try:
            value = int(input(prompt))
            if value < min or value> max:
                raise ValueError
            else:
                ok=True
        except ValueError:
            print("Enter the correct value: ")
        if ok:
            return value
        
v=read_int("Enter value from -10 to 10 ", -10, 10)
print("The number is",v)
