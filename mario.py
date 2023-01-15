def main():
   # print_column(4)
   # print_row(4)
    print_square(3)
    
def print_column(height):
    print("#\n" * height)
    
def print_row(width):
    print("?" * width)
    
def print_square(size):
     # For each row in square
    for i in range(size):
         
         # For each brick in row
        for j in range(size):
            # print brick
            print("#", end="")
        print("")
        
main()