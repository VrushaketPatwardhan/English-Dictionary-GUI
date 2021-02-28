import json
from tkinter import *
from difflib import get_close_matches

#FIRST MAIN FUNTION
#IF VALID WORD IS ENTERED THEN pure_correct FUNCTION IS EXECUTED
#IF COMPLETELY INVALID WORD IS ENTERED WHICH HAS NO SIMILAR WORDS IN JSON FILE THEN invalid_word Function is executed

#IF WRONG WRONG WORD IS ENTERED BUT THERE ARE SIMILAR WORDS IS JSON FILE THEN when_wrong_word_is_entered_but_there_is_similar_word FUNCTION IS EXECUTED
#HERE WE ASK FOR YES OR NO IF YES IS CLICKED THEN similar_word is executed and if pressed no then pressed_no function is executed

#these function also contains some clear function to clear contents of the entry or text widgets
#allthere are exit,okay buttons to destroy the windows
def main():
    window = Tk()#DECLARING THE MAIN WINDOW
    window.configure(bg="#FFA07A")#FOR ADDING BACKGROUND COLOR
    data = json.load(open("data.json"))#LOADING THE CONTENTS OF THE DATA JSON FILE IN THE DATA VARIABLE
    def clear():#FUNCTION TO CLEAR THE TEXT AND THE ENTRY WIDGET
        e1.delete(0,END)
        t1.delete('1.0', END) 




    def invalid_word():#FUNCTION FOR GENERATING W3 WINDOW
        w3=Tk()
        w3.configure(bg="#FFA07A")
        def clear2():
            e1.delete(0,END)
            t1.delete('1.0', END)
            w3.destroy()

        le = Label(w3,text="The word doesn't exist. Please double check it.",bg="#CE93D8",borderwidth=3)#IN CASE OF INVALID WORD
        le.grid(row=0,column=0,columnspan=10,padx=(10,10),pady=10)

        b7 = Button(w3,text="Okay",command=clear2,bg="#FFF176",borderwidth=3)#TO RETURN TO THE FIRST PAGE AND DESTROYING UNNECESSARY WINDOWS
        b7.grid(row=1,column=0,padx=(10,10),pady=20)
        w3.mainloop()





    def pure_correct():#THE FIRST FUNCTION THAT IS CALLED AFTER SEARCH BUTTON IS CLICKED
        def op(wr):
            output = data[wr]#SEARCHING THE MEANING IN JSON FILE AND STORING IT IN OUTPUT 
            if type(output) == list:
                for item in output:
                    t1.insert(END, item)
                    t1.insert(END,"\n")
            else:
                t1.insert(END,data[w])#DISPLAYING OUTPUT IN T1 TEXT BOX
                t1.insert(END,"\n")

        w=var1.get()#USING GET() METHOD TO ACCESS THE WORD TO BE SEARCHED
        t1.delete('1.0', END)#to delete the contents of entry wodget
        w = w.lower()
        #HERE WE ARE DEALING WITH DIFFEENT CASEFORMS OF A WORD TO FIND ITS MEANING
        if w in data:
            op(w)    
        elif w.title() in data:
            op(w.title())
        elif w.upper() in data:
            op(w.upper())       
        elif len(get_close_matches(w, data.keys())) > 0:
            when_wrong_word_is_entered_but_there_is_similar_word()
        else:
            invalid_word()







    def when_wrong_word_is_entered_but_there_is_similar_word():
        w2 = Tk()
        w2.configure(bg="#FFA07A")
        w=var1.get()            
        def Similar_word():#when yes is clicked
            w2.destroy()#CREATING WINDOW 2
            w4 = Tk()
            w4.configure(bg="#FFA07A")
            def clearw4():#to destroy window w4
                w4.destroy()
                e1.delete(0,END)
                t1.delete('1.0', END)
            t2=Text(w4,height=10,width=60,bg="#00FFFF")
            t2.grid(row=0,column=0,padx=10,pady=10)
            output = data[get_close_matches(w.lower(), data.keys())[0]]
            if type(output) == list: #IF OUTPUT IS A LIST ,THEN IT WILL ITERATED AND ELEMENTS WILL BE INSERTED EACH ON A NEW LINE
                for item in output:
                    t2.insert(END, item) 
                    t2.insert(END,"\n")
            else:#IF OUTPUT IS A STRING THEN IT WILL DIRECTLY INSERT THE STRING
                t2.insert(END,data[w])
                t2.insert(END,"\n")

            b7 = Button(w4,text="Search new word",command=clearw4,bg="#FFF176",borderwidth=3)
            b7.grid(row=1,column=0,columnspan=3,padx=(10,10),pady=20)
            w4.mainloop
            

        def pressed_no():#FUNCTION WHEN INVALID WORD/ NO IS CLICKED BY THE USER IN WINDOW 2
            w2.destroy()
            nayi_window = Tk()
            nayi_window.configure(bg="#FFA07A")
            def clear_nayi_window():#FUNCTION TO DESTROY WINDOW 2 AND 4
                nayi_window.destroy()
                e1.delete(0,END)
                t1.delete('1.0', END)
            le = Label(nayi_window,text="The word doesn't exist. Please double check it.",bg="#CE93D8",borderwidth=3)
            le.grid(row=0,column=0,columnspan=10,padx=(10,10),pady=10)
    
            b7 = Button(nayi_window,text="Exit",command=clear_nayi_window,bg="#FFF176",borderwidth=3)
            b7.grid(row=1,column=0,columnspan=3,padx=(10,10),pady=20)
            nayi_window.mainloop()




        #^^^^^^^ SECOND WINDOW TO TO ASK YES AND NO ^^^^^^^
        lw = Label(w2,text="Did you mean %s instead?" % get_close_matches(w.lower(), data.keys())[0],bg="#CE93D8",borderwidth=3)
        lw.grid(row=0,column=0,columnspan=10,padx=(10,10),pady=10)

        b6 = Button(w2,text="YES",command=Similar_word,bg="#FFF176",borderwidth=3)
        b6.grid(row=1,column=0,columnspan=3,padx=(10,10),pady=20)

        b7 = Button(w2,text="NO",command=pressed_no,bg="#FFF176",borderwidth=3)
        b7.grid(row=1,column=4,columnspan=3,padx=(10,10),pady=20)

        w2.mainloop()






######## CREATING FIRST WINDOW #############
    l1 = Label(window,text="Hey There! Welcome, Enter A Word :",bg="#CE93D8",borderwidth=3)
    l1.grid(row=0,column=0,columnspan=10,padx=(10,10),pady=10)

    var1=StringVar()
    e1=Entry(window,textvariable=var1,bg="#BDBDBD",borderwidth=2)
    e1.grid(row=1,column=0,columnspan=9)
    w=var1.get()

    b5 = Button(window,text="Search",command=pure_correct,bg="#FFF176",borderwidth=3)
    b5.grid(row=1,column=10,padx=10)

    b67 = Button(window,text="Clear",command=clear,bg="#FFF176",borderwidth=3)
    b67.grid(row=1,column=11,padx=10)

    t1=Text(window,height=10,width=50,bg="#00FFFF")
    t1.grid(row=2,column=0,padx=10,pady=10)
    window.mainloop()
main()