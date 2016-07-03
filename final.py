import sys,private_window
from PyQt4 import QtCore, QtGui, QtWebKit

class Browser(QtGui.QMainWindow):

    def __init__(self):

        QtGui.QMainWindow.__init__(self)
        self.resize(1000,800)
        self.tabs=QtGui.QTabWidget()
        self.centralwidget = QtGui.QWidget()
        #self.tabs.setDocumentMode(True)
        self.mainLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.mainLayout.setSpacing(0)
        self.mainLayout.setMargin(0)
        self.filename = ""
        self.frame = QtGui.QFrame(self.centralwidget)
        self.gridLayout = QtGui.QVBoxLayout(self.frame)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self.setWindowTitle("WebBrowser")
        self.setWindowIcon(QtGui.QIcon('images2.jpg'))
#creating buttons in toolbar
        navb= QtGui.QToolBar("navigation")
        self.addToolBar(navb)

        self.horizontalLayout = QtGui.QHBoxLayout()
        self.tb_url = QtGui.QLineEdit(self.frame)
        self.bt_back = QtGui.QPushButton()
        self.bt_back.setIcon(QtGui.QIcon(QtGui.QPixmap('arrow-180.png')))
        self.bt_ahead = QtGui.QPushButton()
        self.bt_ahead.setIcon(QtGui.QIcon(QtGui.QPixmap('arrow-000.png')))
        self.bt_reload = QtGui.QPushButton()
        self.bt_reload.setIcon(QtGui.QIcon(QtGui.QPixmap('arrow-circle-315.png')))
        self.bt_go = QtGui.QPushButton()
        self.bt_go.setIcon(QtGui.QIcon(QtGui.QPixmap('images.jpg')))
        self.home=QtGui.QPushButton()
        self.home.setIcon(QtGui.QIcon(QtGui.QPixmap('home.png')))
        self.book=QtGui.QPushButton()
        self.book.setIcon(QtGui.QIcon(QtGui.QPixmap('folder_bookmarks.png')))
        self.stop=QtGui.QPushButton()
        self.stop.setIcon(QtGui.QIcon(QtGui.QPixmap('images.png')))

#connecting buttons
        navb.addWidget(self.bt_back)
        navb.addWidget(self.bt_ahead)
        navb.addWidget(self.bt_reload)
        navb.addWidget(self.home)
        navb.addWidget(self.tb_url)
        navb.addWidget(self.stop)
        navb.addWidget(self.bt_go)
        navb.addWidget(self.book)
        self.mainLayout.addWidget(self.frame)
        self.gridLayout.addLayout(self.horizontalLayout)
        self.setCentralWidget(self.tabs)    #important to make the contents central on the window
#definations of buttons
        self.connect(self.tb_url, QtCore.SIGNAL("returnPressed()"), self.browse)
        self.connect(self.bt_back, QtCore.SIGNAL("clicked()"),self.back)
        self.connect(self.bt_ahead, QtCore.SIGNAL("clicked()"), self.forward)
        self.connect(self.bt_reload, QtCore.SIGNAL(" clicked()"),self.reload)
        self.connect(self.bt_go, QtCore.SIGNAL("clicked()"), self.browse)
        self.connect(self.stop, QtCore.SIGNAL("clicked()"),lambda:self.tabs.currentWidget().stop())
        self.connect(self.home, QtCore.SIGNAL("clicked()"), self.home1)
        self.connect(self.book,QtCore.SIGNAL("clicked()"),self.Bookmark)

#default page on startup
        self.default_url = "http://www.google.com"
        self.tb_url.setText(self.default_url)
        self.add_new_tab("http://www.google.com","homepage")

#menubar
        self.menuBar().setNativeMenuBar(False)
        file_menu = self.menuBar().addMenu("&File")

        new_tab=QtGui.QAction(QtGui.QIcon("ui-tab--plus.png"), 'New Tab', self)
        new_tab.triggered.connect(lambda:self.add_new_tab(QtCore.QUrl(''),"new tab"))
        file_menu.addAction(new_tab)
        new_tab.setShortcut('Ctrl+T')

        new_window=QtGui.QAction(QtGui.QIcon("new-window.jpg"), 'New Window', self)
        new_window.triggered.connect(self.newwindow)
        file_menu.addAction(new_window)
        new_window.setShortcut('Ctrl+W')

        private_win=QtGui.QAction(QtGui.QIcon("Unknown.png"), 'Private Window', self)
        private_win.triggered.connect(private_window.Browser)
        file_menu.addAction(private_win)
        private_win.setShortcut('Ctrl+K')

        open_file=QtGui.QAction(QtGui.QIcon("disk--arrow.png"), 'Open File', self)
        open_file.triggered.connect(self.openfile)
        file_menu.addAction(open_file)
        open_file.setShortcut('Ctrl+O')

        save_file=QtGui.QAction(QtGui.QIcon("disk--pencil.png"), 'Save Webpage', self)
        save_file.triggered.connect(self.savefile)
        file_menu.addAction(save_file)
        save_file.setShortcut('Ctrl+S')

        history=QtGui.QAction(QtGui.QIcon("history-128.png"), 'History', self)
        history.triggered.connect(self.history)

        file_menu.addAction(history)
        history.setShortcut('Ctrl+U')

        printt=QtGui.QAction(QtGui.QIcon("print.jpg"), 'Print', self)
        printt.triggered.connect(self.printt)
        file_menu.addAction(printt)
        printt.setShortcut('Ctrl+P')

        print_prev=QtGui.QAction(QtGui.QIcon("preview.jpg"), 'Print preview', self)
        print_prev.triggered.connect(self.preview)
        file_menu.addAction(print_prev)
        print_prev.setShortcut('Ctrl+Shift+P')

        bookmark=QtGui.QAction(QtGui.QIcon("book.jpg"), 'Bookmarks', self)
        bookmark.triggered.connect(self.bm)
        file_menu.addAction(bookmark)
        bookmark.setShortcut('Ctrl+D')

        quit=QtGui.QAction(QtGui.QIcon("cross-circle.png"), 'Quit', self)
        quit.setShortcut('Ctrl+Q')
        quit.triggered.connect(self.quit)
        file_menu.addAction(quit)

        about=QtGui.QAction(QtGui.QIcon("question.png"),"About the web browser",self)
        about.triggered.connect(self.about)
        file_menu.addAction(about)
        self.tabs.currentChanged.connect(self.current_tab_changed)
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.closetab)
        self.show()

#functions
#quit the browser
    def quit(self):
        Q=QtGui.QDialog()
        layout=QtGui.QVBoxLayout()
        Q.setWindowTitle("EXIT")
        h=QtGui.QLabel("Do you want to Quit?")
        btn=QtGui.QPushButton("QUIT")
        layout.addWidget(h)
        layout.addWidget(btn)
        Q.connect(btn, QtCore.SIGNAL("clicked()"), QtGui.qApp.quit )
        Q.setLayout(layout)
        Q.exec_()


#go back a webpage
    def back(self):
        self.tabs.currentWidget().back()
        self.html.loadFinished.connect(self.current_tab_changed)
        qurl=self.tabs.currentWidget().url()
        #self.tb_url.setText(qurl.toString())
        f=open("history.txt","a")
        f.write(self.tb_url.text())
        f.write("\n")
        f.close()
#forward webpage
    def forward(self):
        self.tabs.currentWidget().forward()
        self.html.loadFinished.connect(self.current_tab_changed)
        qurl=self.tabs.currentWidget().url()
        #self.tb_url.setText(qurl.toString())
        f=open("history.txt","a")
        f.write(self.tb_url.text())
        f.write("\n")
        f.close()
#reload the current webpage
    def reload(self):
        self.tabs.currentWidget().reload()
        self.html.loadFinished.connect(self.current_tab_changed)
        qurl=self.tabs.currentWidget().url()
        #self.tb_url.setText(qurl.toString())
        f=open("history.txt","a")
        f.write(self.tb_url.text())
        f.write("\n")
        f.close()
#print the current page
    def printt(self):
       dialog = QtGui.QPrintDialog()
       if dialog.exec_() == QtGui.QDialog.Accepted:
          self.text.document().print_(dialog.printer())
#have a print preview of the page
    def preview(self):
       preview = QtGui.QPrintPreviewDialog()
       preview.paintRequested.connect(lambda p: self.tabs.currentWidget().print_(p))
       preview.exec_()

#add new bookmarks
    def Bookmark(self):

        b = open("bookmarks.txt","a")
        b.write(self.tb_url.text())
        b.write("\n")
        b.close()
#open a .html page in browser
    def openfile(self):
        self.filename =QtGui.QFileDialog.getOpenFileName(self,"open file",".","(*.html)")
        if self.filename:
            with open(self.filename,'r') as f:
                html= f.read()
        self.html.load(QtCore.QUrl(self.filename))
        self.tb_url.setText(self.filename)
#save a .html page
    def savefile(self):
        if not self.filename :
         self.filename=QtGui.QFileDialog.getSaveFileName(self,"Save file as",".","(*.html)")
         with open(self.filename,"w") as file:
            file.write(self.html.page().mainFrame().toHtml())
#open the bookmarks file
    def bm(self):
        Q=QtGui.QDialog()
        layout=QtGui.QVBoxLayout()
        Q.setWindowTitle("Bookmarks")
        with open("bookmarks.txt","r") as f:
          for line in f:
            s="<a href=\'"+line+"\'>"+line+"</a>"
            h=QtGui.QLabel()
            h.setText(s)
            h.setOpenExternalLinks(True)
            layout.addWidget(h)
            Q.setLayout(layout)
        Q.exec_()

#opening a new url
    def browse(self):
        url = self.tb_url.text() if self.tb_url.text() else self.default_url
        if "http://"  not in url:
           url1 = "http://" + url
           self.html.load(QtCore.QUrl(url1))
        else:
            self.html.load(QtCore.QUrl(url))
        self.html.show()
        self.html.loadFinished.connect(self.current_tab_changed)
        qurl=self.tabs.currentWidget().url()
        #self.tb_url.setText(qurl.toString())
        f=open("history.txt","a")
        f.write(self.tb_url.text())
        f.write("\n")


#new tab
    def add_new_tab(self, q , label ):
        self.html=QtWebKit.QWebView()
        QtWebKit.QWebSettings.globalSettings().setAttribute(QtWebKit.QWebSettings.JavascriptEnabled,True)
        QtWebKit.QWebSettings.globalSettings().setAttribute(QtWebKit.QWebSettings.PluginsEnabled,True)
        i=self.tabs.addTab(self.html,label)
        self.html.load(QtCore.QUrl(q))
       # self.current_tab_changed(i)
        self.html.show()
        self.html.urlChanged.connect(lambda q ,html = self.html: self.update_url(q, html))
        self.html.loadFinished.connect(lambda _,i=i , html = self.html : self.tabs.setTabText(i,html.page().mainFrame().title()))

#check if current tab has correct url
    def current_tab_changed(self):
        qurl=self.tabs.currentWidget().url()
        self.tb_url.setText(qurl.toString())
#go to the homepage
    def home1(self):
        self.default_url = "http://www.google.com"
        self.tb_url.setText(self.default_url)
        self.html.load(QtCore.QUrl(self.default_url))
        f=open("history.txt","a")
        f.write(self.tb_url.text())
        f.write("\n")
        self.html.show()
#check the history of the browser
    def history(self):
        Q=QtGui.QDialog()
        layout=QtGui.QVBoxLayout()
        Q.setWindowTitle("History Of Browser")
        with open("history.txt","r") as f:
          for line in f:
            s="<a href=\'"+line+"\'>"+line+"</a>"
            h=QtGui.QLabel()
            h.setText(s)
            h.setOpenExternalLinks(True)
            layout.addWidget(h)
            Q.setLayout(layout)

        Q.exec_()

#open a new window
    def newwindow(self):
        new=Browser()
        new.show()

#about the browser
    def about(self):
        d = QtGui.QDialog()
        layout=QtGui.QVBoxLayout()
        title=QtGui.QLabel("Web Browser")
        font = title.font()
        font.setPointSize(20)
        title.setFont(font)
        d.setWindowTitle("Web Browser")
        logo=QtGui.QLabel()
        logo.setPixmap(QtGui.QPixmap('images2.jpg'))
        layout.addWidget(logo)
        layout.addWidget(title)
        layout.addWidget(QtGui.QLabel("Copyright 2016 Anisha Jauhari"))
        d.setLayout(layout)
        d.exec_()
#check if current tab has the correct url
    def update_url(self, q, browser= None):
        if browser != self.tabs.currentWidget():
            return
#close tabs
    def closetab(self ,i):
        if self.tabs.count() < 2:
            return
        self.tabs.removeTab(i)




