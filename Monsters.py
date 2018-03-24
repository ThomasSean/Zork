'''
The Monsters file is used to play the Zork game that was assigned in class. Currently not
working. Compiles, does not have correct output.
@author Sean Thomas
@version Zork Game
@date 3/23/2018
Zork Game
'''

import random


"""
The home class keeps all the monsters and the number of monsters in each home.
"""
class Home(object):
    '''
    Constructor for home
    
    @param self
    @param monster_num number of monsters
    @param monsters array of monsters
    '''
    def __init__(self, monster_num, monsters):
        self.monster_num = monster_num
        #if(len(self.monsters) <= self.monster_num):
        self.monsters = monsters
        
    '''
    Used as a selector for which monsters will go into the monsters array
    
    @param self
    ''' 
    def type_of_monster(self):
        number_monster = self.monster_num
        Person   = Person_1
        Zombie   = Zombie_1
        Vampire  = Vampire_1
        Ghoul    = Ghoul_1
        Werewolf = Werewolf_1
        while number_monster != 0 or len(self.monsters) <= number_monster:
            x = random.randint(1,5)
            if x == 1:
                self.monsters.append(Person_1)
                number_monster = number_monster - 1
            elif x == 2:
                self.monsters.append(Zombie_1)
                number_monster = number_monster - 1
            elif x == 3:
                self.monsters.append(Vampire_1)
                number_monster = number_monster - 1
            elif x == 4:
                self.monsters.append(Ghoul_1)
                number_monster = number_monster - 1
            else:
                self.monsters.append(Werewolf_1)
                number_monster = number_monster - 1

        return self.monsters
    
    #Home().type_of_monster()   
        
"""
Neighborhood class is used to create a neighborhood with a set number of houses
housed within a block. 
"""
class Neighborhood(object):
    '''
    Constructor for neighborhood class
    
    @param self
    @param houses_num number of houses
    @param blocks array for all houses
    '''
    def __init__(self, houses_num, blocks):
        self.houses_num = houses_num
        self.blocks = blocks

    '''
    A method used to select and create number of homes for the neighborhood.
    @param self
    '''
    def create_neighborhood(self):
        num = self.houses_num
        new_home = Home(random.randint(0, 10), [])
        new_home_monsters = new_home.type_of_monster()
        while num != 0:
            self.blocks.append(new_home_monsters)
            new_home = Home(random.randint(0, 10), [])
            new_home_monsters = new_home.type_of_monster()
            num = num - 1
        return self.blocks
        

"""
NPC class used to house all data for each monster npc within the game
"""

class NPC(object):
    '''
    Constructor for NPC
    
    @param self
    @param name
    @param attack
    @param health
    '''
    def __init__(self, name, attack, health):
        self.name = name 
        self.attack = attack
        self.health = health
class Person(NPC):
    '''
    Contructor for Person, supers too NPC
    @param self
    @param name
    @param attack
    @param health
    '''
    def __init__(self, name, attack, health):
        super(Person, self).__init__(name, attack, health)
class Zombie(NPC):
    '''
    Contructor for Zombie, supers too NPC
    @param self
    @param name
    @param attack
    @param health
    '''
    def __init__(self, name, attack, health):
        super(Zombie, self).__init__(name, attack, health)
class Vampire(NPC):
    '''
    Contructor for Vampire, supers too NPC
    @param self
    @param name
    @param attack
    @param health
    '''
    def __init__(self, name, attack, health):
        super(Vampire, self).__init__(name, attack, health)
class Ghoul(NPC):
    '''
    Contructor for Ghoul, supers too NPC
    @param self
    @param name
    @param attack
    @param health
    '''
    def __init__(self, name, attack, health):
        super(Ghoul, self).__init__(name, attack, health)
class Werewolf(NPC):
    '''
    Contructor for Werewolf, supers too NPC
    @param self
    @param name
    @param attack
    @param health
    '''
    def __init__(self, name, attack, health):
        super(Werewolf, self).__init__(name, attack, health)

"""
Weapons class is used to create an inventory with a set number of weapons.
These weapons are used to damage monsters.
"""

class Weapons(object):
    '''
    Contructor for Weapons
    @param self
    @param name name of weapon
    @param attack attack ratio damage
    @param uses number of uses for weapon
    '''
    def __init__(self, name, attack, uses):
        self.name = name
        self.attack = attack
        self.uses = uses
class HersheyKisses(Weapons):
    '''
    Contructor for HersheyKisses, supers too Weapons
    @param self
    @param name
    @param attack
    @param uses
    '''
    def __init__(self, name, attack, uses):
        super(HersheyKisses, self).__init__(name, attack, uses)
class SourStraws(Weapons):
    '''
    Contructor for SourStraws, supers too Weapons
    @param self
    @param name
    @param attack
    @param uses
    '''
    def __init__(self, name, attack, uses):
        super(SourStraws, self).__init__(name, attack, uses)
class ChocolateBars(Weapons):
    '''
    Contructor for ChocolateBars, supers too Weapons
    @param self
    @param name
    @param attack
    @param uses
    '''
    def __init__(self, name, attack, uses):
        super(ChocolateBars, self).__init__(name, attack, uses)
class NerdBombs(Weapons):
    '''
    Contructor for NerdBombs, supers too Weapons
    @param self
    @param name
    @param attack
    @param uses
    '''
    def __init__(self, name, attack, uses):
        super(NerdBombs, self).__init__(name, attack, uses)

"""
Player class is used by the player and controls their attack and health.
If the player dies, game over.
"""

class Player(object):
    '''
    Constructor for Player
    
    @param self
    @param health health of player
    @param attack attack of player
    @param weapons_num number of weapons
    @param player_weapons weapon inventory of player housed in an array
    '''
    def __init__(self, health, attack, weapons_num, player_weapons):
        self.health = health
        self.attack = attack
        self.weapons_num = weapons_num
        self.player_weapons = player_weapons

    '''
    Weaponselect method used to select random weapons for player inventory
    
    @param self
    '''
    def weaponselect(self):
        while self.weapons_num != 0:
            x = random.randint(1,4)
            if x == 1:
                self.player_weapons.append(HersheyKisses_1)
                self.weapons_num = self.weapons_num - 1
            elif x == 2:
                self.player_weapons.append(SourStraws_1)
                self.weapons_num = self.weapons_num - 1
            elif x == 3:
                self.player_weapons.append(ChocolateBars_1)
                self.weapons_num = self.weapons_num - 1
            else:
                self.player_weapons.append(NerdBombs_1)
                self.weapons_num = self.weapons_num - 1
        return self.player_weapons
    
'''
Game class is where the game is played. User selects home and weapon then uses
weapon against the monsters within a home. Clearing one by one until either the player
dies or all monsters in the nieghborhood are defeated.
'''
class Game(object):
    '''
    Contructor for the Game class
    
    @param self
    @param neighborhood_monsters number of monsters in game
    @param neighborhood_houses number of houses in game
    @param weapon_inventory weapon inventory in game
    '''
    def __init__(self, neighborhood_monsters, neighborhood_houses, weapon_inventory):       
        self.neighborhood_monsters = neighborhood_monsters
        self.neighborhood_houses = neighborhood_houses
        self.weapon_inventory = weapon_inventory

    '''
    NumberOfMonsters counts how many monsters are in the neighborhood
    
    @param self
    '''
    def NumberOfMonsters(self):
        '''
        num_houses = self.neighborhood_houses
        num_monsters = self.neighborhood_monsters
        while num_houses != 0:
            self.neighborhood_monsters = H.monster_num + self.neighborhood_monsters
            print("test per house")
            print(self.neighborhood_monsters)
            num_houses = num_houses - 1
        '''
        self.neighborhood_monsters = len(templist)
        print(self.neighborhood_monsters)
        return self.neighborhood_monsters

    '''
    NextHome is a method in which the user selects which home is next.
    @param self
    '''
    def NextHome(self):
        num = 0
        for i in N.blocks:
            print("House number ",num, "\n")
            num = num + 1
        userInput = input("Choose a home by typing its number")
        temp = N.blocks[int(userInput)]
        print("this is temp",temp)
        for i in temp:
                print (i.name)
        if(len(N.blocks) == 0):
           G.GameOver()
        else:
           G.CurrentHome(temp)

    '''
    CurrentHome is the method used for actions on current home. Player attacks, monsters attack,
    rinse and repeat.
    @param self
    ''' 
    def CurrentHome(self, curHome):
        
        G.PlayerAttack(curHome)
        G.MonsterAttack(curHome)
        if(len(curHome) == 0 and self.neighborhood_monsters != 0):
           N.blocks.remove(curHome)
           G.NextHome()
        else:
           G.GameOver()

    '''
    PlayerAttack method uses the weapons in inventory. Player selects one, and aplifies their
    attack by the weapon ratio. Attacks monsters. If any die, turn them into human. Return new
    home.
    @param self
    @param curHome current home with all monsters
    '''
    def PlayerAttack(self, curHome):
        num = 0
        weaponlist = []
        PlayerTemp = P
        for i in P.player_weapons:
           print(num , ": " , i.name)
           weaponlist.append(i)
           num = num + 1
        userInput = input('Choose your weapon to attack the monsters by typing its number')
        #if(userInput not in P.player_weapons):
        #   userInput = input('Not typed correctly or not in inventory, try again.')
        curWeapon = weaponlist[int(userInput)]
        P.attack = P.attack * curWeapon.attack
        curWeapon.uses = curWeapon.uses - 1
        if (curWeapon.uses <= 0):
           for i in P.player_weapons:
               if(curWeapon.name == i.name):
                   P.player_weapons.remove(i)
        for i in curHome:
           if(i.name == "Person"):
               i.health = i.health - (PlayerTemp.attack * 0)
           else:
               i.healh = i.health - PlayerTemp.attack
               if (i.health <= 0):
                   curHome.append(Person_1)
                   curHome.remove(i)
        return curHome

    '''
    MonsterAttack method makes all monsters in current home attack player.
    @param self
    @param curHome monsters list for current home
    '''
    def MonsterAttack(self, curHome):
        for i in curHome:
           P.health = P.health - i.attack
        G.GameOver()

    '''
    GameOver method determins if the game should end or recurse based upon number of
    monsters in the neighborhood.
    @param self
    '''            
    def GameOver(self):
        if(P.health == 0):
           print("The monsters have ate you \n You are DEAD!!!")
        elif(self.neighborhood_monsters == 0):
            print("Congrats you have vanquished the monsters \n You WIN!!!")
        else:
            Game(self.neighborhood_monsters, self.neighborhood_houses, self.weapon_inventory)
    


Person_1   = Person("Person", -1, 100)
Zombie_1   = Zombie("Zombie", random.randint(1, 10), random.randint(50, 100))
Vampire_1  = Vampire("Vampire", random.randint(10, 20), random.randint(100, 200))
Ghoul_1    = Ghoul("Ghoul", random.randint(15, 30), random.randint(40, 80))
Werewolf_1 = Werewolf("Werewolf", random.randint(0, 40), 200)

HersheyKisses_1 = HersheyKisses("HersheyKisses", 1, -1)
SourStraws_1 = SourStraws("SourStraws", random.uniform(1, 1.75), 2)
ChocolateBars_1 = ChocolateBars("ChocolateBars", random.uniform(2, 2.4), 4)
NerdBombs_1 = NerdBombs("NerdBombs", random.uniform(3.5, 4), 1)

#H = Home(random.randint(0, 10), [])
#H_list = H.type_of_monster()
#print(H)
#for i in H_list:
#    print(i.name)
#print("this is home \n")
N = Neighborhood(random.randint(1,4), [])
N_list = N.create_neighborhood()
templist = []
for i in N.blocks:
    for j in i:
        templist.append(i)

        print(j.name)
    print("\n")
P = Player(random.randint(100,125), random.randint(10,20), 10, [])
P_list = P.weaponselect()
#for i in P_list:
#    print(i.name, i.attack, i.uses)
#print("test house number")
#print (N.houses_num)
G = Game(0, N.houses_num, P.player_weapons)
G.NumberOfMonsters()
#print("test neighborhood monsters")
#print(G.neighborhood_monsters)
G.NextHome()





