class Node:
    def __init__(self, data):
        self.item = data
        self.nref = None
        self.pref = None

class DoublyLinkedList:
    def __init__(self):
        self.start_node = None
        
            
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.start_node is None:
            
            self.start_node = new_node
            return
        n = self.start_node
        while n.nref is not None:
            n = n.nref
        
        n.nref = new_node
        new_node.pref = n
    
    def delete_element_by_value(self, x):
        if self.start_node is None:
            print("The list has no element to delete")
            return 
        if self.start_node.nref is None:
            if self.start_node.item[0] == x:
                self.start_node = None
            else:
                print("Item not found")
            return 

        if self.start_node.item[0] == x:
            self.start_node = self.start_node.nref
            self.start_node.pref = None
            return

        n = self.start_node
        while n.nref is not None:
            if n.item[0] == x:
                break;
            n = n.nref
        if n.nref is not None:
            n.pref.nref = n.nref
            n.nref.pref = n.pref
        else:
            if n.item[0] == x:
                n.pref.nref = None
            else:
                print("Element not found")
            
    def traverse_list(self):
        if self.start_node is None:
            print("List has no element")
            return
        else:
            n = self.start_node
            while n is not None:
                print(n.item , " ")
                n = n.nref
                
    def insert_names(self):
        n = self.start_node
        while n is not None:
            select.insert(END, n.item[0])
            n = n.nref

    def sortList(self):  
        #Check whether list is empty  
        if(self.start_node == None):  
            return;  
        else:  
            #Current will point to head  
            current = self.start_node  
            while(current.nref != None):  
                #Index will point to node next to current  
                index = current.nref;  
                while(index != None):  
                    #If current's data is greater than index's data, swap the data of current and index  
                    if(current.item[0][0].upper() > index.item[0][0].upper()):  
                        temp = current.item;  
                        current.item = index.item;  
                        index.item = temp;  
                    index = index.nref  
                current = current.nref

    def change(self,x,y,z,l,p):
        n = self.start_node
        while n is not None:
            if n.item[0]==x:
                n.item[0]=y
                n.item[1]=z
                n.item[2]=l
                n.item[3]=p
            n=n.nref

    def returned(self,x):
        n = self.start_node
        while n is not None:
            if n.item[0]==x:
                return n.item
            n=n.nref 

    def backup(self):
        if self.start_node is None:
            print("List has no element")
            return
        else:
            x=0
            n = self.start_node
            while n is not None:
                x=x+1
                n = n.nref

        
        t="D"+str(x)
        sheet_1['G1'].value=x
        if self.start_node is None:
            print("List has no element")
            return
        else:
            n = self.start_node
            while n is not None:
                multiple_cells = sheet_1['A1':t]
                for row in multiple_cells:
                    i=0
                    for cell in row:
                        cell.value=n.item[i]
                        
                        i=i+1
                    n = n.nref
        work_book.save("/home/susil/Desktop/ContactBook_Python/sample.xlsx")



import tkinter as tk
from tkinter import *



root = Tk()
root.geometry('500x500')
root.config(bg = 'SlateGray3')
root.title('Contact Book')
root.resizable(0,0)
k=DoublyLinkedList()

#openpyyxl is to read or write the list in the xlsx sheet

import openpyxl

work_book = openpyxl.load_workbook("/home/susil/Desktop/ContactBook_Python/sample.xlsx")
sheet_1 = work_book['Sheet1']

b=sheet_1['G1'].value
t='D'+str(b)

multiple_cells = sheet_1['A1':t]
for row in multiple_cells:
    v=[]
    for cell in row:
        v.append(cell.value)
    k.insert_at_end(v)

# for i in range(len(contactlist)):
#     v=contactlist[i]
#     k.insert_at_end(v)

#k.traverse_list()


Name = StringVar()
Number = StringVar()
Email = StringVar()
Subject = StringVar()
Body = StringVar()
Other = StringVar()


frame = Frame(root)
frame.pack(side = RIGHT)

scroll = Scrollbar(frame, orient=VERTICAL)
select = Listbox(frame, yscrollcommand=scroll.set, height=12)
scroll.config (command=select.yview)
scroll.pack(side=RIGHT, fill=Y)
select.pack(side=LEFT,  fill=BOTH, expand=1)




def Selected():
    return int(select.curselection()[0])
    

def AddContact():
    k.insert_at_end([Name.get(), Number.get(), Email.get(), Other.get()])
    Select_set()
    

def EDIT():
    k.change(select.get(Selected()), Name.get(), Number.get(), Email.get(), Other.get())
    Select_set()
    
def DELETE():
    k.delete_element_by_value(select.get(Selected()))
    Select_set()
    
def VIEW():
    
    s = k.returned(select.get(Selected()))
    Name.set(s[0])
    Number.set(s[1])
    Email.set(s[2])
    Other.set(s[3])

def SAVE_EXIT():
    k.backup()
    root.destroy()

def EXIT():
    root.destroy()

def RESET():
    Name.set('')
    Number.set('')
    Email.set('')
    Other.set('')

import smtplib
from email.message import EmailMessage

def SEND():
        s = k.returned(select.get(Selected()))
    
        msg= EmailMessage()

        my_address ="(ENTER YOUR EMAIL)"    #sender address

        app_generated_password = "ENTER EMAIL API"    # gmail generated password

        msg["Subject"] = Subject.get()   #email subject 

        msg["From"]= my_address      #sender address

        msg["To"] = s[2]     #reciver address

        msg.set_content(Body.get())   #message body

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            
            smtp.login(my_address,app_generated_password)    #login gmail account
            
            print("sending mail")
            smtp.send_message(msg)   #send message 
            print("mail has sent")
    

def createNewWindow():
    newWindow = tk.Toplevel(root)
    newWindow.geometry('500x200')
    newWindow.config(bg = 'SlateGray3')
    newWindow.title('Send Mail')
    newWindow.resizable(0,0)
    Label(newWindow, text = 'SUBJECT', font='arial 12 bold', bg = 'SlateGray3').place(x= 30, y=20)
    Entry(newWindow, textvariable = Subject).place(x= 120, y=20)
    Label(newWindow, text = 'BODY', font='arial 12 bold',bg = 'SlateGray3').place(x= 30, y=45)
    Entry(newWindow, textvariable = Body).place(x= 130, y=45, width= 300, height= 100)
    Button(newWindow,text=" SEND", font='arial 12 bold',bg='SlateGray4', command = SEND).place(x= 50, y=110)
    

    



def Select_set() :
    
    select.delete(0,END)
    k.sortList()
    k.insert_names()
    
Select_set()




Label(root, text = 'NAME', font='arial 12 bold', bg = 'SlateGray3').place(x= 30, y=20)
Entry(root, textvariable = Name).place(x= 100, y=20)
Label(root, text = 'PHONE NO.', font='arial 12 bold',bg = 'SlateGray3').place(x= 30, y=45)
Entry(root, textvariable = Number).place(x= 130, y=45)
Label(root, text = 'EMAIL', font='arial 12 bold',bg = 'SlateGray3').place(x= 30, y=80)
Entry(root, textvariable = Email).place(x= 130, y=80)
Label(root, text = 'OTHER', font='arial 12 bold',bg = 'SlateGray3').place(x= 270, y=80)
Entry(root, textvariable = Other).place(x= 350, y=80)

Button(root,text=" ADD", font='arial 12 bold',bg='SlateGray4', command = AddContact).place(x= 50, y=110)
Button(root,text="EDIT", font='arial 12 bold',bg='SlateGray4',command = EDIT).place(x= 50, y=260)
Button(root,text="DELETE", font='arial 12 bold',bg='SlateGray4',command = DELETE).place(x= 50, y=210)
Button(root,text="VIEW", font='arial 12 bold',bg='SlateGray4', command = VIEW).place(x= 50, y=160)
Button(root,text="EXIT", font='arial 12 bold',bg='tomato', command = EXIT).place(x= 300, y=320)
Button(root,text="RESET", font='arial 12 bold',bg='SlateGray4', command = RESET).place(x= 50, y=310)
Button(root,text="MAIL", font='arial 12 bold',bg='SlateGray4', command = createNewWindow).place(x= 200, y=320)
Button(root,text="SAVE AND EXIT", font='arial 12 bold',bg='tomato', command = SAVE_EXIT).place(x= 50, y=400)

root.mainloop()
  
