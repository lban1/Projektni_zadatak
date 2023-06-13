from PyQt5.QtWidgets import QApplication, QLineEdit, QMainWindow, QLabel, QPushButton,QComboBox
from PyQt5 import QtGui, QtCore, QtWidgets
import sys
from enumeratori import TipKorisnika, TipArtikla
from korisnici import PoslovniKorisnik,PrivatniKorisnik
from kategorije import unos_kategorije, ispis_svih_kategorija
from korisnici import unos_korisnika, ispis_svih_korisnika
from prodaje import unos_prodaje, ispis_svih_prodaja
from utilities import unos_intervala, provjera_korisnickog_unosa

korisnici = []
kategorije = []
prodaje = []

'''while True:
    print('-' * 20)
    print('1. Unos novog korisnika')
    print('2. Unos nove kategorije')
    print('3. Unos nove prodaje')
    print('4. Ispis korisnika')
    print('5. Ispis kategorija')
    print('6. Ispis prodaja')
    print('7. Zaustavi program')
    print('-' * 20)

    akcija = unos_intervala(1,7)

    if akcija == 1:
        korisnici.append(unos_korisnika(len(korisnici)+1))
    elif akcija == 2:
        kategorije.append(unos_kategorije(len(kategorije)+1))
    elif akcija == 3:
        prodaja_provjera = unos_prodaje(korisnici, kategorije, len(prodaje)+1)
        if prodaja_provjera != 0:
            prodaje.append(prodaja_provjera)
    elif akcija == 4:
        ispis_svih_korisnika(korisnici)
    elif akcija == 5:
        ispis_svih_kategorija(kategorije)
    elif akcija == 6:
        ispis_svih_prodaja(prodaje)
    elif akcija == 7:
        break'''

class MojProzor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Objektno")
        self.setGeometry(500, 300, 400, 300)
        self.initUI()

    def initUI(self):
        self.izbornik = QComboBox(self)
        self.font = QtGui.QFont('Areal', 10)


        for korisnik in TipKorisnika:
            self.izbornik.addItem(korisnik.value)

        self.izbornik.setGeometry(QtCore.QRect(150, 25, 150, 25))
        self.izbornik.currentTextChanged.connect(self.on_combobox_change)

        # Text telefon
        self.text_tel = QtWidgets.QLabel(self)
        self.text_tel.setFont(self.font)
        self.text_tel.setText('Telefon')
        self.text_tel.move(50, 60)

        # Input telefon
        self.input_tel = QtWidgets.QLineEdit(self)
        self.input_tel.setGeometry(QtCore.QRect(150, 60, 150, 25))

        # Text email
        self.text_email = QtWidgets.QLabel(self)
        self.text_email.setFont(self.font)
        self.text_email.setText('Email')
        self.text_email.move(50, 90)

        # Input email
        self.input_email = QtWidgets.QLineEdit(self)
        self.input_email.setGeometry(QtCore.QRect(150, 90, 150, 25))

        # Text ime
        self.text_ime = QtWidgets.QLabel(self)
        self.text_ime.setFont(self.font)
        self.text_ime.setText('Ime')
        self.text_ime.move(50, 120)

        # Input ime
        self.input_ime = QtWidgets.QLineEdit(self)
        self.input_ime.setGeometry(QtCore.QRect(150, 120, 150, 25))

        # Text prezime
        self.text_prezime = QtWidgets.QLabel(self)
        self.text_prezime.setFont(self.font)
        self.text_prezime.setText('Prezime')
        self.text_prezime.move(50, 150)

        # Input prezime
        self.input_prezime = QtWidgets.QLineEdit(self)
        self.input_prezime.setGeometry(QtCore.QRect(150, 150, 150, 25))

        # Text naziv
        self.text_naziv = QtWidgets.QLabel(self)
        self.text_naziv.setFont(self.font)
        self.text_naziv.setText('Naziv')
        self.text_naziv.move(50, 120)
        self.text_naziv.hide()

        # Input naziv
        self.input_naziv = QtWidgets.QLineEdit(self)
        self.input_naziv.setGeometry(QtCore.QRect(150, 120, 150, 25))
        self.input_naziv.hide()

        # Text web
        self.text_web = QtWidgets.QLabel(self)
        self.text_web.setFont(self.font)
        self.text_web.setText('Web')
        self.text_web.move(50, 150)
        self.text_web.hide()

        # Input web
        self.input_web = QtWidgets.QLineEdit(self)
        self.input_web.setGeometry(QtCore.QRect(150, 150, 150, 25))
        self.input_web.hide()

        # Text greska
        self.text_error = QtWidgets.QLabel(self)
        self.text_error.setFont(self.font)
        self.text_error.setAlignment(QtCore.Qt.AlignCenter)
        self.text_error.setStyleSheet('color : red')
        self.text_error.setGeometry(QtCore.QRect(70, 200, 200, 30))

        # Button unos korisnika
        self.button_unoskorisnika = QtWidgets.QPushButton(self)
        self.button_unoskorisnika.setFont(self.font)
        self.button_unoskorisnika.setText('Unesi korisnika')
        self.button_unoskorisnika.setGeometry(QtCore.QRect(100, 240, 150, 30))
        self.button_unoskorisnika.clicked.connect(self.unos_korisnika)
    def on_combobox_change(self):
        if self.izbornik.currentText() == TipKorisnika.POSLOVNI.value:
            self.input_naziv.show()
            self.text_naziv.show()
            self.input_web.show()
            self.text_web.show()
            self.input_ime.hide()
            self.text_ime.hide()
            self.input_prezime.hide()
            self.text_prezime.hide()
            self.input_tel.setText('')
            self.input_email.setText('')
            self.input_ime.setText('')
            self.input_prezime.setText('')
            self.input_naziv.setText('')
            self.input_web.setText('')
            self.text_error.setText('')
        elif self.izbornik.currentText() == TipKorisnika.PRIVATNI.value:
            self.input_naziv.hide()
            self.text_naziv.hide()
            self.input_web.hide()
            self.text_web.hide()
            self.input_ime.show()
            self.text_ime.show()
            self.input_prezime.show()
            self.text_prezime.show()
            self.input_tel.setText('')
            self.input_email.setText('')
            self.input_ime.setText('')
            self.input_prezime.setText('')
            self.input_naziv.setText('')
            self.input_web.setText('')
            self.text_error.setText('')
    def unos_korisnika(self):
        if self.izbornik.currentText() == TipKorisnika.PRIVATNI.value:
            error_privatni = provjera_korisnickog_unosa(self.input_tel.text(), self.input_email.text(), self.input_ime.text(), self.input_prezime.text())

            if error_privatni == None:
                korisnici.append(PrivatniKorisnik(self.input_tel.text(), self.input_email.text(), self.input_ime.text(), self.input_prezime.text()))

                korisnik = korisnici[len(korisnici)-1]
                korisnik.ispis()

                self.input_tel.setText('')
                self.input_email.setText('')
                self.input_ime.setText('')
                self.input_prezime.setText('')
                self.text_error.setText('')
            else:
                self.text_error.setText(error_privatni)
        elif self.izbornik.currentText() == TipKorisnika.POSLOVNI.value:
            error_poslovni = provjera_korisnickog_unosa(self.input_tel.text(), self.input_email.text(), self.input_naziv.text(), self.input_web.text())

            if error_poslovni == None:
                korisnici.append(PoslovniKorisnik(self.input_tel.text(), self.input_email.text(), self.input_naziv.text(), self.input_web.text()))

                korisnik = korisnici[len(korisnici) - 1]
                korisnik.ispis()

                self.input_tel.setText('')
                self.input_email.setText('')
                self.input_naziv.setText('')
                self.input_web.setText('')
                self.text_error.setText('')
            else:
                self.text_error.setText(error_poslovni)

app = QApplication(sys.argv)
window = MojProzor()
window.show()
sys.exit(app.exec_())

