import tkinter as tk
from tkinter import Message ,Text
import cv2,os
import shutil
import csv
import numpy as np
import pandas as pd
import tkinter.ttk as ttk
import tkinter.font as font
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics

def call():
    winnn=tk.Tk()
    possible=0
    aa=txt.get()
    bb=txt1.get()
    cc=txt2.get()
    dd=txt3.get()
    ee=txt4.get()
    ff=txt5.get()
    gg=txt6.get()
    hh=txt7.get()
    size=ee
    if(hh=='no'):
        bad12=tk.Label(winnn,text="Cannot provide loan as no own land",width=50  ,height=2  ,fg="#DF744A"  ,bg="#FEDCD2" ,font=('Arial Rounded MT Bold', 15, ' bold ') )
        bad12.place(x=400,y=300)
    else:    
        c=ff.strip().lower()
        print(c)
        if(c=='paddy'):
            c1=1
        elif(c=='wheat'):
            c1=2
        elif(c=='sugarcane'):
            c1=3
        else:
            c1=0
        d2=dd.strip().lower()
        if(d2=='andhrapradesh'):
            d1=1
        elif(d2=='tamilnadu'):
            d1=2
        elif(d2=='westbengal'):
            d1=3
        elif(d2=='madhyapradesh'):
            d1=4
        elif(d2=='punjab'):
            d1=5
        elif(d2=='gujarat'):
            d1=6
        elif(d2=='haryana'):
            d1=7
        elif(d2=='rajasthan'):
            d1=8
        elif(d2=='uttarakhand'):
            d1=9
        else:
            d1=0
       
        cop=0
        d=pd.read_csv('https://raw.githubusercontent.com/vchar1299/crop/master/Crop_temprain.csv')
        data=pd.read_csv('https://raw.githubusercontent.com/vchar1299/crop/master/Temprain_requ.csv')
        d.fillna(method='bfill',inplace=True)
        set1=data[data['Crop']==c1]

        d=d[d['State']==d1]
        d=d[d['Crop']==c1]
        y=np.array(d['Temperature']).reshape(-1,1)
        X=d.drop('Temperature',1)
        try:
            reg=LinearRegression()
            reg.fit(X,y)
            predictions=reg.predict(X)
            print(predictions[0])
            kk=predictions[0]
            if(float(set1['Min_temp'])<=kk and kk<=float(set1['Max_temp'])):
                 possible+=1
            else:
                sadn="Crop can't be grown in this region"
        except ValueError:
            neg_str="not possible"
        y=np.array(d['Rainfall']).reshape(-1,1)
        X=d.drop('Rainfall',1)
        try:
            reg=LinearRegression()
            reg.fit(X,y)
            predictions=reg.predict(X)
            p=np.array(predictions)
            po=predictions[0]
            l=len(p)
            h=p.mean()
            if(c=='sugarcane'):
                po=po/2.5
            elif(c=='wheat'):
                po=po/12
            elif(c=='paddy'):
                po=po/5
            if(float(set1['Min_rain'])<=po and po<=float(set1['Max_rain'])):
                possible+=1
            else:
                sadne="Crop can't be grown in this region"
           
        except ValueError:  
            sad_news="Crop cannot be grown in this region"
        if(possible==2):
            cop=1  
        if(cop==0):
            sadbut=tk.Label(winnn,text="Cannot grow crop so cannot provide loan",width=50  ,height=2  ,fg="#DF744A"  ,bg="#FEDCD2" ,font=('Arial Rounded MT Bold', 15, ' bold ') )
            sadbut.place(x=600,y=300)
        elif(cop==1):
            das=pd.read_csv('https://raw.githubusercontent.com/vchar1299/crop/master/Crop_Cost.csv')
            das=das[das['Crop']==c1]
            cos_of_cul=das['Cost_of_cultivation_per_acre']
            yield_quin=das['yield_quintal_per_acre']
            spp=das['SP_per_quintal']
            l=[]
            l.append(int(cos_of_cul[0])*int(size))
            l.append(int(yield_quin[0])*int(size))
            l[1]=l[1]*0.0204
            l[1]=l[1]*spp[0]
            going=l[0]
            coming=l[1]
            give=0.75*coming
            good2=tk.Label(winnn,text="Profit Amount",width=20  ,height=2  ,fg="#DF744A"  ,bg="#FEDCD2" ,font=('Arial Rounded MT Bold', 15, ' bold ') )
            good22=tk.Label(winnn,text=str(coming),width=20  ,height=2  ,fg="#DF744A"  ,bg="#FEDCD2" ,font=('Arial Rounded MT Bold', 15, ' bold ') )
            good3=tk.Label(winnn,text="Loan that can be obtained",width=20  ,height=2  ,fg="#DF744A"  ,bg="#FEDCD2" ,font=('Arial Rounded MT Bold', 15, ' bold ') )
            good32=tk.Label(winnn,text=str(give),width=20  ,height=2  ,fg="#DF744A"  ,bg="#FEDCD2" ,font=('Arial Rounded MT Bold', 15, ' bold ') )
            good2.place(x=400,y=300)
            good22.place(x=700,y=300)
            good3.place(x=400,y=400)
            good32.place(x=700,y=400)
window = tk.Tk()
window.title("Bank Loan")

dialog_title = 'QUIT'
dialog_text = 'Are you sure?'
window.configure(background='#BFD8D2')

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)


message = tk.Label(window, text="Bank loan helpline" ,bg="#008F95"  ,fg="#E24E42"  ,width=50  ,height=3,font=('Baskerville Old Face', 30, 'bold underline'))

message.place(x=200, y=20)


lbl = tk.Label(window, text="Name",width=20  ,height=2  ,fg="#DF744A"  ,bg="#FEDCD2" ,font=('Arial Rounded MT Bold', 15, ' bold ') )
lbl.place(x=400, y=200)
txt = tk.Entry(window , width=20  ,bg="WHITE" ,fg="BLACK",font=('times', 15, ' bold '))
txt.place(x=700, y=200)

lbl = tk.Label(window, text="Account Number",width=20  ,height=2  ,fg="#DF744A"  ,bg="#FEDCD2" ,font=('Arial Rounded MT Bold', 15, ' bold ') )
lbl.place(x=400, y=250)

txt1 = tk.Entry(window,width=20  ,bg="WHITE" ,fg="BLACK",font=('times', 15, ' bold '))
txt1.place(x=700, y=250)

lb2 = tk.Label(window, text="District",width=20  ,height=2  ,fg="#DF744A"  ,bg="#FEDCD2" ,font=('Arial Rounded MT Bold', 15, ' bold ') )
lb2.place(x=400, y=300)

txt2 = tk.Entry(window,width=20  ,bg="WHITE" ,fg="BLACK",font=('times', 15, ' bold '))
txt2.place(x=700, y=300)
lb3 = tk.Label(window, text="State",width=20  ,height=2  ,fg="#DF744A"  ,bg="#FEDCD2" ,font=('Arial Rounded MT Bold', 15, ' bold ') )
lb3.place(x=400, y=350)

txt3 = tk.Entry(window,width=20  ,bg="WHITE" ,fg="BLACK",font=('times', 15, ' bold '))
txt3.place(x=700, y=350)
lb4 = tk.Label(window, text="Land size",width=20  ,height=2  ,fg="#DF744A"  ,bg="#FEDCD2" ,font=('Arial Rounded MT Bold', 15, ' bold ') )
lb4.place(x=400, y=400)

txt4 = tk.Entry(window,width=20  ,bg="WHITE" ,fg="BLACK",font=('times', 15, ' bold '))
txt4.place(x=700, y=400)

lb5 = tk.Label(window, text="Crop",width=20  ,height=2  ,fg="#DF744A"  ,bg="#FEDCD2" ,font=('Arial Rounded MT Bold', 15, ' bold ') )
lb5.place(x=400, y=450)

txt5 = tk.Entry(window,width=20  ,bg="WHITE" ,fg="BLACK",font=('times', 15, ' bold '))
txt5.place(x=700, y=450)

lb6 = tk.Label(window, text="Required Loan amount",width=20  ,height=2  ,fg="#DF744A"  ,bg="#FEDCD2" ,font=('Arial Rounded MT Bold', 15, ' bold ') )
lb6.place(x=400, y=500)

txt6 = tk.Entry(window,width=20  ,bg="WHITE" ,fg="BLACK",font=('times', 15, ' bold '))
txt6.place(x=700, y=500)

lb7 = tk.Label(window, text="Own land",width=20  ,height=2  ,fg="#DF744A"  ,bg="#FEDCD2" ,font=('Arial Rounded MT Bold', 15, ' bold ') )
lb7.place(x=400, y=550)

txt7 = tk.Entry(window,width=20  ,bg="WHITE" ,fg="BLACK",font=('times', 15, ' bold '))
txt7.place(x=700, y=550)

bb2=tk.Button(window,command=call,width=20  ,height=2, text="Confirm")
bb2.place(x=700,y=600)


window.mainloop()
