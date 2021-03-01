# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mus_form.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Mus_FormWindow(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(421, 330)
        self.formLayoutWidget = QtWidgets.QWidget(Form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 20, 361, 261))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.ad_lbl = QtWidgets.QLabel(self.formLayoutWidget)
        self.ad_lbl.setEnabled(True)
        self.ad_lbl.setObjectName("ad_lbl")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.ad_lbl)
        self.mus_adi = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.mus_adi.setObjectName("mus_adi")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.mus_adi)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.mus_soyadi = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.mus_soyadi.setObjectName("mus_soyadi")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.mus_soyadi)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.mus_tel = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.mus_tel.setObjectName("mus_tel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.mus_tel)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.mus_adres = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.mus_adres.setObjectName("mus_adres")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.mus_adres)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.dateEdit = QtWidgets.QDateEdit(self.formLayoutWidget)
        self.dateEdit.setObjectName("dateEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.dateEdit)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.isyeri = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.isyeri.setObjectName("isyeri")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.isyeri)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(8, QtWidgets.QFormLayout.LabelRole, spacerItem)
        self.mus_add_btn = QtWidgets.QPushButton(self.formLayoutWidget)
        self.mus_add_btn.setObjectName("mus_add_btn")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.SpanningRole, self.mus_add_btn)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.ad_lbl.setText(_translate("Form", "Müşteri Adı:"))
        self.label_2.setText(_translate("Form", "Müşteri Soyadı:"))
        self.label_3.setText(_translate("Form", "Telefon Numarası:"))
        self.label_4.setText(_translate("Form", "Adres:"))
        self.label_5.setText(_translate("Form", "Kayıt Tarihi:"))
        self.label_6.setText(_translate("Form", "İşyeri & Şirket :"))
        self.mus_add_btn.setText(_translate("Form", "Kayıt Ekle"))
