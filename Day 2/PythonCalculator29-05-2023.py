List=[]
def main():
    print("**************************************");
    Input1=float(input("Enter The First Value: "));
    print("1: For Addition");
    print("2: For Multiplication");
    print("3: For Subtration");
    print("4: For Division");
    print("**************************************");
    Operation=float(input("Choose the Given Operation from the Menu: "));
    Input2=float(input("Enter The Second Value: "));
    
    def ConditionChecker():
        if Operation==1:
            Addition=Input1+Input2
            return Addition
        elif Operation==2:
            Multiplication=Input1*Input2
            return Multiplication
        elif Operation==3:
            Subtraction= Input1-Input2
            return Subtraction
        elif Operation==4:
            Division=Input1/Input2
            return Division
        else:
            return 0
    Solution=ConditionChecker()
    if Solution==0:
        print("Invalid Operation Performed or Input is of Different DataType")
    else:
        print("Your Given Result is: ",Solution)
        List.append(Solution)
main()
    
AgainPlay=int(input("Press 1 to Calculate again and 0 to Exit: "))
if AgainPlay==0:
    print("Thanks for Using This Calculator. Hope so it was a good Experience :)")
elif AgainPlay ==1:
    Counter=int(input("How many Times Do you Want to Calculate Again? "))
    while Counter !=0:
        main()
        print("The given List has following outputs: ", List)
        Counter=Counter-1