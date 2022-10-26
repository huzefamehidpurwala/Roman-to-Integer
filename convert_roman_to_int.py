# import os

# Defining a dictionary having all the possible values of roman
roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}

# Function to convert the roman string to an integer
def roman_to_int(s):
   
   i = 0
   num = 0

   while i < len(s):
      if i+1<len(s) and s[i:i+2] in roman:
         num += roman[s[i:i+2]]
         i+=2
      else:
         num += roman[s[i]]
         i+=1
   return num

# os.system("cls") # to clear the console screen
s = input("Enter the roman number: ").upper()
print()

# to check whether the input is value is a roman number or not to ignore keyvalue error
for i in range(0, len(s)):
    if s[i] not in roman:
        print("Please enter a valid Roman Number!!!")
        break
else:
    print("=================================")
    print("The Integral Value is:", end=" ")
    print(roman_to_int(s))
    print("=================================")
