# Roman to Integer
Convert the Roman Number to the Integral Value in Seconds.

## How to run the script
`python convert_roman_to_int.py`

## Code
```
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

s = input("Enter the roman number: ").upper()
print()

for i in range(0, len(s)):
    if s[i] not in roman:
        print("Please enter a valid Roman Number!!!")
        break
else:
    print("=================================")
    print("The Integral Value is:", end=" ")
    print(roman_to_int(s))
    print("=================================")
```

## Screenshot
<div align="center"><img src="./Screenshot 2022-10-26 120526.png"></div>

## Author Name
[`Huzefa Mehidpurwala (huzefamehidpurwala)`](https://github.com/huzefamehidpurwala)