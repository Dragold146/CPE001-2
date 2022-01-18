PlainText = input("Enter The formula to be ENCRYPTED:  ")
distance = int(input("Enter The Distance: "))
WeightofObject = input("Enter The Object's Weight in ALPHANUMERICAL VALUE: ")
FormulaCode = ""
for ch in WeightofObject:
    ordValue = ord(ch)
    cipherValue = ordValue+distance
    FormulaCode+= chr(cipherValue)
code = ""
for ch in PlainText:
    ordvalue = ord(ch)
    cipherValue = ordvalue+distance
    code+= chr(cipherValue)
print("The Weight of The Object is " + FormulaCode + " Newtons.")
print("The Encrypted Code/Formula is: " + code)