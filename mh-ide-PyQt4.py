#microhope ide 
# Latest version using PyQt4
#icons from :/usr/share/icons/gnome/24x24/actions
from PyQt4 import QtGui
from PyQt4 import QtCore
import sys

class Microhope_Main(QtGui.QMainWindow):
	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		
		self.setFixedSize(1250,710) #here we fix the size to 1250x710 
									#and prevent the resizing the window , and disable the maximising and minimising . 
	def initToolbar(self):
		self.new = QtGui.QAction(QtGui.QIcon("icons/new.png"),"New",self) #for creating new files  . 
		self.new.setShortcut("Ctrl+N")
		self.new.setStatusTip("Create a new document.")

if __name__ == "__main__":
	
	app = QtGui.QApplication(sys.argv)
	mh = Microhope_Main()
	mh.show()
	sys.exit(app.exec_())
