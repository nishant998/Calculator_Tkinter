from tkinter import *
from PIL import Image , ImageTk



class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry('700x800')
        self.title("Calculator")
        self.wm_iconbitmap('calc1_43473.ico')
    def back_img(self):
        self.back_img = ImageTk.PhotoImage(Image.open("calculator_background.jpg"))
        self.back_img_lab = Label(self, image=self.back_img)
        self.back_img_lab.place(x=0, y=0, relwidth=1, relheight=1)

        self.entry_value = StringVar()
        self.result_entry = Entry(self, textvariable=self.entry_value, font=('Helvetica', 35))
        self.result_entry.pack(side=TOP, anchor='sw' , fill = X)


    def result_display_screen(self , event):
        self.textx = event.widget.cget('text')
        print(self.textx)
        if self.textx == '=':
            self.res_str = self.entry_value.get()
            self.res_str.replace('=' , '')
            print(self.res_str)
            no_dict1 = self.res_str.split('+')
            no_dict2 = self.res_str.split('X')
            no_dict3 = self.res_str.split('%')
            no_dict4 = self.res_str.split('-')

            self.result = StringVar()

            if(self.res_str.find('+') > 0):
                self.result.set((int(no_dict1[0]))+ (int(no_dict1[1])))
                print(self.result.get())

            if (self.res_str.find('-') > 0):
                self.result.set((int(no_dict4[0])) - (int(no_dict4[1])))
                print(self.result.get())

            if (self.res_str.find('X') > 0):
                self.result.set((int(no_dict2[0])) * (int(no_dict2[1])))
                print(self.result.get())

            if (self.res_str.find('%') > 0):
                self.result.set((int(no_dict3[0])) % (int(no_dict3[1])))
                print(self.result.get())

            self.entry_value.set(self.result.get())


        elif self.textx == 'AC':
            self.entry_value.set('')
        else :
            self.entry_value.set(self.entry_value.get() + self.textx)



    def number_attribute(self):

        self.main_frame = Frame(self , bg = 'grey', borderwidth=5, relief=GROOVE, width=700, height=320)
        self.main_frame.pack(side = BOTTOM , fill=BOTH, expand=False)


#left frame attributes here
        self.left_frame = Frame(self.main_frame, bg='grey', borderwidth=5, relief=GROOVE, width=580, height=320)
        self.left_frame.pack(side=LEFT, fill=BOTH, expand=True)


        self.left_frame_789 = Frame(self.left_frame, bg='grey', borderwidth=0, relief=GROOVE, width=580, height=80)
        self.left_frame_789.pack(side=TOP, anchor = 'n' , fill=X, expand=True)

        self.no = Button(self.left_frame_789, text="7" ,font=('Helvetica', 24), bg='grey', borderwidth=0,activebackground='#AAAEB1', width = 5 , cursor="hand2" )
        self.no.pack(side = LEFT , anchor = 'nw' , expand = True)
        self.no.bind('<Button-1>', self.result_display_screen)

        self.no = Button(self.left_frame_789, text="8" ,  font=('Helvetica', 24), bg='grey', borderwidth=0,activebackground='#AAAEB1', width=5 , cursor="hand2")
        self.no.pack(side = LEFT, anchor = 'nw' , expand = True)
        self.no.bind('<Button-1>', self.result_display_screen)

        self.no = Button(self.left_frame_789, text="9" ,  font=('Helvetica', 24), bg='grey', borderwidth=0,activebackground='#AAAEB1', width=5 , cursor="hand2")
        self.no.pack(side = LEFT, anchor = 'nw' , expand = True)
        self.no.bind('<Button-1>',self.result_display_screen)

        self.left_frame_456 = Frame(self.left_frame, bg='grey', borderwidth=0, relief=GROOVE, width=580, height=80)
        self.left_frame_456.pack(side=TOP, anchor = 'n' , fill=X, expand=True)

        self.no = Button(self.left_frame_456, text="4",  font=('Helvetica', 24), bg='grey', borderwidth=0,cursor="hand2" ,
                           activebackground='#AAAEB1', width=5)
        self.no.pack(side=LEFT, anchor='nw' , expand = True)
        self.no.bind('<Button-1>',self.result_display_screen)

        self.no = Button(self.left_frame_456, text="5",  font=('Helvetica', 24), bg='grey', cursor="hand2", borderwidth=0,
                           activebackground='#AAAEB1', width=5)
        self.no.pack(side=LEFT, anchor='nw' , expand = True)
        self.no.bind('<Button-1>',self.result_display_screen)

        self.no = Button(self.left_frame_456, text="6",  font=('Helvetica', 24), bg='grey', cursor="hand2", borderwidth=0,
                           activebackground='#AAAEB1', width=5)
        self.no.pack(side=LEFT, anchor='nw' , expand = True)
        self.no.bind('<Button-1>',self.result_display_screen)

        self.left_frame_123 = Frame(self.left_frame, bg='grey', borderwidth=0, relief=GROOVE, width=580, height=80)
        self.left_frame_123.pack(side=TOP, anchor='n', fill=X, expand=True)

        self.no = Button(self.left_frame_123, text="1",  font=('Helvetica', 24), bg='grey', cursor="hand2", borderwidth=0,
                           activebackground='#AAAEB1', width=5)
        self.no.pack(side=LEFT, anchor='nw', expand=True)
        self.no.bind('<Button-1>', self.result_display_screen)

        self.no = Button(self.left_frame_123, text="2",  font=('Helvetica', 24), bg='grey', cursor="hand2", borderwidth=0,
                           activebackground='#AAAEB1', width=5)
        self.no.pack(side=LEFT, anchor='nw', expand=True)
        self.no.bind('<Button-1>',self.result_display_screen)

        self.no = Button(self.left_frame_123, text="3",  font=('Helvetica', 24), bg='grey', cursor="hand2", borderwidth=0,
                           activebackground='#AAAEB1', width=5)
        self.no.pack(side=LEFT, anchor='nw', expand=True)
        self.no.bind('<Button-1>',self.result_display_screen)

        self.left_frame_dot0eq = Frame(self.left_frame, bg='grey', borderwidth=0, relief=GROOVE, width=580, height=80)
        self.left_frame_dot0eq.pack(side=TOP, anchor='n', fill=X, expand=True)

        self.no = Button(self.left_frame_dot0eq, text=".",  font=('Helvetica', 24), bg='grey', cursor="hand2", borderwidth=0,
                           activebackground='#AAAEB1', width=5)
        self.no.pack(side=LEFT, anchor='nw', expand=True)
        self.no.bind('<Button-1>', self.result_display_screen)

        self.no = Button(self.left_frame_dot0eq, text="0",  font=('Helvetica', 24), bg='grey', cursor="hand2", borderwidth=0,
                           activebackground='#AAAEB1', width=5)
        self.no.pack(side=LEFT, anchor='nw', expand=True)
        self.no.bind('<Button-1>', self.result_display_screen)

        self.no = Button(self.left_frame_dot0eq, text="=",  font=('Helvetica', 24), bg='grey', cursor="hand2", borderwidth=0,
                           activebackground='#AAAEB1', width=5)
        self.no.pack(side=LEFT, anchor='nw', expand=True)

        self.no.bind('<Button-1>' , self.result_display_screen)




#right frame attribute from here =
        self.right_frame = Frame(self.main_frame, bg='grey', borderwidth=5, relief=GROOVE, width=120, height=320)
        self.right_frame.pack(side=RIGHT, fill=BOTH, expand=True)

        self.no= Button(self.right_frame, text="AC", font=('Helvetica', 24), bg='grey' , cursor="hand2",borderwidth = 0 ,activebackground = '#AAAEB1')
        self.no.pack(side = TOP , fill = X)
        self.no.bind('<Button-1>', self.result_display_screen)

        self.no = Button(self.right_frame, text="%", font=('Helvetica', 24), bg='grey' , cursor="hand2",borderwidth = 0 ,activebackground = '#AAAEB1')
        self.no.pack(side=TOP, fill=X)
        self.no.bind('<Button-1>', self.result_display_screen)

        self.no = Button(self.right_frame, text="X", font=('Helvetica', 24), bg='grey' , cursor="hand2",borderwidth = 0 ,activebackground = '#AAAEB1')
        self.no.pack(side=TOP, fill=X)
        self.no.bind('<Button-1>', self.result_display_screen)

        self.no = Button(self.right_frame, text="-", font=('Helvetica', 24), bg='grey' , cursor="hand2",borderwidth = 0 ,activebackground = '#AAAEB1')
        self.no.pack(side=TOP, fill=X)
        self.no.bind('<Button-1>', self.result_display_screen)

        self.no = Button(self.right_frame, text="+", font=('Helvetica', 24), bg='grey', cursor="hand2",borderwidth = 0 ,activebackground = '#AAAEB1')
        self.no.pack(side=TOP, fill=X)
        self.no.bind('<Button-1>', self.result_display_screen)


    
if __name__ == '__main__':
    window = GUI()
    window.back_img()
    window.number_attribute()
    window.mainloop()

