from tkinter import *
import random, time

def bros():
    x= random.choice(['b1.png','b2.png','b3.png','b4.png','b5.png','b6.png',])

    return x

def img(event):
    global b1,b2
    for i in range(10):
        b1 = PhotoImage(file=(bros()))
        b2 = PhotoImage(file=(bros()))
        lab1['image'] = b1
        lab2['image'] = b2
        root.update()
        time.sleep(0.12)

root = Tk()
root.geometry('400x200')
root.title('Игра в кости, сделай бросок')
root.resizable(height=False, width=False)  # запрещаем растягивать окно, менять размер
root.iconphoto(True, PhotoImage(file=('icon2.png')))  # иконка окна

# fon = PhotoImage(file=('fon.png'))  # задаем изображение фона
# Label(root, image=fon).pack()  # размещаем изображение фона на окне

lab1 = Label(root)
lab1.place(relx=0.3, rely=0.5, anchor=CENTER) # anchor CENTER значит центр метки будет размещаться по заданным координатам

lab2 = Label(root)
lab2.place(relx=0.7, rely=0.5, anchor=CENTER)

# Button(root, text='Бросок',command=img).pack()
root.bind('<1>',img) # привязываем событие клика мыши

img('event') # вызов чтобы при запуске сразу вызвались lab1 и lab2

root.mainloop()  # замыкаем окно

# print('hi')
