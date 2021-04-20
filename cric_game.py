import tkinter
from tkinter import *
import sports
import requests
import json
from pycricbuzz import Cricbuzz
from tkinter import messagebox

#this function is to get stats from sports.py 
def info():
   
    
    try:
        
        team1.set(e1.get().title())
        team2.set(e2.get().title())
        match_data=requests.get('http://cricapi.com/api/matches?apikey=Liq9wOptv4NAECh2XEqNHOCNIMp1')
        json_data=match_data.json()
        l3=json_data["matches"]
        unique_id1=[]
        json_data3=[]
        for i in range(len(l3)):
            if l3[i]["matchStarted"]==True and l3[i]["squad"]==True and (l3[i]["team-1"]==e1.get().title() or l3[i]["team-1"]==e2.get().title() and l3[i]["team-2"]==e1.get().title() or l3[i]["team-2"]==e2.get().title()):
                unique_id1.append(l3[i]["unique_id"])
                date.set(str(l3[i]["dateTimeGMT"]))
                league.set(str(l3[i]["type"]))
                toss.set(str(l3[i]['toss_winner_team']))
        for i in range(len(unique_id1)):
            match2=requests.get('http://cricapi.com/api/cricketScore?unique_id='+str(unique_id1[0])+\
                           '&apikey=Liq9wOptv4NAECh2XEqNHOCNIMp1')
            json_data3.append(match2.json())
        
        stat.set(str(json_data3[0]["stat"]))
        score.set(str(json_data3[0]["score"]))
        
        
        
        
    except:
        messagebox.showerror("showerror", "No match found")

        
#it will clear the entry widget
def clear():
    e1.delete(0, END) 
    e2.delete(0, END)
    l11.destroy()
    l12.destroy()
    l13.destroy()
    l14.destroy()
    l15.destroy()
    l16.destroy()
    l17.destroy()
    
    
    
    
#this function will gather data from API and show the upcoming matches on a new window   
def upcoming():
    stack=Tk()
    stack.title("Upcoming matches")
    stack.configure(bg="black")
    try:
        match_data=requests.get('http://cricapi.com/api/matches?apikey=Liq9wOptv4NAECh2XEqNHOCNIMp1')
        json_data=match_data.json()
        l=json_data["matches"]
        lb1=Listbox(stack,selectmode=NONE,height=25,width=90,bg="slate grey")
        for i in range (len(l)): 
            if l[i]["matchStarted"]==False:
                lb1.insert(i,str(l[i]["team-1"]+" vs "+str(l[i]["team-2"]+ "  Date:"+str(l[i]["dateTimeGMT"]))))
                lb1.grid(row=0)
    except:
        match_data=requests.get('https://api.api-cricket.com/cricket/?method=get_events&APIkey=5de3088a7c2f2d8e2a3dd7dba32581823434ac64204a8618f818d43c460d3ae1&date_start=2020-10-29&date_stop=2020-11-31')
        l1=match_data.json()
        l2=l1["result"]
        lb1=Listbox(stack,selectmode=NONE,height=25,width=90,bg="slate grey")
        for i in range(len(l2)):
            if l2[i]["event_live"]=='0':
                lb1.insert(i,l2[i]["event_home_team"]+" vs "+l2[i]["event_away_team"]+" date:"+l2[i]["event_date_start"] + " time:"+str(l2[i]["event_time"]))
                lb1.grid(row=0)

    
        
    stack.mainloop()
    
    
    
#to show live match info
def livematches():

    top=Tk()
   
    top.title("live matches")
    
    top.configure(bg="black")
    
    
    try:
        matches = sports.get_sport(sports.CRICKET) 
        lb=Listbox(top,height=25,width=80,bg="lime")
        for i in range (len(matches)): 
            lb.insert(i,str(matches[i]))
            lb.grid(row=0)
   
        l2=Label(top,text="View Match stats On Main Page By Entering Team Names",fg="white",bg="black")
        l2.grid(row=2,column=0)
    except:
        match_data=requests.get('http://cricapi.com/api/matches?apikey=Liq9wOptv4NAECh2XEqNHOCNIMp1')
        json_data=match_data.json()
        l=json_data["matches"]
        unique_id=[]
        json_data1=[]
        for i in range(len(l)):
            if l[i]["matchStarted"]==True and l[i]["squad"]==True:
                unique_id.append(l[i]["unique_id"])
        for i in range(len(unique_id)):
            match=requests.get('http://cricapi.com/api/cricketScore?unique_id='+str(unique_id[i])+\
                       '&apikey=Liq9wOptv4NAECh2XEqNHOCNIMp1')
            json_data1.append(match.json())
        lb=Listbox(top,height=25,width=80,bg="slate grey",fg="white")
        for i in range(len(json_data1)):
            lb.insert(i,str(json_data1[i]["score"])+" "+ str(json_data1[i]["stat"]))
            lb.grid(row=0)
        l2=Label(top,text="View Match stats On Main Page By Entering Team Names",fg="white",bg="black")
        l2.grid(row=2,column=0)
    top.mainloop()
    
def completed():

    master=Tk()
    master.title("completed matches")
    try:
        match_data=requests.get('https://api.api-cricket.com/cricket/?method=get_events&APIkey=5de3088a7c2f2d8e2a3dd7dba32581823434ac64204a8618f818d43c460d3ae1&date_start=2020-10-30&date_stop=2020-11-3')
        l1=match_data.json()
        l2=l1['result']
        
        lb=Listbox(master,height=25,width=95,bg="slate grey",fg="white")
        for i in range(len(l2)):
            if l2[i]["event_live"]=='0' and l2[i]["event_status"]!=None and l2[i]["event_status_info"]!=None:
                lb.insert(i,l2[i]["event_home_team"]+" "+str(l2[i]["event_home_final_result"])+" vs "+str(l2[i]["event_away_final_result"])+l2[i]["event_away_team"]+" status:"+str(l2[i]["event_status"])+" "+str(l2[i]["event_status_info"]))
                lb.grid(row=0)
        
    except:
        match_data=requests.get('http://cricapi.com/api/matches?apikey=Liq9wOptv4NAECh2XEqNHOCNIMp1')
        json_data=match_data.json()
        l=json_data["matches"]
        unique_id=[]
        json_data1=[]
        for i in range(len(l)):
            if l[i]["matchStarted"]==True and l[i]["squad"]==True:
                unique_id.append(l[i]["unique_id"])
        for i in range(len(unique_id)):
            match=requests.get('http://cricapi.com/api/cricketScore?unique_id='+str(unique_id[i])+\
                       '&apikey=Liq9wOptv4NAECh2XEqNHOCNIMp1')
            json_data1.append(match.json())
        lb=Listbox(master,height=25,width=80,bg="slate grey",fg="white")
        for i in range(len(json_data1)):
            lb.insert(i,str(json_data1[i]["score"])+" "+ str(json_data1[i]["stat"]))
            lb.grid(row=0)
    
    
   
    master.mainloop()
    
#the main window configuration begins from here
root = Tk()     
root.configure(background = 'powder blue') 
root.title("SSK")
root.geometry("900x400") 
  

Label(root,text="",fg="indigo",bg="indigo",padx=30,pady=20).grid(row=0,column=0)
Label(root,text="",fg="indigo",bg="indigo",padx=30,pady=20).grid(row=0,column=2)
headlabel = Label(root, text = 'S.S.K. Cricketing  App  ', fg = 'white', bg = "indigo",padx=10,pady=10) 
headlabel.config(font=("Courier", 28))
headlabel.grid(row = 0,column=1) 



label1=Label(root,text="© copyright subjected to subid,sathwik and kushal co.. ")
label1.grid(row=14,columnspan=3,sticky=S)








label2=Label(root,text="Check Match Stats Here:",bg="powder blue")
label2.grid(row=2,column=0,sticky=W)


  
            
date = StringVar()
stat = StringVar()
toss=StringVar()
league = StringVar() 
team1=StringVar()
team2=StringVar()
score = StringVar() 



   
l1=Label(root, text="Enter Team 1 :" , bg = "powder blue")  
l1.grid(row=4, sticky=W) 
l2=Label(root, text="Enter Team 2 :" , bg = "powder blue")
l2.grid(row=5, sticky=W) 
l3=Label(root, text="Date and Time:" , bg = "powder blue")
l3.grid(row=6, sticky=W) 
l10=Label(root, text="Toss winner:" , bg = "powder blue")
l10.grid(row=7, sticky=W)
l4=Label(root, text="Stat :", bg = "powder blue")
l4.grid(row=8, sticky=W) 
l5=Label(root, text="League :", bg = "powder blue")
l5.grid(row=9, sticky=W) 
l6=Label(root, text="Team 1 :", bg = "powder blue")
l6.grid(row=10, sticky=W) 
l7=Label(root, text="Team 2 :", bg ="powder blue")
l7.grid(row=11, sticky=W) 

l9=Label(root, text="score :", bg = "powder blue")
l9.grid(row=12, sticky=W) 

    

e1 = Entry(root) 
e1.grid(row=4, column=1,sticky=W) 
  
e2 = Entry(root) 
e2.grid(row=5, column=1,sticky=W) 
    
l11=Label(root, textvariable= stat ,bg = "powder blue")
l11.grid(row=8,column=1, sticky=W) 
l12=Label(root, text="", textvariable= date ,bg = "powder blue")
l12.grid(row=6,column=1, sticky=W) 
         
         
l13=Label(root, text="", textvariable= toss ,bg = "powder blue")
l13.grid(row=7,column=1, sticky=W) 
         
l14=Label(root, text="", textvariable= league ,bg = "powder blue")
l14.grid(row=9,column=1, sticky=W) 


l15=Label(root,text="",textvariable=team1 ,bg = "powder blue")
l15.grid(row=10,column=1, sticky=W)

l16=Label(root,text="", textvariable=team2 ,bg = "powder blue")
l16.grid(row=11,column=1, sticky=W) 

l17=Label(root, text="", textvariable= score ,bg = "powder blue")
l17.grid(row=12,column=1, sticky=W) 

      
     
e1 = Entry(root) 
e1.grid(row=4, column=1,sticky=W) 
  
e2 = Entry(root) 
e2.grid(row=5, column=1,sticky=W) 

button1 = Button(root, text = "Live Matches   ",padx=30,pady=20,command=livematches)
button1.grid(row = 1, column = 0) 
  
button2 = Button(root, text = "Upcoming Matches",padx=30,pady=20,command=upcoming) 
button2.grid(row = 1, column = 2) 

button3 = Button(root, text = "completed Matches",padx=30,pady=20,command=completed) 
button3.grid(row = 1, column = 1) 


    
b = Button(root, text="Show",bg="powder blue", command=info) 
b.grid(row=4, column=2,columnspan=2, rowspan=2,padx=5, pady=5,sticky=W)
b1 = Button(root, text="Clear",bg="powder blue", command=clear) 
b1.grid(row=5, column=2,columnspan=2, rowspan=2,padx=5, pady=5,sticky=W)
  




root.mainloop() 
