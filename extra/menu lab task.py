student_data ={
    "ami@gmail.com":["Ami",20,2345678,120],
    "riya@gmail.com":["Riya",21,455756,150],
    "Manish@yahoo.com":["manish",22,454354,200],
    "amitlah@gmail.com":['Amitlah',22,345345,110]
   }
while True:
    print("------Menu-----")
    print("1.Add Data of Student")
    print("2.Search Student")
    print("3.Delete student")
    print("4.View all student")
    print("5.Exit")

    choice=int(input("Enter your choice:"))
    match choice:
         case 1: 
            print("Add data of student")
            Email=input("enter Email address :")
            name=input("Please enter name :")
            age=input("Please enter age :")
            c_no=input("Please enter C_No :")
            marks=input("Please enter Marks : ")
            student_data[Email]=[name,age,c_no,marks]
            print("Student Added Successfully")
           
            
         case 2:
            print("Search Student")
            search=input("Please enter email ")
            for i,j in student_data.items():
                if search==i:
                    for i1 in j:
                        print(i1)
                    break
            else:
                print(f"{search} not found in student data")

         case 3:
            print("Delete a student")
            Email=input("Please enter a email")
            if Email in student_data:
                del student_data[Email]
            print("Delete successfully")

         case 4:
            print("View all student")
            for i,j in student_data.items():
                print(i)
                for i1 in j:
                    print("\t",i1)    

         case 5:
            print("I hope u get information")
            break
         case _:
            print("Invalid choice")