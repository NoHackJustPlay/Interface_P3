#!/usr/bin/python3

import sys

from fractions import Fraction
import numpy as np
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QPushButton

class Window(QWidget):
    def __init__ (self):
        super.setWindowTitle( " Mon application")
        self.setGeometry(50,50,400,300)
        self.UI()
        
    def UI(self):
        self.text1=QLabel("Lancer la fonction",self)
        enterButton=QPushButton(" Entrer",self)
        self.text1.move= (100,80)
        enterButton.clicked.connect=(self.enter_Function)
        self.show()
    
    def enter_Function(self):
        data=[]

        DP=np.linspace(2, 3, 4)
        
        for i in DP:

            data += [(Fraction(str(i)))]
    
            print(data,end =',')

def main():
    App=QApplication(sys.argv)
    window=Window()
    sys.exit(App.exec_())
        