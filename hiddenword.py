#programma finding the hidden word !
list=["c","a","t"]
first_letter=input("give first letter ")
if first_letter==list[0]:
    print("you found the first letter")
while first_letter!=list[0]:
    print("you need to try again")
    first_letter=input("give first letter ")
    if first_letter==list[0]:
        print("you found it")
        break
    
second_letter=input("give second letter ")
if second_letter==list[1]:
    print("you found the second letter")
while second_letter!=list[1]:
    print("you need to try again")
    second_letter=input("give second letter ")
    if second_letter==list[1]:
        print("you found it")
        break
    
third_letter=input("give third letter ")
if third_letter==list[2]:
    print("you found the third letter")
while third_letter!=list[2]:
    print("you need to try again")
    third_letter=input("give sthird letter ")
    if third_letter==list[2]:
        print("you found it")
        break
    
print("The animal is " + "".join(list))