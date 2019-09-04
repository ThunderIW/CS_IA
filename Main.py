import time
import string
global character_information
import emoji
import random
character_information = {}
character_info=()
f=open('character_info','r')
class_Info=f.readlines()
cash=100
def store(cash):
    n_2=0
    lines_from_quote=[]
    items_in_shop=[]
    costs_item=[]
    f_2=open('Shop.Items','r+')
    f_3=open('random quotes for shop keeper','r+')
    f_4=open('COST_OF_ITEM','r+')


    cost=f_4.readlines()
    for c in cost:
        striped_c = c.strip('\n')
        costs_item.append(striped_c)
    print(costs_item)


    quote=f_3.readlines()
    for lines in quote:
        striped_lines=lines.strip('\n')
        lines_from_quote.append(striped_lines)

    items=f_2.readlines()
    for n in items:
        striped_items = n.strip('\n')
        items_in_shop.append(striped_items)
    print(len(items_in_shop))
    while '' in items_in_shop:
        items_in_shop.remove('')


    print(emoji.emojize(':department_store::department_store::department_store:'))
    print('Welcome to my shop hope you find anything interesting')
    print('Here are some of the items that I sell in my shop-->{}'.format(items_in_shop))
    while True:
        print(emoji.emojize('you have->{} :pound: left', use_aliases=True))
        item_to_buy=input('please enter b when you what to buy an item:{}\nIf you want to leave the shop type E--> '.format(items_in_shop[n_2]))
        print("******************************************************************")
        n_2+=1
        if item_to_buy.upper()=="B":
            print('You have selected to buy->{}\nThis item costs->{}'.format(items_in_shop[n_2],costs_item[n_2]))
            confirm=input('Do want to buy {} type y to buy the item or type n to not buy the item->'.format(items_in_shop[n_2]))


        if cash==0:
            print('sorry you have no more money left')
            break

        if confirm.upper() == 'Y':
            print('Item has been bought')
            cash = cash - int(costs_item[n_2])

        if item_to_buy.upper()=='E':
            print(random.choice(lines_from_quote))
            break
        if len(items_in_shop)==n_2:
            n_2=0
    main_game()



def main_game():
    print('')


def character_confirm():
    print('Your character information are as follow')
    for key, value in character_information.items():
        print('********************')
        print(key, '->', value)
        print('********************')

    confirm = input('is everything correct->')
    if confirm.upper() == 'YES':
        main_game()

    if confirm.upper() == 'NO':
        print('ALright lets us fix that')
        print('Here is your character information->{}'.format(character_information.keys()))
        ItemToRemove = input(str('What would like to remove->'))
        if str(ItemToRemove) in character_information:
            del character_information[str(ItemToRemove)]
        print('The updated list->{}'.format(character_information))

        fix = input(
            'If you want to change your Class role type C\nIf you want to change your name type N\nI you want to change your skills type S\n-->')

        if fix.upper() == 'C':
            character_making()
        if fix.upper() == 'N':
            character_name()
        if fix.upper() == 'S':
            skills()


def intro():
    player_name = input('adventurer welcome to the game what is name adventurer-->')
    ReadyToPlay = input('welcome [{}] to my computer scince IA, woud you like to play-->'.format(player_name))

    if ReadyToPlay.upper() == 'YES' or ReadyToPlay.upper()=='Y':
        print('welcome player')
        character_making()
    if ReadyToPlay.upper() == 'NO':
        print('Thank you for dropping by hope you come back')


def skills():
    traits = {}
    Traits = ['strength', 'Perception', 'Endurance', 'Intelligence', 'Agility']
    n = 0
    num_of_points = 15
    num_strength = 0
    num_Perception = 0
    num_Endurance = 0
    num_Intelligence = 0
    num_Agility = 0
    print('You have a total of->{}'.format(num_of_points))
    while num_of_points != 0:
        skill_selection = input(
            'Cuurent trait selected->{} and you have->{} skill points remaining ,type D  to add points to the skill->'.format(
                Traits[n], num_of_points))
        print('--------------------------------------------------------------')
        if skill_selection.upper() == 'D':

            if Traits[n].upper() == "STRENGTH":
                num_strength += 1
                print('Point added to strength->{}'.format(num_strength))
                num_of_points -= 1
                traits['Strength'] = num_strength

            if Traits[n].upper() == 'PERCEPTION':
                num_Perception += 1
                print('Point added to Perception->{}'.format(num_Perception))
                num_of_points -= 1
                traits['Perception'] = num_Perception

            if Traits[n].upper() == 'ENDURANCE':
                num_Endurance += 1
                print('Point added to Endurance->{}'.format(num_Endurance))
                num_of_points -= 1
                traits['Endurance'] = num_Endurance

            if Traits[n].upper() == 'INTELLIGENCE':
                num_Intelligence += 1
                print('Point added to Intelligence->{}'.format(num_Intelligence))
                num_of_points -= 1
                traits['Intelligence'] = num_Intelligence

            if Traits[n].upper() == 'AGILITY':
                num_Agility += 1
                print('Point added to Agility->{}'.format(num_Agility))
                num_of_points -= 1
                traits['Agility'] = num_Agility

        n += 1
        if n == len(Traits):
            n = 0

    print('Your skills are as followed->{}'.format(traits))
    time.sleep(1)
    character_information['Skills'] = traits
    character_confirm()


def character_name():
    final_name=str()
    letters_uppercase=list(string.ascii_uppercase)
    final_name=[]
    n=0
    while True:
        choice=input('Current letter-->{},press E when your happy with your chosen letter\nType D if your happy with your character name->'.format(letters_uppercase[n]))
        if choice.upper()=='E':
            final_name.append(letters_uppercase[n])
            name=''.join(final_name)
            print(name)
        if choice.upper()=='D':
            break
        n+=1
        if n==len(letters_uppercase):
            n=0
    print('Your character name-->{}'.format(name))
    time.sleep(1)
    character_information['Player name']=name
    skills()


def character_making():
    character_class = ['Gunslinger', "Hacker", 'Medic', 'Ranger', 'Cybernetics Investigator',
                       'Extra-dimensional Investigator', 'Neutron Cyborg Assassin']
    n = 0
    while True:
        character_slection = input(
            'Your character role is:{} if your happy with your choice type D\nLike to hear more information type Info-->'.format(
                character_class[n]))
        print('--------------------------')
        if character_slection.upper() == "D":
            character_role = character_class[n]
            character_information['Class'] = character_role
            break

        if character_slection.upper() == 'WEEB':
            print('New class unlocked->Weeb master')
            character_class.append('Weeb Master')
        if character_slection.upper() == 'TIME IS EVERYTHING':
            print('New Class unlocked->Time Doctor')
            character_class.append('Time Doctor')

        if character_slection.upper() == 'INFO':
            if character_class[n] == 'Gunslinger':
                print(class_Info[0])

            if character_class[n] == 'Hacker':
                print(class_Info[1])
                time.sleep(1)
            if character_class[n] == 'Medic':
                print(class_Info[2])
                time.sleep(1)
            if character_class[n] == 'Ranger':
                print(class_Info[4])
                time.sleep(1)
            if character_class[n] == 'Weeb Master':
                print(class_Info[3])
            if character_class[n] == "Cybernetics Investigator":
                print('TEST info for Cybernetics Investigator')
            if character_class[n] == 'Extra-dimensional Investigator':
                print('TEST info for Extra-dimensional Investigator')
            if character_class[n] == 'Neutron Cyborg Assassin':
                print('TEST INFO FOR Neutron Cyborg Assassin')
            if character_class[n] == 'Time Doctor':
                print('TEST INFO FOR Time Doctor')
        n += 1
        if n == len(character_class):
            n = 0

    print('Outside')
    print('Your character_class is:{}'.format(character_role))
    time.sleep(1)
    character_name()


#intro()
store(cash)
