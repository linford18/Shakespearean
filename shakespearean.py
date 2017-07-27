from tkinter  import *
import tkinter.messagebox as msg
import text_generator as tg

def poem():
    num=int(entry.get())
    m=tg.Markov(2)
    m.train('poem.txt')
    text = Text(frame)
    x=" "
    
    x=x+m.word(1)+" "+m.generate(num-2)+m.word(0)
    
    print (x)
    text_field.delete('1.0', END)
    text_field.insert(INSERT,x)
    text_field.pack(side=TOP)
    
root = Tk()
root.title("Shakespearean Poem-Genterate your own poem")
frame = Frame(root,width=700,height=500)
frame.pack_propagate(0)
frame.pack()

theLabel = Label(frame,text="SHAKESPEAREAN POEM GENERATOR",fg="green",font=(12))
theLabel.pack(side=TOP)

text_field=Text(frame)
text_field.pack(side=TOP)

EntryLabel=Label(frame,text="Enter the number of words in poem:")
EntryLabel.pack(side=BOTTOM)
entry=Entry(root)
entry.pack()

sub_button= Button(text="Submit",fg="red",command=poem,pady=10,bd=5)

sub_button.pack()

    
    
    
    


root.mainloop()
