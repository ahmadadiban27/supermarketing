from tkinter import*
from tkinter import messagebox
from backend import Market
new1=Market('f:/mam.db')

win=Tk()
win.title("سوپرمارکت ")
x=win.winfo_screenwidth()
y=win.winfo_screenheight()
x1=400
y1=470
win.geometry(f'{x1}x{y1}+{(x//2)-(x1//2)}+{(y//2)-(y1//2)}')
win.configure(bg='#987284')

#-------------------------------------function-------------------------------------
def insert():
    en1=ent_item.get()
    en2=ent_buy.get()
    en3=ent_sale.get()
    en4=ent_number.get()
    if en1!='' and en2 !='' and en3!='' and en4!='' and en4.isdigit():
        new1.insert(en1,en2,en3,en4)
        clear()
        fetch() 
    else:
        messagebox.showerror('خطا' , 'لطفا تمام فیلد ها را به صورت کامل و صحیح پر نمایید')
        mes= messagebox.askyesno('نمایش موجودی'," آیا میخواهید موجودی قبلی نمایش داده شود")
        if mes==1:
           fetch()
    

def search():
    en1=ent_item.get()
    en2=ent_buy.get()
    en3=ent_sale.get()
    en4=ent_number.get()
    list1.delete(0,END)
    newlist=new1.search(en1,en2,en3,en4)
    if not newlist:
        messagebox.showinfo('اطلاع رسانی','جستجو نتیجه ای در بر نداشت')
       
    else:
        for i in newlist:
            list1.insert(END,i)
    clear()


def delete():
    global list_item
    mes=messagebox.askquestion('حذف کالا', " آیا از حذف کالای مورد نظر مطمین هستید؟")
    if mes==1:
        new1.delete(list_item[0])
        clear()
    fetch()    


def edit():
    global list_item 
    en1=ent_item.get()
    en2=ent_buy.get()
    en3=ent_sale.get()
    en4=ent_number.get()
    if en1!='' and en2 !='' and en3!='' and en4!='' and en4.isdigit():
        new1.edit(list_item[0],en1,en2,en3,en4)
        clear()
        fetch() 
    else:
        messagebox.showerror('خطا' , 'لطفا تمام فیلد ها را به صورت کامل و صحیح پر نمایید')
        mes= messagebox.askyesno('نمایش موجودی'," آیا میخواهید موجودی قبلی نمایش داده شود")
        if mes:
           fetch()

def exit():
    mes=messagebox.askquestion(' خروج از برنامه', "آیا میخواهید از برنامه خارج شوید")
    if mes==1:
        win.destroy()

def about():
    messagebox.showinfo('About', 'program name: super market \nWritten by: Ahmad Adiban \n    Data : 03/15/2024')


def clear():
    ent_item.delete(0,END)
    ent_buy.delete(0,END)
    ent_sale.delete(0,END)
    ent_number.delete(0,END)
    ent_item.focus()

def select_item(event):
    global list_item
    index=list1.curselection()
    list_item=list1.get(index)
    clear()
    ent_item.insert(0,list_item[1])
    ent_buy.insert(0,list_item[2])
    ent_sale.insert(0,list_item[3])
    ent_number.insert(0,list_item[4])
    but_delete.config(state=NORMAL)
    but_edit.config(state=NORMAL)

def fetch():
    list1.delete(0,END)
    newlist=new1.fetch()
    for i in newlist:
        list1.insert(END , i)

#------------------------------------widget----------------------------------------
lab_item=Label(win, bg='#987284', text='نام کالا')
lab_buy=Label(win , bg='#987284', text=' خرید')
lab_sale=Label(win , bg='#987284', text=' فروش')
lab_number=Label(win , bg='#987284', text='تعداد')

ent_item=Entry(win , bd=3 )
ent_buy=Entry(win , bd=3 )
ent_sale=Entry(win , bd=3)
ent_number=Entry(win , bd=3)

list1=Listbox(win, width=55 , height=15 , bd=5)
scor1=Scrollbar(win )
scor1.config(command=list1.yview)
but_insert=Button(win ,width=50, bd=3 ,command= insert, text = 'اضافه کردن')
but_search=Button(win ,width=8, bd=3,command= search, text = 'جستجوی کالا')
but_delete=Button(win ,state=DISABLED,width=8, bd=3,command= delete, text = 'حذف کالا')
but_edit=Button(win ,state=DISABLED,width=8, bd=3,command= edit, text = 'ویرایش')
but_exit=Button(win ,width=8, bd=3,command= exit, text = 'بستن')
but_about=Button(win ,width=8, bd=3,command= about, text = 'درباره')

lab_item.place(x=5 , y=10)
lab_buy.place(x=210 , y=10)
lab_sale.place(x=5 , y=40)
lab_number.place(x=210 , y=40)

ent_item.place(x=60 , y=10)
ent_buy.place(x=260 , y=10)
ent_sale.place(x=60 , y=40)
ent_number.place(x=260 , y=40)

list1.place(x=20 , y=70 )
scor1.place(x=365 , y=70 , height=251)

but_insert.place(x=20 , y=330)
but_search.place(x=20 , y=370)
but_delete.place(x=170 , y=370)
but_edit.place(x=313 , y=370)
but_exit.place(x=313 , y=430)
but_about.place(x=20 , y=430)
#-------------------------------------------------------------------
ent_item.focus()
list1.bind('<<ListboxSelect>>',select_item)

win.mainloop()