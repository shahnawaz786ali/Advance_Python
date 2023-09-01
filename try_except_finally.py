try:
    a=int(input("Enter ur number:"))
    print(a)
    
except Exception as e:
    print(e)
    exit()
    
finally:
    print("We are successfull.")
    
