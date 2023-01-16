with open('D11/input.txt', 'r') as file:
    r = file.read()
    data = r.splitlines()

class Monkey():
    def __init__(self,name) -> None:
        self.name = name
        self.items = []
        self.inspections = 0
        #monkey to pass to if condition true
        self.true : int = 0
        # monkey to pass to if condition false
        self.false : int = 0
        #condition (divisible by:)
        self.test : int = 0
        #operation (new = old * {operand})
        self.operation : str = ''
    def move(self,monkey,amount):
        monkey.items.append(amount)
        self.inspections += 1

monkeys = []
for command in data:
    command = command.strip()
    if command.startswith('Monkey'):
        monkeys.append(Monkey(str(command[-2])))
    elif command.startswith('Starting'):
        for value in command.split(':')[1].split(','):
            monkeys[-1].items.append(int(value))   
    elif command.startswith('Operation'):
        monkeys[-1].operation = '{old} ' + command.split('old ')[1].strip()
    elif command.startswith('Test'):
        monkeys[-1].test = int(command.split()[-1])
    elif command.startswith('If'):
        if 'true' in command:
            monkeys[-1].true = int(command[-1])
        else:
            monkeys[-1].false = int(command[-1])            

def part_1():
    for _ in range(20):
        for monkey in monkeys:
            if len(monkey.items) > 0:
                for item in monkey.items:
                    try:
                        worry = eval(monkey.operation.format(old=item))
                    except NameError:
                        worry = eval(monkey.operation[:8:].format(old=item) + str(item))
                    if int(worry / 3) % monkey.test == 0:
                        monkey.move(monkeys[monkey.true],int(worry / 3))
                    else:
                        monkey.move(monkeys[monkey.false],int(worry / 3)) 
                monkey.items = [] 
    monkeys.sort(key=lambda x: x.inspections,reverse=True)
    return monkeys[0].inspections * monkeys[1].inspections

if __name__ == '__main__':
    print(part_1())
