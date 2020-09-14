class CoffeeMachine:
    in_machine = {'water': 400, 'milk': 540, 'coffee': 120, 'cups': 9, 'money':  550}

    def start(self):
        while True:
            self.action(input('Write action (buy, fill, take, remaining, exit):'))

    def action(self, action):
        if action == 'buy':
            self.buy()
        elif action == 'fill':
            self.fill()
        elif action == 'take':
            self.take()
        elif action == 'remaining':
            self.status()
        elif action == 'exit':
            exit()

    def buy(self):
        espresso = {'water': -250, 'coffee': -16, 'cups': -1, 'money': 4}
        latte = {'water': -350, 'milk': -75, 'coffee': -20, 'cups': -1, 'money': 7}
        cappuccino = {'water': -200, 'milk': -100, 'coffee': -12, 'cups': -1, 'money': 6}
        print()
        order = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
        if order == '1':
            self.make_coffee(espresso)
        elif order == '2':
            self.make_coffee(latte)
        elif order == '3':
            self.make_coffee(cappuccino)
        elif order == 'back':
            print()

    def fill(self):
        print()
        self.in_machine['water'] += int(input('Write how many ml of water do you want to add:'))
        self.in_machine['milk'] += int(input('Write how many ml of milk do you want to add:'))
        self.in_machine['coffee'] += int(input('Write how many grams of coffee beans do you want to add:'))
        self.in_machine['cups'] += int(input('Write how many disposable cups of coffee do you want to'))
        print()

    def take(self):
        print(f"I gave you ${self.in_machine['money']}")
        print()
        self.in_machine['money'] = 0

    def make_coffee(self, recipe):
        count = 0
        for key in recipe:
            if self.in_machine[key] + recipe[key] < 0:
                print(f'Sorry, not enough {key}!')
                print()
                count += 1
                break
            else:
                self.in_machine[key] += recipe[key]
        if count == 0:
            print('I have enough resources, making you a coffee!')
            print()

    def status(self):
        print(f"""
The coffee machine has:
{self.in_machine['water']} of water
{self.in_machine['milk']} of milk
{self.in_machine['coffee']} of coffee beans
{self.in_machine['cups']} of disposable cups
{self.in_machine['money']} of money
""")


coffee_machine = CoffeeMachine()
CoffeeMachine.start(coffee_machine)
