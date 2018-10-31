# Stop watch using Tkinter 
#importing the required libraries 
import tkinter as Tkinter 
import sqlite3

count = 1
counter = -1
running = False
conn=sqlite3.connect("time.db")
c=conn.cursor()
def counter_label(label): 
    def count(): 
        if running: 
            global counter 

            # To manage the intial delay. 
            if counter==-1:          
                display="Starting..."
            else: 
                display=str(counter) 

            label['text']=display  
            label.after(1000, count) 
            counter += 1

    # Triggering the start of the counter. 
    count()  

# start function of the stopwatch 
def Start(label): 
    global running, count 
    running=True
    counter_label(label) 
    start['state']='disabled'
    stop['state']='normal'
    reset['state']='normal'


# Stop function of the stopwatch 
def Stop(): 
    global running, count, counter, c 
    start['state']='normal'
    stop['state']='disabled'
    reset['state']='normal'
    running = False
    c.execute("CREATE TABLE IF NOT EXISTS TIME(Count INTEGER,Time INTEGER)")
    c.execute("INSERT INTO TIME(Count ,Time) VALUES (?,?)",(count, counter))
    count += 1
    conn.commit()

# Reset function of the stopwatch 
def Reset(label): 
    global counter,count 
    counter=-1

    # If rest is pressed after pressing stop. 
    if running==False:   
        reset['state']='disabled'
        label['text']='Welcome!'

    # If reset is pressed while the stopwatch is running. 
    else:            
        label['text']='Starting...'
    window = Tkinter.Toplevel(root)
    txt = 'STOP' + " "*(9-len('STOP'))
    Tkinter.Label(window, text=txt,borderwidth=1, font="Verdana 30 bold").grid(row=0,column=0)
    txt = 'TIME' + " "*(9-len('TIME'))
    Tkinter.Label(window, text=txt,borderwidth=1, font="Verdana 30 bold").grid(row=0,column=1)
    c.execute("SELECT * FROM TIME")
    data = c.fetchall()
    ro = len(data)
    #print(data)
    for row1 in range(ro):
        for col in range(2):
            txt = str(" " + str(data[row1][col]) + " "*(9-len(str(data[row1][col]))))
            Tkinter.Label(window, text=txt,borderwidth=1,font="Verdana 20 bold").grid(row=row1+1,column=col)
            
    count = 1
    c.execute("DROP TABLE TIME")
    conn.commit()

root = Tkinter.Tk() 
root.title("Stopwatch") 

# Fixing the window size. 
root.minsize(width=250, height=70) 
label = Tkinter.Label(root, text="Welcome!", fg="black", font="Verdana 30 bold") 
label.pack() 
start = Tkinter.Button(root, text='Start', 
width=15, command=lambda:Start(label)) 
stop = Tkinter.Button(root, text='Stop', 
width=15, state='disabled', command=Stop) 
reset = Tkinter.Button(root, text='Reset', 
width=15, state='disabled', command=lambda:Reset(label)) 
start.pack() 
stop.pack() 
reset.pack() 
root.mainloop() 
