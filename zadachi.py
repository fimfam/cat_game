import tkinter
class Zadachi:
    def __init__(self,t,a):
        self.text=t
        self.answer=a
        self.enter=None


    def ekran(self):
        self.okno=tkinter.Tk()
        self.okno.geometry("500x400")
        self.label=tkinter.Label(text=self.text)
        self.label.pack()
        self.entry=tkinter.Entry()
        self.entry.pack()
        self.button=tkinter.Button(text='Ввести ответ',command=self.knopka)
        self.button.pack()

        self.okno.mainloop()

    def knopka(self):
        self.enter=self.entry.get()

        if self.enter==self.answer:
            self.okno.destroy()
        else:
            self.again=tkinter.Label(text="ответ не верный")
            self.again.pack()
            print(self.enter)






if __name__=='__main__':
    zadacha1=Zadachi("как дела?",'хорошо')
    zadacha1.ekran()



yslovia1=Zadachi("Система уравнений позвзволяет узнать необходимое количество капель каждого из веществ, чтобы создать нужное зелье. В ответ введите x y z через пробел.","30 20 40")
