#!/usr/bin/env python
import wx

import sys, os, Image
import helpers

class MainWindow(wx.Frame):
  def __init__(self, parent, title):
    # main window
    wx.Frame.__init__(self, parent, title = title, size = (800, 600))

    # type folder / image
    self.fileRadio = wx.RadioButton(self, label = 'Single file', pos = (20, 0))
    self.folderRadio = wx.RadioButton(self, label = 'Folder', pos = (120, 0))

    # directory dialog
    self.openDirBrowser = wx.Button(self, label = 'Search for file or folder', pos = (20, 180))
    self.Bind(wx.EVT_BUTTON, self.OpenDirDialog, self.openDirBrowser)

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

  def OpenDirDialog(self, event):
    dirDialog = wx.DirDialog(self, message = 'Choose a directory or image: ', defaultPath = os.getcwd(),  style = wx.DD_DEFAULT_STYLE, pos = (60, 220))
    if dirDialog.ShowModal() == wx.ID_OK:
      print "You chose %s" % dirDialog.GetPath()
    dirDialog.Destroy()

  def OnClick(self, event):
    imgHelper = helpers.ImageHelper();
    # if len(sys.argv) > 1:
    #   # image file
    #   if sys.argv[1] != '-folder':
    #     imageFile = Image.open(sys.argv[2]);
    #     imageX = imageFile.size[0] / 2;
    #     imageY = imageFile.size[1] / 2;

    #   # SINGLE FILE
    #   if sys.argv[1] == '-image':
    #     imgHelper.createThumb(imageFile);
    #     imgHelper.saveFile(imageFile);
    #   # FOLDER
    #   elif sys.argv[1] == '-folder':
    #     for root, dirs, files in os.walk(sys.argv[2]):
    #       for file in files:
    #         if file.endswith('.jpg') or file.endswith('.png'):
    #           imageFile = Image.open(sys.argv[2] + file);
    #           imgHelper.createThumb(imageFile);
    #           imgHelper.saveFile(imageFile, file);
    #   # CROP
    #   elif sys.argv[1] == '-crop':
    #     size = sys.argv[3];
    #     box = (imageX - (int(size) / 2), imageY - (int(size) / 2), imageX + int(size), imageY + int(size));
    #     region = imageFile.crop(box);

    #     region.save(
    #       os.path.splitext(sys.argv[2])[0] + '.thumb' + os.path.splitext(sys.argv[2])[1],
    #       imageFile.format
    #     );

    # write the status of the current operation
    self.pathTxt.SetValue('button clicked')

# run the app
app = wx.App(False)
frame = MainWindow(None, "GUI for thumb creation")
app.MainLoop()
