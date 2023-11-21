from tkinter import *

class Application(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.main()

    def main(self):
        Label(self, text = "Choose your favorite programming languages", fg = "red").grid(row = 0, column = 0, sticky = W)

        Label(self, text = "Please check the choice you want:").grid(row = 2, column = 0, sticky = W)

        #C++
        self.cplusplus = BooleanVar()
        Checkbutton(self, text = "C++", variable = self.cplusplus, command = self.insert_text).grid(row = 3, column = 0, sticky = W)

        #C
        self.c = BooleanVar()
        Checkbutton(self, text = "C", variable = self.c, command = self.insert_text).grid(row = 4, column = 0, sticky = W)

        #Python
        self.python = BooleanVar()
        Checkbutton(self, text = "Python", variable = self.python, command = self.insert_text).grid(row = 5, column = 0, sticky = W)

        #C#
        self.csharp = BooleanVar()
        Checkbutton(self, text = "C#", variable = self.csharp, command = self.insert_text).grid(row = 6, column = 0, sticky = W)

        #Ruby
        self.ruby = BooleanVar()
        Checkbutton(self, text = "Ruby", variable = self.ruby, command = self.insert_text).grid(row = 7, column = 0, sticky = W)

        #Perl
        self.perl = BooleanVar()
        Checkbutton(self, text = "Perl", variable = self.perl, command = self.insert_text).grid(row = 8, column = 0, sticky = W)

        #VB.NET
        self.vb = BooleanVar()
        Checkbutton(self, text = "VB.NET", variable = self.vb, command = self.insert_text).grid(row = 9, column = 0, sticky = W)

        self.result = Text(self, width = 40, height = 5, wrap = WORD)
        self.result.grid(row = 9, column = 0, columnspan = 3)
        
    def insert_text(self):
        likes = ""

        if self.cplusplus.get():
            likes += "C++ "
        if self.c.get():
            likes += "C "
        if self.python.get():
            likes += "Python "    
        if self.csharp.get():
            likes += "C# "
        if self.ruby.get():
            likes += "Ruby "
        if self.perl.get():
            likes += "Perl "
        if self.vb.get():
            likes += "VB.NET "


        
        self.result.delete(0.0, END)
        self.result.insert(0.0, likes)

root = Tk()
root.title("Programming Languages")
app = Application(root)

app.mainloop()        


