from tkinter import*
import webbrowser
def my_fancation():
    link= my_text.get()
    webbrowser.open(link)
    

window =Tk()
my_labol=Label(window, text="welcome Mahmoud",font="arial 30 bold")
my_labol.pack(pady=30)
window .title("my App")
window .geometry('500x300')
my_button= Button(window, text="Go to link", fg="green",bg="red",font="arial 20 bold",
                  padx=10,pady=8,command= my_fancation)
my_button.pack()
my_button1= Button(window, text="Go to link", fg="red",bg="green",font="arial 20 bold",
                  padx=10,pady=8,command= my_fancation)
my_button.pack(pady=20)
my_text=Entry(window, width=50)
my_text.pack(pady=15)

window.mainloop()