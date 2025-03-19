# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'map_generator.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
                           QCursor, QFont, QFontDatabase, QGradient,
                           QIcon, QImage, QKeySequence, QLinearGradient,
                           QPainter, QPalette, QPixmap, QRadialGradient,
                           QTransform)
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QHBoxLayout, QLabel,
                               QLineEdit, QMainWindow, QMenu, QMenuBar,
                               QPushButton, QSizePolicy, QSlider, QSpacerItem,
                               QSpinBox, QStackedWidget, QStatusBar, QToolButton,
                               QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1290, 1175)
        self.actionDefault_Mode = QAction(MainWindow)
        self.actionDefault_Mode.setObjectName(u"actionDefault_Mode")
        self.actionExpert_Mode = QAction(MainWindow)
        self.actionExpert_Mode.setObjectName(u"actionExpert_Mode")
        self.actionHelp = QAction(MainWindow)
        self.actionHelp.setObjectName(u"actionHelp")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_3 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.generator_stack = QStackedWidget(self.centralwidget)
        self.generator_stack.setObjectName(u"generator_stack")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout = QVBoxLayout(self.page)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.generate_image_label_def = QLabel(self.page)
        self.generate_image_label_def.setObjectName(u"generate_image_label_def")
        self.generate_image_label_def.setMinimumSize(QSize(700, 700))
        self.generate_image_label_def.setScaledContents(False)
        self.generate_image_label_def.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.generate_image_label_def)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)

        self.label = QLabel(self.page)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(12)
        self.label.setFont(font)

        self.verticalLayout_2.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.shape_spin_def = QSpinBox(self.page)
        self.shape_spin_def.setObjectName(u"shape_spin_def")
        self.shape_spin_def.setMaximum(2561)
        self.shape_spin_def.setDisplayIntegerBase(10)

        self.horizontalLayout.addWidget(self.shape_spin_def)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.label_3 = QLabel(self.page)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_2.addWidget(self.label_3)

        self.seed_spin_def = QSpinBox(self.page)
        self.seed_spin_def.setObjectName(u"seed_spin_def")
        self.seed_spin_def.setMaximum(99990)

        self.verticalLayout_2.addWidget(self.seed_spin_def)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.generate_button_def = QPushButton(self.page)
        self.generate_button_def.setObjectName(u"generate_button_def")
        self.generate_button_def.setEnabled(True)

        self.verticalLayout_4.addWidget(self.generate_button_def)

        self.label_2 = QLabel(self.page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.generator_stack.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.horizontalLayout_13 = QHBoxLayout(self.page_2)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.generate_image_label_exp = QLabel(self.page_2)
        self.generate_image_label_exp.setObjectName(u"generate_image_label_exp")
        self.generate_image_label_exp.setMinimumSize(QSize(700, 700))
        self.generate_image_label_exp.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.generate_image_label_exp)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_5)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_5)

        self.label_4 = QLabel(self.page_2)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_3.addWidget(self.label_4)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.scale_slider = QSlider(self.page_2)
        self.scale_slider.setObjectName(u"scale_slider")
        self.scale_slider.setMinimum(10)
        self.scale_slider.setMaximum(200)
        self.scale_slider.setSingleStep(1)
        self.scale_slider.setTracking(True)
        self.scale_slider.setOrientation(Qt.Horizontal)
        self.scale_slider.setTickInterval(0)

        self.horizontalLayout_4.addWidget(self.scale_slider)

        self.scale_spin_box = QDoubleSpinBox(self.page_2)
        self.scale_spin_box.setObjectName(u"scale_spin_box")
        self.scale_spin_box.setMinimum(0.100000000000000)
        self.scale_spin_box.setMaximum(2.000000000000000)
        self.scale_spin_box.setSingleStep(0.100000000000000)

        self.horizontalLayout_4.addWidget(self.scale_spin_box)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.label_5 = QLabel(self.page_2)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_3.addWidget(self.label_5)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.octaves_slider = QSlider(self.page_2)
        self.octaves_slider.setObjectName(u"octaves_slider")
        self.octaves_slider.setMinimum(1)
        self.octaves_slider.setMaximum(12)
        self.octaves_slider.setOrientation(Qt.Horizontal)
        self.octaves_slider.setTickPosition(QSlider.NoTicks)

        self.horizontalLayout_5.addWidget(self.octaves_slider)

        self.octaves_spin_box = QSpinBox(self.page_2)
        self.octaves_spin_box.setObjectName(u"octaves_spin_box")
        self.octaves_spin_box.setMinimum(1)
        self.octaves_spin_box.setMaximum(12)

        self.horizontalLayout_5.addWidget(self.octaves_spin_box)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.label_6 = QLabel(self.page_2)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_3.addWidget(self.label_6)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.persistence_slider = QSlider(self.page_2)
        self.persistence_slider.setObjectName(u"persistence_slider")
        self.persistence_slider.setMinimum(10)
        self.persistence_slider.setMaximum(200)
        self.persistence_slider.setSingleStep(1)
        self.persistence_slider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_6.addWidget(self.persistence_slider)

        self.persistence_spin_box = QDoubleSpinBox(self.page_2)
        self.persistence_spin_box.setObjectName(u"persistence_spin_box")
        self.persistence_spin_box.setMinimum(0.100000000000000)
        self.persistence_spin_box.setMaximum(2.000000000000000)
        self.persistence_spin_box.setSingleStep(0.100000000000000)

        self.horizontalLayout_6.addWidget(self.persistence_spin_box)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.label_7 = QLabel(self.page_2)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_3.addWidget(self.label_7)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.lacunarity_slider = QSlider(self.page_2)
        self.lacunarity_slider.setObjectName(u"lacunarity_slider")
        self.lacunarity_slider.setMinimum(10)
        self.lacunarity_slider.setMaximum(400)
        self.lacunarity_slider.setSingleStep(1)
        self.lacunarity_slider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_7.addWidget(self.lacunarity_slider)

        self.lacunarity_spin_box = QDoubleSpinBox(self.page_2)
        self.lacunarity_spin_box.setObjectName(u"lacunarity_spin_box")
        self.lacunarity_spin_box.setMinimum(0.100000000000000)
        self.lacunarity_spin_box.setMaximum(4.000000000000000)
        self.lacunarity_spin_box.setSingleStep(0.100000000000000)

        self.horizontalLayout_7.addWidget(self.lacunarity_spin_box)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        self.get_default_vals_button_exp = QPushButton(self.page_2)
        self.get_default_vals_button_exp.setObjectName(u"get_default_vals_button_exp")

        self.verticalLayout_3.addWidget(self.get_default_vals_button_exp)

        self.label_8 = QLabel(self.page_2)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_3.addWidget(self.label_8)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.shape_spin_exp = QSpinBox(self.page_2)
        self.shape_spin_exp.setObjectName(u"shape_spin_exp")
        self.shape_spin_exp.setMaximum(2561)

        self.horizontalLayout_8.addWidget(self.shape_spin_exp)


        self.verticalLayout_3.addLayout(self.horizontalLayout_8)

        self.label_9 = QLabel(self.page_2)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_3.addWidget(self.label_9)

        self.seed_spin_exp = QSpinBox(self.page_2)
        self.seed_spin_exp.setObjectName(u"seed_spin_exp")
        self.seed_spin_exp.setMaximum(99989)

        self.verticalLayout_3.addWidget(self.seed_spin_exp)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_10 = QLabel(self.page_2)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_12.addWidget(self.label_10)

        self.terrain_info = QToolButton(self.page_2)
        self.terrain_info.setObjectName(u"terrain_info")

        self.horizontalLayout_12.addWidget(self.terrain_info)


        self.verticalLayout_3.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.terrain_json_line_edit = QLineEdit(self.page_2)
        self.terrain_json_line_edit.setObjectName(u"terrain_json_line_edit")
        self.terrain_json_line_edit.setEnabled(True)
        self.terrain_json_line_edit.setDragEnabled(False)

        self.horizontalLayout_11.addWidget(self.terrain_json_line_edit)

        self.terrain_json_button = QPushButton(self.page_2)
        self.terrain_json_button.setObjectName(u"terrain_json_button")

        self.horizontalLayout_11.addWidget(self.terrain_json_button)


        self.verticalLayout_3.addLayout(self.horizontalLayout_11)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_6)


        self.horizontalLayout_9.addLayout(self.verticalLayout_3)

        self.generate_button_exp = QPushButton(self.page_2)
        self.generate_button_exp.setObjectName(u"generate_button_exp")

        self.horizontalLayout_9.addWidget(self.generate_button_exp)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer)


        self.horizontalLayout_13.addLayout(self.horizontalLayout_9)

        self.generator_stack.addWidget(self.page_2)

        self.horizontalLayout_3.addWidget(self.generator_stack)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 1290, 23))
        self.menu_File = QMenu(self.menuBar)
        self.menu_File.setObjectName(u"menu_File")
        self.menu_Expert_Mode = QMenu(self.menuBar)
        self.menu_Expert_Mode.setObjectName(u"menu_Expert_Mode")
        MainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menu_File.menuAction())
        self.menuBar.addAction(self.menu_Expert_Mode.menuAction())
        self.menu_File.addAction(self.actionHelp)
        self.menu_Expert_Mode.addAction(self.actionDefault_Mode)
        self.menu_Expert_Mode.addAction(self.actionExpert_Mode)

        self.retranslateUi(MainWindow)

        self.generator_stack.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionDefault_Mode.setText(QCoreApplication.translate("MainWindow", u"Default mode", None))
        self.actionExpert_Mode.setText(QCoreApplication.translate("MainWindow", u"Expert mode", None))
        self.actionHelp.setText(QCoreApplication.translate("MainWindow", u"How to use", None))
        self.generate_image_label_def.setText(
            QCoreApplication.translate("MainWindow", u"Click button to generate image", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Shape", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Seed", None))
        self.generate_button_def.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Image will be saved to outputs folder", None))
        self.generate_image_label_exp.setText(
            QCoreApplication.translate("MainWindow", u"Click button to generate image", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Scale", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Octaves", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Persistence", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Lacunarity", None))
        self.get_default_vals_button_exp.setText(QCoreApplication.translate("MainWindow", u"Default values", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Shape", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Seed", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Terrain config file", None))
        self.terrain_info.setText(QCoreApplication.translate("MainWindow", u"Info", None))
        self.terrain_json_line_edit.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"Path to json file", None))
        self.terrain_json_button.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.generate_button_exp.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.menu_File.setTitle(QCoreApplication.translate("MainWindow", u"&Help", None))
        self.menu_Expert_Mode.setTitle(QCoreApplication.translate("MainWindow", u"&Mode", None))
    # retranslateUi

