﻿import os
import sys
import random

# import hashlib
# import win32clipboard
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QProgressBar

Path = str(os.getcwd())
distr = Path + '\\distr'

sys.path.append(distr)

import interfaceOR
import Choosing
import ChoosingQ

# if Path[0:8] in ['D:\\Drive', 'C:\\Drive']:
#	os.system(Path + "\\conventerOR.bat")
# chooseFile = Path + '\\Choosing.py'

# def get_hash_md5(filename):
#     with open(filename, 'rb') as f:
#         m = hashlib.md5()
#         while True:
#             data = f.read(8192)
#             if not data:
#                 break
#             m.update(data)
#         return m.hexdigest()

# hashCheck = get_hash_md5(chooseFile)
# hashSave = '160b6e24b9808161901a2af8571ec57f'
Hash = True
# Hash = True if hashCheck == hashSave else False

class ExampleApp(QtWidgets.QMainWindow, interfaceOR.Ui_MainWindow):

	def __init__(self, x, strLG, strY, strZ, strR, strRL, strDT, strJT, strLGRR, strYRR, strZRR, strRRR, strRLRR, strDTRR, strJTRR, strDPtmp):
		super().__init__()
		self.setupUi(self)
		self.setWindowIcon(QtGui.QIcon(distr + '\\iconOR.ico'))
		self.setWindowTitle('Open Roller')

		self.LDcount = x

		self.LuckGlobal = strLG
		self.y = strY
		self.z = strZ
		self.r = strR
		self.RandList = strRL
		self.DetalText = strDT
		self.JoinText = strJT
		self.DPtmp = strDPtmp


		self.LuckGlobalRR = strLGRR
		self.yRR = strYRR
		self.zRR = strZRR
		self.rRR = strRRR
		self.RandListRR = strRLRR
		self.DetalTextRR = strDTRR
		self.JoinTextRR = strJTRR

		self.RunQt.clicked.connect(self.RandomGO)
		self.LDQt.clicked.connect(self.LuckDiceGO)
		self.WPchQt.stateChanged.connect(self.WPch)
		self.StrQt.stateChanged.connect(self.Checks)
		self.WPstrQt.clicked.connect(self.RandomGO)
		self.RRstrQt.clicked.connect(self.RandomGO)
		self.FAQQt.clicked.connect(self.FAQ)

	def FAQ(self):
		faq='''Dice: 3	← Запас кубов
Roll: 1	← Кол-во бросков
WP: True	← трата ПСВ (True - есть, False - нет)
OM: 2	← Основной модификатор (+/- успехи)
RR: True	← Переброс неудачных кубов за черту за ПСВ
		(True - есть, False - нет)

Q: 0	← Качество, Профа и т.д.
		  Определяет то, какие значения
		    добрасываются при выпадении успехов:
		    -2 - ужасное кач-во, вычитание успеха
		    -1 - плохое кач-во, запрет доброса
		     0 - обычное кач-во, доброс 0
		     1 - хорошее кач-во, доброс 9 и 0
		     2 - отличное кач-во, доброс 8, 9 и 0


---Rolls #1---		← Номер броска
(1 = 4)		← в скобках кубик переброса за перк
        1 = 5		← “X = Y”, где X - номер кубика, Y - результат
 2 = 0            +, Q	← “+” - успех”, “Q” - доброс
 3 = 9            +
--------------		← Начались добросы
(4 = 5)
       4 = 1      -, RR-	← ”-” - единица, “RR-” - техническая запись, нет переброса
      >>> OM <<<	← Основной модификатор
Успех = 10     Драм = 1	← Успехов и единиц на броске
>>> Except <<< 10 это 16	← Подсчет эксепта
+++++ Успех = 16 +++++	← сумма успехов за броски'''
		self.DetTextQt.setText(faq)


	def Checks(self):
		Str = self.StrQt.isChecked()
		if Str:
			self.WPchQt.setChecked(False)
			self.WPchQt.setEnabled(False)
			self.RRchQt.setChecked(False)
			self.RRchQt.setEnabled(False)
			self.WPstrQt.setEnabled(True)

		else:
			self.WPchQt.setChecked(False)
			self.WPchQt.setEnabled(True)
			self.RRchQt.setChecked(False)
			self.RRchQt.setEnabled(False)
			self.RRstrQt.setEnabled(False)
			self.WPstrQt.setEnabled(False)

	def LuckDiceGO(self):
		dice = random.randint(0, 9)
		Q = self.QQt.currentText()
		Q = int(Q[0:Q.find(':')])

		LuckR, LuckRR, LuckDel = ChoosingQ.select(Q)

		if dice == 0:
			y = 1
			LDluck = []
			LDluck.append(dice)
			while True:
				dice = random.randint(0, 9)
				LDluck.append(dice)
				if dice in LuckRR:
					y += 1
				else:
					if dice in LuckR:
						y += 1
					break

			if y > 1:
				DetalText = ': Успехов ' + str(y) + '! (' + str(LDluck) + ')'
			else:
				DetalText = ': Успех! (' + str(LDluck) + ')'

		elif dice == 1:
			DetalText = ': Драмат! (' + str(dice) + ')'
		else:
			DetalText = ': Неудачно (' + str(dice) + ')'

		DetalText = str(self.LDcount) + DetalText
		self.DetTextQt.setText(DetalText)
		self.LDcount += 1

	def WPch(self):
		if self.WPchQt.isChecked():
			self.RRchQt.setEnabled(True)
		else:
			self.RRchQt.setChecked(False)
			self.RRchQt.setEnabled(False)

	def RandomGO(self):

		WillPower = self.WPchQt.isChecked()
		DicePull = self.DicePullQt.value()
		NumRoll = self.NumRollQt.value()
		Str = self.StrQt.isChecked()
		sender = self.sender().text()

		if sender == 'GO':
			self.DPtmp = DicePull
		elif sender == 'RR':
			DicePull = self.DPtmp

		if sender == 'RR':
			RR = True
			self.RRstrQt.setEnabled(False)
		else:
			RR = self.RRchQt.isChecked()

		Q = self.QQt.currentText()
		Q = int(Q[0:Q.find(':')])
		OM = self.OMQt.value()

		LuckR, LuckRR, LuckDel = ChoosingQ.select(Q)
		Luck = LuckRR + LuckR

		if Str:
			if RR:
				LuckGlobal = self.LuckGlobalRR
				y = self.yRR
				z = self.zRR
				r = self.rRR
				RandList = self.RandListRR
				WillPower = True
				WP3 = False


				if y == 0:
					DetalText = ''
					JoinText = ('Dice:'  + str(DicePull) +
								' Roll:' + str(NumRoll) +
								' WP:'   + str(WillPower) +
								' Q:'    + str(Q) +
								' RR:'   + str(RR) +
								' OM:'   + str(OM) +
												'\r\n')
				else:
					_JT = self.JoinTextRR
					_JT = _JT.split('\r\n')
					_JT.pop()
					_JT.pop()
					_JT = '\r\n'.join(_JT) + '\r\n'
					JoinText = (_JT +
								'\nDice:' + str(DicePull) +
								' Roll:' + str(NumRoll) +
								' WP:' + str(WillPower) +
								' Q:' + str(Q) +
								' RR:' + str(RR) +
								' OM:' + str(OM) +
												'\r\n')
					DetalText = self.DetalTextRR
			else:
				LuckGlobal = self.LuckGlobal
				y = self.y
				z = self.z
				r = self.r

				if sender == 'WP':
					WillPower = True
					WP3 = True
					self.RRstrQt.setEnabled(False)
				else:
					WillPower = False
					WP3 = False
					self.RRstrQt.setEnabled(True)

				if y == 0:
					RandList = []
					DetalText = ''
					JoinText = ('Dice:' + str(DicePull) +
								' Roll:' + str(NumRoll) +
								' WP:' + str(WillPower) +
								' Q:' + str(Q) +
								' RR:' + str(RR) +
								' OM:' + str(OM) +
												'\r\n')
				else:
					JoinText = (self.JoinText +
								'\nDice:' + str(DicePull) +
								' Roll:' + str(NumRoll) +
								' WP:' + str(WillPower) +
								' Q:' + str(Q) +
								' RR:' + str(RR) +
								' OM:' + str(OM) +
												'\r\n')
					DetalText = self.DetalText
					RandList = self.RandList
		else:
			JoinText = ('Dice:' + str(DicePull) +
						' Roll:' + str(NumRoll) +
						' WP:' + str(WillPower) +
						' Q:' + str(Q) +
						' RR:' + str(RR) +
						' OM:' + str(OM) +
											'\r\n')
			WP3 = True if WillPower and not RR else False
			LuckGlobal = y = z = r = 0
			DetalText = ''
			RandList = []

		Pp = 2 if RR else 1
		z_all = NumRoll * DicePull * Pp * 5
		if z_all < 100: z_all = 100

		if not RandList:
			while z <= z_all:
				RandList.append(random.randint(0, 9))
				z += 1


		if sender == 'GO' and Str:
			self.LuckGlobalRR = LuckGlobal
			self.yRR = y
			self.zRR = z
			self.rRR = r
			self.RandListRR = RandList
			self.DetalTextRR = DetalText
			self.JoinTextRR = JoinText
#
# Rolls start
#
		while y < NumRoll or Str:
			if y:
				DetalText += ('\n' * 2)

			DetalText += ('---> Бросок №' + str(y+1) + ' <---\n')

			DicePullTMP = DicePull + 3 if WP3 else DicePull
			DPch = DicePullTMP

			y += 1
			Roll = []


			if NumRoll > 1:
				JoinText += '[' + str(y) + '] '
			else: JoinText += ''


			LuckCount = DramCount = DicePullQ = x = 0

			while x < DicePullTMP + DicePullQ:
				Space = 7 if (x+1) // 10 else 8

				Roll.append(RandList[r])

				(ShortText, LongText, LuckCount,
					DramCount, DicePullQ, DicePullTMP) = (Choosing.main(x, Roll[x], Luck,
														LuckRR, LuckR, WillPower, DicePullTMP,
														DicePullQ, LuckCount, RR, DramCount,
														Space, RandList, r))

				DetalText += LongText
				JoinText  += ShortText

				if x == DPch-1:
					DetalText += ('--------------\n')
					JoinText = JoinText[:-2] + ': '

				r += 1
				x += 1

			if JoinText[-2:-1] == '-':
				JoinText = JoinText[:-2]
			if JoinText[-2:-1] == ':':
				JoinText = JoinText[:-2] + '---> '
			else:
				JoinText += '---> '

			DetalText += ('Успехов = ' + str(LuckCount) +
						 '\tЕдиниц = ' + str(DramCount) + ' \n')

			if LuckDel and LuckCount > 0:
				DetalText += (' > > Ужасное качество < <\t-успехи\n')
				LuckCount -= DramCount
				if LuckCount < 0: LuckCount = 0

			if OM and LuckCount > 0:
				DetalText += ('        > > OM < <\t' + str(OM) + ' успех\n')
				LuckCount += OM
				if LuckCount < 0: LuckCount = 0

			if DramCount > LuckCount:
				LuckCount = -DramCount
				DetalText += ('      > > Драмат < <\n')

			elif LuckCount == 0 and y != NumRoll:
				DetalText += (' > > Успехов не набрано < <\t-1 куб\n')
				if Str: self.DicePullQt.setValue(DicePull-1)
				DicePull -= 1

			elif LuckCount >= 5:
				if NumRoll > 1:
					Except = LuckCount - 4
					DetalText += ('      > > Except < <\t' + str(LuckCount) + ' это ' + str(LuckCount + Except) + '\n')
					LuckCount += Except
				else:
					Except = LuckCount - 4
					DetalText += ('      > > Except < <\t(если бросок длительный: ' + str(LuckCount) + ' это ' + str(LuckCount + Except) + ')\n')

			LuckGlobal += LuckCount
			JoinText += str(LuckCount) + '\r\n'

			Spam, SpamG = (5, 18) if LuckGlobal//10 else (6, 19) # >= 1 else (6, 19)

			if y == NumRoll or DicePull == 0:
				DetalText += ('+'*SpamG + '\n')
			DetalText += ('+'*Spam + ' Успех = ' + str(LuckGlobal) + ' ' + '+'*Spam + '\n')
			if y == NumRoll or DicePull == 0:
				DetalText += ('+'*SpamG + '\n')

			if DicePull == 0:
				DetalText += ('Кубов не осталось\n')
				break
			elif Str: break

#
# Rolls end
#



		if not Str or (y >= NumRoll or DicePull == 0):
			DetalText += ('\n' * 3)
			JoinText += 'Итого: ' + str(LuckGlobal) + '\r\n\n'

			if Hash:
				DetalText = JoinText + DetalText
			else:
				DetalText = 'Мошенник!!!'

			self.DetTextQt.setText(DetalText)

			self.LuckGlobal = 0
			self.y = 0
			self.z = 0
			self.r = 0
			self.RandList = []
			self.DetalText= ''
			self.JoinText = ''

			# win32clipboard.OpenClipboard()
			# win32clipboard.EmptyClipboard()
			# win32clipboard.SetClipboardText(JoinText)
			# win32clipboard.CloseClipboard()

		else:
			self.LuckGlobal = LuckGlobal
			self.y = y
			self.z = z
			self.r = r
			self.RandList = RandList
			self.DetalText= DetalText
			self.JoinText = JoinText

			DetalText += ('\n' * 3)
			JoinText += '> > ' + str(LuckGlobal) + ' < <\r\n\n'
			if Hash:
				DetalText = JoinText + DetalText
			else:
				DetalText = 'Мошенник!!!'

			self.DetTextQt.setText(DetalText)
		self.RunQt.setEnabled(True)

def main():
	app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
	window = ExampleApp(1, 0, 0, 0, 0, [], '', '', 0, 0, 0, 0, [], '', '', 0) # Создаём объект класса ExampleApp
	window.show()  							# Показываем окно
	app.exec_()  							# и запускаем приложение

if __name__ == '__main__':  				# Если мы запускаем файл напрямую, а не импортируем
	main()									# то запускаем функцию main()
