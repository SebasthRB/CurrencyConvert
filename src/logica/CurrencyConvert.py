import sys
import os
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5 import uic

class Dialogo (QMainWindow):
    # Tipo de cambio 20240619
    USDtoPEN = 3.84
    USDtoEUR = 0.93
    USDtoGBP = 0.79

    def __init__(self):
        ruta = os.path.dirname ( os.path.abspath ( __file__ ) ) + r"\..\vista\currencyConvert.ui"
        QMainWindow.__init__(self)
        uic.loadUi(ruta,self)

        self.pbTipoCambio.clicked.connect(self.calcularConversion)

    def calcularConversion( self ):
        convertido=0.0
        inicial=0.0

        inicial=float(self.leImporte.text())
        convertido=inicial

        #CALCULO DE CAMBIO DE MONEDA
        if self.rbDeUSD.isChecked():
            if self.rbAUSD.isChecked():
                convertido = 1
            elif self.rbAEUR.isChecked():
                convertido = inicial * self.USDtoEUR
            elif self.rbAPEN.isChecked():
                convertido = inicial * self.USDtoPEN
            elif self.rbAGBP.isChecked():
                convertido = inicial * self.USDtoGBP

        elif self.rbDeEUR.isChecked():
            if self.rbAUSD.isChecked():
                convertido = inicial / self.USDtoEUR
            elif self.rbAEUR.isChecked():
                convertido = 1
            elif self.rbAPEN.isChecked():
                convertido = (inicial / self.USDtoEUR) * self.USDtoPEN
            elif self.rbAGBP.isChecked():
                convertido = (inicial / self.USDtoEUR) * self.USDtoGBP

        elif self.rbDePEN.isChecked():
            if self.rbAUSD.isChecked():
                convertido = inicial / self.USDtoPEN
            elif self.rbAEUR.isChecked():
                convertido = (inicial / self.USDtoPEN) * self.USDtoEUR
            elif self.rbAPEN.isChecked():
                convertido = 1
            elif self.rbAGBP.isChecked():
                convertido = (inicial / self.USDtoPEN) * self.USDtoGBP

        elif self.rbDeGBP.isChecked():
            if self.rbAUSD.isChecked():
                convertido = inicial / self.USDtoGBP
            elif self.rbAEUR.isChecked():
                convertido = (inicial / self.USDtoGBP) * self.USDtoEUR
            elif self.rbAPEN.isChecked():
                convertido = (inicial / self.USDtoGBP) * self.USDtoPEN
            elif self.rbAGBP.isChecked():
                convertido = 1
        # FIN DE CALCULO DE CAMBIO DE MONEDA

        self.lblCambio.setText(f"{convertido:.2f}")

if __name__ == '__main__':
    app=QApplication(sys.argv)
    dialogo=Dialogo()
    dialogo.show()
    app.exec_()