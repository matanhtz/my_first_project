from training.new_file import index

# sen = "My name is Matan"
# ind = sen[13] or sen.index("t")
# for i in range(0,sen.index(ind)):
#     print(sen[:i])

# emails = ["abc@aa.com","ssss.com","sss@rerrr.com"]
# for email in emails:
#     if "@" in email:
#         print("valid email")
#
#     else:
#         print("invalid email")

newnums = []
notdiv = []
tra = []

for i in range(1,31):
    if i%7==0:
        newnums.append(i)

    else:
        notdiv.append(i)

for num in notdiv:
    num = str(num)
    if "7" in num:
        tra.append(num)

for n in tra:
    n = int(n)

print(tra)
