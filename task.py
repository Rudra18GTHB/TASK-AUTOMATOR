import datetime as dt 
import mysql.connector as c 

def operation():
    print("""What you want to do: 

    1) Enter Task
    2) Show Priority
    """)
    choice=int(input(print("ENter your choice: ")))
    if choice==1:
        task()
    else:
        priority_setting()


    
def task():
    cn=True
    while cn==True:
        a=input(print("Enter the task"))
        d=input(print("Description: "))
        cur.execute("insert into tasks values('{}','{}')".format(a,d))
        con.commit()
        t=input(print("All task entered: "))
        if t=="y":
            priority_setting()
            cn=False

def priority_setting():
    current=dt.datetime.now()
    string=current.strftime("%A")
    
    if string=="Sunday":
        sunday()
    elif string=="Monday":
        monday()
    elif string=="Tuesday":
        tuesday()
    elif string=="Wednesday":
        wednesday()
    elif string=="Thursday":
        thursday()
        
def sunday():
    cur.execute("Select * from tasks")
    tasks=cur.fetchall()
    for i_monday in Monday:
        for j_sunday in tasks:
            if i_monday in j_sunday[0]:
                cur.execute("insert into priority values('{}')".format(j_sunday[0]))
                con.commit()
    to_do()

def monday():
    cur.execute("Select * from tasks")
    tasks=cur.fetchall()
    for i_tuesday in Tuesday:
        for j_monday in tasks:
            if i_tuesday in j_monday[0]:
                cur.execute("insert into priority values('{}')".format(j_monday[0]))
                con.commit()
    to_do()

def tuesday():
    cur.execute("Select * from tasks")
    tasks=cur.fetchall()
    for i_wednesday in Wednesday:
        for j_tuesday in tasks:
            if i_wednesday in j_tuesday[0]:
                cur.execute("insert into priority values('{}')".format(j_tuesday[0]))
                con.commit()
    to_do()

def wednesday():
    cur.execute("Select * from tasks")
    tasks=cur.fetchall()
    for i_thursday in Thursday:
        for j_thursday in tasks:
            if i_thursday in j_thursday[0]:
                cur.execute("insert into priority values('{}')".format(j_thursday[0]))
                con.commit()
    to_do()

def thursday():
    cur.execute("Select * from tasks")
    tasks=cur.fetchall()
    for i_friday in Friday:
        for j_friday in tasks:
            if i_friday in j_friday[0]:
                cur.execute("insert into priority values('{}')".format(j_friday[0]))
                con.commit()
            else:
                to_do()

def to_do():
    cur.execute("select priority.task,description from tasks,priority where tasks.task=priority.task")
    todo=cur.fetchall()
    for lt in todo:
        print("To do: ",lt[0])
        print("Description: ",lt[1])
        new=input("Task Completed: ")
        if new=="y":
            print("Good, Take a Break!")
            cur.execute("Delete from tasks where task='{}'".format(lt[0]))
            con.commit()
            cur.execute("Delete from priority where task='{}'".format(lt[0]))
            con.commit()

        else:
            print("Complete as soon as possible!")
    cur.execute("Delete from priority")
    con.commit()
    print("Enjoy your day!")
    con.close()
    
    
con=c.connect(host="localhost",user="root",passwd="rudraxcode",database="task")
if con.is_connected():
    cur=con.cursor()
    Monday=["DBMS Lab","OS","IT Work"]
    Tuesday=["CSS","ET","OS","Maths Lab"]
    Wednesday=["DBMS","OS","ET Lab"]
    Thursday=["CSS","ET","C","C Lab"]
    Friday=["DBMS","C","CSS"]
    operation()