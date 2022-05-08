

a=int(input("Enter Index: "))
b=int(input("Enter Number: "))
my_list=[1,2,3,4,5,6]
print("Old List",my_list)
final_list=[]
for i in my_list[:a:]:
    final_list.append(i)

final_list.append(b)

for i in my_list[a:5:]:
    final_list.append(i)
print("New List",final_list)


