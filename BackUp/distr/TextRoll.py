import os
import sys
import random

import win32clipboard
import datetime

Path = str(os.getcwd())
sys.path.append(Path)

import Choosing

while True:
    try:
        DicePull = int(input('Запас кубов: '))
        print('------------------')
        if DicePull not in list(range(1, 51)): print('!!! Введи целое число от 1 до 50')
        else: break
    except: print('!!! Введи целое число от 1 до 50')


while True:
    try:
        NumRoll = int(input('Кол-во бросков: '))
        print('------------------')
        if NumRoll not in list(range(1,51)): print('!!! Введи целое число от 1 до 50')
        else: break
    except: print('!!! Введи целое число от 1 до 50')

print("Есть ли переброс неудачных кубов? (+/-) ")
while True:
    PERC = input()
    if PERC == '+':
        PERC = True
        break
    elif PERC == '-':
        PERC = False
        break
    else: print('Введи "+" или "-"')

print('Что добрасывается ("взрывается", качество, способности):')
print(' 0. Доброс 10 (обычные качество)')
print(' 1. Доброс 9 и 10 (хорошее качество)')
print(' 2. Доброс 8, 9, 10 (отличное качество)')
print('-1. Запрет доброса 10 (плохое качество)')
print('-2. Вычитается один успех из броска (ужасное качество)')

while True:
    try:
        print('------------------')
        Q = int(input('Что добрасывается: '))
        if Q not in list(range(-2, 3)): print('!!! Введи целое число от -2 до 2')
        else:
            if Q == 0:
                LuckRR = [-1, 0]
                LuckRR.remove(-1)
                LuckRR = tuple(LuckRR)
                LuckR = (8,9)
                LuckDel = False
            elif Q == 1:
                LuckRR = (9, 0)
                LuckR = [-1, 8]
                LuckR.remove(-1)
                LuckR = tuple(LuckR)
                LuckDel = False
            elif Q == 2:
                LuckRR = (8, 9, 0)
                LuckR = ()
                LuckDel = False
            elif Q == -1:
                LuckRR = ()
                LuckR = (8, 9, 0)
                LuckDel = False
            elif Q == -2:
                LuckRR = ()
                LuckR = (8, 9, 0)
                LuckDel = True
            else: print('Что-то пошло не так с качеством')
            Luck = LuckRR + LuckR
            break
    except: print('!!! Введи целое число от -2 до 2')

while True:
    try:
        OM = int(input('Основной модификатор (+успехи): '))
        print('------------------')
        if OM not in list(range(-5, 6)): print('!!! Введи целое число от -5 до 5')
        else: break
    except: print('!!! Введи целое число от 0 до 5')


while True:
    try:
        WillPower = int(input('Сколько тратишь ПСВ?: '))
        print('------------------')
        if WillPower not in list(range(0, NumRoll+1)):
            print('!!! Введи целое число от 0 до', NumRoll)
        else: break
    except: print('!!! Введи целое число от 0 до', NumRoll)


LuckGlobal = DramAll = i = r = y = 0
RandList, lall, Roll = [], [], []
WPCh = False

if PERC == True: PERCplus = 2
else: PERCplus = 1

RandListCount = NumRoll * DicePull * PERCplus * 2

while RandListCount >= i:
    RandList.append(random.randint(0, 9))
    i = i + 1
#print(RandList)
#print(RandList.count(1))
#print(RandList.count(8))
#print(RandList.count(9))
#print(RandList.count(0))

DetailedText = ''
print("Сохранять лог? (+/-) ")
while True:
    txt = input()
    if txt == '+':
        DetailedText += ('Запас кубов: '+str(DicePull)+'\n')
        DetailedText += ('Кол-во бросков: '+str(NumRoll)+'\n')
        DetailedText += ('Что добрасывается (качество, свойства) (0=Обычное): '+str(Q)+'\n')
        DetailedText += ('Основной модификатор (+ успехи): '+str(OM)+'\n')
        DetailedText += ('Есть ли переброс неудачных кубов: '+str(PERC)+'\n')
        DetailedText += ('ПСВ (на переброс или +3 куба): '+str(WillPower)+'\n')
        break
    elif txt == '-': break
    else: print('Введи "+" или "-"')



DetailedText+=('\n')
DetailedText+=('--------------\n')
DetailedText+=('--------------\n')
DetailedText+=('--------------\n')
DetailedText+=('\n')



JoinText = 'Кубы:'+str(DicePull)+' Броски:'+str(NumRoll)+' ПСВ:'+str(WillPower)+' Q:'+str(Q)+' OM:'+str(OM)+' RR:'+str(PERC)+'\r\n'

while y < NumRoll:
    DetailedText += ('\n')
    DetailedText += ('\n')
    DetailedText += ('\n')
    DetailedText += ('---> Бросок №'+str(y+1)+' <---\n')

    if WillPower > 0:
        if PERC == False: DicePullTMP = DicePull+3
        else: DicePullTMP = DicePull
    else:
        WPCh = True
        DicePullTMP = DicePull
        
    DPch=DicePullTMP
    DicePullR0=0
    y=y+1

    JoinText+=str(y)+'. '
    
    x=0
    Roll=[]
    LuckCount=0
    DramCount=0
    while x < DicePullTMP+DicePullR0:
        if (x+1)//10>=1: Space=7
        else: Space=8
        
        Roll.append(RandList[r])

        ShortText, LongText, LuckCount, DramCount, DicePullR0, DicePullTMP = Choosing.main(x, Roll[x], Luck, LuckRR, LuckR, WillPower, DicePullTMP, DicePullR0, LuckCount, PERC, DramCount, Space, RandList, r)

        DetailedText+=LongText
        JoinText+=ShortText

        if x==(DPch-1):
            DetailedText+=('--------------\n')
            JoinText=JoinText[:-2]+': '

        r=r+1
        x=x+1
    if JoinText[-2:-1]=='-': JoinText=JoinText[:-2]
    if JoinText[-2:-1]==':': JoinText=JoinText[:-2]+'---> '
    else: JoinText+='---> '

    if OM!=0:
        if LuckCount>0:
            DetailedText+=('      >>> OM <<<         успехи '+str(OM)+'\n')
            LuckCount+=OM
    
    if LuckDel==True:
        if LuckCount>0:
            DetailedText+=('>>> Ужасное качество <<< -успех\n')
            LuckCount-=1
    
    if LuckCount<0:LuckCount=0
    DetailedText+=('Успехов = '+str(LuckCount)+'     Единиц = '+str(DramCount)+' \n')

    if DramCount > LuckCount:
        LuckCount = -DramCount
        DetailedText+=('   >>> Драмат <<<        -успехи\n')
        DetailedText+=('Успех = '+str(LuckCount)+'\n')
    elif LuckCount==0:
        DetailedText+=('Успехов не набрано => -1 куб\n')
        DicePull=DicePull-1
    elif LuckCount>=5:
        Except=LuckCount-4
        DetailedText+=('   >>> Except <<<        '+str(LuckCount)+' это '+str(LuckCount+Except)+'\n')
        LuckCount+=Except
    
    LuckGlobal=LuckGlobal+LuckCount
    JoinText+=str(LuckCount)+'\r\n'
    if WillPower>0: WillPower=WillPower-1
    if WillPower==0 and WPCh==False:
        if y!=NumRoll: DetailedText+=('   >>> WillPower OFF <<<\n')
        WPCh=True

    lall.append(LuckCount)

    if LuckGlobal//10>=1:
        Spam=5
        SpamG=22
    else:
        Spam=6
        SpamG=23
    
    if y==NumRoll or DicePull==0: DetailedText+=('+'*SpamG+' \n')
    DetailedText+=('+'*Spam+' Успех = '+str(LuckGlobal)+' '+'+'*Spam+' \n')
    
    if y==NumRoll or DicePull==0: DetailedText+=('+'*SpamG+' \n')
    if DicePull==0:
        DetailedText+=('Кубов не осталось\n')
        break

DetailedText+=('\n')
DetailedText+=('\n')
DetailedText+=('\n')

JoinText+='>>> '+str(LuckGlobal)+' <<<'


if txt=='+':
    
    now = datetime.datetime.now()
    FileName = now.strftime("%DramAll-%m-%Y %H-%M-%S")

    with open(Path+'\\try '+FileName+'.txt', "w") as file:
        file.write(DetailedText)

print(DetailedText)
print('Текст ниже скопирован в буфер обмена')
print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
print(JoinText)


win32clipboard.OpenClipboard()
win32clipboard.EmptyClipboard()
win32clipboard.SetClipboardText(JoinText)

win32clipboard.CloseClipboard()

while True:
    Finish=input('Введи + и нажми Enter для окончания программы ')
    if Finish=='+':break
