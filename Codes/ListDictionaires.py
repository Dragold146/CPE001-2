def main():
    
    inputfile=open('example.txt','r')

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
            break

        elif linenumber > len(lines):
            print("Error: specified number must be less than ", len(lines))
        else:
            print(linenumber, " : ", lines[linenumber - 1])
            print("The calculator has ",len(lines)," lines")
main()
