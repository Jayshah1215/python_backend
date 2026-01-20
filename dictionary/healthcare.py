#lab task: booking appoitment

name=input("Enter name:")
m_no=int(input("Enter Mobile number:"))
age=int(input("Enter age:"))
dr_dict={"Dr.Harmi" : {"10am":0 , "11am":0},
         "Dr.Jay": {"8am":0 , "11am":0 , "2pm":0}}

max_slot =3
for i in range(5):

    print(dr_dict.keys(),end=" ")
    pre_dr=input("ENter preffered Doctor from:")

    print(dr_dict[pre_dr],end=" ")
    sel_slot=input("Enter slot:")
 
    print(f"current slot {dr_dict[pre_dr]}")    
    print(f"{name} appoitment is booked with {pre_dr} at {sel_slot}")

    dr_dict[pre_dr][sel_slot]+=1    
    print(f"After booking slot {dr_dict[pre_dr]}")

    if dr_dict[pre_dr][sel_slot] >= max_slot:
        print(f"Slot {sel_slot} is FULL ")