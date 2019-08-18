from tkinter import *
import json
import os.path

def add_sheets(id_search,search_field):
    cus_sup=int(search_field.get())
    with open('customer_list.json') as f:
        data=json.load(f)
        data[id_search]['supply']=data[id_search]['supply']+cus_sup
        with open('customer_list.json','w') as f:
            f.write(json.dumps(data))

def sub_sheets(id_search,search_field):
    cus_sup=int(search_field.get())
    with open('customer_list.json') as f:
        data=json.load(f)
        if data[id_search]['supply'] > cus_sup:
            data[id_search]['supply']=data[id_search]['supply']-cus_sup
            with open('customer_list.json','w') as f:
                f.write(json.dumps(data))
        else:
            root = Tk()
            root.title("error")
            root.geometry("300x50")
            the_amount_of_curtains=Label(root,text="customer don't have enough money!!!").grid(row=0 , column=0)





def search(x):
    id_search=x.get()
    with open('customer_list.json') as f:
        data=json.load(f)
        if id_search in data:
            root = Tk()
            root.title("search box")
            root.geometry("300x100")
            the_amount_of_curtains=Label(root,text="How many sheets: ").grid(row=0 , column=0)
            search_field = Entry(root,bg='light gray',width=30,bd=2,selectborderwidth=5)
            search_field.grid(row=0,column=3)
            Button(root, text='Add',command=lambda : add_sheets(id_search,search_field)).grid(row=2,column=0,sticky = W)
            Button(root, text='sub',command=lambda : sub_sheets(id_search,search_field)).grid(row=2,column=1,sticky = W)

        else:
            root = Tk()
            root.title("error")
            root.geometry("300x50")
            the_amount_of_curtains=Label(root,text="This ID number not found!!!").grid(row=0 , column=0)


def withraw(deposit_field_1):
    id_search=withdraw_field_1.get()
    with open('customer_list.json') as f:
        data=json.load(f)
        if id_search in data:
            data.pop(id_search)
            with open('customer_list.json','w') as f:
                f.write(json.dumps(data))
        else:
            root = Tk()
            root.title("error")
            root.geometry("300x50")
            the_amount_of_curtains=Label(root,text="This ID number not found!!!").grid(row=0 , column=0)

def add():
    a=win_field_1.get()
    b=win_field_2.get()
    c=win_field_3.get()
    d=win_field_4.get()
    e=win_field_5.get()
    f=int(e)    
    cus_specification={'Name':a,'lastname':b,'id':c,'bank_account':d,'supply':f}
    all_cus_specification[c]=cus_specification
    if not os.path.isfile('customer_list.json'):
        with open('customer_list.json','w')as f:
            f.write(json.dumps(all_cus_specification))
    else:
        with open('customer_list.json')as f:
            feeds=json.load(f)
        feeds.update(all_cus_specification)
        with open('customer_list.json','w') as f:
            f.write(json.dumps(feeds))

def deposit():
    root = Tk()
    root.title("deposit box")
    root.geometry("400x100")
    id_number_for_search=Label(root,text="ID number for deposit: ").grid(row=0 , column=0)
    deposit_field_1 = Entry(root,bg='light gray',width=30,bd=2,selectborderwidth=5)
    deposit_field_1.grid(row=0,column=3)
    Button(root, text='search',command=lambda : search(deposit_field_1)).grid(row=2,column=0,sticky = W)
    root.mainloop()

def withdraw():
    root = Tk()
    root.title("search box")
    root.geometry("400x100")
    id_number_for_search=Label(root,text="ID number for withdraw: ").grid(row=0 , column=0)
    withdraw_field_1 = Entry(root,bg='light gray',width=30,bd=2,selectborderwidth=5)
    withdraw_field_1.grid(row=0,column=3)
    Button(root, text='withdraw',command=lambda : withraw(withdraw_field_1)).grid(row=2,column=0,sticky = W)
    root.mainloop()



def dump():
    root = Tk()
    root.title("search box")
    root.geometry("400x100")
    id_number_for_search=Label(root,text="ID number for dump: ").grid(row=0 , column=0)
    dump_field_1 = Entry(root,bg='light gray',width=30,bd=2,selectborderwidth=5)
    dump_field_1.grid(row=0,column=3)
    Button(root, text='search',command=lambda : search(dump_field_1)).grid(row=2,column=0,sticky = W)
    root.mainloop()
    


cus_specification={}
all_cus_specification={}
root = Tk()        
root.title("Bank account")
root.geometry("330x400")

win_field_1 = Entry(root,bg='light gray',width=30,bd=2,selectborderwidth=5)
win_field_1.grid(row=0 , column=3 )

L_1=Label(root,text="Name: ")
L_1.grid(row=0 , column=0 , sticky = W)

win_field_2 = Entry(root,bg='light gray',width=30,bd=2,selectborderwidth=5)
win_field_2.grid(row=1 , column=3 )

L_2=Label(root,text="LastName: ")
L_2.grid(row=1 , column=0 , sticky = W)

win_field_3 = Entry(root,bg='light gray',width=30,bd=2,selectborderwidth=5)
win_field_3.grid(row=2 , column=3)

L_3=Label(root,text="ID Num: ")
L_3.grid(row=2 , column=0 , sticky = W)

win_field_4 = Entry(root,bg='light gray',width=30,bd=2,selectborderwidth=5)
win_field_4.grid(row=3 , column=3)

L_4=Label(root,text="Bank Account Number: ")
L_4.grid(row=3 , column=0 , sticky = W)

win_field_5 = Entry(root,bg='light gray',width=30,bd=2,selectborderwidth=5)
win_field_5.grid(row=4 , column=3)

L_5=Label(root,text="supply: ")
L_5.grid(row=4 , column=0 , sticky = W)  

Button(root, text='Add', command=add).place(x=2,y=120)
Button(root, text='Deposit', command=deposit).place(x=40,y=120)
Button(root, text='Withdraw', command=withdraw).place(x=95,y=120)
Button(root, text='Dump', command=dump).place(x=161,y=120)


root.mainloop()
        


                
