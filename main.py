import sys

import pygame as p

from zadachi import yslovia1

p.init()
d=p.display.set_mode((1080,810))
b=p.time.Clock()
intro=[]
flag_intro=0
tick=0.5
for i in range(19):
    intro.append(p.image.load(f"C:/Users/Dasha/PycharmProjects/pythonProject1/интро{i+1}.png"))
#загрузки для первой задачи
fon1=p.image.load("лаборатория1080.png")
cat=p.image.load("кот стоит прозрачно.png")
cat1_x=10
table1=p.image.load("столпередкотом.png")
probirki=p.image.load("пробирки.png")
probirki1=probirki.copy()
intro_number=0


nomerzadachi=0

def introrules():
    global nomerzadachi
    global intro_number
    global flag_intro
    global tick
    #блок отрисовки
    d.blit(intro[intro_number],(0,0))
    p.display.update()
    #блок обработки событий
    a=p.event.get()
    for t in a:
        if t.type==p.QUIT:
            p.quit()
            sys.exit()
        if t.type==p.MOUSEBUTTONDOWN and 500<t.pos[0]<720 and 480<t.pos[1]<560:
            flag_intro=1

    #замедление
    b.tick(tick)
    #логика
    if intro_number<18:
        intro_number+=1
    elif flag_intro==1:
         nomerzadachi=1
    else:
        tick=30
    return


def zadacha1():
    global nomerzadachi
    global cat1_x
    global probirki
    global fon1
    # блок отрисовки
    d.blit(fon1,(0, 0))
    d.blit(cat,(cat1_x,255))
    d.blit(table1,(150,470))
    d.blit(probirki,(650,457))
    p.display.update()
    # блок обработки событий
    a = p.event.get()

    #подсветка пробирок
    if 550<cat1_x<740:
        p.draw.rect(probirki,(255,255,255),(0,0,133,103),5)
        probirki_flag=1
    else:
        probirki = p.image.load("пробирки.png")
        probirki_flag=0


    #подсветка доски

    if 110<cat1_x<410:
        p.draw.rect(fon1,(255,255,255),(240,20,720,400),5)
        doska_flag=1
    else:
        fon1 = p.image.load("лаборатория1080.png")
        doska_flag=0



    for t in a:
        if t.type == p.QUIT:
            p.quit()
            sys.exit()

        if t.type== p.KEYDOWN and t.key==p.K_LEFT:
            cat1_x-=10
        if t.type== p.KEYDOWN and t.key==p.K_RIGHT:
            cat1_x+=10

        if t.type==p.MOUSEBUTTONDOWN   and t.button==1 and doska_flag==1:
            yslovia1.ekran()



    # замедление
    b.tick(30)
    # логика

def zaglushka():
    #блок отрисовки
    d.fill((45,67,89))
    p.display.update()
    #блок обработки событий
    a=p.event.get()
    for t in a:
        if t.type==p.QUIT:
            p.quit()
            sys.exit()


    #замедление
    b.tick(30)
    #логика



while True:
    if nomerzadachi==0:
        introrules()
    if nomerzadachi==1:
        zadacha1()
    else:
        zaglushka()



