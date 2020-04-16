import sys
from PyQt5 import QtWidgets
import sqlite3
class Pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.conn()
        self.init_ui()
    def conn(self):
        self.baglanti=sqlite3.connect("kullanici.db")
        self.cursor=self.baglanti.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS members(username TEXT,pass TEXT)")
        self.baglanti.commit()
    def init_ui(self):
        self.kullanici_adi=QtWidgets.QLineEdit()
        self.parola=QtWidgets.QLineEdit()
        self.parola.setEchoMode(QtWidgets.QLineEdit.Password)
        self.giris=QtWidgets.QPushButton("Giris Yap(Login)")
        self.yazialan=QtWidgets.QLabel("")
        self.reg=QtWidgets.QPushButton("Kayıt Ol(Register)")
        v_box=QtWidgets.QVBoxLayout()
        v_box.addWidget(self.kullanici_adi)
        v_box.addWidget(self.parola)
        v_box.addWidget(self.yazialan)
        v_box.addStretch()
        v_box.addWidget(self.giris)
        v_box.addWidget(self.reg)
        h_box=QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()
        self.setLayout(h_box)
        self.setWindowTitle("Kullanıcı Giris Example")
        self.giris.clicked.connect(self.login)
        self.reg.clicked.connect(self.register)
        self.show()
    def login(self):
        name=self.kullanici_adi.text()
        pas=self.parola.text()
        self.cursor.execute("Select * From members where username=? and pass=?",(name,pas))
        data=self.cursor.fetchall()
        if len(data)==0:
            self.yazialan.setText("Malesef Böyle Bİr Kullanıcı Yok\nLütfen Tekrar Deneyin")
        else:
            self.yazialan.setText("Welcome "+name)
    def register(self):
        name=self.kullanici_adi.text()
        pas=self.parola.text()
        self.cursor.execute("Insert into members Values(?,?)",(name,pas))
        self.baglanti.commit()
        self.yazialan.setText("Basariyla Kaydedildi(Succesful!)")
app=QtWidgets.QApplication(sys.argv)
pencere=Pencere()
sys.exit(app.exec())