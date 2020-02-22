import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide2.QtCore import QFile
from calcui import Ui_Form

def takeLastItem(strMath):
    sNum = ''
    listNumAndSymbol = []
    strMath = strMath.replace(' ','')
    for k in strMath:
        if k.isdigit() or k == '.':
            sNum += k
        elif sNum:
            listNumAndSymbol.append(sNum)
            listNumAndSymbol.append(k)
            sNum = ''
        else:
            listNumAndSymbol.append(k)

    if sNum:
        listNumAndSymbol.append(sNum)
    
    return listNumAndSymbol[-1]

def lastIsSymb(a):
    li = takeLastItem(a)
    if li.replace('.','').isdigit():
        return False
    return True

def checkDotInString(a):
    num = takeLastItem(a)
    d = 0;
    for k in str(num):
        if k == '.':
            d = d + 1
    if d > 1:
        return False
    return True


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
    def stest(self):
        print (self.text())

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    ob = window.ui

    def pasteValueOnLineEdit(self):
        if self:
            print (self.text())
        else:
            print ('Click without argument')
    
    # Problem: When i paste argument into connect function, function worked without click



    # Ready and easy to use
    ob.pushButton_1.clicked.connect(lambda: ob.lineEdit.setText(ob.lineEdit.text() + '1'))
    ob.pushButton_2.clicked.connect(lambda: ob.lineEdit.setText(ob.lineEdit.text() + '2'))
    ob.pushButton_3.clicked.connect(lambda: ob.lineEdit.setText(ob.lineEdit.text() + '3'))
    ob.pushButton_4.clicked.connect(lambda: ob.lineEdit.setText(ob.lineEdit.text() + '4'))
    ob.pushButton_5.clicked.connect(lambda: ob.lineEdit.setText(ob.lineEdit.text() + '5'))
    ob.pushButton_6.clicked.connect(lambda: ob.lineEdit.setText(ob.lineEdit.text() + '6'))
    ob.pushButton_7.clicked.connect(lambda: ob.lineEdit.setText(ob.lineEdit.text() + '7'))
    ob.pushButton_8.clicked.connect(lambda: ob.lineEdit.setText(ob.lineEdit.text() + '8'))
    ob.pushButton_9.clicked.connect(lambda: ob.lineEdit.setText(ob.lineEdit.text() + '9'))
    ob.plusButton.clicked.connect(lambda: ob.lineEdit.setText(ob.lineEdit.text() + '+'))
    ob.minusButton.clicked.connect(lambda: ob.lineEdit.setText(ob.lineEdit.text() + '-'))
    ob.miltiplyButton.clicked.connect(lambda: ob.lineEdit.setText(ob.lineEdit.text() + '*'))
    ob.dividButton.clicked.connect(lambda: ob.lineEdit.setText(ob.lineEdit.text() + '/'))
    ob.pushButton_0.clicked.connect(lambda: ob.lineEdit.setText(ob.lineEdit.text() + '0'))
    ob.startBracketButton.clicked.connect(lambda: ob.lineEdit.setText(ob.lineEdit.text() + '('))
    ob.endBracketButton.clicked.connect(lambda: ob.lineEdit.setText(ob.lineEdit.text() + ')'))
   

    # Button then need special functional

    def canDot():
        if not ob.lineEdit.text():
            ob.lineEdit.setText('0.')
        elif checkDotInString(ob.lineEdit.text()):
            ob.lineEdit.setText(ob.lineEdit.text() + '.')  
        elif lastIsSymb(ob.lineEdit.text()):
            ob.lineEdit.setText(ob.lineEdit.text() + '0.')    
            
    ob.dotButton.clicked.connect(canDot)

    ob.equalsButton.clicked.connect(lambda: ob.lineEdit.setText(str(eval(ob.lineEdit.text()))))
    ob.clearButton.clicked.connect(lambda: ob.lineEdit.setText(''))
    ob.deleteButton.clicked.connect(lambda: ob.lineEdit.setText(ob.lineEdit.text()[0:-1]))

    sys.exit(app.exec_())

    
