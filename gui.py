from worker import start_routine, change_product
from visualizer import visualize
import wx

def start_gui():
    app = wx.App()
    frame = wx.Frame(None, title="Amazon Price Tracker")
    frame.SetSize(0, 0, 600, 400)

    panel = wx.Panel(frame, wx.ID_ANY)
    start_button = wx.Button(panel, wx.ID_ANY, "Start scraping", (10, 10))
    start_button.Bind(wx.EVT_BUTTON, onButton)
    
    vis_button = wx.Button(panel, wx.ID_ANY, "Visualize the Data", (10, 40))
    
    change_button = wx.Button(panel, wx.ID_ANY, "Change the Product", (10, 70))
    
    exit_button = wx.Button(panel, wx.ID_ANY, "Exit", pos=(10, 100), size=(60, 40))
    exit_button.Bind(wx.CLOSE, exitBtn)

    frame.Show()
    frame.Centre()
    app.MainLoop()

def onButton(self):
    print("Button pressed")

def exitBtn(self, event):
    self.Destroy()

'''
def makeMenuBar(frm):
    fileMenu = wx.Menu()
    helloItem = fileMenu.Append(-1, "&Hello...\tCtrl-H",
                "Help string shown in status bar for this menu item")
    fileMenu.AppendSeparator()
    exitItem = fileMenu.Append(wx.ID_EXIT)
    helpMenu = wx.Menu()
    aboutItem = helpMenu.Append(wx.ID_ABOUT)

    menuBar = wx.MenuBar()
    menuBar.Append(fileMenu, "&File")
    menuBar.Append(helpMenu, "&Help")

    frm.SetMenuBar(menuBar)
'''

start_gui()