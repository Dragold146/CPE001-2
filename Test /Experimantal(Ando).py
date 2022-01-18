import newlib as nw
 
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

      nw.mass(M_Value1, M_Value2)
    

    if ask == 'V' or ask == 'v':
      V_Value1 = float(input("What is the Mass:"))
      V_Value2 = float(input("What is the acceleration of gravity:"))
              
      nw.volume(V_Value1, V_Value2)
    

    if ask == 'W' or ask == 'w':
      W_Value1 = float(input("What is the Mass:"))
      W_Value2 = float(input("What is the acceleration of gravity:"))
              
      nw.weight(W_Value1, W_Value2)

    
    if ask == 'D' or ask == 'd':
      D_Value1 = float(input("What is the Mass:"))
      D_Value2 = float(input("What is the Volume:"))

      nw.density(D_Value1, D_Value2)

outfile = input("Do you want to save the results:")

if outfile == 'Yes' or outfile == 'yes':
  out_filename = input("What is the filename:")

  file = open(out_filename, 'w')
  file.write()
  print("Data has been save to "+ out_filename)
  file.close()

if outfile == 'No' or outfile == 'no':
  print("Okay data will not be saved!")


else:
  exit()