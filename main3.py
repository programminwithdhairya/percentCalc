def percentage():
    try:
        
        first = int(input("Enter the first number"))
        second = int(input("Enter the first number"))
        Percent = (f'the {second}% of {first} is \n{second/100 * first}')
        print(Percent)
    except Exception as e:
        print("Enter a correct value")
    
percentage()