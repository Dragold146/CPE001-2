code = input("Enter The formula to be DECRYPTED:  ")
distance = int(input("Enter The Distance: "))
FormulaCode = input("Enter The Object's Encrypted Weight in ALPHANUMERICAL VALUE: ")
WeightofTheObject = ""
for ch in FormulaCode:
    ordValue = ord(ch)
    cipherValue = ordValue-distance
    WeightofTheObject+= chr(cipherValue)
PlainText = ""
for ch in code:
    ordvalue = ord(ch)
    cipherValue = ordvalue-distance
    PlainText+= chr(cipherValue)
print("The Weight of The Object is " + WeightofTheObject + " Newtons.")
print("The Encrypted Code/Formula is: " + PlainText)