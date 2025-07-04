import tkinter
from PIL import ImageTk, Image
class Zadachi:
    def __init__(self,t,a,i=None):
        self.text=t
        self.answer=a
        self.enter=None
        self.itog=0
        self.image=i



    def ekran(self):
        self.okno=tkinter.Tk()
        self.okno.geometry("500x400")
        self.label=tkinter.Label(text=self.text)
        self.label.pack()
        if self.image:
            img = Image.open(self.image)
            image = ImageTk.PhotoImage(img)
            panel = tkinter.Label(self.okno, image=image)
            panel.pack(side="top", fill="both", expand="no")
        self.entry=tkinter.Entry()
        self.entry.pack()
        self.button=tkinter.Button(text='Ввести ответ',command=self.knopka)
        self.button.pack()

        self.okno.mainloop()

    def knopka(self):
        self.enter=self.entry.get()

        if self.enter==self.answer:
            self.okno.destroy()
            self.itog=1
        else:
            self.again=tkinter.Label(text="ответ не верный")
            self.again.pack()
            print(self.enter)


def okoshko(kartinka):
    okno = tkinter.Tk()
    okno.geometry("600x600")
    img = Image.open(kartinka)
    image = ImageTk.PhotoImage(img)
    panel = tkinter.Label(okno, image=image)
    panel.pack(side="top", fill="both", expand="no")

    okno.mainloop()


if __name__=='__main__':
    probirki1()



yslovia1=Zadachi("Система уравнений позвзволяет узнать\n необходимое количество капель каждого\n из веществ, чтобы создать нужное зелье.\n В ответ введите x y z через пробел.","30 20 40")


yslovia3=Zadachi("Каков должен быть угол отклонения качелей от вертикали, чтобы кот долетел до двери, расположенной в 3 м дальше и в 2 м выше точки отрыва от качелей? Длина качелей 2 м. Рассмотрите тот случай, когда он вылетает с качелей с минимальной кинетической энергией. Найдите скорость, с которой кот проходит нижнюю точку качелей, чтобы этот полет состоялся. Ответы введите через пробел, округляя до десятых","1 1")


yslovia2_1=Zadachi("выбери книжку1","1","полка1.png")
yslovia2_2=Zadachi("выбери книжку2","1")
yslovia2_3=Zadachi("выбери книжку3","1")

yslovia4=Zadachi("выберете записку","1")
