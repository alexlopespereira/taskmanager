# -*- coding: utf-8 -*-
"""
/***************************************************************************
 taskmanagerDialog
                                 A QGIS plugin
 Atribui uma feição a um usuário
                             -------------------
        begin                : 2016-02-02
        git sha              : $Format:%H$
        copyright            : (C) 2016 by Alex Lopes Pereira
        email                : alex.pereira@sipam.gov.br
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os

from PyQt4 import QtGui, uic
from PyQt4.QtGui import *
from PyQt4.QtCore import *

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'db_connection.ui'))


class dbconnectionDialog(QtGui.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(dbconnectionDialog, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
        self.buttonBox.button(QDialogButtonBox.Ok).clicked.connect(self.handleLogin)

    def handleLogin(self):
        self.textName = self.lineEdit.text()
        self.textPass = self.lineEdit_2.text()
        if (self.textName != '' and self.textPass != ''):
            self.accept()
        else:
            QtGui.QMessageBox.warning(self, 'Error', 'Bad user or password')

    def getUsername(self):
        return self.textName

    def getPassword(self):
        return self.textPass

    def setUsername(self, name):
        self.textName=name

    def setRealm(self, realm):
        self.label_4.setText(realm)