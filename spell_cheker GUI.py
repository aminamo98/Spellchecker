

# ----------------------------------------------------------

from tkinter import *
from tkinter.ttk import Combobox,Progressbar,Style
from tkinter import messagebox, scrolledtext
from functools import partial
import time

# --------------------------------------------------------------------------------------------------------------------------

class Words: #class for spell checker

    def __init__ (self,word):
        self.user_word = word
        self.list = set()
        self.dictionary = set()

    def add_dictionary(self):
        dummy = []
        with open("C:\\Users\Lenovo\Desktop\spellchecker\DICTIONARY.txt", "r") as database:
            for i in database:
                dummy += [i.strip()]
        
        for i in dummy:
            self.dictionary.add(i)

    def check_word(self):
        check = True
        char = "[ @ _ ! # $ % ^ & * ( ) < > ? / \ | } { ~ : ] ' . , -"
        for i in self.user_word: #limit user input to word only (no numbers & special char)
            if i.isdigit() or i in char.split():
                check = False
        return check

    def check_exist(self): 
        if self.user_word in self.dictionary:
            return True
        else:
            return False

    def extra_char(self):
        error = True
        extra= Label(bottom_frame, text= "Extra character:", font=("Arial Bold", 10), fg='salmon1', bg='gray9')
        extra.grid(column=0, row=2, padx=10, pady=5, sticky=N)
        l=40
        for i in range(len(self.user_word)):
            removed_a_letter = self.user_word[:i] + self.user_word[i+1:]
            if removed_a_letter in self.dictionary and removed_a_letter not in self.list:
                self.list.add(removed_a_letter)
                item = Label(bottom_frame, text= removed_a_letter, font=("Arial Italic", 10), fg='salmon1', bg='gray9')
                item.grid(column=0, row=2, padx=10, pady=l, sticky=N)
                l+=20
                error = False

        if error:
            item = Label(bottom_frame, text= "NONE", font=("Arial Italic", 10), fg='salmon1', bg='gray9')
            item.grid(column=0, row=2, padx=10, pady=40, sticky=N)     		
           
                    
    def wrong_char(self):
        error = True
        wrong = Label(bottom_frame, text= "Wrong character:", font=("Arial Bold", 10), fg='goldenrod1', bg='gray9')
        wrong.grid(column=1, row=2, padx=10, pady=5, sticky=N)        
        l=40
        for i in range(97,123):
            for j in range(len(self.user_word)):
                replaced_char = self.user_word[:j] + chr(i) + self.user_word[j+1:]
                if replaced_char != self.user_word and replaced_char in self.dictionary and replaced_char not in self.list:
                    self.list.add(replaced_char)
                    item = Label(bottom_frame, text= replaced_char, font=("Arial Italic", 10), fg='goldenrod1', bg='gray9')
                    item.grid(column=1, row=2, padx=10, pady=l, sticky=N)
                    l+=20
                    error = False
        if error:
            item = Label(bottom_frame, text= "NONE", font=("Arial Italic", 10), fg='goldenrod1', bg='gray9')
            item.grid(column=1, row=2, padx=10, pady=40, sticky=N)    		

    def missing_char(self):
        error = True
        missing = Label(bottom_frame, text= "Missing character:", font=("Arial Bold", 10), fg='seagreen1', bg='gray9')
        missing.grid(column=2, row=2, padx=10, pady=5, sticky=N)
        l = 40
        for i in range(97,123):
            for j in range(len(self.user_word)+1):
                added_char = self.user_word[:j] + chr(i) + self.user_word[j:]
                if added_char != self.user_word and added_char in self.dictionary and added_char not in self.list:
                    self.list.add(added_char)
                    item = Label(bottom_frame, text= added_char, font=("Arial Italic", 10), fg='seagreen1', bg='gray9')
                    item.grid(column=2, row=2, padx=10, pady=l, sticky=N)
                    l+=20
                    error = False
        if error:
            item = Label(bottom_frame, text= "NONE", font=("Arial Italic", 10), fg='seagreen1', bg='gray9')
            item.grid(column=2, row=2, padx=10, pady=40, sticky=N)   		

    def shuffled_char(self):
        error = True
        shuffled = Label(bottom_frame, text= "Shuffled character:", font=("Arial Bold", 10), fg='cadetblue1', bg='gray9')
        shuffled.grid(column=3, row=2, padx=10, pady=5, sticky=N)
        l = 40
        for i in range(0, len(self.user_word)-1):
            swapped_char = self.user_word[:i] + ''.join(self.user_word[i:i+2][::-1]) + self.user_word[i+2:len(self.user_word)+1]
            if swapped_char != self.user_word and swapped_char in self.dictionary and swapped_char not in self.list:
                self.list.add(swapped_char)
                item = Label(bottom_frame, text= swapped_char, font=("Arial Italic", 10), fg='cadetblue1', bg='gray9')
                item.grid(column=3, row=2, padx=10, pady=l, sticky=N)
                l +=20
                error = False
        if error:
            item = Label(bottom_frame, text= "NONE", font=("Arial Italic", 10), fg='cadetblue1', bg='gray9')
            item.grid(column=3, row=2, padx=5, pady=40, sticky=N)    		


    def extra_missing_char(self):
        error = True
        extra_miss = Label(bottom_frame, text= "Extra and missing character:", font=("Arial Bold", 10), fg='orchid1', bg='gray9')
        extra_miss.grid(column=4, row=2, padx=10, pady=5, sticky=N)
        l = 40
        for i in range(len(self.user_word)):
            remove_char = self.user_word[:i] + self.user_word[i+1:]
            for j in range(97,123):
                for k in range(len(remove_char)+1):
                    add_char = remove_char[:k] + chr(j) + remove_char[k:]
                    if add_char != self.user_word and add_char in self.dictionary and add_char not in self.list:
                        self.list.add(add_char)
                        item = Label(bottom_frame, text= add_char, font=("Arial Italic", 10), fg='orchid1', bg='gray9')
                        item.grid(column=4, row=2, padx=10, pady=l, sticky=N)
                        l +=20
                        error = False
        if error:
            item = Label(bottom_frame, text= "NONE", font=("Arial Italic", 10), fg='orchid1', bg='gray9')
            item.grid(column=4, row=2, padx=5, pady=40, sticky=N)    	   		

# ----------------------------------------------------------------------------------------------------------------------

#LAYOUT

gui = Tk()
gui.geometry ('1024x720')
gui.config(bg='black')
# gui.attributes('-fullscreen', True)
gui.grid_rowconfigure(0, weight=1)
gui.grid_rowconfigure(1, weight=1)
gui.grid_rowconfigure(2, weight=1)
gui.grid_rowconfigure(3, weight=1)
gui.grid_columnconfigure(0, weight=1)
gui.title ("SPELL CHECKER PROGRAM")

canvas = Canvas(gui)
canvas.grid(column=0,row=0, sticky=NSEW)
canvas.grid_rowconfigure(0,weight=1)
canvas.grid_columnconfigure(0,weight=1)

scroll= Scrollbar(gui, orient=VERTICAL, command=canvas.yview)
scroll.grid(row=0, column=1, sticky=NS)
canvas.configure(yscrollcommand=scroll.set, scrollregion=canvas.bbox(ALL))

def menu():
    global menu_frame
    menu_frame = Frame(gui, bg="aquamarine4")
    menu_frame.grid(column=0, row=0, sticky=NSEW)
    menu_frame.grid_columnconfigure(0, weight=1)
    menu_frame.grid_rowconfigure(0, weight=1)

    label = Label(menu_frame, text= "\nSPELL CHECKER\nPROGRAM\n", font=("Arial Bold Italic", 35), fg='yellow2', bg='aquamarine4')
    label.grid(column=0, row=0, pady=10, sticky=N)
    label2 = Label(menu_frame, text= "This program offers spell checking of the word input by user.\nIt predicts the correct word that user entered\nand provides suggestions based on the database", font=("Arial Italic", 11), fg='lightgoldenrod', bg='aquamarine4')
    label2.grid(column=0, row=0, pady=250, sticky=N)

    start_btn = Button(menu_frame, text='START', bg='deepskyblue', fg='white', font=("Arial Bold",15), command=partial(click,1), height=1, width=10)
    start_btn.grid(column=0, row=0, padx=10, pady=220, sticky=S)
    start_btn.config (activebackground='lightsalmon', relief=RIDGE)

    exit_btn = Button(menu_frame, text='EXIT', bg='red3', command= partial(close,0), font=("Arial Bold",11), fg='white', width=8)
    exit_btn.grid(column=0, row=0, padx=10, pady=170, sticky=S)
    exit_btn.config (activebackground='lightsalmon', relief=RIDGE)


def top():
    global top_frame
    top_frame = Frame(canvas, bg="gray6")
    top_frame.grid(column=0, row=0, sticky=NSEW)
    top_frame.grid_columnconfigure(0, weight=1)
    top_frame.grid_rowconfigure(0, weight=1)

def mid():    
    global mid_frame
    mid_frame = Frame(canvas, bg="darkslategray")
    mid_frame.grid(column=0, row=1, sticky=NSEW)
    mid_frame.grid_columnconfigure(0, weight=1)
    mid_frame.grid_rowconfigure(0, weight=1)

def bottom():
    global bottom_frame
    bottom_frame = Frame(canvas, bg="gray9")
    bottom_frame.grid(column=0, row=2, sticky=NSEW)
    bottom_frame.grid_rowconfigure(0, weight=1)
    bottom_frame.grid_columnconfigure(0, weight=1)
    bottom_frame.grid_columnconfigure(1, weight=1)
    bottom_frame.grid_columnconfigure(2, weight=1)
    bottom_frame.grid_columnconfigure(3, weight=1)
    bottom_frame.grid_columnconfigure(4, weight=1)
    bottom_frame.grid_columnconfigure(5, weight=1)

# ------------------------------------------------------------------------------------------------------------------------------------

#WIDGET

def progressbar():
    style = Style()
    style.theme_use('default')
    style.configure("black.Horizontal.TProgressbar", background='red4')
    bar = Progressbar(top_frame, length=500, mode='determinate', style='black.Horizontal.TProgressbar')
    bar.grid(column=0, row=0, padx=10, pady=80, sticky=S)
    bar ['maximum'] = 100
    currentValue = 0
    for i in range(10):
        currentValue += 10
        time.sleep(0.06)
        bar ['value'] = currentValue
        bar.update() 
    if currentValue == 100:
        bar.grid_forget()

def click(val):
    
    if val == 1:
        menu_frame.grid_forget()
        top()
        mid()
        bottom()
        spell_check()
    
    elif val == 2:
        clear_frame()
        word = input_word.get()
        if word:
            spellCheck = Words(word.lower())

            if spellCheck.check_word():
                spellCheck.add_dictionary()
                if spellCheck.check_exist():
                    messagebox.showinfo('CORRECT!',"Congrats! The word '" + word.upper() + "' is spelled correctly")

                else:
                    suggestion = []
                    messagebox.showwarning ('WRONG!',"Oops! The word entered might be wrong")
                    spellCheck.extra_char()
                    spellCheck.wrong_char()
                    spellCheck.missing_char()
                    spellCheck.shuffled_char()
                    spellCheck.extra_missing_char()

                    if spellCheck.list:
                        
                        suggest = Label(bottom_frame, text= "Correct work suggestion:", font=("Arial Bold", 10), fg='lawngreen', bg='gray9')
                        suggest.grid(column=5, row=2, padx=10, pady=5, sticky=N)
                    
                        for i in spellCheck.list:
                            suggestion += [i]
                                
                        choose = Label(bottom_frame, text= 'Please choose the desired word from the list below', font =("Arial", 10), bg='gray9', fg='olivedrab1')
                        choose.grid(column=5, row=2, padx=10, pady=40, sticky=N)

                        global combo
                        combo = Combobox(bottom_frame, values = suggestion, width=23, font=("Arial",12))
                        combo.current (0)
                        combo.grid(column=5, row=2, pady=80, sticky=N)
                        combo.config(justify='center')

                        enter = Button(bottom_frame, text='I CHOOSE THIS WORD', command= partial(click,3), font=("Arial Bold",10), bg='mediumpurple4', fg='azure')
                        enter.grid(column=5, row=2, padx=10, pady=120, sticky=N)
                        enter.config(activebackground='lightpink1', relief=RIDGE)

                    else:
                        messagebox.showwarning('SORRY!','No suitable word can be found in dictionary :(')
            else:
                messagebox.showerror('ERROR!','The word cannot contain any number or special character!')

        else:
            messagebox.showerror('ERROR!','There is no word to be checked')

    elif val == 3:
        correction = combo.get()
        suggest = Label(bottom_frame, text= "The correct word : " + correction.upper(), font=("Arial Bold", 11), fg='gold', bg='gray9')
        suggest.grid(column=5, row=2, padx=5, pady=170, sticky=N)

def close(event):
    if messagebox.askokcancel('EXIT','Do you want to quit the program?'):
        gui.quit()
          
def clear_frame():
    for i in bottom_frame.winfo_children():
        i.grid_forget()

def spell_check():
    
    label = Label(top_frame, text= "\nSPELL CHECKER\nPROGRAM\n", font=("Arial Bold Italic", 25), fg='gold', bg='gray6')
    label.grid(column=0, row=0, pady=10)
    exit_btn = Button(top_frame, text='EXIT', bg='red3', command= partial(close,0), font=("Arial Bold",11), fg='white', width=8)
    exit_btn.grid(column=0, row=0, padx=10, pady=10, sticky=NE)
    exit_btn.config (activebackground='lightsalmon', relief=RIDGE)

    progressbar()
    global input_word
    prompt_user = Label(mid_frame, text='Enter the word: ', font=("Arial Bold Italic",11), fg='white', bg='darkslategray')
    prompt_user.grid(column=0, row=0, padx=10, pady=5, sticky=N)
    input_word = Entry(mid_frame, width=30)
    input_word.grid(column=0, row=0, padx=10, pady=40, sticky=N)
    enter = Button(mid_frame, text='ENTER', command= partial(click,2), font=("Arial Bold",10), bg='firebrick2', fg='white')
    enter.grid(column=0, row=0, padx=10, pady=70, sticky=N)
    enter.config (activebackground='goldenrod1', relief=RIDGE)
              

# ------------------------------------------------------------------------------------------------------------------------------------

gui.bind('<Escape>', close)
menu()
gui.mainloop()

