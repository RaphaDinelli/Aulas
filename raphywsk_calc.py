from tkinter import *

class Cauculator:
    def __init__(self, toplevel):
        self.window = toplevel
        toplevel.resizable(width=False, height=False)
        toplevel.title('CALCULADORA')

        self.values = '' #Valores digitados
        
        
        # Valores de height e width dos botões
        
        number_hw = 2
        button_height = 1
        button_width = 4
        # Valores de padx e pady
        number_padx= 5
        number_pady= 5
        button_pad= 5
        
        self.canvas1 = Canvas(toplevel, width=200, height=75, bd=5, bg='white')
        self.canvas1.create_text(20,50, text=('0'), anchor=W,
                                    font=('Verdana', 16, 'bold'), fill='blue',
                                    width=190, tag='numeros')
        self.canvas1.pack()
        
        self.f1=Frame(toplevel)
        self.f1.pack()
        
        self.f2=Frame(toplevel)
        self.f2.pack(side=LEFT)
        
        self.f3=Frame(toplevel)
        self.f3.pack(side=LEFT)
        
        self.f4=Frame(toplevel)
        self.f4.pack(side=LEFT)
        
        self.f5=Frame(toplevel)
        self.f5.pack(side=LEFT)
        
        self.f6=Frame(toplevel)
        self.f6.pack()

        Label(self.f1, text='CALCULATOR',
              font=('Verdana', 20, 'bold')).pack()

        #Botões +, 1, 4, 7 e ,.
        self.b_plus = Button(self.f2, text='+', font=('Verdana', 10, 'bold'),
                        fg='red', height=button_height, width=button_width)
        self.b_plus.bind('<Button-1>', self.plus)
        self.b_plus.pack(padx=button_pad, pady=button_pad)
        
        self.b1 = Button(self.f2, text='1', height=number_hw, width=number_hw)
        self.b1.bind('<Button-1>', self.n1)
        self.b1.pack(padx=number_padx, pady=number_pady)
        
        self.b4 = Button(self.f2, text='4', height=number_hw, width=number_hw)
        self.b4.bind('<Button-1>', self.n4)
        self.b4.pack(padx=number_padx, pady=number_pady)
        
        self.b7 = Button(self.f2, text='7', height=number_hw, width=number_hw)
        self.b7.bind('<Button-1>', self.n7)
        self.b7.pack(padx=number_padx, pady=number_pady)
        
        self.b_comma = Button(self.f2, text=',', height=number_hw, width=number_hw)
        self.b_comma.bind('<Button-1>', self.comma)
        self.b_comma.pack(padx=number_padx, pady=number_pady)

        #Botões -,2, 5 e 8.
        self.b_minus = Button(self.f3, text='-', font=('Verdana', 10, 'bold'),
                        fg='red', height=button_height, width=button_width)
        self.b_minus.bind('<Button-1>', self.minus)
        self.b_minus.pack(padx=button_pad, pady=button_pad)

        self.b2 = Button(self.f3, text='2', height=number_hw, width=number_hw)
        self.b2.bind('<Button-1>', self.n2)
        self.b2.pack(padx=number_padx, pady=number_pady)
        
        self.b5 = Button(self.f3, text='5', height=number_hw, width=number_hw)
        self.b5.bind('<Button-1>', self.n5)
        self.b5.pack(padx=number_padx, pady=number_pady)
        
        self.b8 = Button(self.f3, text='8', height=number_hw, width=number_hw)
        self.b8.bind('<Button-1>', self.n8)
        self.b8.pack(padx=number_padx, pady=number_pady)
        
        self.b0 = Button(self.f3, text='0', height=number_hw, width=number_hw)
        self.b0.bind('<Button-1>', self.n0)
        self.b0.pack(padx=number_padx, pady=number_pady)

        #Botões X, 3, 6, 9 e =.
        self.b_multiplying = Button(self.f4, text='x', font=('Verdana', 10, 'bold'),
                        fg='purple', height=button_height, width=button_width)
        self.b_multiplying.bind('<Button-1>', self.mult)
        self.b_multiplying.pack(padx=button_pad, pady=button_pad)

        self.b3 = Button(self.f4, text='3', height=number_hw, width=number_hw)
        self.b3.bind('<Button-1>', self.n3)
        self.b3.pack(padx=number_padx, pady=number_pady)
        
        self.b6 = Button(self.f4, text='6', height=number_hw, width=number_hw)
        self.b6.bind('<Button-1>', self.n6)
        self.b6.pack(padx=number_padx, pady=number_pady)
        
        self.b9 = Button(self.f4, text='9', height=number_hw, width=number_hw)
        self.b9.bind('<Button-1>', self.n9)
        self.b9.pack(padx=number_padx, pady=number_pady)
        
        self.b_equals = Button(self.f4, text='=', height=number_hw,
                               width=number_hw)
        self.b_equals.bind('<Button-1>', self.equals)
        self.b_equals.pack(padx=number_padx, pady=number_pady)

        #Botões /, C, Back, Off, Credits
        self.b_division = Button(self.f5, text='/', font=('Verdana', 10, 'bold'),
                        fg='purple', height=button_height, width=button_width)
        self.b_division.bind('<Button-1>', self.divi)
        self.b_division.pack(padx=button_pad, pady=button_pad)

        self.b_C = Button(self.f5, text='C', font=('Verdana', 10, 'bold'),
                        fg='blue', height=button_height, width=button_width)
        self.b_C.bind('<Button-1>', self.erase)
        self.b_C.pack(padx=button_pad, pady=button_pad)

        self.b_back = Button(self.f5, text='Back', font=('Verdana', 10, 'bold'),
                        fg='blue', height=button_height, width=button_width)
        self.b_back.bind('<Button-1>', self.back)
        self.b_back.pack(padx=button_pad, pady=button_pad)
        
        self.b_off = Button(self.f5, text='Off', font=('Verdana', 10, 'bold'),
                        fg='red', height=button_height, width=button_width)
        self.b_off.bind('<Button-1>', self.off)
        self.b_off.pack(padx=button_pad, pady=button_pad)

        self.b_credits = Button(self.f5, text='Credits', font=('Verdana', 10, 'bold'),
                        fg='yellow', height=button_height +3,
                                width=button_width +1)
        self.b_credits.bind('<Button-1>', self.txt_credits)
        self.b_credits.pack(padx=button_pad -2, pady=button_pad + 2)

        # Funções da calculadora

    def n1(self, event):
        self.values += '1'
        self.canvas1.delete('numeros')
        self.canvas1.create_text(20,50, text=(self.values), anchor=W,
                font=('Verdana', 16, 'bold'), fill='black',
                width=190, tag='numeros')

    def n2(self, event):
        self.values += '2'
        self.canvas1.delete('numeros')
        self.canvas1.create_text(20,50, text=(self.values), anchor=W,
                font=('Verdana', 16, 'bold'), fill='black',
                width=190, tag='numeros')

    def n3(self, event):
        self.values += '3'
        self.canvas1.delete('numeros')
        self.canvas1.create_text(20,50, text=(self.values), anchor=W,
                font=('Verdana', 16, 'bold'), fill='black',
                width=190, tag='numeros')

    def n4(self, event):
        self.values += '4'
        self.canvas1.delete('numeros')
        self.canvas1.create_text(20,50, text=(self.values), anchor=W,
                font=('Verdana', 16, 'bold'), fill='black',
                width=190, tag='numeros')

    def n5(self, event):
        self.values += '5'
        self.canvas1.delete('numeros')
        self.canvas1.create_text(20,50, text=(self.values), anchor=W,
                font=('Verdana', 16, 'bold'), fill='black',
                width=190, tag='numeros')

    def n6(self, event):
        self.values += '6'
        self.canvas1.delete('numeros')
        self.canvas1.create_text(20,50, text=(self.values), anchor=W,
                font=('Verdana', 16, 'bold'), fill='black',
                width=190, tag='numeros')

    def n7(self, event):
        self.values += '7'
        self.canvas1.delete('numeros')
        self.canvas1.create_text(20,50, text=(self.values), anchor=W,
                font=('Verdana', 16, 'bold'), fill='black',
                width=190, tag='numeros')

    def n8(self, event):
        self.values += '8'
        self.canvas1.delete('numeros')
        self.canvas1.create_text(20,50, text=(self.values), anchor=W,
                font=('Verdana', 16, 'bold'), fill='black',
                width=190, tag='numeros')

    def n9(self, event):
        self.values += '9'
        self.canvas1.delete('numeros')
        self.canvas1.create_text(20,50, text=(self.values), anchor=W,
                font=('Verdana', 16, 'bold'), fill='black',
                width=190, tag='numeros')

    def n0(self, event):
        self.values += '0'
        self.canvas1.delete('numeros')
        self.canvas1.create_text(20,50, text=(self.values), anchor=W,
                font=('Verdana', 16, 'bold'), fill='black',
                width=190, tag='numeros')

    def back(self, event):
        self.canvas1.delete('numeros')
        self.values = self.values[:-1]
        self.canvas1.create_text(20,50, text=(self.values), anchor=W,
                font=('Verdana', 16, 'bold'), fill='black',
                width=190, tag='numeros')

    def plus(self, event):
        self.values += ' + '
        self.canvas1.delete('numeros')
        self.canvas1.create_text(20,50, text=(self.values), anchor=W,
                font=('Verdana', 16, 'bold'), fill='black',
                width=190, tag='numeros')

    def mult(self, event):
        self.values += ' * '
        self.canvas1.delete('numeros')
        self.canvas1.create_text(20,50, text=(self.values), anchor=W,
                font=('Verdana', 16, 'bold'), fill='black',
                width=190, tag='numeros')

    def minus(self, event):
        self.values += ' - '
        self.canvas1.delete('numeros')
        self.canvas1.create_text(20,50, text=(self.values), anchor=W,
                font=('Verdana', 16, 'bold'), fill='black',
                width=190, tag='numeros')

    def divi(self, event):
        self.values += ' / '
        self.canvas1.delete('numeros')
        self.canvas1.create_text(20,50, text=(self.values), anchor=W,
                font=('Verdana', 16, 'bold'), fill='black',
                width=190, tag='numeros')

    def equals(self, event):
        self.canvas1.delete('numeros')
        try:
            self.values = '%.2f' %eval(self.values)
            self.canvas1.create_text(20,50, text=self.values, anchor=W,
                    font=('Verdana', 16, 'bold'), fill='blue',
                    width=190, tag='numeros')
            self.values = str(self.values)
        except:
            self.canvas1.create_text(20,50, text='ERROR! Division by zero.', anchor=W,
                    font=('Verdana', 16, 'bold'), fill='blue',
                    width=190, tag='numeros')
            self.values = ''

    def comma(self, event):
        self.values += '.'
        self.canvas1.create_text(20,50, text=(self.values), anchor=W,
                font=('Verdana', 16, 'bold'), fill='black',
                width=190, tag='numeros')

    def erase(self, event):
        self.canvas1.delete('numeros')
        self.values = ''
        self.canvas1.create_text(20,50, text='0', anchor=W,
                font=('Verdana', 16, 'bold'), fill='blue',
                width=190, tag='numeros')
        self.values = ''

    def off(self, event):
        self.window.destroy()

    def txt_credits(self, event):
        self.canvas1.delete('numeros')
        credit = '''THANKS FOR ALL PEOPLE THAT WROTE THE BOOKS THAT
MAKE IT'S POSSIBLE!
                '''
        self.canvas1.create_text(20,50, text= credit, anchor=W,
                font=('Verdana', 10, 'bold'), fill='purple',
                width=190, tag='numeros')

root=Tk()
Cauculator(root)
root.mainloop()
