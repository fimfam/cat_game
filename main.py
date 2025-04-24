import sys

import pygame as p

from zadachi import yslovia1, probirki25, yslovia3, yslovia2_1, yslovia2_2, yslovia2_3

p.init()
d=p.display.set_mode((840,700),p.RESIZABLE)
b=p.time.Clock()
intro=[]
flag_intro=0
tick=5
for i in range(19):
    abc=p.image.load(f"C:/Users/Dasha/PycharmProjects/pythonProject1/интро{i+1}.png")
    abc=p.transform.scale(abc, (840,700))
    intro.append(abc)
#загрузки для первой задачи
fon1=p.image.load("лаборатория1080.png")
cat=p.image.load("кот стоит прозрачно.png")
cat=p.transform.scale(cat,(250,500))
cat1_x=10
table1=p.image.load("столпередкотом.png")
table1=p.transform.scale(table1,(700,300))
probirki=p.image.load("пробирки.png")
probirki=p.transform.scale(probirki,(90,67))
probirki1=probirki.copy()
intro_number=0

#загрузки для задачи 3
fon3=p.image.load("площадка.png")
cat3=p.transform.scale(cat,(90,180))
cat3_x=10
cat3_y=510
kacheli_flag=0
#загрузки для задачи 2
fon2=p.image.load("библиотека.png")
cat2=cat
shkaf1=p.image.load("шкаф1.png")
shkaf2=p.image.load("шкаф2.png")
shkaf3=p.image.load("шкаф3.png")
counter_shkaf=0
yslovia=[yslovia2_1,yslovia2_2,yslovia2_3]
shkaf=[shkaf1,shkaf2,shkaf3]
flag_shkaf=0
shkaf_x_1=340
shkaf_x_2=0
shkaf_x_3=340



nomerzadachi=0

def introrules():
    global nomerzadachi
    global intro_number
    global flag_intro
    global tick
    global d
    #блок отрисовки
    d.blit(intro[intro_number],(0,0))
    p.display.update()
    #блок обработки событий
    a=p.event.get()
    for t in a:
        if t.type==p.QUIT:
            p.quit()
            sys.exit()
        if t.type==p.MOUSEBUTTONDOWN:# and 500<t.pos[0]<720 and 480<t.pos[1]<560:
            print(t)
            flag_intro=1

    #замедление
    b.tick(tick)
    #логика
    if intro_number<18:
        intro_number+=1
    elif flag_intro==1:
         nomerzadachi=1
         d = p.display.set_mode((1080,700), p.RESIZABLE)
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
    d.blit(cat,(cat1_x,240))
    d.blit(table1,(300,400))
    d.blit(probirki,(660,365))
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

        if t.type== p.KEYDOWN and t.key==p.K_LEFT and cat1_x>0:
            cat1_x-=10
        if t.type== p.KEYDOWN and t.key==p.K_RIGHT and cat1_x<900:
            cat1_x+=10


        if t.type==p.MOUSEBUTTONDOWN   and t.button==1 and doska_flag==1:
            yslovia1.ekran()
            break
        if t.type==p.MOUSEBUTTONDOWN and t.button==1 and probirki_flag==1:
            probirki25()



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

def zadacha3():
    global nomerzadachi
    global cat3_x
    global cat3_y
    global kacheli_flag
    global fon3
    #блок отрисовки
    d.blit(fon3,(0,0))
    d.blit(cat3,(cat3_x,cat3_y))
    p.display.update()
    #блок лбработки событий
    a = p.event.get()
    i=p.key.get_pressed()
    if i[p.K_LEFT]==1 and cat3_x > 0 and cat3_y>500:
        cat3_x -= 1
    if i[p.K_RIGHT] and cat3_x < 980 and cat3_y>500:
        cat3_x += 1
    if i[p.K_UP]==1 and cat3_y > 0 and 100<cat3_x<200:
        cat3_y -= 1
    if i[p.K_DOWN] and 100<cat3_x<200 and cat3_y<510:
        cat3_y += 1
    if i[p.K_RIGHT] and 0<=cat3_y<45 and 100<cat3_x<200:
        cat3_y=152
        cat3_x=440
    if i[p.K_DOWN] and cat3_y==152 and cat3_x==440:
        cat3_y=510


    for t in a:
        if t.type == p.QUIT:
            p.quit()
            sys.exit()
        if t.type==p.KEYDOWN and t.key==p.K_SPACE:
            print(cat3_x,cat3_y)
        if t.type==p.MOUSEBUTTONDOWN   and t.button==1 and kacheli_flag==1:
            kacheli_flag=0
            yslovia3.ekran()
            break
        if t.type==p.MOUSEBUTTONDOWN   and t.button==1 and yslovia3.itog==1:
            nomerzadachi+=1


    if cat3_x==440 and cat3_y==152:
        p.draw.rect(fon3,(255,255,0),(440,152,180,180),5)
        kacheli_flag=1
    else:
        fon3 = p.image.load("площадка.png")
        kacheli_flag=0

    if yslovia3.itog==1:
        cat3_x=980
        cat3_y=1
        p.draw.rect(fon3,(255,255,255),(880,0,200,200),5)

def zadacha2():
    global nomerzadachi
    global shkaf1
    global shkaf2
    global shkaf3
    global counter_shkaf
    global flag_shkaf
    global shkaf_x_1, shkaf_x_2, shkaf_x_3
    #отрисовка
    d.blit(fon2,(0,0))
    if counter_shkaf<3:
        d.blit(shkaf[2],(shkaf_x_3,87))
    if counter_shkaf<2:
        d.blit(shkaf[1],(shkaf_x_2,87))
    if counter_shkaf==0:
        d.blit(shkaf[0],(shkaf_x_1,87))

    p.display.update()
    #обработка событий
    a=p.event.get()
    i=p.key.get_pressed()
    if flag_shkaf==1 and counter_shkaf==0 and i[p.K_RIGHT]:
        if shkaf_x_1>1080:
            flag_shkaf=0
            counter_shkaf=1
            p.draw.rect(shkaf2, (255, 255, 255), (340, 30, 50, 50), 5)
        else:
            shkaf_x_1+=7
            print(shkaf_x_1)
    if flag_shkaf==1 and counter_shkaf==1 and i[p.K_LEFT]:
        if shkaf_x_2<-540:
            flag_shkaf=0
            counter_shkaf=2
            p.draw.rect(shkaf3, (255, 255, 255), (340, 30, 50, 50), 5)
        else:
            shkaf_x_2-=7
    if flag_shkaf==1 and counter_shkaf==2 and i[p.K_RIGHT]:
        if shkaf_x_3>1080:
            flag_shkaf=0
            counter_shkaf=3
            p.draw.rect(fon2, (255, 255, 255), (500,400,100,200), 5)
        else:
            shkaf_x_3+=7

    if counter_shkaf==0 and flag_shkaf==0:
        p.draw.rect(shkaf1, (255, 255, 255), (340, 30, 50, 50), 5)

    for t in a:
        if t.type == p.QUIT:
            p.quit()
            sys.exit()
        if t.type==p.MOUSEBUTTONDOWN   and t.button==1 and counter_shkaf<3 and flag_shkaf==0:
            yslovia[counter_shkaf].ekran()
            flag_shkaf=1
            shkaf[counter_shkaf]=p.image.load(f'шкаф{counter_shkaf+1}.png')
            break
        if t.type==p.MOUSEBUTTONDOWN   and t.button==1 and counter_shkaf==3:
            nomerzadachi+=1
            break



while True:
    if nomerzadachi==0:
        introrules()
    elif nomerzadachi==1:
        zadacha2()
    else:
        zaglushka()



