import tkinter as tk
from tkinter import ttk
import tkinter
from tkinter import *
from functools import partial
from PIL import ImageTk, Image
from tkinter import filedialog
import os
import knn

BUTTON_COLOR = "peachPuff2"

def getResults():
    results = []
    for i in range(20):
        results.append(0)

    questions=[
              ["?איך היית מגדיר את בת הזוג שלך","רומנטית","מצחיקה","אנרגטית","נבונה","מיסתורית","רוחנית"],
              ["?עד כמה חשוב לה להיות ייחודית",-1],
              ["כשהיא בסביבת אנשים, היא","אוהבת להתמזג בסביבה","אוהבת לבלוט"],
              ["?מהו הבילוי האולטימטיבי עבורה","בבית, על הספה מול הטלוויזיה","מסיבה מטורפת","מסע שופינג","מסעדה יוקרתית","ספורט"],
              ["?מה יחסיה עם אומנות","אומנות היא החיים עבורה","היא מעריכה אומנות, אבל היא לא קוסמת לה יותר מידי","היא לא מבינה את רוב יצירות האומנות","היא נהנת במיוחד מאומנות פרובוקטיבית"],
              ["?מה לדעתך היא חושבת שאומנות אמורה לייצג","נפש האדם","מציאות","אהבה","היסטוריה"],
              ["?מה היא מחפשת ביצירת אומנות","סיפור","אסתטיקה","פשטות","תשוקה","מרד"],
              ["?מהו הצבע האהוב עליה","לבן","ירוק/טורקיז","כחול/תכלת","ורוד","צהוב","סגול","שחור","אדום","חום"],
              ["?איזה סגנון עיצוב היא תעדיף","קלאסי","בוהו שיק","מודרני","'וינטג"],
              ["?איך היית מגדיר את הסטייל שלה","רגוע","אופנתי","נשי","נועז"],
              ["?כמה תכשיטים היא עונדת כרגע",-1],
              ["?באיזה צבע רוב התכשיטים שלה","זהב צהוב","זהב לבן","זהב אדום"],
              ["?כמה תכשיטי יהלומים יש לה",-1],
              ["?האם היא מעדיפה תכשיטים צבעוניים או ניטרליים","ניטרליים","צבעוניים"],
              ["?האם התכשיטים שלה עדינים או מאסיבים","עדינים","מאסיבים"],
              ["?האם היא אוהבת לשלב בלבוש שלה צבעים","לא","כן"],
              ["?האם את חושבת שתכשיט יקר הוא תכשיט איכותי","לא","כן"],
              ["?מה חשוב לה יותר, להיראות טוב או להרגיש בנוח","תלוי לאן היא הולכת","להרגיש בנוח","להיראות טוב"],
              ["?איך היא מתאפרת לעבודה","איפור עדין, במראה טבעי","היא לא מתאפרת בכלל","איפור עם נוכחות"],
              ["?עד כמה היא יצירתית", -1],
    ]

    global current
    current=-1
    surveyRoot=tk.Tk()
    surveyRoot.title("ring survey")
    surveyRoot.geometry("800x800")
    #surveyRoot.attributes("-fullscreen", True)
    #surveyRoot.geometry('1200x1000+350+5')


    def start():
        global current
        current+=1
        if current==0:
            title.destroy()
            button.place(relx=0.5,rely=0.9,anchor=CENTER)
            button.config(text="שאלה הבאה",command=start)
            button['state']='disabled'
            global mainFrame
            mainFrame=tk.Frame(surveyRoot,width=1200,height=400)
            mainFrame.place(relx=0.5,rely=0.5,anchor=CENTER)
        if current!=0:
            button['state'] = 'disabled'
            for widgets in mainFrame.winfo_children():
                widgets.destroy()
        if current == 20:
            print(results)
            button.destroy()
            ring_result = knn.run_from_gui(results) #SEND TO KNN ALGO
            endLabel=tk.Label(mainFrame, text=" התוצאה: " + ring_result, font=("Segoe UI Semibold", 30))
            endLabel.place(relx=0.5, rely=0.2, anchor=CENTER)
            photoArrS = [tkinter.PhotoImage(file="img/s1.png"), tkinter.PhotoImage(file="img/s2.png"),
                        tkinter.PhotoImage(file="img/s3.png"), tkinter.PhotoImage(file="img/s4.png"),
                        tkinter.PhotoImage(file="img/s5.png")]
            photoArrNS = [tkinter.PhotoImage(file="img/ns1.png"), tkinter.PhotoImage(file="img/ns2.png"),
                        tkinter.PhotoImage(file="img/ns3.png"), tkinter.PhotoImage(file="img/ns4.png"),
                        tkinter.PhotoImage(file="img/ns5.png")]
            frame = tk.Frame(surveyRoot, width=800, height=150)
            frame.place(relx=0.5, rely=0.9, anchor=S)
            if ring_result == "טבעת סטנדרטית (טבעת יהלום)":
                endLabel2 = tk.Label(mainFrame,
                                     text=".בת הזוג שלך מעדיפה את העיצוב המסורתי והקלאסי של טבעת האירוסין\n .העיצוב צריך להיות נקי ואלגנטי ובמרכז הטבעת אבן\n ...היא לא תתנגד ליהלום מנצנץ",
                                     font=("Segoe UI Semilight", 18), fg="peachpuff4")
                endLabel2.place(relx=0.5, rely=0.5, anchor=CENTER)
                for i in range(5):
                    canvas = tk.Canvas(frame, width=150, height=150)
                    photoA = photoArrS[i]
                    canvas.photoA = photoA
                    canvas.create_image(75, 75, anchor=CENTER, image=photoA)
                    canvas.grid(row=0, column=i, padx=30)
            else:
                endLabel2 = tk.Label(mainFrame,
                                     text=".בת הזוג שלך מעדיפה את הטבעת הלא מסורתית, בעלת עיצוב ייחודי \n .בחר טבעת שתתן לה השראה, שתספר סיפור \n .חפש אבן יחודית, צורה מעניינת או צבעוניות",
                                     font=("Segoe UI Semilight", 18), fg="peachpuff4")
                endLabel2.place(relx=0.5, rely=0.5, anchor=CENTER)
                for i in range(5):
                    canvas = tk.Canvas(frame, width=150, height=150)
                    photoA = photoArrNS[i]
                    canvas.photoA = photoA
                    canvas.create_image(75, 75, anchor=CENTER, image=photoA)
                    canvas.grid(row=0, column=i, padx=30)
            return

        def choice(num,type):
            button['state']='normal'
            if type==1:
                chosenLabel.grid(row=1,column=num+1)
            elif type==-1:
                chosenLabel.grid(row=2, column=num)
            results[current]=num
            print(results)
        question=tk.Label(mainFrame, text=questions[current][0], font=("Segoe UI Semilight", 25),fg="peachpuff4")
        question.place(relx=0.5,rely=0.1,anchor=N)
        answersFrame = tk.Frame(mainFrame, width=20, height=20)
        answersFrame.place(relx=0.5,rely=0.5,anchor=CENTER)
        chosenLabel = tk.Label(answersFrame, text="נבחר", font=("Segoe UI Light", 10))
        if questions[current][1]!=-1 and questions[current][1]!=0:
            for i in range(1,len(questions[current])):
                #global vMarkPhoto
                tk.Button(answersFrame, text=questions[current][i],bg="white smoke", font=("Segoe UI Semilight", 13),command=partial(choice,i-1,1)).grid(row=0,column=i,stick=E,padx=25)
        elif questions[current][1]==-1:
            for i in range(11):
                tk.Button(answersFrame,text=i, font=("Segoe UI Semilight", 15), command=partial(choice, i ,-1), bg="white smoke").grid(row=1, column=i,padx=20)


    button=tk.Button(surveyRoot, text="התחל", font=("Segoe UI Semibold", 20), command=start, bg=BUTTON_COLOR)
    survey_name=tk.Label(surveyRoot, text="Engagement Ring Style finder", font=("Segoe UI Semilight", 15), fg="peachpuff4")
    title=tk.Label(surveyRoot, text="? מחפש את טבעת האירוסין המושלמת עבור אישתך לעתיד\n\n ענה על 20 שאלות \n ותגלה איזו טבעת אירוסין היא תעדיף", font=("Segoe UI Semilight", 22))
    img = tk.PhotoImage(file="ring.png")
    label_img = tk.Label(surveyRoot, image=img)
    label_img.pack(side=tk.TOP)
    survey_name.place(relx=0.5, rely=0.3, anchor=CENTER)
    title.place(relx=0.5,rely=0.5,anchor=CENTER)
    button.place(relx=0.5,rely=0.8,anchor=CENTER)

    surveyRoot.mainloop()
    return results

print(getResults())