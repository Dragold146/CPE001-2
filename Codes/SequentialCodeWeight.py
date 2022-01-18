Mass = float(input("Enter the Mass of the Object: "))
Gravity = float(input("Enter the Acceleration of Gravity upon an Object in m/s^2: "))

WeightofObject = Mass*Gravity
print("The Weight of The Object is","%.4f" %WeightofObject + " Newtons.")

if Gravity == 9.8:
    print("The Object's Weight was measured on Earth.")
else:
    print("The Object's Weight was not measured on Earth.")
