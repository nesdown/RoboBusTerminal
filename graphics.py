from tkinter import *

WIDTH = 800
HEIGHT = 600
GEOMETRY = str(WIDTH) + 'x' + str(HEIGHT)
PADDING = 30

root = Tk()
root.title('RoboHouse Terminal v1.0')
root.geometry(GEOMETRY)

menu_screen = Frame(root)
label_data = Label(text='Платіжна система RoboBus')

btn_course_pay = Button(menu_screen, text='Сплатити за курс')
btn_merch_pay = Button(menu_screen, text='Сплатити за мерч')
btn_donate = Button(menu_screen, text='Допомогти розвитку')
btn_info = Button(menu_screen, text='Про проект')

label_data.pack(anchor='n', pady=15)

menu_screen.pack(fill=X, pady=100)
btn_course_pay.pack(anchor='w', pady=PADDING)
btn_merch_pay.pack(anchor='w', pady=PADDING)
btn_donate.pack(anchor='w', pady=PADDING)
btn_info.pack(anchor='e', pady=PADDING)

root.mainloop()


