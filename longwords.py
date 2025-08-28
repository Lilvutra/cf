w = input("Input: ")
def replace(w):
    if len(w) > 10:   
        middle_length = len(w) - 2
        new_string = w[0] + str(middle_length) + w[-1]
        print(new_string)
        
        #z = w[1:-1]
        #middle_length = len(z)
        #new_string = w[0] + str(middle_length) + w[-1]
        #print(new_string)
    else:
        print(w)

replace(w)