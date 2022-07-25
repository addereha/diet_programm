import os
import tkinter
from tkinter import *
from tkinter import ttk
import tkinter.messagebox as mb
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)
from matplotlib.figure import Figure


def opening(file):
	file = open(os.path.abspath(f'data/{file}'), 'r', encoding='UTF-8')
	return file


def change_day():
	global day, massa_day, self_day, kkal_day
	day_of_week = WEEK[day]
	button_start['text'] = 'Следующий день'
	day += 1
	menu = day_of_week
	for i_food in eats[day_of_week]:
		menu = f'{menu}\n{i_food}'
	plan_label['text'] = menu
	print(day_of_week)
	if day_of_week == 'Понедельник':
		massa_label = Label(window_diet, text='Введите свою массу за сегодня', font=("Inter", 12))
		massa_day = Entry(window_diet)
		kkal_label = Label(window_diet, text='Введите количество калорий за сегодня', font=("Inter", 12))
		kkal_day = Entry(window_diet)
		self_label = Label(window_diet, text='Введите свое самочувствие\nпо шкале от 1 до 10',
						   font=("Inter", 12))
		self_day = Entry(window_diet)
		kkal_label.pack()
		kkal_day.pack()
		massa_label.pack()
		massa_day.pack()
		self_label.pack()
		self_day.pack()
	if day_of_week != "Понедельник":
		if calories-200<int(kkal_day.get())<calories:
			mb.showinfo('Итоги дня', 'Все в порядке!')
		elif int(kkal_day.get()) < calories:
			mb.showinfo('Итоги дня', 'Недостаточное потребление пищи!')
		elif int(kkal_day.get()) > calories:
			mb.showinfo('Итоги дня', 'Потребление калорий сверх нормы!')
		data_list.extend([int(massa_day.get()), int(self_day.get())])
		massa_day.delete('0', 'end')
		self_day.delete('0', 'end')
	if day_of_week == 'Воскресенье':
		window_graph = Tk()
		window_graph.title('Масса:')
		fig = Figure(figsize=(4, 4), dpi=100)
		plot1 = fig.add_subplot(111)
		plot1.plot(data_list[::2])
		canvas = FigureCanvasTkAgg(fig, master=window_graph)
		canvas.draw()
		canvas.get_tk_widget().pack()
		
		window_graph = Tk()
		window_graph.title('Cамочувствие:')
		fig = Figure(figsize=(4, 4), dpi=100)
		plot1 = fig.add_subplot(111)
		plot1.plot(data_list[1::2])
		canvas = FigureCanvasTkAgg(fig, master=window_graph)
		canvas.draw()
		canvas.get_tk_widget().pack()


def diet():
	global eats, plan_label, button_start, window_diet
	
	eats = normal_eats if combo.get() != 'Ничего' else normal_plus_eats
	knopka['state'] = DISABLED
	plan = ''
	window_diet = Tk()
	window_diet.geometry('350x500')
	plan_label = Label(window_diet, text=plan, font=("Inter", 12))
	button_start = Button(window_diet, text='Начать', command=change_day, width=30, height=3)
	plan_label.pack()
	button_start.pack()
	window_diet.mainloop()


data_list = []
WEEK = ('Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье')
day = 0
window = Tk()
window.geometry('500x150')
window.resizable(True, False)
window.title('ИМТ')


troubles_list = [i for i in opening('troubles.txt').read().split('\n')]
normal = [[j for j in i.split('_')] for i in opening('Normal.txt').read().split('\n')]
normal_plus = [[j for j in i.split('_')] for i in opening('Normal+.txt').read().split('\n')]
param = [int(i) for i in opening('info.txt').read().split()]
height, weight, number = param
calories = (0.062 * weight + 2.036) * 240 * 1.3 if number == 1 else (0.062 * weight + 2.896) * 240 * 1.3
calories = int(calories)

normal_eats = dict(zip(WEEK, normal))
normal_plus_eats = dict(zip(WEEK, normal_plus))

combo = ttk.Combobox(window, values=troubles_list, width=40, state='readonly')
combo.current(len(troubles_list) - 1)
combo.place(x=0, y=50)
knopka = tkinter.Button(window, text='Сформировать\n диету', font=('Inter', '10'), command=diet)
knopka.place(x=350, y=35, width=100, height=50)

body_mass_ind = weight / (height / 100) ** 2
text = Label(window, text=f'Ваш ИМТ равен {int(body_mass_ind)}')
text.place(x=1, y=1)

window.mainloop()
