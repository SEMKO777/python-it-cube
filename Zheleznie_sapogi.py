import random

karma = 0
print('Добо пожаловать во вселенную "Железные сапоги", сдесь ты будешь проходить сюжет, и вообще делать всё')
inventory = {
    'Шлем' : 'Нет',
    'Броня' : 'Нет',
    'Ботинки' : 'Нет',
    'Оружие' : 'Нет',
    'Щит' : 'Нет'
    }
money = 10
def inv():
    for key,value in inventory.items():
        print(key + ' - ' + value)
    print('У вас есть ' + str(money) + ' монет')
your_HP = 15
your_P = 5
print('Ты стоишь перед воротами в крепость, щит стажника блестит на солнце и слепит тебе глаза')
d = int(input('1 - пройти через ворота, 2 - украсть щит у охранника'))
if d == 1:
    print('Ты вошёл в ворота')
elif d == 2:
    d = random.randint(0,11)
    if d >= 9:
        print('Ты украл щит. Незнаю как. И вошёл в город.(перемещено в инвентарь, что бы посмотреть введи в поле выбора действия "22")')
        inventory['Щит'] = 'Свекающий щит'
        karma += 1
    else:
        karma += 1
        print('Охранник не дал тебе украсть щит. Нехорошо.')
elif d == 22:
    inv()
else:
    print('Нет.')
print('Ты вошёл в Геон - небольшой город который,тем не менее является торговой столицей')
print('В каждом доме на первом этаже находится тоговая лавка, большинство домов двухэтажные,но так же есть дома до четырёх этажей')
while True:
    f = int(input('В какую лавку пойдёшь? 1 - бронник, 2 - оружейник, 3 - заработать денег(Введи 10 что бы закончить закупаться)'))
    if f == 1:
        print('Ты вошёл в лавку бронника, что хочешь купить?(Введи 10 что бы закончить закупаться)')
        e = int(input('1 - железный нагудник(7 монет,35 классов брони), 2 - железный шлем(5 монет,25 классов брони), 3 - сапоги(3 монеты, 15 классов брони)')) 
        if e == 1:
            if money >= 7:
                print('Вы купили нагудник')
                money -= 7
                inventory['Броня'] = 'стальной нагрудник'
                your_HP += 35
            else:
                print('Не хватает денег')
        if e == 2:
            if money >= 5:
                print('Вы купили шлем')
                money -= 5
                inventory['Шлем'] = 'стальной шлем'
                your_HP += 25
            else:
                print('Не хватает денег')
        if e == 3:
            if money >= 3:
                print('Вы купили сапоги')
                money -= 3
                inventory['Ботинки'] = 'сапоги'
                your_HP += 15
            else:
                print('Не хватает денег')
    elif f == 2:
        print('Ты вошёл в лавку оружейника,что хочешь купить?(Введи 10 что бы закончить закупаться)')
        e = int(input('1 - арбалет(7 монет,35 урона), 2 - меч(5 монет,25 классов брони), 3 - кинжал(1 монета, 5 урона),4 - щит(2 монеты,10 классов брони,10 урона)')) 
        if e == 1:
            if money >= 7:
                print('Вы купили арбалет')
                inventory['Оружие'] = 'арбалет'
                money -= 7
                your_P += 35
            else:
                print('Не хватает денег')
        if e == 2:
            if money >= 5:
                print('Вы купили меч')
                inventory['Оружие'] = 'меч'
                money -= 5
                your_P += 25
            else:
                print('Не хватает денег')
        if e == 3:
            if money >= 1:
                print('Вы купили кинжал')
                money -= 3
                your_P += 15
            else:
                print('Не хватает денег')
        if e == 4:
            if money >= 2:
                print('Вы купили щит')
                inventory['Щит'] = 'стальной щит'
                money -= 2
                your_P += 10
                your_HP += 10
            else:
                print('Не хватает денег')
    elif f == 3:
        while True:
            try:
                a = int(input('Введи любую цифру что бы заработать 1 монету 11 что бы выйти'))
                if a == 11:
                    break
                money += 1
                print("ты заработал 1 монету")
            except ValueError:
                print("вводите числа")
    elif f == 22:
        inv()
    elif f == 10:
        break
    else:
        print('Нет.')
if inventory['Щит'] == 'Сверкающий щит':
    your_HP += 20
    your_P += 20
print('Ты приближаешься к цели своего путешествия,к пещере где живёт тролль который когда то уничтожил твою родную деревню')
print('Тролль пробудился и вышел к тебе навстречу, битва начинается!')
troll_HP = 70
l = 0
mmmmmmmmmm = 0
while True:
    print('твоё здоовье - ' + str(your_HP) + ' здоровье тролля' + ' - ' + str(troll_HP))
    v = int(input('1 - удар, 2 - уворот'))
    if v == 1:
        mmmmmmmmmm += 1
        k = random.randint(0,10)
        if k > 6:
            troll_HP -= your_P * 2
            print('Критический удар!Двойной урон!')
        else:
            troll_HP -= your_P
            your_HP -= 10
    elif v == 22:
        inv()
    else:
        print('Ты увернулся')
        d = random.randint(0,21)
        if d == 10:
            troll_HP -= 70
            print('Тролль был невыспавшийся и упал с обрыва. Вот так.')
            break
        l += 1
        if l >= 5:
            print('После очередного переката ты упал с обыва и умер смертью идиота.')
            break
    if troll_HP <= 0:
        print('Ты убил тролля! Победа!')
        if karma == 1:
            print('Но не воруй больше.')
        else:
            print('Молодец! Лучшая концовка!')
        if mmmmmmmmmm == 1:
            print('Убийство с одного удара!')
        break
    elif your_HP <= 0:
        print('Троль убил тебя. Ты умер смертью героя')

