

class Complex:
    def __init__(self, real, imaginary):
        self.real = float(real)
        self.imaginary = float(imaginary)

    def __add__(self, second_val):
        return Complex((self.real + second_val.real), (self.imaginary + second_val.imaginary))
        
    def __iadd__(self, second_val):
        #overloads the += operator
        self.real = (self.real + second_val.real)
        self.imaginary = (self.imaginary + second_val.imaginary)
        return self
    
    def __repr__(self):
        #returns a string representation of each object
        if self.imaginary < 0:
            return(f"({int(self.real)} - {abs(int(self.imaginary))}i)")
        else:
            return (f"({int(self.real)} + {int(self.imaginary)}i)")