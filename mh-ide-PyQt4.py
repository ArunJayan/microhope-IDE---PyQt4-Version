#microhope ide 
# Latest version using PyQt4
#icons from :/usr/share/icons/gnome/24x24/actions
from PyQt4 import QtGui
from PyQt4 import QtCore
import sys

class Microhope_Main(QtGui.QMainWindow):
	def __init__(self , app , parent = None):
		QtGui.QMainWindow.__init__(self,parent)
		
		self.app = app 
		self.filename = ""
		self.changesSaved = True
		self.setFixedSize(1250,710) #here we fix the size to 1250x710 
									#and prevent the resizing the window , and disable the maximising and minimising . 
	def initToolbar(self):
		# New Action
		self.new_file = QtGui.QAction(QtGui.QIcon("icons/document-new.png"),"New",self) #for creating new files  . 
		self.new_file.setShortcut("Ctrl+N")
		self.new_file.setStatusTip("Create a new document.")
		self.new_file.triggered.connect(self.new)
		##             ##           ## 
		#Open Action
		self.open_file = QtGui.QAction(QtGui.QIcon("icons/document-open.png"),"Open file",self)
		self.open_file.setStatusTip("Open existing document")
		self.open_file.setShortcut("Ctrl+O")
		self.open_file.self.openAction.triggered.connect(self.open)
		##             ##           ##
		# Save Action
		self.save_file = self.saveAction = QtGui.QAction(QtGui.QIcon("icons/save.png"),"Save",self)
		self.save_file.setStatusTip("Save document")
		self.save_file.setShortcut("Ctrl+S")
		self.save_file.triggered.connect(self.save)
		##             ##           ##
		#
	# function for new document .
	def new(self):
		new = Microhope_Main(self.app)
		new.show()
	def open(self):
		self.filename = QtGui.QFileDialog.getOpenFileName(self, 'Open File',".","")
		if self.filename:
			with open(self.filename,"rt",encoding="utf-8") as file:
				self.text.setText(file.read())
	def save(self):
		if not self.filename:
			self.filename = QtGui.QFileDialog.getSaveFileName(self, 'Save File')
		if self.filename:
			if os.path.splitText(self.filename)[1]=='':
				self.filename += ".c"
		with open(self.filename,"wt", encoding="utf-8") as file:
			file.write(self.text.toHtml())
		
		self.changesSaved = True
			
	
	
	

if __name__ == "__main__":
	
	app = QtGui.QApplication(sys.argv)
	mh = Microhope_Main(app)
	mh.show()
	sys.exit(app.exec_())
