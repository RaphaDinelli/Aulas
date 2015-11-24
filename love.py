from tkinter import *
import pygame.mixer as sounds
import time



class Player:
    def __init__(self, master):
        self.master = master
        self.master.config(bg='pink')
        self.master.title('Uma linda historia de amor!')
        self.master.geometry('1350x700+0+0')
        self.count = 0
        self.running = True

        # The pictures that will appear
        self.pictures = ['foto1.png','foto2.png','foto3.png','foto4.png',
                'foto5.png','foto6.png','foto7.png']
        # Some clichés phrases
        self.titles = ['Amor da minha vida', 'Minha princesa linda',
                     'Nao vivo sem você','Eternamente apaixonado',
                     'Penso em você a todo instante','Você acende meu desejo',
                     'Te amo para sempre!']
        # A love song 
        self.file = '244 - WHITESNAKE - IS THIS LOVE.mp3'

        self.label_title = Label(master, text = 'Title of page',
                    bg = '#87CEFA', fg = '#8B7D7B', font=('Verdana', 20, 'bold'),
                                 relief=SUNKEN, width=50)
        self.label_title.place(x=190, y=20)

        # A Romantic text chosen by the autor
        self.love_text = Text(master,bg='#87CEFA', height=400, width=100
                ,fg='#8B7D7B', font=('Vladimir Script', 20, 'normal'))
        r = open('frases_de_amor.txt')
        for line in r.readlines():
            self.love_text.insert(END, line)
        self.love_text.config(state=DISABLED)
        self.love_text.place(x=850, y=100)
        r.close()

        self.button_start = Button(master,text='START',command=self.create_img,
                bd=10,bg='white', font=('arial',13, 'bold'),anchor=W)
        self.button_start.bind('<Button-1>', self.music_start)
        self.button_start.place(x=610, y=200)

        self.button_stop = Button(master, text='STOP',
                bd=10, bg='red', font=('arial',13, 'bold'), anchor=W)
        self.button_stop.bind('<Button-1>', self.music_stop)
        self.button_stop.place(x=615, y=280)


    def create_img(self):
        try:
            self.toplevel.destroy()
            self.img = PhotoImage(file=self.pictures[self.count])
            self.toplevel = Toplevel()
            self.toplevel.title(self.titles[self.count])
            self.toplevel.configure(bg='#8B7D7B')
            self.toplevel.geometry('550x650+%s+%s'%(self.count*50, self.count*25))
            self.canvas = Canvas(self.toplevel, width=500, height=600,bg='red',
                                 relief=SUNKEN, bd=20)    
            self.canvas.create_image(20,20, anchor=NW, image=self.img)
            self.canvas.pack(side=LEFT)
            self.toplevel.transient(root)
            self.toplevel.focus_force()
            #self.toplevel.grab_set()
            if self.count > 5:
                self.count = 0
                root.after(4250, self.create_img)
            else:
                if self.running:
                    self.count += 1
                    root.after(4250, self.create_img)

        except:
            self.img = PhotoImage(file=self.pictures[self.count])
            self.toplevel = Toplevel()
            self.toplevel.title(self.titles[self.count])
            self.toplevel.configure(bg='#8B7D7B')
            self.toplevel.geometry('550x650+%s+%s'%(self.count*50, self.count*25))
            self.canvas = Canvas(self.toplevel, width=500, height=600,bg='red',
                                 relief=SUNKEN, bd=20)    
            self.canvas.create_image(20,20, anchor=NW, image=self.img)
            self.canvas.pack(side=LEFT)
            self.toplevel.transient(root)
            self.toplevel.focus_force()
            #self.toplevel.grab_set()
            if self.count > 5:
                self.count = 0
                root.after(4250, self.create_img)
            else:
                if self.running:
                    self.count += 1
                    root.after(4250, self.create_img)

    def music_start(self, event):
        self.running = True
        sounds.init()
        sounds.music.load(self.file)
        sounds.music.play()

    def music_stop(self, event):
        sounds.music.stop()
        self.running = False


root = Tk()
Player(root)
mainloop()
