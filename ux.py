#!/usr/bin/env python
import wx

class MainWindow(wx.Frame):
  def __init__(self, parent, title):
    # main window
    wx.Frame.__init__(self, parent, title = title, size = (800, 600))

    # label
    self.pathLabel = wx.StaticText(self, label = 'File or folder (complete path): ', pos = (20, 30))
    self.stringLabel = wx.StaticText(self, label = 'Append to end of file: ', pos = (20, 60))
    # path control (input)
    self.pathTxt = wx.TextCtrl(self, pos = (300, 30))
    self.stringTxt = wx.TextCtrl(self, pos = (300, 60))

    # button
    self.applyBtn = wx.Button(self, label = 'Create thumbs', pos = (500, 90))
    self.Bind(wx.EVT_BUTTON, self.OnClick, self.applyBtn)

    # render the frame
    self.Show()

  def OnClick(self, event):
    self.pathTxt.SetValue('button clicked')

# run the app
app = wx.App(False)
frame = MainWindow(None, "GUI for thumb creation")
app.MainLoop()
