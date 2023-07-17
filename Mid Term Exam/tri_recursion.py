userinput = int(input("Enter a number: "));

def tri_recursion(k):
    if k>0 :
        result= k+tri_recursion(k-1)
        print("Value of recursion at k = ", k, " is: ", result)
    else:
        result = 0
        print("Value of recursion at k = ", k, " is: ", result)
    return result

tri_recursion(userinput)