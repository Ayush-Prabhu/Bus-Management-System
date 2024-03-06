import mysql.connector,time
from tkinter import *
from tkinter import messagebox

####

def bus_table():
    try:
        cn=mysql.connector.connect(user='Bus_Admin',password='I Am The Bus Admin', host='localhost',database='bus_trial' ,raise_on_warnings=True)
        cr=cn.cursor()
        sql="create table bus(bus_id int(4) primary key,bus_name varchar(20) not null,model varchar(20),type char(1),capacity numeric(2),depot_id numeric(10),foreign key(depot_id) references depot(depot_id))"
        cr.execute(sql)
        cn.close()
        messagebox.showinfo('Success','Bus Table Created')
    except Exception as ex:
        messagebox.showerror('Failure',str(ex))
def users_table():
    try:
        cn=mysql.connector.connect(user='Bus_Admin',password='I Am The Bus Admin', host='localhost',database='bus_trial' ,raise_on_warnings=True)
        cr=cn.cursor()
        sql="create table users(userid varchar(10) primary key,password varchar(10) not null)"
        cr.execute(sql)
        cn.close()
        messagebox.showinfo('Success','Users Table Created')
    except Exception as ex:
        messagebox.showerror('Failure',str(ex))
def bus_stop_table():
    try:
        cn=mysql.connector.connect(user='Bus_Admin',password='I Am The Bus Admin', host='localhost',database='bus_trial' ,raise_on_warnings=True)
        cr=cn.cursor()
        sql="create table bus_stop(stop_id numeric(10,0) primary key,stop_name varchar(10) not null,route_id numeric(10,0), foreign key(route_id) references route(route_id))"
        cr.execute(sql)
        cn.close()
        messagebox.showinfo('Success','Bus Stop Table Created')
    except Exception as ex:
        messagebox.showerror('Failure',str(ex))
def depot_table():
    try:
        cn=mysql.connector.connect(user='Bus_Admin',password='I Am The Bus Admin', host='localhost',database='bus_trial' ,raise_on_warnings=True)
        cr=cn.cursor()
        sql="create table depot(depot_id numeric(10) primary key,depot_name varchar(10) not null)"
        cr.execute(sql)
        cn.close()
        messagebox.showinfo('Success','Depot Table Created')
    except Exception as ex:
        messagebox.showerror('Failure',str(ex))
def route_table():
    try:
        cn=mysql.connector.connect(user='Bus_Admin',password='I Am The Bus Admin', host='localhost',database='bus_trial' ,raise_on_warnings=True)
        cr=cn.cursor()
        sql="create table route(route_id numeric(10) primary key,source_id numeric(10) not null,dest_id numeric(10),travel_time decimal(6,0))"
        cr.execute(sql)
        cn.close()
        messagebox.showinfo('Success','Route Table Created')
    except Exception as ex:
        messagebox.showerror('Failure',str(ex))
def schedule_table():
    try:
        cn=mysql.connector.connect(user='Bus_Admin',password='I Am The Bus Admin', host='localhost',database='bus_trial' ,raise_on_warnings=True)
        cr=cn.cursor()
        sql="create table schedule(schedule_id numeric(10) primary key,bus_id int(4) not null, foreign key(bus_id) references bus(bus_id),route_id numeric(10), foreign key(route_id) references route(route_id),departure time not null,arrival time)"
        cr.execute(sql)
        cn.close()
        messagebox.showinfo('Success','Schedule Table Created')
    except Exception as ex:
        messagebox.showerror('Failure',str(ex))



def users_entry():
    def usave():
        v1=t1.get().strip()
        v2=t2.get().strip()
        v3=t3.get().strip()
        if len(v1)<1:
            messagebox.showerror('Error','type min 1 charector')
            t1.delete(0,END)
            t1.focus_force()
            return
        if len(v2)<1:
            messagebox.showerror('Error','type min 1 charector')
            t2.delete(0,END)
            t2.focus_force()
            return
        if v2!=v3:
            messagebox.showerror('Error','password and retyped password mismatch')
            t3.delete(0,END)
            t3.focus_force()
            return
        try:
            cn=mysql.connector.connect(user='Bus_Admin',password='I Am The Bus Admin',host='localhost',database='bus_trial',raise_on_warnings=True)
            cr=cn.cursor()
            sql="insert into users values('%s','%s')" %(v1,v2)
            cr.execute(sql)
            cn.commit()
            messagebox.showinfo('Success','One user created')
        except Exception as ex:
            cn.rollback()
            messagebox.showerror('error',str(ex))
            return
        cn.close()
        ucancel()
        
    def ucancel():
        t1.delete(0,END)
        t2.delete(0,END)  
        t3.delete(0,END)
        t1.focus_force()
    def uexit():
        uwin.destroy()
        prowin.focus_force()
             
    uwin=Tk()
    uwin.title("user creation")
    uwin.geometry('400x250')
    l1=Label(uwin,text='User name')
    l2=Label(uwin,text='password')
    l3=Label(uwin,text='Retype password')
    t1=Entry(uwin)
    t2=Entry(uwin,show='*')
    t3=Entry(uwin,show='*')
    b1=Button(uwin,text='Save',bg='Green',fg='white',command=usave)
    b2=Button(uwin,text='Cancel',bg='Magenta',fg='red',command=ucancel)
    b3=Button(uwin,text='Exit',bg='blue',fg='white',command=uexit)
    l1.place(x=50,y=30);t1.place(x=200,y=30,width=150)
    l2.place(x=50,y=80);t2.place(x=200,y=80,width=150)
    l3.place(x=50,y=130);t3.place(x=200,y=130,width=150)
    b1.place(x=50,y=200,width=80)
    b2.place(x=150,y=200,width=80)
    b3.place(x=250,y=200,width=80)
    t1.focus_force()
    uwin.mainloop()
def change_password():
    def upchange():
        try:
            v1=t1.get().strip()
            cn=mysql.connector.connect(user='Bus_Admin',password='I Am The Bus Admin',host='localhost',database='bus_trial',raise_on_warnings=True)
            cr=cn.cursor()
            sql="select * from users where userid ='%s'" %(v1)
            cr.execute(sql)
            rs=cr.fetchone()
            t2.delete(0,END)
            t3.delete(0,END)
            t4.delete(0,END)
            v2=rs[1]
            cn.close()
            upwin.geometry('500x400')
            t2.config(state='normal')
            t2.insert(0,v1)
            t3.focus_force()
        except Exception as ex:
            messagebox.showerror('Failure',str(ex))
       
    def upexit():
        upwin.destroy()
        prowin.focus_force()

    def upsave():
        v1=t2.get().strip()
        v2=t3.get().strip()
        v3=t4.get().strip()
        v4=t5.get().strip()
        if len(v3)<1:
            messagebox.showerror('error','new password not typed')
            t4.delete(0,END)
            t4.focus_force()
            return 
        if len(v4)<1:
            messagebox.showerror('error','new password not typed')
            t5.delete(0,END)
            t5.focus_force()
            return 
        if v3!=v4:
            messagebox.showerror('error','mismatch in the password')
            t5.delete(0,END)
            t5.focus_force()
            return 
        if v2==v3:
            messagebox.showerror('error','old and new password is same')
            t4.delete(0,END)
            t5.delete(0,END)
            t4.focus_force()
            return 
        try:
            cn=mysql.connector.connect(user='Bus_Admin',password='I Am The Bus Admin',host='localhost',database='bus_trial',raise_on_warnings=True)
            cr=cn.cursor()
            sql="select * from users where userid ='%s'" %(v1)
            cr.execute(sql)
            rs=cr.fetchone()
            if v2!=rs[1]:
                messagebox.showerror('Error','User old password is not right')
                t3.delete(0,END)
                t3.focus_force()
                return 
            sql="update users set password='%s' where userid='%s'" %(v3,v1)
            cr.execute(sql)
            cn.commit()
            cn.close()
            messagebox.showinfo('Success','The password of user change successfully')
            upcancel()
        except Exception as ex:
            cn.rollback()
            messagebox.showerror('Error',str(ex))
            upwin.focus_force()
        
    def upcancel():
        t1.delete(0,END)
        upwin.geometry('500x100')
        t1.focus_force()
    upwin=Tk()
    upwin.title('User password change')
    upwin.geometry('500x100')
    l1=Label(upwin,text='Enter User name')
    l2=Label(upwin,text='User Name')
    l3=Label(upwin,text='Old Password')
    l4=Label(upwin,text='New Password')
    l5=Label(upwin,text='Retype New Password')
    t1=Entry(upwin)
    t2=Entry(upwin)
    t3=Entry(upwin,show='*')
    t4=Entry(upwin,show='*')
    t5=Entry(upwin,show='*')
    b1=Button(upwin,text='Change Password',bg='green',fg='white',command=upchange)
    b2=Button(upwin,text='Exit',bg='magenta',fg='black',command=upexit)
    b3=Button(upwin,text='Save',bg='blue',fg='white',command=upsave)
    b4=Button(upwin,text='Cancel',bg='green',fg='white',command=upcancel)
    l1.place(x=50,y=30)
    l2.place(x=50,y=120)
    l3.place(x=50,y=160)
    l4.place(x=50,y=200)
    l5.place(x=50,y=240)
    t1.place(x=150,y=30, width=100)
    t2.place(x=150,y=120, width=200)
    t3.place(x=150,y=160, width=200)
    t4.place(x=150,y=200, width=200)
    t5.place(x=150,y=240, width=200)
    b1.place(x=275,y=30,width=100)
    b2.place(x=390,y=30,width=60)
    b3.place(x=50,y=360,width=100)
    b4.place(x=160,y=360,width=200)
    upwin.mainloop()
def schedule_entry():
    def isave():
        v1=int(t1.get().strip())
        v2=int(t2.get().strip())
        v3=int(t3.get().strip())
        v4=int(t4.get().strip())
        v5=int(t5.get().strip())

        if v1<1 :
            messagebox.showerror('error','invalid schedule id')
            t1.delete(0,END)
            t1.focus_force()
            return
        if v2<1 :#foreign key validation pending
            messagebox.showerror('error','Invalid bus id')
            t2.delete(0,END)
            t2.focus_force()
            return
        if v3<1 :#foreign key validation pending
            messagebox.showerror('error','Invalid route id')
            t3.delete(0,END)
            t3.focus_force()
            return
        if v4>235959 or v4<0 :#minute and second validation pending
            messagebox.showerror('error','Enter time in hhmmss format')
            t4.delete(0,END)
            t4.focus_force()
            return
        if v5<0 or v5>235959:#minute and second validation pending
            messagebox.showerror('error','Enter time in hhmmss format')
            t5.delete(0,END)
            t5.focus_force()
            return
        try:                
            cn=mysql.connector.connect(user='Bus_Admin',password='I Am The Bus Admin',host='localhost',database='bus_trial',raise_on_warnings=True)
            cr=cn.cursor()
            sql="insert into schedule values('%d','%d','%d','%d','%d')" %(v1,v2,v3,v4,v5)
            cr.execute(sql)
            cn.commit()
            messagebox.showinfo('Success','One schedule saved')
            iwin.focus_force()
        except Exception as ex:
            cn.rollback()
            messagebox.showerror('Failure',str(ex))
            return
        cn.close()
        icancel()
          
    def icancel():
        t1.delete(0,END)
        t2.delete(0,END)  
        t3.delete(0,END)
        t4.delete(0,END)
        t5.delete(0,END)
        iwin.geometry('500x100')
        t1.focus_force()
    def iadd ():
        iwin.geometry('500x480')
        t1.focus_force()
              
    iwin=Tk()
    iwin.title("Schedule creation")
    iwin.geometry('500x100')
    l1=Label(iwin,text='schedule id')
    l2=Label(iwin,text='Bus id')
    l3=Label(iwin,text='Route id')
    l4=Label(iwin,text='departure time')
    l5=Label(iwin,text='arrival time')
    t1=Entry(iwin)
    t2=Entry(iwin)
    t3=Entry(iwin)
    t4=Entry(iwin)
    t5=Entry(iwin)
    b1=Button(iwin,text='Add Schedule',bg='blue',fg='white',font='arial 12',command= iadd)
    b2=Button(iwin,text='Exit',bg='red',fg='white',font='arial 12',command= iwin.quit)
    b3=Button(iwin,text='Save',bg='Green',fg='white',font='arial 12',command=isave)
    b4=Button(iwin,text='Cancel',bg='black',fg='white',font='arial 12',command=icancel)
    l1.place(x=50,y=140); t1.place(x=250,y=140,width=200)
    l2.place(x=50,y=180); t2.place(x=250,y=180,width=200)
    l3.place(x=50,y=220); t3.place(x=250,y=220,width=200)
    l4.place(x=50,y=260); t4.place(x=250,y=260,width=200)
    l5.place(x=50,y=300); t5.place(x=250,y=300,width=200)

    b1.place(x=50,y=50,width=150)
    b2.place(x=250,y=50,width=150)
    b3.place(x=50,y=400,width=150)
    b4.place(x=250,y=400,width=150)
    iwin.mainloop()






prowin=Tk()
prowin.title('Bus Management System')
prowin.geometry('400x250')
prowin.config(bg='teal')
mb=Menu(prowin)
m1=Menu(mb)
m2=Menu(mb)
#m3=Menu(mb)
mb.add_cascade(label='Create Table',menu=m1)
mb.add_cascade(label='Entry',menu=m2)
#mb.add_cascade(label='Reports',menu=m3)
m1.add_command(label='Bus_Stop',command=bus_stop_table)
m1.add_command(label='Bus',command=bus_table)
m1.add_command(label='Users',command=users_table)
m1.add_command(label='Schedule',command=schedule_table)
m1.add_command(label='Route',command=route_table)
m1.add_command(label='Depot',command=depot_table)
m1.add_separator()
m1.add_command(label='Exit',command=prowin.quit)
m2.add_command(label='Schedule Entry',command=schedule_entry)
#m2.add_command(label='Purchase or sale',command=trans_entry)
m2.add_command(label='Users Entry',command=users_entry)
m2.add_separator() #for seperator linr
#m2.add_command(label='Item Price Change',command=change_price)
m2.add_command(label='Change User Password',command=change_password)
"""m3.add_command(label='Items Query',command=items_query)
m3.add_command(label='Item Stock Report',command=items_report)
m3.add_command(label='Item Transactions',command=trans_report)"""
prowin.config(menu=mb)
prowin.mainloop()


""" remaining parts:
0. Entry functions for tables:route,depot,bus,bus_stop + multiple validations
1. Reporting tables
2. employee table, with constraints
3. passenger/ticket table

Bugs:
exit needs to be clicked twice

"""