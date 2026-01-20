status =True
while status:

    print("------Menu-----")
    print("1. pizza           price = 180rs/pcs")
    print("2. Burger          price = 100rs/pcs")
    print("3. Dosa            price = 120rs/pcs")
    print("4. Idli            price = 50rs/pcs")


    choice =int(input("Enter your choice:"))


    match choice:
        case 1:
            print("You have selected pizza")
            quantity = int(input("Enter quantity:"))
            print(f"Amount: {quantity*180}")
            amount = quantity*180
            print(f"Total Amount is :",amount)

            order=input("Do you want place more order: y or n:")
            if order=='n' or choice=='no':
                status=False
                print("Total amount:" ,quantity*amount)
                print("Thanks for Visit.....")
                
            


        case 2:
            print("You have selected Burger")
           
            quantity = int(input("Enter quantity:"))
            print(f"Amount: {quantity*100}")
            amount = quantity*100
            print(f"Total Amount is :",amount)

            order=input("Do you want place more order: y or n:")
            if order=='n' or choice=='no':
                status=False

            
        
        case 3:
            print("You have selected Dosa")
            quantity = int(input("Enter quantity:"))
            print(f"Amount: {quantity*120}")
            amount = quantity*120
            print(f"Total Amount is :",amount)

            order=input("Do you want place more order: y or n:")
            if order=='n' or choice=='no':
                status=False

        case 4:
            print("You have selected Idli")

            quantity = int(input("Enter quantity:"))
            print(f"Amount: {quantity*50}")
            amount = quantity*50
            print(f"Total Amount is :",amount)

            order=input("Do you want place more order: y or n:")
            if order=='n' or choice=='no':
                status=False


        

        