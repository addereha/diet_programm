from tkinter import ttk
from tkinter import *


def ok():
	with open('data/info.txt', 'w') as file:
		inf = ''
		for i_info in range(1, 5, 2):
			inf = f'{inf} {list_info[i_info].get()}'
		
		inf = f'{inf} {list_info[-2].current()}'
		file.write(inf)
		
		file.close()
		import UMT
		window.destroy()


window = Tk()
window.geometry('500x300')
window.resizable(False, False)
window.title('Знакомство')
list_info = [Label(window, text='Введите ваш рост:', font=('Inter', 20)),
			 Entry(window, width=35),
			 Label(window, text='Введите вашу массу:', font=('Inter', 20)),
			 Entry(window, width=35),
			 Label(window, text='Ваш пол:', font=('Inter', 20)),
			 ttk.Combobox(window, width=35, values=['Мужчина', 'Женщина'], state='readonly'),
			 Button(window, text='ОК', command=ok, width=10)]
for i in list_info:
	i.pack()
window.mainloop()
