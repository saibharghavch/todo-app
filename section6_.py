# name = input("Add a new member: ")
# lines = open(f"files/members.txt","r")
# names = lines.readlines()
# lines.close()
# file = open(f"files/members.txt","w")
# print(names)
# names.append(name)
# for i in names:
#     file.write(i)
# file.close()
filenames = ['doc.txt', 'report.txt', 'presentation.txt']
for i in filenames:
    file = open(f"files/{i}","r")
    content = "Hello " + file.read()
    print(content)
    file.close()
    file = open(f"files/{i}","w")
    file.write(content)
    file.close()