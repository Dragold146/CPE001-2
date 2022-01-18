from os import system, name
from datetime import datetime




def backtostart():
  answer = input("Do you wish to solve again? (Yes/No)")

  if answer == 'Yes' or answer == 'yes':
    clear()
    return main()
  
  if answer == 'No' or answer == 'no':
    print("Thank you for using this calculator!")
    exit()

def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def start():
  print(
    "Welcome to the Density or Weight Calculator\n\n\n"
    "If you wish to start type: S or s\n"
    "If you wish to see the formulas type: F or f\n"
    "If you want to exit/quit Type: Q or q" 
  )
  start1 = input("What would you like to do?:")
  
  if start1 == 'S' or 's':
    clear()
    return main()

  if start1 == 'Q' or 'q':
    clear()
    print(
      "Thank you for using the calculator!\n"
      "Goodbye"
    )
    exit()

  if start1 == 'F' or 'f':
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


def main():
  
    print(
        
        "Type the specific letter to choose what you would like to calculate.\n\n"
        "If you want to calculate Density Type: D or d\n"
        "If you want to calculate Weight Type: W or w\n"
        "If you want to calculate Volume Type: V or v\n"
        "If you want to calculate Mass Type: M or m\n"
        " \n"
        " \n"
        " \n"
        "If you want to exit/quit Type: Q or q \n"
        )

    

    now = datetime.now()

    time = now.time().strftime("%H:%M:%S")

    date = now.date().strftime("%d/%m/%Y")

    ask = input("What would you like to calculate:")

    if ask == 'M' or 'm':
        M_Value1 = float(input("What is the Density:"))
        M_Value2 = float(input("What is the acceleration of gravity:"))
                
        Mass = M_Value1 * M_Value2
        Mass = int(Mass)
        Mass_history = {'Mass': Mass, 'Date': date , 'Time': time}
        dataM = str(Mass_history)

        with open('MassHistory.txt', 'w') as historyM:
            historyM.write(dataM)
            historyM.close()
            

        print(Mass_history)

        print("The Mass is "+ '%.2f'%(Mass))
        backtostart()

    if ask == 'V' or 'v':
        V_Value1 = float(input("What is the Mass:"))
        V_Value2 = float(input("What is the acceleration of gravity:"))
                
        Volume = V_Value1 * V_Value2
        Volume = int(Volume)
        Volume_history = {'Volume': Volume, 'Date': date , 'Time': time}
        dataV = str(Volume_history)

        with open('VolumeHistory.txt', 'w') as historyV:
            historyV.write(dataV)
            historyV.close()

        print("The Volume is "+ '%.2f'%(Volume))
        backtostart()

    if ask == 'W' or 'w':
        W_Value1 = float(input("What is the Mass:"))
        W_Value2 = float(input("What is the acceleration of gravity:"))
                
        weight = W_Value1 * W_Value2
        Weight = int(weight)
        Weight_history = {'Weight': Weight, 'Date': date , 'Time': time}
        dataW = str(Weight_history)

        with open('WeightHistory.txt', 'w') as historyW:
            historyW.write(dataW)
            historyW.close()

        print("The Weight is "+ '%.2f'%(Weight))
        backtostart()

    if ask == 'D' or 'd':
        D_Value1 = float(input("What is the Mass:"))
        D_Value2 = float(input("What is the Volume:"))

        Density = D_Value1 / D_Value2
        Density = int(Density)
        Density_history = {'Density': Density, 'Date': date , 'Time': time}
        dataD = str(Density_history)

        with open('DensityHistory.txt', 'w') as historyD:
            historyD.write(dataD)
            historyD.close()


        print("The Density is "+ '%.2f'%(Density))
        backtostart()

    if ask == 'Q' or 'q':
      print("Thank you for using this calculator!")
      exit()
    
    elif ask == "":
      clear()
      print("Please Try again!")
      return main()

start()