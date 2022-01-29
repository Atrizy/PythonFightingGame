import player as p
import computer as c

print("Welcome to my fighting game!")

player = p.Player
comp = c.Computer

while(True):
    print(f"Player HP: {player.current_hp} -- Computer Hp: {comp.current_hp}")
    selection = input("Please Select 1 for high attack or 2 for low attack")

    dmg = player.attack(selection)
    comp.get_attacked(dmg)
    print(f"Player hits the computer for {dmg} points!")
    if(comp.currenr_hp <=0):
        print("You won!")
        exit()

    dmg = comp.attack()
    player.get_attacked(dmg)
    print(f"Computer hits player for {dmg} points!")
    if(player.current_hp <= 0):
        print("You lost! :(")
        exit()