def powers(power):
    def numbers(number):
        result=number**power
        return result
    return numbers
cube = powers(3)
square=powers(2)
print(cube(5),square(5))
