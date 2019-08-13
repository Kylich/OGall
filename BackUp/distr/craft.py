import os, sys

Path=str(os.getcwd())
sys.path.append((Path, Path+'\\BluePrints', Path+'\\Crafters'))

ListDirBP, ListDirCR = os.listdir(Path+'\\BluePrints'), os.listdir(Path+'\\Crafters')

ListDirBP.remove('__pycache__')
ListDirCR.remove('__pycache__')

if 'desktop.ini' in ListDirCR:ListDirCR.remove('desktop.ini')
if 'desktop.ini' in ListDirBP:ListDirBP.remove('desktop.ini')

x=0
while x != len(ListDirBP):
	ListDirBP[x]=ListDirBP[x].replace('.py',''); x=x+1
x=0
while x != len(ListDirCR):
	ListDirCR[x]=ListDirCR[x].replace('.py',''); x=x+1


BluePrintIn, BluePrintOut = False, False

print("Есть ли Сохраненный лист Чертежа? (+/-)")
while not (BluePrintOut==True or BluePrintIn==True):
	IsBluePrint=input()
	print('------------------')
	if IsBluePrint=='+':
		while True:
			print('Выбери из этих', ListDirBP)
			BluePrintName=input('BluePrint Name: ')
			print('------------------')
			if os.path.exists(Path+'\\BluePrints\\'+BluePrintName+'.py') or os.path.exists(Path+'\\BluePrints\\'+BluePrintName):
				try: exec(open(Path+'\\BluePrints\\'+BluePrintName+'.py').read())
				except: exec(open(Path+'\\BluePrints\\'+BluePrintName).read())
				BluePrintIn=True
				break
			elif BluePrintName=='-':
				BluePrintOut=True
				break
			else: print ("Файл не найден. Введи название Чертежа или '-' для создания нового")
	elif IsBluePrint=='-':
		BluePrintOut=True
		break
	else: print('Введи "+" или "-"')

if BluePrintOut==True:
	from BP import BPname, TY, R, OMM, OMR, Q, N, TCh, PCh, OS, OMA, OMW, OMD, DM


OM=OMA+OMW+OMD

OY=TCh+PCh+OS+DM+Q*2+DM
if OM>0: OY+=OM+1
elif OM<0: OY=OY-OM-1
#DM
if N>TY:
		Nshow=N-TY
		OY+=N-TY
else: Nshow=0


print('OY = T + P + OM + N + OS + Q + DM')
print('    ',TCh,'+',PCh,'+',OM+1,' +',Nshow,'+',OS,' +',Q*2,'+',DM,'=',OY)
OYall=OY*5
print('Требуется Успехов:',OYall)


CrafterIn=False
CrafterOut=False
print("Есть ли Сохраненный лист крафтера? (+/-)")
while not (CrafterOut==True or CrafterIn==True):
		IsCrafter=input()
		print('------------------')
		if IsCrafter=='+':
				while True:
						print('Выбери из этих', ListDirCR)
						CRname=input('Crafter Name: ')
						print('------------------')
						if os.path.exists(Path+'\\Crafters\\'+CRname+'.py') or os.path.exists(Path+'\\Crafters\\'+CRname):
								try:exec(open(Path+'\\Crafters\\'+CRname+'.py').read())
								except:exec(open(Path+'\\Crafters\\'+CRname).read())
								CrafterIn=True
								break
						elif CRname=='-':
								CrafterOut=True
								break
						else: print ("Файл не найден. Введи имя или '-' для создания нового дек листа")
		elif IsCrafter=='-':
				CrafterOut=True
				break
		else:print('Введи "+" или "-"')

if CrafterOut==True:
	from Crafter import CRname, INT, CRFT, PERC, PROF, PROFall, TM, TERP, SINC, COMP


print("Есть ли подходящая Специализация? (+/-)")
while True:
	SPEC=input()
	print('------------------')
	if SPEC=='+':
		SPEC=1
		break
	elif SPEC=='-':
		SPEC=0
		break
	else: print('Введи "+" или "-"')


while True:
	try:
		M = int(input('Уровень Мастерской: '))
		print('------------------')
		if M not in list(range(1,6)): print('!!! Введи целое число от 1 до 5')
		else: break
	except: print('!!! Введи целое число от 1 до 5')


if R<TY: NZ=R
else: NZ=TY

KolTY=R**2
print('Требуется деталей:',KolTY)

if TY<7:
	print("Есть ли",KolTY//2+1,"Деталей ТУ",TY+1,"? (+/-) ")
	while True:
		KTYC=input()
		print('------------------')
		if KTYC=='+':
			print('+1 dice')
			KTYC=1
			break
		elif KTYC=='-':
			KTYC=0
			break
		else:print('Введи "+" или "-"')
else:KTYC=0      

SURV=1
DEX=3
STR=2

if TY==1:
	if INT>DEX: ATT=INT
	else: ATT=DEX
	if SURV>CRFT:
		MERIT=SURV
		MERITch='SURV'
	else:
		MERIT=CRFT
		MERITch='CRFT'
elif TY==2:
	if INT>STR:ATT=INT
	else:ATT=STR
	MERIT=CRFT
	MERITch='CRFT'
elif TY==3:
	ATT=INT
	MERIT=CRFT
	MERITch='CRFT'
elif TY==4:
	ATT=INT
	if CRFT>SINC:
		MERIT=SINC
		MERITch='SINC'
	elif CRFT<SINC:
		MERIT=CRFT
		MERITch='CRFT'
	else:
		MERIT=CRFT
		MERITch=['CRFT','SINC']

else:
	ATT=INT
	while True:
		print('Введи наименьший Навык, по которому считается ДайсПул для ТУ>=5')
		print("('CRFT', 'SINC', 'COMP')")
		print("если наименьших несколько, выбери либо тот, от которого бонус больше (профа, спеца и т.д.), либо пофиг")
		
		MERITch=input()
		print('------------------')
		if MERITch not in ['CRFT', 'SINC', 'COMP']:
			print('Выбери из списка, введи побуквенно')
		else:break
	if MERITch=='CRFT':MERIT=CRFT
	elif MERITch=='SINC':MERIT=SINC
	elif MERITch=='COMP':MERIT=COMP
	else:
		print('Что-то пошло не так..., выбрано COMP наугад')
		MERIT=COMP


if PROF==True and MERITch in PROFall: print("Реролл 9+")
else: PROF=False

if MERIT==0: MERITdp=-3
else: MERITdp=MERIT

DicePull = ATT + MERITdp + M - TY + SPEC - (N-1) + KTYC
print('DicePull = ATT + MERIT + M - TY + SPEC - (N-1) + KTYC')
print('           ',ATT,' +  ',MERITdp,'  +',M,'-',TY,' + ',SPEC,'  -  ',(N-1),'  + ',KTYC,'  =  ',DicePull)

if TERP==True:TERP=2
else:TERP=0

if MERIT<=0: MERIT=0

NumRoll = ATT + MERIT + TERP
print('NumRoll = ATT + MERIT + TERP')
print('          ',ATT,' +  ',MERIT,'  + ',TERP,'  =  ',NumRoll)

print("Есть ли Ассистеры? (+/-)")
while True:
	Asst=input()
	print('------------------')
	if Asst in ['+','-']: break
	else: print('Введи "+" или "-"')
if Asst=='+':
	while True:
		try:
			ASS=int(input('Сколько в среднем от ассиста: '))
			print('------------------')
			if ASS not in list(range(0,11)): print('!!! Введи целое число от 0 до 10')
			else: break
		except: print('!!! Введи целое число от 0 до 10')
	while True:
		try:
			ASSc=int(input('Сколько бросков от ассистера: '))
			print('------------------')
			if ASSc not in list(range(1,11)): print('!!! Введи целое число от 1 до 10')
			else: break
		except: print('!!! Введи целое число от 1 до 10')
else: ASS = ASSc = 0
ASSend = ASSc


if PERC==True: print('Трата ПСВ на +3 куба или реролл всех неудачных кубов')
else: print('Трата ПСВ на +3 куба')
while True:
	try:
		WillPower = int(input('Сколько тратит ПСВ?: '))
		print('------------------')
		if WillPower<0: print('!!! Введи целое число от 0')
		else: break
	except: print('!!! Введи целое число от 0')
WPend=WillPower

if WillPower>0 and PERC==True:
	while True:
		try:
			WPchoose = input('На что тратишь ПСВ: "RR" или "+3": ')
			print('------------------')
			if WPchoose=='RR':
				WP3=0
				break
			elif WPchoose=='+3':
				WP3=3
				PERC=False
				break
			else: print('Введи "RR" или "+3"')
		except: print('Введи "RR" или "+3"')
elif WillPower>0: 
	WPchoose='+3'
	WP3=3
else:
	WPchoose='+3'
	WP3=0

print('PROF',PROF, MERITch)

if PROF==True:
	LuckRR=(9,0)
	LuckR=[-1,8]
	LuckR.remove(-1)
	LuckR=tuple(LuckR)
else:
	LuckRR=[-1,0]
	LuckRR.remove(-1)
	LuckRR=tuple(LuckRR)
	LuckR=(8,9)

Luck=LuckRR+LuckR

#DICE ROLL

while True:
	try:
		k=int(input('Погнали! Сколько раз повторять? '))
		print('------------------')
		if k<=0:print('Введи целое положительное число (прим. 1, 10, 100, 1000)')
		else:break
	except:print('Введи целое положительное число (прим. 1, 10, 100, 1000)')


import random, Choosing
all = u = d = z = r = 0
DicePullRep=DicePull
NMend=NumRoll
KolTYend=KolTY

RandList = lall = []
if PERC == True: PERCplus = 2
else: PERCplus = 1

zall = NumRoll * k * (DicePull * 2 + ASS) * PERCplus

while z<=zall:
	RandList.append(random.randint(0,9))
	z=z+1


while all != k:
	all+=1
	LuckGlobal=0
	Roll=[]
	y=0
	WPCh, ASSCh = False, False
	WillPower=WPend
	DicePull=DicePullRep
	ASSc=ASSend
	NumRoll=NMend
	KolTY=KolTYend

	if 1<k<=5: print('')
	if 1<k<=5: print('--------------')
	if 1<k<=5: print('--------------')
	if 1<k<=5: print('--------------')
	if 1<k<=5: print('')

	while y<NumRoll:
		if k<=5: print('')
		if k<=5: print('')
		if k<=5: print('')
		if k<=5: print('---Rolls #'+str(y+1)+'---')
		
		# Тут ассистер + DramCount

		if WillPower>0:
			if WP3==3:
				DicePullTMP=DicePull+3
				DPch=DicePullTMP
			else:
				DicePullTMP=DicePull
				DPch=DicePullTMP
		else: 
			WPCh=True
			DicePullTMP=DicePull
			DPch=DicePullTMP

		if ASSc>0: 
			DicePullTMP=DicePullTMP+ASS
			DPch=DicePullTMP
		else: ASSCh=True

		DicePullR0=0
		y=y+1
		x=0
		Roll=[]
		LuckCount=0
		DramCount=0
		while x < DicePullTMP+DicePullR0:
			if (x+1)//10>=1: Space=7
			else: Space=8
			
			Roll.append(RandList[r])

			ShortText, LongText, LuckCount, DramCount, DicePullR0, DicePullTMP = Choosing.main(x, Roll[x], Luck, LuckRR, LuckR, WillPower, DicePullTMP, DicePullR0, LuckCount, PERC, DramCount, Space, RandList, r)
			if k <=5: print(LongText[:-1])
			
			if ASSCh==False and WPCh==False:
				if x==(DPch-1):
					if k<=5: print('--------------')
			elif ASSCh==False and WPCh==True:
				if x==(DPch-1):
					if k<=5: print('--------------')
			elif ASSCh==True and WPCh==False:
				if x==(DPch-1):
					if k<=5: print('--------------')
			else:
				if x==(DPch-1):
					if k<=5: print('--------------')
			
			r=r+1
			x=x+1
		if TY>M:
			if LuckCount>0:
				LuckCount=LuckCount-TY+M
				if LuckCount<0:LuckCount=0
			if k<=5: print(M-TY,'успехов за Мастерскую')

		if TY>CRFT:
			if LuckCount>0:
				LuckCount=LuckCount-TY+CRFT
				if LuckCount<0:LuckCount=0
			if k<=5: print(CRFT-TY,'успехов за Навык')
		
		if k<=5: print('Успех =',LuckCount,'    Драм =',DramCount)
		if DramCount>LuckCount:
			LuckCount=-(DramCount)
			if k<=5: print('Успех =',LuckCount,'    ДРАМАТ')
			d=d+1

		elif LuckCount==0:
			if k<=5: print('Успехов не набрано => -1 куб')
			DicePull=DicePull-1

		if LuckCount>=5:
			if KolTY>2:KolTY=KolTY-1
			Except=LuckCount-4
			if k<=5: print('   >>>Except<<       ',LuckCount,'это',LuckCount+Except,'   Деталей требуется:', KolTY)
			LuckCount+=Except
		LuckGlobal=LuckGlobal+LuckCount
		EarlyFinish=False
		EF=0
		if y!=NumRoll:
			if LuckGlobal>=OYall:
				EarlyFinish=True
				EF=y
				y=NumRoll

		if WillPower>0: WillPower=WillPower-1
		if WillPower<=0 and WPCh==False:
			if k<=5 and y!=NumRoll: print('   >>>WillPower OFF<<<')
			WPCh=True

		if ASSc>0: ASSc=ASSc-1
		if ASSc<=0 and ASSCh==False:
			if k<=5 and y!=NumRoll: print('   >>>Assist OFF<<<')
			ASSCh=True

		lall.append(LuckCount)

		if LuckGlobal//10>=1:
			Spam=4
			SpamG=20
		else:
			Spam=5
			SpamG=21
		
		if y==NumRoll or DicePull==0:
			if k<=5: print('+'*SpamG)
		if k<=5: print('+'*Spam+' Успех =',LuckGlobal,'+'*Spam)
		if y==NumRoll or DicePull==0:
			if k<=5: print('+'*SpamG)
		if DicePull==0:
			if k<=5: print('Кубов не осталось')
			break

	if k<=5: print('')
	if k<=5: print('')
	print('')

	if LuckGlobal>=OYall:
		print('Успехов =',LuckGlobal,'>>> OY =',OYall)
		print('Скрафчено\t\t\t\t',all)
		if EarlyFinish==True: print('Справился заранее. Бросков:',EF)
		u=u+1
	else:
		print('Успехов =',LuckGlobal,'<<< OY =',OYall)
		print('Фейл\t\t\t\t\t', all)
	if k<=5: print('Потрачено деталей:',KolTY)
	if EarlyFinish==True:NumRoll=EF
	if WPend>NumRoll:WPitogo=NumRoll
	else:WPitogo=WPend
	if k<=5: print('Потрачено ПСВ:', WPitogo)
	if TM==True:
		if NumRoll%2!=0:Week=NumRoll//2+1
		else:Week=NumRoll//2
	else:Week=NumRoll
	if k<=5: print('Потрачено недель:', Week)

print('')
print('Итоговый шанс: '+str(u*100/k)+'%')
def mean(numbers):
	return float(sum(numbers)) / max(len(numbers), 1)

print('Успехов за бросок ~',round(mean(lall)))
print('Драматов ~ '+str(format(d*100/(NumRoll*k),'.2f'))+'%')

while True:
	Finish=input('Введи + и нажми Enter для окончания программы ')
	if Finish=='+':break