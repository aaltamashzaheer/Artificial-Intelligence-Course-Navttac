def quadratic_formula(a,b,c):

    disc = b**2 - 4*a*c

    if disc > 0:
        root1 = (-b + disc**(1 / 2))  / (2 * a)
        root2 = (-b - disc**(1 / 2)) / (2 * a)
        return root1,root2

    elif disc==0:
        root =( - b/ ( 2* a ) )
        return root,root

    else :
        return 0

a=float(input("enter Float value of a:"))
b=float(input("enter Float value of b:"))
c=float(input("enter Float value of c:"))

solution = quadratic_formula(a,b,c)

if solution ==0 :
    print("no solution exit")
else :
    print("Roots of the values are:",solution)