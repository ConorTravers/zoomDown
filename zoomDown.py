import tkinter as tk

class Overview:
    def __init__(self, master):
        self.master = master
        #self.geometry("300x300")
        master.title("Main window")
        fnt = ("Arial",16)
        self.letters_bool = tk.IntVar()
        self.numbers_bool = tk.IntVar()
        self.conundrum_bool = tk.IntVar()
        self.label_letters = tk.Label(text="Letters",font=fnt)
        self.label_numbers = tk.Label(text="Numbers",font=fnt)
        self.label_letters.grid(row=0,column=0)
        self.label_numbers.grid(row=1,column=0)
        self.target = tk.Label(text="Target",font=fnt)
        self.p1_score = tk.Label(text="P1 score",font=fnt)
        self.p2_score = tk.Label(text="P2 score",font=fnt)
        self.conundrum_label = tk.Label(text="Scramble",font=fnt)
        self.conundrum_label.grid(row=4,column=0)
        self.conundrum_reveal = tk.Button(text="Reveal",command=self.reveal_conundrum)
        self.conundrum_reveal.grid(row=4,column=4)
        self.target.grid(row=2,column=0)
        self.p1_score.grid(row=3,column=0)
        self.p2_score.grid(row=3,column=2)
        self.letter_box = tk.Entry(font=("Arial",16),width=14)
        self.letter_box.grid(row=0,column=1)
        self.letter_box["state"] = "disabled"
        self.scramble_box = tk.Entry(font=("Arial",16),width=14)
        self.scramble_box.grid(row=4,column=1)
        self.scramble_box["state"] = "disabled"
        self.letter_check = tk.Checkbutton(variable=self.letters_bool,command=self.letters_check_handler).place(rely=0.02,relx=0.6)
        self.number_check = tk.Checkbutton(variable=self.numbers_bool,command=self.numbers_check_handler).place(rely=0.25,relx = 0.6)
        self.conundrum_check = tk.Checkbutton(variable=self.conundrum_bool,command=self.conundrum_check_handler).place(rely=0.5,relx=0.6)
        selection = ""
        #self.letters_output()
        self.numbers_input()
        self.letter_box.bind("<KeyRelease>",self.letters_press)

    def letters_check_handler(self):
        #print(self.letters_bool.get())
        if self.letters_bool.get():
            self.letters_output()
            self.letter_box["state"] = "normal"
            self.letter_box.update()
        #else:
        #    self.letters_box["state"] = "disabled"
    def numbers_check_handler(self):
        if self.numbers_bool.get():
            self.numbers_output()
            for i in range(6):
                self.nums_entry[i]["state"] = "normal"
            self.target_entry["state"] = "normal"

    def conundrum_check_handler(self):
        print("duck")
        if self.conundrum_bool.get():
            self.conundrum_output()
            self.scramble_box["state"] = "normal"

    def letters_close_handler(self):
        self.letter_box.delete("0","end")
        self.letter_box["state"] = "disabled"
        self.letters_bool.set(False)
        self.letters_window.destroy()

    def numbers_close_handler(self):
        for i in range(6):
            self.nums_entry[i].delete("0","end")
            self.nums_entry[i]["state"] = "disabled"
        self.target_entry.delete("0","end")
        self.target_entry["state"] = "disabled"
        self.numbers_bool.set(False)
        self.numbers_window.destroy()

    def conundrum_close_handler(self):
        self.scramble_box.delete("0","end")
        self.scramble_box["state"] = "disabled"
        self.conundrum_bool.set(False)
        self.conundrum_window.destroy()

    def numbers_input(self):
        self.nums_entry = []
        for i in range(6):
            self.nums_entry.append(tk.Entry(font=("Arial",15),width=3))
            self.nums_entry[i].place(rely=0.13,relx=0.22+0.08*i)
            self.nums_entry[i]["state"] = "disabled"
        self.target_entry = tk.Entry(font=("Arial",17),width=5)
        self.target_entry.place(rely=0.24,relx = 0.25)
        self.target_entry["state"] = "disabled"

    def letters_output(self):
        self.letters_window = tk.Toplevel(master=root,bg="white")
        self.letters_window.title("Letters")
        self.letters_window.geometry("1000x170+75+330")
        self.letters_window.protocol("WM_DELETE_WINDOW",self.letters_close_handler)
        self.canvas = []
        for i in range(9):
            self.canvas.append(tk.Canvas(self.letters_window, height=100, width=100, bg="green",borderwidth=2,relief="solid"))
            self.txt_id = self.canvas[i].create_text(53,50,fill="white",font=("Arial",45,"bold"),text="")
            self.canvas[i].pack(side="left")
            #self.canvas[i].place(relx=i * 0.105+0.02, rely=0.2)

    def conundrum_output(self):
        self.conundrum_window = tk.Toplevel(master=root)
        self.conundrum_window.title("Conundrum")
        self.conundrum_window.geometry("1000x170+75+330")
        self.conundrum_window.protocol("WM_DELETE_WINDOW",self.conundrum_close_handler)
        self.canvas2 = []
        for i in range(9):
            self.canvas2.append(tk.Canvas(self.conundrum_window, height=100, width=100, bg="green", borderwidth=2, relief="solid"))
            self.txt_id = self.canvas2[i].create_text(53, 50, fill="white", font=("Arial", 45, "bold"), text="")
            self.canvas2[i].pack(side="left")

    def numbers_output(self):
        #print(self.numbers_bool.get())
        self.numbers_window = tk.Toplevel(master=root)
        self.numbers_window.title("Numbers")
        self.numbers_window.geometry("780x300+400+0")
        self.numbers_window.protocol("WM_DELETE_WINDOW",self.numbers_close_handler)
        self.lblTarget = tk.Label(self.numbers_window,text="000",font=("lcd",80),borderwidth=2, relief="solid")
        self.lblTarget.place(relx=0.35, rely=0.55)
        self.canvasNums = []
        lblTarget = tk.Label(root, text="000", font=("lcd", 80), borderwidth=2, relief="solid")
        for i in range(6):
            self.canvasNums.append(tk.Canvas(self.numbers_window, height=110, width=110, bg="green",borderwidth=2, relief="solid"))
            self.txt_nums = self.canvasNums[i].create_text(55,55,font=("lcd",45,"bold"),fill="white",text="")
            self.canvasNums[i].place(relx=i * 0.15 + 0.02, rely=0.15)
        self.numbers_bindings()

    def numbers_bindings(self):
        for i in range(6):
            self.nums_entry[i].bind("<KeyRelease>",lambda ev, arg=i: self.numbers_press(arg))
        self.target_entry.bind("<KeyRelease>", lambda ev, arg=10: self.numbers_press(arg))
    def numbers_press(self,i):
        if i != 10:
            num = self.nums_entry[i].get()
            self.canvasNums[i].itemconfigure(self.txt_nums,text=num)
        else:
            num = self.target_entry.get()
            self.lblTarget.configure(text=num)

    def letters_press(self,event):
        selection = self.letter_box.get()
        selection = selection.upper()
        for i in range(len(selection)):
            self.canvas[i].itemconfigure(self.txt_id,text=selection[i])
        for j in range(len(selection),9):
            self.canvas[j].itemconfigure(self.txt_id,text="")

    def reveal_conundrum(self):
        scramble = self.scramble_box.get()
        scramble = scramble.upper()
        for i in range(len(scramble)):
            self.canvas2[i].itemconfigure(self.txt_id,text=scramble[i])


root = tk.Tk()
root.geometry("450x250+50+50")
#root.configure(bg="white")
app = Overview(root)
root.mainloop()