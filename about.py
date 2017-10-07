from tkinter import *


about = Tk()

screen_width = about.winfo_screenwidth()
screen_height = about.winfo_screenheight()
    
about.geometry("%sx%s+0+0"%(screen_width,screen_height))
about.resizable(width=True, height=True)

    # titel
about.title("Smart Home System Software V 1.0.0 - About System")

logo = PhotoImage(file="../pictures/logo.png")
w1 = Label(about, image=logo).pack(side="right")

Label(about, text="iPMM Co.").pack(anchor = "nw")
Label(about, text="idea pardazan mechatronc mehr company").pack(anchor = "nw")

Label(about, text=" ").pack(anchor = "nw")
Label(about, text=" ").pack(anchor = "nw")

Label(about, text="Contact Us :").pack(anchor = "nw")
Label(about, text="\n\tphone : +98912-0883990").pack(anchor = "nw")
Label(about, text="\temail : info@iPMM.co.ir").pack(anchor = "nw")
Label(about, text="\tweb : www.iPMM.co.ir").pack(anchor = "nw")
    
about.mainloop()

    


# Programming By Ali Dehghan Chaharabi
# www.alidehghanchaharabi.info