import os
import sys
import random
import hashlib

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QProgressBar

Path = str(os.getcwd())
BluePrints = Path + '\\BluePrints'
Crafters = Path + '\\Crafters'
distr = Path + '\\distr'

sys.path.append(BluePrints)
sys.path.append(Crafters)
sys.path.append(distr)

import interfaceOC
import Choosing

# if Path[0:8] in ['D:\\Drive','C:\\Drive']:
#    os.system(Path + "\\conventerOC.bat")

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

# if hashCheck == hashSave:
Hash = True
# else:
#     Hash = False

ListDirBP = [x[:-3] for x in os.listdir(BluePrints) if x[-3:] == '.py']
ListDirCR = [x[:-3] for x in os.listdir(Crafters) if x[-3:] == '.py']

CRall, BPall = {}, {}

for i in ListDirCR:
    Str, k, v = [], [], []
    for line in open(Crafters + '\\' + i + '.py'):
        Str.append(line.rstrip())
    for h in Str:
        k.append(h [:h.find(' = ')])
        v_ = h [h.find(' = ')+3:].replace("'",'')
        if v_[0].isdigit(): v.append(int(v_))
        elif v_[0] == '[':
            if v_ == '[]':
                v.append([])
            else:
                v.append(list(v_[1:-1].split(', ')))
        else: v.append((v_))
    CRall[str(v[0])] = dict(zip(k[1:],v[1:]))


for i in ListDirBP:
    Str, k, v = [], [], []
    for line in open(BluePrints + '\\' + i + '.py'):
        Str.append(line.rstrip())
    for h in Str:
        k.append(h [:h.find(' = ')])
        v_ = h [h.find(' = ')+3:].replace("'",'')
        try: v.append(int(float(v_)))
        except: v.append(v_)
    BPall[str(v[0])] = dict(zip(k[1:],v[1:]))


class ExampleApp(QtWidgets.QMainWindow, interfaceOC.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon(Path + '\\distr\\iconOC.ico'))
        self.setWindowTitle('OpenCrafter')
        self.show()

        self.StartBtnQt.clicked.connect(self.Starting)
        self.CRnameQt.currentIndexChanged.connect(self.DelSelectCR)
        self.CRnameQt.currentIndexChanged[str].connect(self.CrafterNameChange)
        self.BPnameQt.currentIndexChanged.connect(self.DelSelectBP)
        self.BPnameQt.currentIndexChanged[str].connect(self.BPnameChange)
        self.ASSnameQt.currentIndexChanged[str].connect(self.ASSnameChange)

        self.INTQt.valueChanged.connect(self.NumRollChange)
        self.MERITQt.valueChanged.connect(self.NumRollChange)
        self.TERPQt.stateChanged.connect(self.NumRollChange)

        self.TYQt.valueChanged.connect(self.NZChange)
        self.RQt.valueChanged.connect(self.NZChange)

        self.TYQt.valueChanged.connect(self.PChange)
        self.PChQt.valueChanged.connect(self.PChange)

        self.RQt.valueChanged.connect(self.KolTYChange)
        self.TYQt.valueChanged.connect(self.KTYCChange)

        self.OMMQt.valueChanged.connect(self.OMMChange)
        self.OMRQt.valueChanged.connect(self.OMMChange)
        self.OMMChQt.valueChanged.connect(self.OMMChange)
        self.NZQt.valueChanged.connect(self.OMminmax)
        self.OMQt.valueChanged.connect(self.OMMRMminmax)
        self.OMQt.valueChanged.connect(self.OMChange)
        self.NAQt.stateChanged.connect(self.OMChange)
        self.NAQt.stateChanged.connect(self.OMMChange)

        self.TYQt.valueChanged.connect(self.TChange)
        self.STRQt.valueChanged.connect(self.TChange)
        self.TChQt.valueChanged.connect(self.TChange)

        self.PROFQt.stateChanged.connect(self.PROFallChange)
        self.CRnameQt.currentTextChanged.connect(self.PROFallChange)

        self.TYQt.valueChanged.connect(self.MERITChange)
        self.CRFTQt.valueChanged.connect(self.MERITChange)
        self.SINCQt.valueChanged.connect(self.MERITChange)
        self.COMPQt.valueChanged.connect(self.MERITChange)
        self.PSINCQt.stateChanged.connect(self.MERITChange)
        self.PCRFTQt.stateChanged.connect(self.MERITChange)
        self.PCOMPQt.stateChanged.connect(self.MERITChange)

        self.PChQt.valueChanged.connect(self.OYChange)
        self.TChQt.valueChanged.connect(self.OYChange)
        self.OMQt.valueChanged.connect(self.OYChange)
        self.NQt.valueChanged.connect(self.OYChange)
        self.OSQt.valueChanged.connect(self.OYChange)
        self.OMMChQt.valueChanged.connect(self.OYChange)
        self.QQt.currentTextChanged.connect(self.OYChange)
        self.DMQt.valueChanged.connect(self.OYChange)

        self.NZQt.valueChanged.connect(self.Qminmax)
        self.NZQt.valueChanged.connect(self.DMminmax)

        self.WPQt.valueChanged.connect(self.WPChoose)
        self.RRchQt.stateChanged.connect(self.WPChoose)

        self.NumRollQt.valueChanged.connect(self.NRmax)

        self.MQt.valueChanged.connect(self.DicePullChange)
        self.KTYCQt.stateChanged.connect(self.DicePullChange)
        self.NQt.valueChanged.connect(self.DicePullChange)
        self.OtherQt.valueChanged.connect(self.DicePullChange)
        self.MERITQt.valueChanged.connect(self.DicePullChange)
        self.TYQt.valueChanged.connect(self.DicePullChange)
        self.INTQt.valueChanged.connect(self.DicePullChange)
        self.NumRollQt.valueChanged.connect(self.DicePullChange)
        self.RRQt.toggled.connect(self.DicePullChange)

        self.CRsaveBTNQt.clicked.connect(self.SavingCR)
        self.BPsaveBTNQt.clicked.connect(self.SavingBP)

        self.PSINCQt.stateChanged.connect(self.PROFChange)
        self.PCRFTQt.stateChanged.connect(self.PROFChange)
        self.PCOMPQt.stateChanged.connect(self.PROFChange)
        self.MERITQt.valueChanged.connect(self.PROFChange)

        self.ASSchQt.stateChanged.connect(self.ASSch)
        self.ASScQt.valueChanged.connect(self.ASScCh)

        self.PQt.valueChanged.connect(self.SChange)
        self.RQt.valueChanged.connect(self.SChange)

        self.OYQt.valueChanged.connect(self.KChange)
        self.DicePullQt.valueChanged.connect(self.KChange)
        self.NumRollQt.valueChanged.connect(self.KChange)
        self.CRnameQt.currentTextChanged.connect(self.KChange)
        self.OMMQt.valueChanged.connect(self.KChange)
        self.OMRQt.valueChanged.connect(self.KChange)
        self.OMQt.valueChanged.connect(self.KChange)

        self.RunQt.clicked.connect(self.RandomGO)

        self.KQt.valueChanged.connect(self.pbar)

        self.NAQt.stateChanged.connect(self.NAch)

    def NAch(self):
        if self.NAQt.isChecked():
            self.OMMQt.setEnabled(True)
            self.OMRQt.setEnabled(True)
        else:
            self.OMMQt.setEnabled(False)
            self.OMRQt.setEnabled(False)
            self.OMRQt.setValue(0)
            self.OMMQt.setValue(0)
            self.OMMChQt.setEnabled(False)
            self.OMMChQt.setValue(0)
            self.DebaffMRQt.hide()


    def OMChange(self):
        if self.OMQt.value() == 0:
            self.NAQt.setChecked(False)
            self.NAQt.setEnabled(False)
        else:
            self.NAQt.setEnabled(True)


    def pbar(self):
        DicePull = self.DicePullQt.value()
        NumRoll = self.NumRollQt.value()
        k = self.KQt.value()
        ASS = self.ASSQt.value() if self.ASSchQt.isChecked() else 0
        Pp = 2 if self.RRchQt.isChecked() else 1

        zall = NumRoll * k * (DicePull * 2 + ASS) * Pp

        if k > 100:
            self.RunBarQt = QtWidgets.QProgressBar(self.centralwidget)
            self.RunBarQt.setGeometry(QtCore.QRect(10, 480, 71, 281))
            self.RunBarQt.setProperty("value", 0)
            self.RunBarQt.setMaximum(k)

            self.RunBarQt.setOrientation(QtCore.Qt.Vertical)
            self.RunBarQt.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
            self.RunBarQt.setObjectName("RunBarQt")
            self.RunBarQt.show()

        if zall > 10000:
            self.RunBarQt = QtWidgets.QProgressBar(self.centralwidget)
            self.RunBarQt.setGeometry(QtCore.QRect(10, 480, 71, 281))
            self.RunBarQt.setProperty("value", 0)
            self.RunBarQt.setMaximum(zall)

            self.RunBarQt.setOrientation(QtCore.Qt.Vertical)
            self.RunBarQt.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
            self.RunBarQt.setObjectName("RunBarQt")
            self.RunBarQt.show()


    def RandomGO(self):
        DicePull = self.DicePullQt.value()
        NumRoll = self.NumRollQt.value()
        RR = self.RRchQt.isChecked()
        OYall = self.OYQt.value() * 5
        KolTY = self.KolTYQt.value()
        CRFT = self.CRFTQt.value()
        TM = self.TMQt.isChecked()
        TY = self.TYQt.value()
        M = self.MQt.value()

        if self.ASSchQt.isChecked():
            ASS = self.ASSQt.value()
            ASSc= self.ASScQt.value()
        else:
            ASS = ASSc = 0
        ASSend = ASSc

        WillPower = self.WPQt.value()
        WPend = WillPower

        if WillPower > 0 and RR:
            if self.RRQt.isChecked():
                WP3 = 0
            else:
                WP3 = 3
                RR = False
        elif WillPower > 0:
            WP3 = 3
        else:
            WP3 = 0


        if self.PROFQt.isChecked():
            LuckRR = (9, 0)
            LuckR  = (8,)
        else:
            LuckRR = (0,)
            LuckR  = (8, 9)

        Luck = LuckRR + LuckR

        k = self.KQt.value()
        k5 = True if k <= 5 else False

        DetalText = ''
        RandList = lall = []
        all = u = d = z = r = 0

        DicePullRep = DicePull
        KolTYend = KolTY
        NMend = NumRoll

        Pp = 2 if RR else 1
        zall = NumRoll * k * (DicePull*2 + ASS) * Pp

        while z <= zall:
            if zall > 10000: self.RunBarQt.setValue(z)
            RandList.append(random.randint(0,9))
            z += 1


        while all != k:
            if k > 10: self.RunBarQt.setValue(all)

            if all > 0 and k5:
                DetalText += ('\n')
                DetalText += ('--------------\n' * 3)
                DetalText += ('\n')

            if k >= 2: DetalText += ('--> Попытка №' + str(all+1) + ' <--\n')

            all += 1
            LuckGlobal = y = 0
            WPCh, ASSCh = False, False

            ASSc = ASSend
            KolTY = KolTYend
            NumRoll = NMend
            DicePull = DicePullRep
            WillPower = WPend
#
# Rolls start
#
            while y < NumRoll:

                if k5 and y > 0:
                    DetalText += ('\n' * 3)
                if k5:
                    DetalText += ('---> Бросок №' + str(y+1) + ' <---\n')

                if WillPower > 0:
                    if WP3 == 3:
                        DicePullTMP = DicePull + 3
                    else:
                        DicePullTMP = DicePull
                else:
                    DicePullTMP = DicePull
                    WPCh = True

                if ASSc > 0:
                    DicePullTMP += ASS
                else:
                    ASSCh = True

                DPch = DicePullTMP

                y += 1
                Roll = []
                DicePullQ = LuckCount = DramCount = x = 0
                while x < DicePullTMP + DicePullQ:
                    Space = 7 if (x+1) // 10 >= 1 else 8

                    Roll.append(RandList[r])

                    (ShortText, LongText, LuckCount,
                     DramCount, DicePullQ, DicePullTMP) = (Choosing.main(x, Roll[x], Luck,
                                                            LuckRR, LuckR, WillPower, DicePullTMP,
                                                            DicePullQ, LuckCount, RR, DramCount,
                                                            Space, RandList, r))

                    if k5: DetalText += LongText
                    if k5 and x == DPch-1:
                        DetalText += ('--------------\n')

                    r += 1
                    x += 1

                if TY > M:
                    if LuckCount > 0:
                        LuckCount += -TY + M
                        if LuckCount < 0: LuckCount = 0
                        if k5: DetalText += (str(M-TY) + ' успехов за Мастерскую\n')

                if TY > CRFT:
                    if LuckCount > 0:
                        LuckCount += -TY + CRFT
                        if LuckCount < 0: LuckCount = 0
                        if k5: DetalText += (str(CRFT-TY) + ' успехов за Навык\n')

                if k5: DetalText += ('Успехов = ' + str(LuckCount) + '     Единиц = ' + str(DramCount) + ' \n')

                if DramCount > LuckCount:
                    if k5: DetalText += ('    > > Драмат < <\n')
                    LuckCount = -DramCount
                    d += 1
                #elif LuckCount == 0:
                #    if k5: DetalText += ('Успехов не набрано => -1 куб\n')
                #    DicePull += -1
                elif LuckCount >= 5:
                    if KolTY > 1: KolTY += -1
                    Except = LuckCount - 4
                    if k5: DetalText += ('    > > Except < <\t' + str(LuckCount) + ' это ' + str(LuckCount + Except) + '    - деталь\n')
                    LuckCount += Except

                LuckGlobal += LuckCount
                EarlyFinish = False
                EF = 0
                if y != NumRoll:
                    if LuckGlobal >= OYall:
                        EarlyFinish = True
                        EF = y
                        y = NumRoll

                if WillPower > 0: WillPower += -1
                if WillPower <= 0 and not WPCh:
                    if k5 and y!= NumRoll:
                        DetalText += ('    > > WillPower OFF < <\n')
                    WPCh = True

                if ASSc > 0: ASSc += -1
                if ASSc <= 0 and not ASSCh:
                    if k5 and y != NumRoll:
                        DetalText += ('    > > Assist OFF < <\n')
                    ASSCh = True

                lall.append(LuckCount)

                Spam, SpamG = (5, 18) if LuckGlobal // 10 >= 1 else (6, 19)


                if k5:
                    if y == NumRoll or DicePull == 0:
                        DetalText += ('+'*SpamG + ' \n')
                    DetalText += ('+' * Spam + ' Успех = ' + str(LuckGlobal) + '+'*Spam + ' \n')
                    if y == NumRoll or DicePull == 0:
                        DetalText += ('+'*SpamG + ' \n')

                if DicePull == 0:
                    if k5: DetalText += ('Кубов не осталось\n')
                    break

#
# Rolls end
#

            if k5: DetalText += ('\n' * 2)
            DetalText += ('\n')

            if LuckGlobal >= OYall:
                  DetalText += ('Успехов = '+str(LuckGlobal)+' > > OY = '+str(OYall)+' \n> > Скрафчено < <\n')
                  if EarlyFinish:
                    DetalText += ('Справился заранее. Бросков: '+str(EF)+' \n')
                  u += 1
            else: DetalText += ('Успехов = ' + str(LuckGlobal) + ' < < OY = ' + str(OYall) + ' \n> > Зафейлено < <\n')

            if k5: DetalText += ('Потрачено деталей: ' + str(KolTY) + ' \n')

            if EarlyFinish: NumRoll = EF

            WPitogo = NumRoll if WPend > NumRoll else WPend

            if k5: DetalText += ('Потрачено ПСВ: ' + str(WPitogo) + ' \n')

            if TM: Week = (NumRoll//2 + 1) if NumRoll%2 != 0 else (NumRoll // 2)
            else:  Week = NumRoll
            if k5: DetalText += ('Потрачено недель: '+ str(Week) + ' \n')

        DetalText += '^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n'

        ICh = ('Итоговый шанс: '+str(format((u*100/k),'.2f'))+'%\n')
        ItogText = ICh
        DetalText += ICh

        def mean(numbers):
            return float(sum(numbers)) / max(len(numbers), 1)
        UzB = ('Успехов за бросок ~ ' + str(round(mean(lall))) + ' \n')
        DzB = ('Драматов за броски~ ' + str(format(d * 100 / (NumRoll * k),'.2f')) + '%')
        ItogText += UzB + DzB
        DetalText += UzB + DzB

        if not Hash: ItogText = DetalText = 'Мошенник!!!'

        self.DetTextQt.setText(DetalText)
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Итоги крафта")
        msg.setText(ItogText)
        msg.exec()


    def KChange(self):
        if (self.OYQt.value() == 0 or
            self.CRnameQt.currentText() == 'Select...' or
            self.BPnameQt.currentText() == 'Select...' or
            self.DicePullQt.value() == 0 or
            self.NumRollQt.value() == 0 or
            (self.OMQt.value() * 2 != self.OMMQt.value() + self.OMRQt.value() and self.NAQt.isChecked())):
                self.RunQt.setEnabled(False)
                self.KQt.setEnabled(False)
        else:
            self.KQt.setEnabled(True)
            self.RunQt.setEnabled(True)

    def SChange(self):
        self.SQt.setValue(self.RQt.value()+self.PQt.value())

    def ASSnameChange(self, CurrentASS):
        if CurrentASS in ListDirCR:
            TY=self.TYQt.value()

            INT  = CRall[CurrentASS]['INT']
            CRFT = CRall[CurrentASS]['CRFT']
            SINC = CRall[CurrentASS]['SINC']
            COMP = CRall[CurrentASS]['COMP']
            TERP = CRall[CurrentASS]['TERP']

            z = 0
            TERP = 2 if TERP else 0

            if TY <= 3:
                self.ASScQt.setValue(INT+CRFT+TERP)
            elif TY == 4:
                while True:
                    if CRFT == z: break
                    elif SINC == z: break
                    else: z += 1
                self.ASScQt.setValue(z + INT + TERP)
            else:
                while True:
                    if CRFT == z: break
                    elif SINC == z: break
                    elif COMP == z: break
                    else: z += 1
                self.ASScQt.setValue(z + INT + TERP)
            self.ASScQt.setEnabled(False)
            self.ASSQt.setEnabled(True)
        elif CurrentASS == 'New...':
            self.ASScQt.setEnabled(True)
            self.ASScQt.setMaximum(self.NumRollQt.value())
            self.ASScQt.setValue(self.NumRollQt.value())
            if self.ASScQt.value() > 0:
                self.ASSQt.setEnabled(True)
            else:
                self.ASSQt.setEnabled(False)
                self.ASSQt.setValue(0)
        else:
            self.ASSQt.setEnabled(False)
            self.ASScQt.setEnabled(False)
            self.ASScQt.setValue(0)
            self.ASSQt.setValue(0)
            self.ASSnameQt.setEnabled(True)

    def ASScCh(self):
        if self.ASScQt.value() > 0:
            self.ASSQt.setEnabled(True)
        else:
            self.ASSQt.setEnabled(False)
            self.ASSQt.setValue(0)

        if self.NumRollQt.value() > self.ASScQt.value(): self.DebaffASSQt.show()
        else: self.DebaffASSQt.hide()

    def ASSch(self):
        if self.ASSchQt.isChecked():
            self.ASScQt.setEnabled(True)
            self.ASSnameQt.setEnabled(True)
            self.ASSnameQt.clear()
            self.ASSnameQt.addItem('New...')
            x=0
            while x != len(ListDirCR):
                if ListDirCR[x] != self.CRnameQt.currentText():
                    self.ASSnameQt.addItem(ListDirCR[x])
                x += 1
            self.ASSnameQt.setCurrentIndex(0)
        else:
            self.ASSQt.setEnabled(False)
            self.ASScQt.setEnabled(False)
            self.ASScQt.setValue(0)
            self.ASSQt.setValue(0)
            self.ASSnameQt.setEnabled(False)
            self.ASSnameQt.clear()
            self.DebaffASSQt.hide()

    def PROFChange(self):
        PROFall = []
        if self.PCRFTQt.isChecked():
            PROFall.append('CRFT')
        if self.PSINCQt.isChecked():
            PROFall.append('SINC')
        if self.PCOMPQt.isChecked():
            PROFall.append('COMP')
        self.BuffPROFQt.show() if self.MERITchQt.text() in PROFall else self.BuffPROFQt.hide()

    def KTYCChange(self):
        if self.TYQt.value() == 7:
            self.KTYCQt.setEnabled(False)
            self.KTYCQt.setChecked(False)
        else:
            self.KTYCQt.setEnabled(True)

    def SavingCR(self):
        CRname = self.CRsaveQt.text()[0].upper() + self.CRsaveQt.text()[1:].lower()

        if (len(CRname) < 3 or not CRname.isalnum() or ' ' in CRname):
            self.CRsaveQt.clear()
            QMessageBox.warning(self, "Имя кривое", "Введи другое имя: хотя бы 3 символа, без знаков препинания и без пробелов")
            self.CRsaveQt.setFocus()
        elif CRname in ListDirCR:
            self.CRsaveQt.clear()
            QMessageBox.warning(self, "Имя занято", "Этот крафтер уже сохранен. Выбери другое имя")
            self.CRsaveQt.setFocus()
        else:
            INT  = self.INTQt.value()
            CRFT = self.CRFTQt.value()
            SINC = self.SINCQt.value()
            COMP = self.COMPQt.value()
            RR   = self.RRchQt.isChecked()
            TM   = self.TMQt.isChecked()
            TERP = self.TERPQt.isChecked()
            PROF = self.PROFQt.isChecked()

            PROFall = []
            if self.PCRFTQt.isChecked():
                PROFall.append('CRFT')
            if self.PSINCQt.isChecked():
                PROFall.append('SINC')
            if self.PCOMPQt.isChecked():
                PROFall.append('COMP')
            lines=["CRname = '"+ str(CRname) + "'",
                   'INT = '    + str(INT),
                   'CRFT = '   + str(CRFT),
                   'SINC = '   + str(SINC),
                   'COMP = '   + str(COMP),
                   'RR = '     + str(int(RR)),
                   'PROF = '   + str(int(PROF)),
                   'PROFall = '+ str(PROFall),
                   'TM = '     + str(int(TM)),
                   'TERP = '   + str(int(TERP)),
                   ]

            with open(Path + '\\Crafters\\' + CRname + '.py', 'w') as file:
                for line in lines:
                    file.write(line + '\n')

            self.CRnameQt.hide()
            self.CRsaveBTNQt.hide()
            self.INTQt.setEnabled(False)
            self.CRFTQt.setEnabled(False)
            self.PROFQt.setEnabled(False)
            self.TMQt.setEnabled(False)
            self.TERPQt.setEnabled(False)
            self.SINCQt.setEnabled(False)
            self.COMPQt.setEnabled(False)
            self.PCRFTQt.setEnabled(False)
            self.PSINCQt.setEnabled(False)
            self.PCOMPQt.setEnabled(False)
            QMessageBox.warning(self, "Требуется перезапуск", "Крафтер сохранен. Для дальнейшего изменения крафтеров требуется перезагрузка программы")

    def SavingBP(self):
        BPname = self.BPsaveQt.text()[0].upper() + self.BPsaveQt.text()[1:].lower()

        if (len(BPname) < 3 or
            not BPname.isalnum() or
            ' ' in BPname):
                    self.BPsaveQt.clear()
                    QMessageBox.warning(self, "Название кривое", "Введи другое название: хотя бы 3 символа, без знаков препинания и без пробелов")
                    self.BPsaveQt.setFocus()
        elif BPname in ListDirBP:
            self.BPnameQt.clear()
            QMessageBox.warning(self, "Название занято", "Этот чертеж уже существует. Выбери другое название")
            self.BPnameQt.setFocus()
        else:
            BPname= self.BPsaveQt.text()
            TY    = self.TYQt.value()
            R     = self.RQt.value()
            OM    = self.OMQt.value()
            OMM   = self.OMMQt.value()
            OMR   = self.OMRQt.value()
            OMMch = self.OMMChQt.value()
            Q     = self.QQt.currentText()
            STR   = self.STRQt.value()
            TCh   = self.TChQt.value()
            N     = self.NQt.value()
            PCh   = self.PChQt.value()
            OS    = self.OSQt.value()
            DM    = self.DMQt.value()
            NA    = self.NAQt.isChecked()

            NA = 1 if NA else 0
            Q = int(Q[0:Q.find(':')])

            lines=["BPname = '"+ str(BPname)+"'",
                   'TY = '     + str(TY),
                   'R = '      + str(R),
                   'OM = '     + str(OM),
                   'OMM = '    + str(OMM),
                   'OMR = '    + str(OMR),
                   'OMMch = '  + str(OMMch),
                   'Q = '      + str(Q),
                   'STR = '    + str(STR),
                   'TCh = '    + str(TCh),
                   'N = '      + str(N),
                   'PCh = '    + str(PCh),
                   'OS = '     + str(OS),
                   'DM = '     + str(DM),
                   'NA = '     + str(int(NA)),
                   ]

            with open(Path+'\\BluePrints\\'+BPname+'.py', 'w') as file:
                for line in lines: file.write(line + '\n')

            self.BPnameQt.hide()
            self.BPsaveBTNQt.hide()
            self.TYQt.setEnabled(False)
            self.RQt.setEnabled(False)
            self.OMQt.setEnabled(False)
            self.QQt.setEnabled(False)
            self.STRQt.setEnabled(False)
            self.TChQt.setEnabled(False)
            self.NQt.setEnabled(False)
            self.NAQt.setEnabled(False)
            self.PChQt.setEnabled(False)
            self.OSQt.setEnabled(False)
            self.KolTYQt.setEnabled(False)
            self.OMMQt.setEnabled(False)
            self.OMRQt.setEnabled(False)
            self.OMMChQt.setEnabled(False)
            self.BPsaveQt.setEnabled(False)
            QMessageBox.warning(self, "Требуется перезапуск", "Чертеж сохранен. Для дальнейшего изменения чертежей требуется перезагрузка программы")

    def DicePullChange(self):
        M    = self.MQt.value()
        N    = self.NQt.value()
        MERIT= self.MERITQt.value()
        TY   = self.TYQt.value()
        INT  = self.INTQt.value()
        CRFT = self.CRFTQt.value()
        Other= self.OtherQt.value()

        if M < TY:
            self.DebaffMQt.show()
        else:
            self.DebaffMQt.hide()

        if CRFT < TY:
            self.DebaffCRFTQt.show()
        else:
            self.DebaffCRFTQt.hide()

        KTYC = 1 if self.KTYCQt.isChecked() else 0

        if N==1: N = 0
        else: N -= 1

        if MERIT == 0: MERIT = -3

        DicePull = M - N + MERIT + INT + Other + KTYC - TY

        self.DicePullQt.setValue(DicePull)


    def NRmax(self):
        self.WPQt.setMaximum(self.NumRollQt.value())
        self.WPQt.setValue(self.NumRollQt.value())
        if self.ASSchQt.isChecked():
            if self.ASSnameQt.currentText() not in ListDirCR:
                self.ASScQt.setMaximum(self.NumRollQt.value())
                self.ASScQt.setValue(self.NumRollQt.value())
            else:
                CurrentASS = self.ASSnameQt.currentText()
                TY   = self.TYQt.value()
                INT  = CRall[CurrentASS]['INT']
                CRFT = CRall[CurrentASS]['CRFT']
                SINC = CRall[CurrentASS]['SINC']
                COMP = CRall[CurrentASS]['COMP']
                TERP = CRall[CurrentASS]['TERP']

                z = 0
                TERP = 2 if TERP else 0

                if TY <= 3:
                    self.ASScQt.setValue(INT+CRFT+TERP)
                elif TY == 4:
                    while True:
                        if CRFT == z: break
                        elif SINC == z: break
                        else: z += 1
                    self.ASScQt.setValue(z + INT + TERP)
                else:
                    while True:
                        if CRFT == z: break
                        elif SINC == z: break
                        elif COMP == z: break
                        else: z += 1
                    self.ASScQt.setValue(z + INT + TERP)
        else:
            self.ASScQt.setMaximum(0)
        if self.ASSchQt.isChecked():
            self.DebaffASSQt.show() if self.NumRollQt.value()>self.ASScQt.value() else self.DebaffASSQt.hide()

    def WPChoose(self):
        if self.WPQt.value()>0:
            if self.RRchQt.isChecked():
                self.WP3Qt.setEnabled(True)
                self.RRQt.setEnabled(True)
                self.RRQt.setChecked(True)
            else:
                self.WP3Qt.setEnabled(True)
                self.WP3Qt.setChecked(True)
                self.RRQt.setEnabled(False)
        else:
            self.WP3Qt.setEnabled(False)
            self.RRQt.setEnabled(False)
        self.DebaffWPQt.show() if self.WPQt.value()<self.NumRollQt.value() else self.DebaffWPQt.hide()


    def Qminmax(self):
        # Q def
        Q0 = '0: (10)'
        Q1 = '+1: (9, 10)'
        Q2 = '+2: (8, 9, 10)'
        Q_1 = '-1: (-)'
        Q_2 = '-2: (-1)'
        NZ = self.NZQt.value()
        if NZ < 2:
            self.QQt.clear()
            self.QQt.addItem(Q0)
        elif 4 > NZ >= 2:
            self.QQt.clear()
            self.QQt.addItem(Q1)
            self.QQt.addItem(Q0)
            self.QQt.addItem(Q_1)
            self.QQt.setCurrentIndex(1)
        else:
            self.QQt.clear()
            self.QQt.addItem(Q2)
            self.QQt.addItem(Q1)
            self.QQt.addItem(Q0)
            self.QQt.addItem(Q_1)
            self.QQt.addItem(Q_2)
            self.QQt.setCurrentIndex(2)

    def OYChange(self):
        # TCh + PCh + OM+1  + N + OS + Q*2 + OMMCh = OY
        TCh = self.TChQt.value()
        PCh = self.PChQt.value()
        OM  = self.OMQt.value()
        N   = self.NQt.value()
        OS  = self.OSQt.value()
        TY  = self.TYQt.value()
        DM  = self.DMQt.value()
        OMMch = self.OMMChQt.value()
        try: Q  = int(self.QQt.currentText()[0:self.QQt.currentText().find(':')])
        except: Q = 0

        OY = TCh + PCh + OS + Q * 2 + DM

        if OM > 0: OY += OM + 1
        elif OM < 0: OY += OM - 1

        if OMMch != 0: OY += OMMch

        if N > TY: OY += N - TY

        self.OYQt.setValue(OY)
        self.DebaffOYQt.show() if OY < 1 else self.DebaffOYQt.hide()


    def MERITChange(self):
        z = 0
        q = False
        MeritList, PROFall = [], []
        TY   = self.TYQt.value()
        CRFT = self.CRFTQt.value()
        SINC = self.SINCQt.value()
        COMP = self.COMPQt.value()
        if self.PCRFTQt.isChecked():
            PROFall.append('CRFT')
        if self.PSINCQt.isChecked():
            PROFall.append('SINC')
        if self.PCOMPQt.isChecked():
            PROFall.append('COMP')
        self.MERITchQt.clear()

        if TY <= 3:
            self.MERITchQt.setText('CRFT')
            self.MERITQt.setValue(CRFT)
        elif TY == 4:
            while True:
                if CRFT == z:
                    MeritList.append('CRFT')
                    q = True
                if SINC == z:
                    MeritList.append('SINC')
                    q = True
                if q: break
                z += 1
            #q2 = False
            #while True:
            #    if q2: break
            for i in MeritList:
                if i in PROFall:
                    self.MERITchQt.setText(i)
                    if i == 'CRFT':
                        self.MERITQt.setValue(CRFT)
                    else:
                        self.MERITQt.setValue(SINC)
            #        q2 = True
            if self.MERITchQt.text()=='':
                self.MERITchQt.setText(MeritList[0])
            if self.MERITchQt.text() == 'CRFT':
                self.MERITQt.setValue(CRFT)
            else:
                self.MERITQt.setValue(SINC)
            #q2 = True
        else:
            while True:
                if CRFT == z:
                    MeritList.append('CRFT')
                    q = True
                if SINC == z:
                    MeritList.append('SINC')
                    q = True
                if COMP == z:
                    MeritList.append('COMP')
                    q = True
                if q: break
                z += 1
            #q2 = False
            #while True:
            #if q2: break
            for x in MeritList:
                if x in PROFall:
                    self.MERITchQt.setText(x)
                    if x == 'CRFT':
                        self.MERITQt.setValue(CRFT)
                    elif x == 'SINC':
                        self.MERITQt.setValue(SINC)
                    else:
                        self.MERITQt.setValue(COMP)
            #        q2 = True
            if self.MERITchQt.text() == '':
                self.MERITchQt.setText(MeritList[0])
            if self.MERITchQt.text() == 'CRFT':
                self.MERITQt.setValue(CRFT)
            elif self.MERITchQt.text() == 'COMP':
                self.MERITQt.setValue(COMP)
            else:
                self.MERITQt.setValue(SINC)
            #q2 = True
        self.BuffPROFQt.show() if self.MERITchQt.text() in PROFall else self.BuffPROFQt.hide()

    def PROFallChange(self):
        if self.PROFQt.isChecked() and self.CRnameQt.currentText() == "New...":
            self.PCRFTQt.setEnabled(True)
            self.PSINCQt.setEnabled(True)
            self.PCOMPQt.setEnabled(True)

        elif not self.PROFQt.isChecked():
            self.PCRFTQt.setEnabled(False)
            self.PSINCQt.setEnabled(False)
            self.PCOMPQt.setEnabled(False)
            self.PCRFTQt.setChecked(False)
            self.PSINCQt.setChecked(False)
            self.PCOMPQt.setChecked(False)

        else:
            self.PCRFTQt.setEnabled(False)
            self.PSINCQt.setEnabled(False)
            self.PCOMPQt.setEnabled(False)
            CurName=self.CRnameQt.currentText()
            if CurName in ListDirCR and CurName!='New...':
                ProfTaked=CRall[CurName]['PROFall']
                self.PCRFTQt.setChecked(True) if 'CRFT' in ProfTaked else self.PCRFTQt.setChecked(False)
                self.PSINCQt.setChecked(True) if 'SINC' in ProfTaked else self.PSINCQt.setChecked(False)
                self.PCOMPQt.setChecked(True) if 'COMP' in ProfTaked else self.PCOMPQt.setChecked(False)

    def TChange(self):
        TY  = self.TYQt.value()
        STR = self.STRQt.value()
        TCh = self.TChQt.value()

        if STR > TY:
            self.TChQt.setEnabled(True)
            self.TChQt.setMinimum(TY-STR)
            self.TChQt.setMaximum(0)
            self.TQt.setValue(TY-TCh)

        elif STR == TY:
            self.TChQt.setEnabled(False)
            self.TChQt.setValue(0)
            self.TQt.setValue(TY)
            self.TChQt.setEnabled(False)

        elif STR < TY:
            self.TChQt.setEnabled(True)
            self.TChQt.setMinimum(0)
            self.TChQt.setMaximum(TY-STR)
            self.TQt.setValue(TY-TCh)

        self.DebaffSTRQt.show() if STR<self.TQt.value() else self.DebaffSTRQt.hide()

    def OMMRMminmax(self):
        OMall = self.OMQt.value() * 2
        NA = self.NAQt.isChecked()
        if OMall == 0:
            self.OMMQt.setEnabled(False)
            self.OMRQt.setEnabled(False)
            self.OMMQt.setValue(0)
            self.OMRQt.setValue(0)
            self.OMMChQt.setEnabled(False)
            self.OMMChQt.setValue(0)
        elif NA:
            self.OMMQt.setEnabled(True)
            self.OMRQt.setEnabled(True)
            self.OMMChQt.setEnabled(True) if OMall>0 and self.OMMChQt.value()>0 else self.OMMChQt.setEnabled(False)
            if self.OMQt.value() > 0:
                self.OMRQt.setMinimum(0)
                self.OMRQt.setMaximum(OMall)
                self.OMMQt.setMinimum(0)
                self.OMMQt.setMaximum(OMall)
            elif self.OMQt.value() < 0:
                self.OMRQt.setMinimum(OMall)
                self.OMRQt.setMaximum(0)
                self.OMMQt.setMinimum(OMall)
                self.OMMQt.setMaximum(0)
            else:
                self.OMRQt.setMinimum(0)
                self.OMRQt.setMaximum(0)
                self.OMMQt.setMinimum(0)
                self.OMMQt.setMaximum(0)

        if self.OMMQt.value() + self.OMRQt.value() == self.OMQt.value()*2 and not NA:
            self.DebaffMRQt.hide()
        else:
            self.DebaffMRQt.show()

    def OMminmax(self):
        NZ = self.NZQt.value()

        self.OSQt.setMinimum(0)
        self.OSQt.setMaximum(NZ**2)

        self.OMQt.setMinimum(1-NZ)
        self.OMQt.setMaximum(NZ-1)

    def DMminmax(self):
        self.DMQt.setMinimum(-self.NZQt.value())
        self.DMQt.setMaximum(self.NZQt.value())

    def OMMChange(self):
        OMM = self.OMMQt.value()
        OMR = self.OMRQt.value()
        OM2 = self.OMQt.value() * 2
        NA = self.NAQt.isChecked()

        if OMM > 0:
            self.OMMChQt.setMaximum(OMM)
            self.OMMChQt.setEnabled(True)
        else:
            self.OMMChQt.setEnabled(False)
            self.OMMChQt.setValue(0)

        if OMM - self.OMMChQt.value() <= 0:
            self.DebaffOMMQt.hide()
        else:
            self.DebaffOMMQt.show()

        if OMM + OMR == OM2 and NA:
            self.DebaffMRQt.hide()
        else:
            self.DebaffMRQt.show()

    def KolTYChange(self):
        self.KolTYQt.setValue(self.RQt.value()**2)

    def PChange(self):
        PCh = self.PChQt.value()
        TY = self.TYQt.value()

        P = TY//2

        if P:
            self.PChQt.setMinimum(1 - P)
        else:
            self.PChQt.setMinimum(0)

        self.PQt.setValue(P + PCh)

    def NZChange(self):
        R = self.RQt.value()
        TY = self.TYQt.value()
        if TY < R:
            self.NZQt.setValue(TY)
        else:
            self.NZQt.setValue(R)


    def NumRollChange(self):
        if self.TYQt.value != 0:
            Terp = 2 if self.TERPQt.isChecked() else 0
            self.NumRollQt.setValue(self.INTQt.value() + self.MERITQt.value() + Terp)

    def CrafterNameChange(self, CurrentCR):
        self.ASSchQt.setChecked(False)
        if CurrentCR in ListDirCR:
            self.INTQt.setEnabled(False)
            self.CRFTQt.setEnabled(False)
            self.PROFQt.setEnabled(False)
            self.TMQt.setEnabled(False)
            self.TERPQt.setEnabled(False)
            self.SINCQt.setEnabled(False)
            self.COMPQt.setEnabled(False)
            self.CRsaveQt.hide()
            self.CRsaveBTNQt.hide()

            self.INTQt.setValue(CRall[CurrentCR]['INT'])
            self.CRFTQt.setValue(CRall[CurrentCR]['CRFT'])
            self.SINCQt.setValue(CRall[CurrentCR]['SINC'])
            self.COMPQt.setValue(CRall[CurrentCR]['COMP'])
            self.RRchQt.setChecked(CRall[CurrentCR]['RR'])
            self.PROFQt.setChecked(CRall[CurrentCR]['PROF'])
            self.TMQt.setChecked(CRall[CurrentCR]['TM'])
            self.TERPQt.setChecked(CRall[CurrentCR]['TERP'])

        elif CurrentCR=='New...':
            self.INTQt.setEnabled(True)
            self.CRFTQt.setEnabled(True)
            self.PROFQt.setEnabled(True)
            self.TMQt.setEnabled(True)
            self.TERPQt.setEnabled(True)
            self.SINCQt.setEnabled(True)
            self.COMPQt.setEnabled(True)
            self.CRsaveQt.show()
            self.CRsaveBTNQt.show()

        else:
            self.INTQt.setEnabled(False)
            self.CRFTQt.setEnabled(False)
            self.PROFQt.setEnabled(False)
            self.TMQt.setEnabled(False)
            self.TERPQt.setEnabled(False)
            self.SINCQt.setEnabled(False)
            self.COMPQt.setEnabled(False)
            self.CRsaveQt.hide()
            self.CRsaveBTNQt.hide()


    def BPnameChange(self, CurrentBP):
        if CurrentBP in ListDirBP:
            self.TYQt.setEnabled(False)
            self.RQt.setEnabled(False)
            self.OMQt.setEnabled(False)
            self.QQt.setEnabled(False)
            self.STRQt.setEnabled(False)
            self.TChQt.setEnabled(False)
            self.NQt.setEnabled(False)
            self.PChQt.setEnabled(False)
            self.OSQt.setEnabled(False)
            self.KolTYQt.setEnabled(False)
            self.OMMQt.setEnabled(False)
            self.OMRQt.setEnabled(False)
            self.OMMChQt.setEnabled(False)
            self.DMQt.setEnabled(False)
            self.BPsaveQt.hide()
            self.BPsaveBTNQt.hide()

            #BPall.append([BPname,TY,R,OM,OMM,OMR,OMMCh,Q,STR,TCh,N,PCh,OS,DM])

            self.TYQt.setValue(BPall[CurrentBP]['TY'])
            self.RQt.setValue(BPall[CurrentBP]['R'])
            self.PChQt.setValue(BPall[CurrentBP]['PCh'])
            self.NQt.setValue(BPall[CurrentBP]['N'])
            self.OMQt.setValue(BPall[CurrentBP]['OM'])
            self.NAQt.setChecked(BPall[CurrentBP]['NA'])
            self.OMMQt.setValue(BPall[CurrentBP]['OMM'])
            self.OMRQt.setValue(BPall[CurrentBP]['OMR'])
            self.OMMChQt.setValue(BPall[CurrentBP]['OMMch'])
            self.DMQt.setValue(BPall[CurrentBP]['DM'])
            self.STRQt.setValue(BPall[CurrentBP]['STR'])
            self.TChQt.setValue(BPall[CurrentBP]['TCh'])
            self.OSQt.setValue(BPall[CurrentBP]['OS'])

            # Q def
            if BPall[CurrentBP]['Q'] == 0:
                self.QQt.setCurrentText('0: (10)')
            elif BPall[CurrentBP]['Q'] == 1:
                self.QQt.setCurrentText('+1: (9, 10)')
            elif BPall[CurrentBP]['Q'] == 2:
                self.QQt.setCurrentText('+2: (8, 9, 10)')
            elif BPall[CurrentBP]['Q'] == -1:
                self.QQt.setCurrentText('-1: (-)')
            elif BPall[CurrentBP]['Q'] == -2:
                self.QQt.setCurrentText('-2: (-1)')
            else:
                print('seems error in BPname Q')
            self.OMMQt.setEnabled(False)
            self.OMRQt.setEnabled(False)
            self.NAQt.setEnabled(False)
            self.OMMChQt.setEnabled(False)
            self.TChQt.setEnabled(False)

        elif CurrentBP=='New...':
            self.TYQt.setEnabled(True)
            self.RQt.setEnabled(True)
            self.OMQt.setEnabled(True)
            self.QQt.setEnabled(True)
            self.STRQt.setEnabled(True)
            self.TChQt.setEnabled(True)
            self.NQt.setEnabled(True)
            self.NAQt.setEnabled(True)
            self.PChQt.setEnabled(True)
            self.OSQt.setEnabled(True)
            if self.OMQt.value() > 0:
                self.OMMQt.setEnabled(True)
                self.OMRQt.setEnabled(True)
            if self.OMMQt.value() > 0:
                self.OMMChQt.setEnabled(True)
            self.TChQt.setEnabled(True)
            self.BPsaveQt.show()
            self.BPsaveBTNQt.show()
            self.DMQt.setEnabled(True)

        else:
            self.TYQt.setEnabled(False)
            self.RQt.setEnabled(False)
            self.OMQt.setEnabled(False)
            self.QQt.setEnabled(False)
            self.STRQt.setEnabled(False)
            self.TChQt.setEnabled(False)
            self.NQt.setEnabled(False)
            self.NAQt.setEnabled(False)
            self.PChQt.setEnabled(False)
            self.OSQt.setEnabled(False)
            self.OMMQt.setEnabled(False)
            self.OMRQt.setEnabled(False)
            self.OMMChQt.setEnabled(False)
            self.BPsaveQt.hide()
            self.BPsaveBTNQt.hide()
            self.DMQt.setEnabled(False)

    def Starting(self):
        self.CRnameQt.clear()
        self.CRnameQt.addItem('New...')
        x = 0
        while x != len(ListDirCR):
            self.CRnameQt.addItem(ListDirCR[x])
            x += 1
        self.CRnameQt.addItem('Select...')
        self.CRnameQt.addItem('Select...')
        self.CRnameQt.setCurrentIndex(x+1)

        self.BPnameQt.clear()
        self.BPnameQt.addItem('New...')
        x = 0
        while x != len(ListDirBP):
            self.BPnameQt.addItem(ListDirBP[x])
            x += 1
        self.BPnameQt.addItem('Select...')
        self.BPnameQt.addItem('Select...')
        self.BPnameQt.setCurrentIndex(x+1)

        self.DebaffSTRQt.hide()
        self.DebaffOMMQt.hide()
        self.BuffPROFQt.hide()
        self.DebaffCRFTQt.hide()
        self.DebaffMQt.hide()
        self.DebaffASSQt.hide()
        self.CRsaveBTNQt.hide()
        self.BPsaveBTNQt.hide()
        self.BPsaveQt.hide()
        self.CRsaveQt.hide()
        self.DebaffMRQt.hide()
        self.StartBtnQt.hide()
        self.OMQt.setValue(0)
        self.DMQt.setValue(0)

    def DelSelectCR(self):
        if self.CRnameQt.findText('Select...') != -1:
            self.CRnameQt.removeItem(len(self.CRnameQt) - 1)
    def DelSelectBP(self):
        if self.BPnameQt.findText('Select...') != -1:
            self.BPnameQt.removeItem(len(self.BPnameQt) - 1)



def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()                   # Создаём объект класса ExampleApp
    window.show()                           # Показываем окно
    app.exec_()                             # и запускаем приложение

if __name__ == '__main__':                  # Если мы запускаем файл напрямую, а не импортируем
    main()                                  # то запускаем функцию main()
