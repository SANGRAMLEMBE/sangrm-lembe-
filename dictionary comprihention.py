# l=[1,2,3,4,5,6,7]
# sq_dict={i:i*i for i in l}
# print(sq_dict)

# str1="welcoooooome"
# char_count={i:str1.count(i) for i in str1}
# print(char_count)

# l=[1,2,3,4,5,6,7,8]
# even_odd={i:("even" if i%2==0 else "odd")for i in l}
# print(even_odd)

# names=["madam","sos","john","mom","dad","dads"]
#
# palin={i:("palin" if i==i[::-1] else ("not palindrom")) for i in names}
# print(palin)

# names=["madam","sos","john","black","mom"]
# k={i:len(i) for i in names}
# print(k)

# stu_marks={"sangram":98,"jeevan":91,"rohit":42,"rohan":16,"aditya":54}
# # marks={i:(if j>=50) for i,j in stu_marks}
# marks={i:k for i,k in stu_marks.items() if k>= 50}
# print(marks)

# stud_age={"sam":18,"soham":45,"akshay":85,"om":10}
# age={i:("young" if k<=50 else"old") for i,k in stud_age.items()}
# print(age)

n=int(input("enter the number "))
mul={i:i*n for i in range(1,11)}
print(mul)









