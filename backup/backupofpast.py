from os import system, name

def mass(mass1, mass2):
    Mass = mass1 * mass2
    Mass = int(Mass)

def volume(vol1, vol2):
    Volume = vol1 * vol2
    Volume = int(Volume)

def weight(weight1, weight2):
    weight = weight1 * weight2
    weight = int(weight)

def density(den1, den2):
    Density = den1 / den2
    Density = int(Density)

def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def backtostart():
  answer = input("Do you wish to solve again? (Yes/No)")

  if answer == 'Yes' or answer == 'yes':
    clear()
    return main
  
  if answer == 'No' or answer == 'no':
    print("Thank you for using this calculator!")
    exit()


def main():
    print(
        " \n"
        "Welcome to the Density or Weight Calculator\n\n\n"
        "Type the specific letter to choose what you would like to calculate:\n\n"
        "Type D or d for Density\n"
        "Type W or w for Weight\n"
        "Type V or v for Volume\n"
        "Type M or m for Mass\n"
        "Type F of f to see the formulas\n"
        "Type Q of q to exit the program\n"
        )

    ask = input("What would you like to calculate:")

    if ask == 'M' or ask == 'm':
        M_Value1 = float(input("What is the Density:"))
        M_Value2 = float(input("What is the acceleration of gravity:"))
                
        Mass = mass(M_Value1,M_Value2)

        print("The Mass is "+ '%.2f'%(Mass))
        backtostart()

    if ask == 'V' or ask == 'v':
        V_Value1 = float(input("What is the Mass:"))
        V_Value2 = float(input("What is the acceleration of gravity:"))
                
        Volume = volume(V_Value1, V_Value2)

        print("The Volume is "+ '%.2f'%(Volume))
        backtostart()

    if ask == 'W' or ask == 'w':
        W_Value1 = float(input("What is the Mass:"))
        W_Value2 = float(input("What is the acceleration of gravity:"))
                
        Weight = weight(W_Value1, W_Value2)

        print("The Weight is "+ '%.2f'%(Weight))
        backtostart()
        
    if ask == 'D' or ask == 'd':
        D_Value1 = float(input("What is the Mass:"))
        D_Value2 = float(input("What is the Volume:"))

        Density = density(D_Value1, D_Value2)
        

        print("The Density is "+ '%.2f'%(Density))
        backtostart()

    if ask == 'F' or ask == 'f':
        inputfile=open('formula.txt','r')

        lines=[]

        for line in inputfile:
          lines.append(line)

        inputfile.close()

        print(
        "The calculator has ",len(lines)," formulas"
        )

        while True:
            linenumber=int(input("Enter the specific number to show the formula or 0 to quit: "))
            if linenumber == 0:
                clear()
                return main()

            elif linenumber > len(lines):
                print("Error: specified number must be less than ", len(lines))
            else:
                print(linenumber, " : ", lines[linenumber - 1])
                print("The calculator has ",len(lines)," lines")

    if ask == 'Q' or ask == 'q':
      exit()


main()