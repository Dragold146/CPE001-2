answer = input("Please choose if File or Text:")


if answer == 'File' or answer == 'file':
    infile = input("Filename:")
    outfile = input("File to save:")

    file_open = open(infile, 'r')

    


if answer == 'Text' or answer == 'text':
    ask = input("Is it W, D, V or M:")

    if ask == 'M' or ask == 'm':
      M_Value1 = float(input("What is the Density:"))
      M_Value2 = float(input("What is the acceleration of gravity:"))
              
      Mass = M_Value1 * M_Value2
      Mass = int(Mass)
      print("The Mass is "+ '%.2f'%(Mass))
    

    if ask == 'V' or ask == 'v':
      V_Value1 = float(input("What is the Mass:"))
      V_Value2 = float(input("What is the acceleration of gravity:"))
              
      Volume = V_Value1 * V_Value2
      Volume = int(Volume)
      print("The Volume is "+ '%.2f'%(Volume))
    

    if ask == 'W' or ask == 'w':
      W_Value1 = float(input("What is the Mass:"))
      W_Value2 = float(input("What is the acceleration of gravity:"))
              
      weight = W_Value1 * W_Value2
      weight = int(weight)
      print("The Weight is "+ '%.2f'%(weight))
    
    if ask == 'D' or ask == 'd':
      D_Value1 = float(input("What is the Mass:"))
      D_Value2 = float(input("What is the Volume:"))

      Density = D_Value1 / D_Value2
      Density = int(Density)
      print("The Density is "+ '%.2f'%(Density))

outfile = input("Do you want to save the results:")

if outfile == 'Yes' or outfile == 'yes':
  out_filename = input("What is the filename:")

  output = open(out_filename, 'w')
  output.write()
  print("Data has been save to "+ outfile)
  output.close()

if outfile == 'No' or outfile == 'no':
  print("Okay data will not be saved!")


else:
  exit()