def enter(k):
    if k==1:
        inp=int(input("Enter 1 for Meal entry 2 for Exercise count: "))
        if inp==1:
            with open("meal.txt","a") as meal:
                print(name.capitalize())
                a=input("Enter food:\n")
                meal.write(a)
        elif inp==2:
            with open("exer.txt","a") as count:
                # print(name.capitalize())
                b=input("Enter exercise:\n")
                count.write(b)
        else:
            print("Enter 1 or 2 only!")
    elif k==2:
        m_e=int(input("Enter 1 to retrieve meal log 2 for exercise log: "))
        if m_e==1:
            with open("meal.txt") as meal:
                # print(name.capitalize())
                for i in meal:
                    print(i,end="")
        elif m_e==2:
            with open("exer.txt") as count:
                print(name.capitalize())
                for i in count:
                    print(i,end="")
        else:
            print("Enter 1 or 2 only!")

print("Hello, Welcome to the Health Management System")
name=input("Your Good Name: ")
k=int(input("Press 1 for Enter data 2 for Retrieve data: "))
enter(k)


