import sys


def helpDashboard():
    s = "------------------------help dashboard---------------------"
    s += "\ncommand line structure: [program name] [command] [arg1.....argN]"
    s += '\ncommands:'
    s += '\nMax: calculates the maxumin value of arguments'
    s += "\nMin: calculates the minimum value of arguments"
    s += "\nAvg: calculates the average value of arguments"
    s += "\nHelp: shows the help dashboard"
    s += "\nHINTS:"
    s += "\n1. you can only choose from commands below"
    s += "\n2. you can only enter numbers"
    s += "\n3. you should enter more than a number to the binary operations"
    return s


def extract(args):
    command = args[1]
    values = []
    for i in range(2,len(args)):
        try: arg = float(args[i])
        except: pass
        else: values.append(arg)
    return (command,values)



def selectCommand(command):
    global values
    global commands
    if command not in commands:
        raise Exception ("thre's no such command. print help for more info...")
    if command == 'min': findMin(values)
    elif command == 'max': findMax(values)
    elif command == 'avg' : findAvg(values)
    elif command == 'help' : helpDashboard()



def findMin(values):
    min = values[0]
    for i in range (1,len(values)):
        if values[i]<min: min = values[i]
    print (f"mnimum value is {min}")


def findMax(values):
    max = values[0]
    for i in range (1,len(values)):
        if values[i]>max: max = values[i]
    print(f"maximum value is {max}")



def findAvg(values):
    avg = 0
    for i in values:
        avg += i/len(values)
    print(f"average value is {avg}")



# main
commands = ['min','max','avg','help']
print(sys.argv)
if len(sys.argv) == 1:
    raise Exception ("you didn't enter any commands. print help for more info...")
elif len(sys.argv) == 2 and sys.argv[1] != 'help':
    raise Exception ("you didn't enter any arguments. print help for more info...")
elif sys.argv[1] == 'help': print(helpDashboard())
elif len(sys.argv) == 3:
    raise Exception ("you entered only one argument. this is a binary operation. print help for more info...")
else:
    command,values = extract(sys.argv)
    selectCommand(command)
    print('see you next time.')