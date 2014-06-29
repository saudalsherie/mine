import sys
import random

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from radio_button import * #provides the radio button widget
from manual_grow_dialog_class import * #provides the manual grow dialog window

from wheat_class import *
from potato_class import *

class CropWindow(QMainWindow):
    """this class creates a main window to observe the growth of a simulation"""

    #constructor
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Crop Simulation")#set window title
        self.create_select_crop_layout()
               
        #create stacked layout/widget
        self.stacked_layout = QStackedLayout()
        self.stacked_layout.addWidget(self.select_crop_widget)

        #assign stacked layout to stacked widget
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.stacked_layout)

        #create the central widget to hold the layouts 
        self.setCentralWidget(self.central_widget)


    def create_select_crop_layout(self):
        #this is the initial layout of the window - to select the crop type
        self.crop_radio_buttons = RadioButtonWidget("Crop Simulation", "Please select a crop",("Wheat","Potato"))
        self.instantiate_button = QPushButton("Create a crop")

        #create layouit to hold the widgets
        self.initial_layout = QVBoxLayout()
        self.initial_layout.addWidget(self.crop_radio_buttons)
        self.initial_layout.addWidget(self.instantiate_button)

        self.select_crop_widget = QWidget()
        self.select_crop_widget.setLayout(self.initial_layout)

        #add connection
        self.instantiate_button.clicked.connect(self.instantiate_crop)
        

    def create_view_crop_layout(self,crop_type):
        #this is the second layer of the window - view the crop growth

        self.growth_label = QLabel("Growth")
        self.days_label = QLabel("Days Growing")
        self.status_label = QLabel("Crop Status")

        self.growth_line_edit = QLineEdit()
        self.days_line_edit = QLineEdit()
        self.status_line_edit = QLineEdit()

        self.manual_grow_button = QPushButton("Manually Grow")
        self.auto_grow_button = QPushButton("Automatically Grow")

        self.grow_grid = QGridLayout()
        self.status_grid = QGridLayout()

        #add label widget to status layout
        self.status_grid.addWidget(self.growth_label,0,0)
        self.status_grid.addWidget(self.days_label,1,0)
        self.status_grid.addWidget(self.status_label,2,0)

        #add line edit widgets to status layout
        self.status_grid.addWidget(self.growth_line_edit,0,1)
        self.status_grid.addWidget(self.days_line_edit,1,1)
        self.status_grid.addWidget(self.status_line_edit,2,1)

        self.status_widget = QWidget()
        self.status_widget.setLayout(self.status_grid)

        #add widgets/layouts to the grow layout
        self.grow_grid.addWidget(self.status_widget,0,1)
        self.grow_grid.addWidget(self.manual_grow_button,1,0)
        self.grow_grid.addWidget(self.auto_grow_button,1,1)

        #create a widget to hold layout
        self.view_crop_widget = QWidget()
        self.view_crop_widget.setLayout(self.grow_grid)

        #connection
        self.auto_grow_button.clicked.connect(self.auto_grow_crop)
        self.manual_grow_button.clicked.connect(self.manual_grow_crop)


    def instantiate_crop(self):
        crop_type = self.crop_radio_buttons.selected_button() #get the radio button that was selected
        if crop_type == 1:
            self.simulated_crop = Wheat()
            
        elif crop_type == 2:
            self.simulated_crop = Potato()
            
        self.create_view_crop_layout(crop_type) #create a view crop growth layout
        self.stacked_layout.addWidget(self.view_crop_widget)#add this layout to the stacked layout
        self.stacked_layout.setCurrentIndex(1)#change the visible layout in the stacked layout
        
        
    def auto_grow_crop(self):
        for days in range(30):
            light = random.randint(1,10)
            water = random.randint(1,10)
            self.simulated_crop.grow(light,water)
        self.update_crop_view_status()

    def manual_grow_crop(self):
        manual_values_dialog = ManualGrowDialog()
        manual_values_dialog.exec_() #run the dialog window
        light, water = manual_values_dialog.values()
        self.simulated_crop.grow(light,water)
        self.update_crop_view_status()
        
    def update_crop_view_status(self):
        crop_status_report = self.simulated_crop.report()#get crop report

        #update the text fields
        self.growth_line_edit.setText(str(crop_status_report["growth"]))#update growth field
        self.days_line_edit.setText(str(crop_status_report["days growing"]))#update days growing field
        self.status_line_edit.setText(str(crop_status_report["status"]))#update status field
    

def main():
    crop_simulation = QApplication(sys.argv)
    crop_window = CropWindow()
    crop_window.show()
    crop_window.raise_()
    crop_simulation.exec_()

if __name__ == "__main__":
    main()
