from random import choice
from tkinter import *

root = Tk()
root.title('Groups Selector')
opt1=IntVar()

main = []
answer = []
question = []
#a = ['A','B','C','D','E','F','G','H']
options = []
def Selecting_Choice(opt1):
	global n,options, options2
	n = int(ent.get())
	opt2 = opt1.get()
	if opt2==1:
		Letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
		for k in range(n):
			options.append(Letters[k])
	else:
		Numbers = '123456789'
		for k in range(n):
			options.append(Numbers[k])
	temp = options.copy()

def randomize(z):
	global n,main, options, opt, final, answer

	Selecting_Choice(opt1)
	
	temp = options.copy()
	
	for k in range (n//2):
		b = choice(options)
		question.append(b)
		options.remove(b)
		c = choice(options)
		answer.append(c)
		options.remove(c)
		d = b+':'+c
		main.append(d)
	question.append(options[0])
	
	for k in range(n//2):
		b = choice(answer)
		answer.remove(b)
		c = choice(question)
		question.remove(c)
		d = b+':'+c
		main.append(d)
	
	if options[0] != question[0]:
		final = '\t'.join(main)
		final = final +'\t' + options[0]+':'+question[0]
		temp = options[0]+':'+question[0]
		main.append(temp)
		print(main)

		print(final)
		Label(root, height =4,background = 'RosyBrown1',text=final).place(x=63,y=210)
		
		boot = Tk()
		boot.title('Groups')
		Label(boot, background = 'sienna1', height=400, width=700).place(x=0,y=0)
		Label(boot, background = 'sienna1', text=final,font = ('Times New Roman', 25)).place(x=70,y=100)
		boot.geometry('1300x350')
		boot.resizable(width=False, height=False)
		boot.mainloop()

	else:
		randomize()


def display(z):
	boot = Tk()
	boot.title('Credits')
	Label(boot, background = 'turquoise', height=400, width=700).place(x=0,y=0)
	Label(boot, background = 'dodgerblue', height=5, width=37).place(x=30,y=8)
	Label(boot, background = 'dodgerblue', text='Monniiesh Velmurugan', font = ('Times New Roman', 15)).place(x=70,y=10)
	Label(boot, background = 'dodgerblue', text='monniiesh22@gmail.com', font = ('Times New Roman', 15)).place(x=60,y=35)
	Label(boot, background = 'dodgerblue', text='+956 69609445', font = ('Times New Roman', 15)).place(x=94,y=60)
	boot.geometry('320x100')
	boot.mainloop()

Label(root, width=400, height=300, background='LightSkyBlue1').place(x=1,y=1)

Label(root, height=2, width=78,relief='solid',borderwidth=2,background='tomato').place(x=1,y=1)

Label(root, text="Number of Teams", width=40, height=1, relief='solid',borderwidth=2,background='tomato').place(x=128,y=40)
ent=Entry(root,width=4)
ent.place(x=255,y=65)

Label(root, text="Type", width=25, height=1, relief='solid',borderwidth=2,background='medium spring green').place(x=180,y=100)

Radiobutton(root,text='Numbers',variable=opt1,value=2,background='LightSkyBlue1').place(x=325,y=125)
Radiobutton(root,text='Letters',variable=opt1,value=1,background='LightSkyBlue1').place(x=160,y=125)

sub=Button(root,text='Enter',width=10,background='medium spring green', relief = SOLID)
sub.bind('<Button-1>', randomize)
sub.place(x=233,y=160)

credits=Button(root,text='Credits',width=10,background='light coral' ,relief = SOLID)
credits.bind('<Button-1>', display)
credits.place(x=5,y=5)

Label(root, width=78, height=6, relief='solid',borderwidth=2,background='SteelBlue1').place(x=1,y=195)
Label(root, width=66, height =5,background = 'RosyBrown1').place(x=40,y=200)

root.geometry('554x300')
root.resizable(width=False, height=False)
root.mainloop()