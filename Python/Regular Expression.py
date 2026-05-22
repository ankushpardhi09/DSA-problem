# Application of Regular Expression

# import re

# def main():
#     text = ("A Function is Python, define by a def Statement. "
#             "python the General Syntax of a Function is def Function_Name(Parameters list)")

#     pattern = re.compile(r"\bfunction\b", re.IGNORECASE)

#     matches = list(pattern.finditer(text))
#     for m in matches:
#         print(m.start(), "...", m.end(), "....", m.group())
#     print("Total number of function is", len(matches))

# if __name__ == "__main__":
#     main()


# import re
# count = 0
# matcher = re.finditer("Hi", "HiHiHiHiHiHi")

# for i in matcher:
#     count += 1
#     print(i.start(), "....", i.end(), "....", i.group())
# print("The number of occerrence", count)

# import re
# s = input("Enter mail id: ")
# m = re.fullmatch("\w[a-zA-Z0-9_.]*@gmail[.]com", s)
# if m != None:
#     print("Valid mail id")
# else:
#     print("Invalid mail id")



# import re
# mo = input("Enter mobile no: ")
# object = re.fullmatch("[0-5]\d{9}", mo)
# if object != None:
#     print("Valid mail id")
# else:
#     print("Invalid mail id")



#Search() function 

# import re
# a = input("Enter a string to perform matchin opration: ")
# match = re.search(a,"python sss dyanmic larnn")
# print(match)
# if match != None:
#     print(match.start(), "....", match.end(), "....", match.group())
# else:
#     print("Not found")


#charecter class

# import re
# match = re.search("[A-Z]","NBDOWEBCIPkpdnmv kndkimkMKPDMCepdwf &*&%$")
# print(match)


# Sub() function
# the subtitude function is used to replace the pattern with the given string and return the new string

# import re
# replece = re.sub('[a-zA-Z]', '*', "2435 ACCV njfr deff")
# print(replece)

# subn() function
# the Subtitude Funtion with count of replacement and return a tuple with new string and count of replacement
# import re
# replece = re.subn('[a-zA-Z]', '*', "2435 ACCV njfr deff")
# print(replece)
# print("Total number of replacement is", replece[0])
# print("Total number of replacement is", replece[1])


import re 
f1 = open("input.txt", "r")
f2 = open("newfile.txt", "w")
for line in f1:
    replece = re.sub("[a-zA-Z]", "*", line)
    f2.write(replece)
f1.close()
f2.close()
