'''2) Strings in python'''

str="Welcome to the console!!!"
print(str.endswith("to",4,10)) #checks whether string ends with following character/string.returns true is correct else -1

str1="He's name is Dan. he is an honest man."
print(str1.find("is"))  #find function searches for first occurance and return index where it is present
#print(str1.index("ishh"))

str2="WelcometotheConsole"
print(str2.isalnum())#verify that string contains numeric or character ..or both and returns true

str3="Welcome"
print(str3.isalpha()) #verify that string contains only alphabets and gives true otherwise false
 
str4="hello world"
print(str4.islower())#verify that string contains only only lowercase alphabets and gives true oterwise false

str5="happy birthday bhai"#gives true when string is has printables
print(str5.isprintable())
str6="happy birthday bhai\n"# ex \n is non printable gives false
print(str6.isprintable())

str7="                  "
print(str7.isspace())# using spacebar
str8="  "
print(str8.isspace())#using tab

str9="World Health Organisation"
print(str9.istitle()) #checks whether string has capital letter 
str10="to kill a mocking bird"
print(str10.istitle()) #false here

str11="pytHon is a iNterpreted language"
print(str11.swapcase())  #swaps the lower with upper and vice-versa

str12="his name is dan.dan is an honest man"
print(str12.title()) #Capitalizes each letter of the word within the string