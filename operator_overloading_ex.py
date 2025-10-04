'''Example of Operator Overloading from Pearson textbook 
"Intro to Python for Computer Science and Data Science 1e" 
by Paul Deitel, Harvey Deitel'''


#####################################
# Import Modules
#####################################

from complexnumber import Complex


#####################################
# Functionality
#####################################

#display complex number in a readable string
x = Complex(real = 2, imaginary = 4)
print(f"x = {x}")

#display complex number with negative imaginary in a readable string
y = Complex(real = 5, imaginary= -1)
print(f"y = {y}")

# use + operator to add Complex objects together
print(f" x + y = {x + y}")

# make sure neither elements were altered by the + operator
print(f"x still = {x}")
print(f"y still = {y}")
print("(unchanged)\n")

# use += operator to modify x 
x += y 
print("x += y")
#print(f"x += y : {x += y}")
print(f"now, x = {x}") 


#####################################
# Main Execution
#####################################

def main():
    return None




if __name__ == "__main__":
    main()
