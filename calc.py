from tkinter import *
 
 
class Block:
    num1 = 0
    num2 = 0
    oper = '+'
    res = 0
    font = ("Comic Sans MS", 24, "bold")
    width = 40
    def __init__(self, master, func1, func2, func4, func5, func3, funcN):
        self.ent = Entry(master, width=self.width, bg='gray', fg='white', font=self.font)
        self.but1 = Button(master, width=self.width, text="+", bg='orange', fg='white', font=self.font)
        self.but2 = Button(master, width=self.width, text="-", bg='orange', fg='white', font=self.font)
        self.but4 = Button(master, width=self.width, text="*", bg='orange', fg='white', font=self.font)
        self.but5 = Button(master, width=self.width, text="/", bg='orange', fg='white', font=self.font)
        self.but3 = Button(master, width=self.width, text="=", bg='orange', fg='white', font=self.font)
        self.butN = Button(master, width=self.width, text="C", bg='orange', fg='white', font=self.font)
        self.lab = Label(master, width=self.width, bg='green', fg='white', font=self.font)
        self.but1['command'] = eval('self.' + func1)
        self.but2['command'] = eval('self.' + func2)
        self.but4['command'] = eval('self.' + func4)
        self.but5['command'] = eval('self.' + func5)
        self.but3['command'] = eval('self.' + func3)
        self.butN['command'] = eval('self.' + funcN)
        self.ent.pack()
        self.but1.pack()
        self.but2.pack()
        self.but4.pack()
        self.but5.pack()
        self.but3.pack()
        self.butN.pack()
        self.lab.pack()

 
    def make_add(self):
        self.oper = '+'
        s = self.ent.get()
        if s!='':
            self.num1 = int(s)
        else:
            self.num1 = self.res
        self.ent.delete(0, 'end')
 
    def make_sub(self):
        self.oper = '-'
        s = self.ent.get()
        if s!='':
            self.num1 = int(s)
        else:
            self.num1 = self.res
        self.ent.delete(0, 'end')

    def make_mul(self):
        self.oper = '*'
        s = self.ent.get()
        if s!='':
            self.num1 = int(s)
        else:
            self.num1 = self.res
        self.ent.delete(0, 'end')

    def make_div(self):
        self.oper = '/'
        s = self.ent.get()
        if s!='':
            self.num1 = int(s)
        else:
            self.num1 = self.res
        self.ent.delete(0, 'end')


    def get_res(self):
        s = self.ent.get()
        if s!='':
            self.num2 = int(s)

        if self.oper=='+':
            self.res = self.num1+self.num2
        elif self.oper=='-':
            self.res = self.num1-self.num2
        elif self.oper=='*':
            self.res = self.num1*self.num2
        elif self.oper=='/':
            self.res = self.num1/self.num2

        self.ent.delete(0, 'end')
        self.lab['text'] = self.res

    def clear(self):
        self.res = 0
        self.ent.delete(0, 'end')
        self.lab['text'] = ''


 
root = Tk()

first_block = Block(root, 'make_add', 'make_sub', 'make_mul', 'make_div', 'get_res', 'clear')
 
root.mainloop()