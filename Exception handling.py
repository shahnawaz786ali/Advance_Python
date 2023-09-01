while True:
    try:
        a=int(input("Enter your number."))
        
        if a > 10:
            print("number is greater than 10.")        


    except Exception as e:
        print(f"Your input resulted in an error {e}")