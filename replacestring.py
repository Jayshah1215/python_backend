s1="my fav lang is python"
print(s1.replace("python","java"))
print(s1)

#----------------------------------------
print(s1.find("fav"))

#-----------------------------------------

s2="python,java,ds,da"
s2_split = s2.split(",")
print(s2)
print(s2_split)

#----------------------------------------

s3="my python programming language"
#separate word from given string and count total words in string

s3_words_list= s3.split(" ")
print(s3)
print(s3_words_list)
print(f"toatal words{len(s3_words_list)}")

#--------------------------------------
#count repeated or specific word in string

s1 = "my python progr is python is great lang"
print(s1)
print(s1.count("python"))