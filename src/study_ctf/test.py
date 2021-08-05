import string

str1 = "qwerty"
str2 = "qwerty "
str3 = " qwerty"
str4 = "!qwerty"
str5 = "-qwerty"

str1 = str1.strip()
str2 = str2.strip()
str3 = str3.strip()
str4 = str4.strip().lstrip().rstrip()
str5 = str5.strip("-")

print(str1[1])
print(str2)
print(str3)
print(str4)
print(str5)