# student={
# "NAME":"SANGRAM LEMBE",
# "AGE": 19,
# "PHONE NO":9158416688,
#     "CITY":"SATARA"
#
# }
#
# for key,val in student.items():
#     print(f"{key}:{val}")
# print()
# print()
# for val in student.values():
#     print(val)
# print()
# print()
# for key in student.keys():
#     print(key)

## charactor count dictionary
name = " sangram lembe"
char_count={}

for i in name:
    char_count.update({i: name.count(i)})

print(char_count)
