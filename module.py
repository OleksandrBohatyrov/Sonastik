from gtts import *
from random import *
import os
def loe_failist(f):
    fail=open(f,'r',encoding="utf-8-sig")
    mas=[] 
    for rida in fail:
        mas.append(rida.strip())
    fail.close()
    return mas
def list_failisse(f,list_):
    fail=open(f,'w',encoding="utf-8-sig")
    for k in list_:
        fail.write(k+"\n")
    fail.close()
    return list_
def salvesta_failisse(f,text):    
    fail=open(f,'a',encoding="utf-8-sig")
    fail.write(text+"\n")
    fail.close()
    mas=[]
    mas=loe_failist(f)
    return mas
def uued_sonad():
    rus_sona=input("Введи слово на русском:")
    est_sona=input("Sisesta sõna eesti keeles:")
    rus_list=salvesta_failisse("rus.txt",rus_sona)
    est_list=salvesta_failisse("est.txt",est_sona)
    return rus_list, est_list
def tolkimine(rus_list,est_list):
    slovo=input("Введите слово для перевода: ")
    if slovo in rus_list:
        ind=rus_list.index(slovo)
        print(f"{slovo} - {est_list[ind]}")
    elif slovo in est_list:
        ind=est_list.index(slovo)
        print(f"{slovo} - {rus_list[ind]}")
    else:
        print(f"{slovo.upper()} отсутствует в словаре")
        v=input("Желаете добавить слово в словарь?")
        if v.lower()=="да": uued_sonad()
def parandus(rus_list,est_list):
    viga=input("Введите слово с ошибкой: ")
    if viga in rus_list:
        ind=rus_list.index(viga)#index
        print(f"Будет исправлена пара слов{viga} - {est_list[ind]}")
        rus_list.pop(ind)
        est_list.pop(ind)
        rus_list=list_failisse("rus.txt",rus_list)
        est_list=list_failisse("est.txt",est_list)
        uued_sonad()
        
    elif viga in est_list:
        ind=est_list.index(viga)
        print(f"Будет исправлена пара слов{viga} - {rus_list[ind]}")
        rus_list.pop(ind)
        est_list.pop(ind)
        rus_list=list_failisse("rus.txt",rus_list)
        est_list=list_failisse("est.txt",est_list)
        uued_sonad()
    else:
        print(f"{viga.upper()} отсутствует в словаре")
    rus_list=loe_failist("rus.txt")
    est_list=loe_failist("est.txt")
    return rus_list,est_list

def game(rus_list,est_list):
    x=[]
    v=k=0
    rus,est=(rus_list,est_list)
    numb=input("Сколько игр вы хотите сыграть? ")
    for i in range(int(numb)):
        num=randint(0,(len(rus)-1))
        while num in x:
            num=randint(0,(len(rus)-1))
    try:
        keel=input("На каком языке вы хотите играть?\n1-русский\n2-эстонский ").lower()
    except:
        print("Value Error")
    if keel==1:                                               #russian language
        tolk=input(f"Как переводиться {rus[num]} правильно? ") 
        if tolk==est[num]:
            game.append(f"{i+1} {keel} ответ - правильный")
            print("Правильно") 
            v+=1
        else:
            game.append(f"{i+1}, {keel} ответ - неправильный") 
            print("Неправильно")
            k+=1
    elif keel==2:                                                              #eesti
        tolk=input(f"Как переводиться {est[num] } правильно? ") 
        if tolk==rus[num]:
            game.append(f"{i+1} {keel} ответ - правильный")
            print("правильно")
            v+=1
        else:
            game.append(f"{i+1}, {keel} ответ - неправильный") 
            print("Неправильно")
            k+=1
    x.append(num)
    resV=round((v/num*100),1)
    resK=round((k/num*100),1)
    print(f"Процент выигрыша - {resV}%")
    print(f"Процент потерь - {resK}%")
