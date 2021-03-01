from win import Ui_MainWindow
import mysql.connector
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import *
from PyQt5.QtCore import *
import sys
from db_bilgileri import *
from datetime import datetime
import pandas as pd

class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data,header_labels):
        super(TableModel, self).__init__()
        self._data = data
        self.header_labels = header_labels

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self.header_labels[section]
        return QAbstractTableModel.headerData(self, section, orientation, role)
        

    def data(self, index, role):
        if role == Qt.DisplayRole:
            # See below for the nested-list data structure.
            # .row() indexes into the outer list,
            # .column() indexes into the sub-list
            return self._data[index.row()][index.column()]

    def rowCount(self, index):
        # The length of the outer list.
        return len(self._data)

    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        try:
            return len(self._data[0])
        except:
            return len(self._data)


class Muhasebe(QMainWindow):

    def __init__(self):
        super(Muhasebe,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.db_baglantisi()
        self.dbden_kayit_getir("musteri")
        self.ui.mus_add_btn.clicked.connect(self.kontrol_musteri)
        
        self.menubar = QMenuBar(self)
        self.setMenuBar(self.menubar)
        
        self.uyariMenusu = QMenu(self)
        self.uyariMenusu.setTitle("Uyarı")
        self.menubar.addMenu(self.uyariMenusu)

        self.uyariAksiyonu = QAction(self)
        self.uyariAksiyonu.setText("Uyarı")
        self.uyariMenusu.addAction(self.uyariAksiyonu)
        
        # self.ui.table_record.itemChanged.connect(lambda: self.veri_degisti(self.ui.table_record))
        self.ui.mus_sil.clicked.connect(lambda: self.kayit_sil(self.ui.table_view))
        self.ui.search_box.textChanged.connect(lambda: self.arama(self.ui.table_view))
        self.ui.drop_down.currentIndexChanged.connect(lambda: self.arama(self.ui.table_view))

    def siraya_gore_id_bul(self,row,tablo_adi):
        pass
        #KULLANILMIYOR
        # fetch_query = """SELECT id{} FROM {}""".format(tablo_adi,tablo_adi)
        # self.cursor.execute(fetch_query)
        # veriler = self.cursor.fetchall()
        # return veriler[row][0]
        
    def kontrol_telefon(self,nesne,value):
        try:
            return nesne.objectName() == "mus_tel" and not value.isnumeric()
        except Exception:
            return nesne == "Telefon" and not value.isnumeric()
    
    def kontrol_tarih(self,value):
        try:
            tarih = datetime.strptime(value,'%d.%m.%Y')
            print(tarih)
            return tarih
        except Exception as err:
            print(err)

    def uyari_tel(self,nesne):
        self.uyariKutusuGoster("Telefon numarası rakamlardan oluşmalıdır!","warning")
        try:
            nesne.setFocus()
        except Exception:
            pass
    
    def aynisi_varmi(self,tablo:str,**kwargs):

        if tablo == "musteri" and kwargs["ad"] and kwargs["soyad"]:
            sql = """SELECT Ad, Soyad FROM musteri WHERE Ad = '{}' and Soyad = '{}'""".format(kwargs["ad"],kwargs["soyad"])
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            print(len(result))
            if len(result) > 0:
                self.uyariKutusuGoster("Eklemeye çalıştığınız müşteri kaydı veritabanında zaten mevcut!","warning")
                return False
            else:
                return True

    def kontrol_musteri(self):
        musteri_bilgileri = []
        zorunlular = 0
        result = self.ui.mus_form
        
        for i in range(result.count()):
            if isinstance(result.itemAt(i).widget(),(QLineEdit,QDateEdit)):
                zorunlular += 1
                nesne = result.itemAt(i).widget()
                value = nesne.text()
                
                if not value:
                    self.uyariKutusuGoster("Lütfen müşteri bilgilerini eksiksiz doldurunuz!","warning")
                    break
                
                elif self.kontrol_telefon(nesne,value):
                    self.uyari_tel(nesne)
                    break
                    
                
                elif nesne.objectName() == "dateEdit":
                    tarih = self.kontrol_tarih(value)
                    musteri_bilgileri.append(tarih)
                    
                else:
                    musteri_bilgileri.append(value)
                    nesne.clear()
        
        if zorunlular == len(musteri_bilgileri) and self.aynisi_varmi(tablo="musteri",ad=musteri_bilgileri[0],soyad=musteri_bilgileri[1]):
            self.kayit_db(veriler = musteri_bilgileri, tablo = "musteri")
                        
    def db_baglantisi(self):
        self.conn = mysql.connector.connect(host=hostname,user=username,password=password,database=dbname)
        self.cursor = self.conn.cursor()
        
    def kayit_db(self,veriler,tablo:str):
        try:
            if tablo == "musteri":
                sql = "INSERT INTO {} (Ad, Soyad, Telefon, Adres, Tarih, İsyeri) VALUES (%s,%s,%s,%s,%s,%s)".format(tablo)
                self.cursor.execute(sql,veriler)
                self.conn.commit()
                
                self.uyariKutusuGoster(f"{self.cursor.rowcount} müşteri kaydı başarıyla eklendi","info")
                
                self.dbden_kayit_getir(tablo)
        except Exception as err:
            print(err)
            
        finally:
            pass
                        
    def uyariKutusuGoster(self,mesaj:str,uyarı_turu:str):
        
        if uyarı_turu == "warning":
            QMessageBox.warning(self, "Hata", mesaj)
        
        elif uyarı_turu == "info":
            QMessageBox.information(self, "Bilgi", mesaj)

    def combo_box_doldur(self,kolon_isimleri,tablo:str):
        if tablo == "musteri":
            self.ui.drop_down.addItems(kolon_isimleri[1:])

    def dbden_kayit_getir(self,tablo:str):
        data = []
        sorgu = "SELECT * FROM {} ".format(tablo)
        self.cursor.execute(sorgu)
        kayitlar = self.cursor.fetchall()
        kolon_isimleri = self.cursor.description
        kolon_isimleri = tuple(i[0] for i in kolon_isimleri)
        self.combo_box_doldur(kolon_isimleri,tablo)

        for i in kayitlar:
           stri = str(i[-1])
           i = i[:-1]
           li = [x for x in i]
           li.append(stri)
           data.append(li)
        self.model = TableModel(data,kolon_isimleri)
        self.ui.table_view.setModel(self.model)
        self.ui.table_view.setColumnHidden(0,True)

    def veri_degisti(self,tablo):
        result = tablo.selectedIndexes()
        if tablo.objectName() == "table_record":
            tablo_adi = "musteri"
            for nesne in result:
                
                data = nesne.data()
                row = nesne.row()
                kolon = nesne.column()+1
                degistirilecek = self.siraya_gore_id_bul(row,tablo_adi)
                kolon_adi = tablo.horizontalHeaderItem(kolon-1).text()
                if self.kontrol_telefon(kolon_adi,data):
                    self.uyari_tel(nesne)
                    sql = """select {} from {} where id{} = {}""".format(kolon_adi,tablo_adi,tablo_adi,degistirilecek)
                    self.cursor.execute(sql)
                    deger = str(self.cursor.fetchone()[0])
                    self.ui.table_record.item(row,kolon-1).setText(deger)
                    break
                
                
                sql = "update {} set {} = '{}' where id{} = {}".format(tablo_adi,kolon_adi,data,tablo_adi,degistirilecek)
                print(sql)
                sql = self.cursor.execute(sql) 
                self.conn.commit()
                    
      
    def kayit_sil(self,tablo):
        result = tablo.selectionModel().selectedIndexes()
        print(result)
        result.reverse()
        print(tablo.objectName())
        if len(result) < 1:
            self.uyariKutusuGoster("Lütfen silmek istediğiniz kaydı/kayıtları seçin!","warning")

        if tablo.objectName() == "table_view":
            tablo_adi = "musteri"
            for i in result:
                index = i.row()
                x = tablo.model().index(index,0)
                res = tablo.model().data(x,role=0)
                sql = """DELETE FROM {} WHERE id{} = {}""".format(tablo_adi,tablo_adi,res)
                self.cursor.execute(sql)
                self.conn.commit()

            self.dbden_kayit_getir("musteri")
        
    def arama(self,tablo:str):
        self.filtre = QSortFilterProxyModel()
        self.filtre.setSourceModel(self.model)
        kolon = int(self.ui.drop_down.currentIndex()) + 1
        self.filtre.setFilterKeyColumn(kolon)
        text = self.ui.search_box.text()
        self.filtre.setFilterRegExp(text)
        self.ui.table_view.setModel(self.filtre)
        

                
        
def app():
    app = QtWidgets.QApplication(sys.argv)
    win = Muhasebe()
    win.show()
    sys.exit(app.exec())
app()