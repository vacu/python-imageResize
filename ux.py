#!/usr/bin/env python
import wx

import sys, os, Image
import helpers

class MainWindow(wx.Frame):
  def __init__(self, parent, title):
    # main window
    wx.Frame.__init__(self, parent, title = title, size = (800, 600))
    self.selectedPath = None;
    self.InitUI()
    # render the frame
    self.Center()
    self.Show()

  def InitUI(self):
    # type folder / image
    self.fileRadio = wx.RadioButton(self, label = 'Single file', pos = (20, 0))
    self.fileRadio.SetValue(True)
    self.Bind(wx.EVT_RADIOBUTTON, self.changeDialogTypeFile, self.fileRadio)

    self.folderRadio = wx.RadioButton(self, label = 'Folder', pos = (120, 0))
    self.Bind(wx.EVT_RADIOBUTTON, self.changeDialogTypeDir, self.folderRadio)

    # directory dialog
    self.openDirBrowser = wx.Button(self, label = 'Search for file or folder', pos = (20, 30))

    # path control (input)
    self.stringLabel = wx.StaticText(self, label = 'Append to end of file: ', pos = (20, 60))
    self.stringTxt = wx.TextCtrl(self, pos = (300, 60))

    # button
    self.applyBtn = wx.Button(self, label = 'Create thumbs', pos = (500, 90))
    self.Bind(wx.EVT_BUTTON, self.OnClick, self.applyBtn)

    # status text
    self.console = wx.TextCtrl(self, style = wx.TE_MULTILINE | wx.TE_READONLY, size = (600, 300), pos = (20, 120))

  def changeDialogTypeFile(self, event):
    self.Bind(wx.EVT_BUTTON, self.OpenFileDialog, self.openDirBrowser)

  def changeDialogTypeDir(self, event):
    self.Bind(wx.EVT_BUTTON, self.OpenDirDialog, self.openDirBrowser)

  def OpenDirDialog(self, event):
    dirDialog = wx.DirDialog(
      self,
      message = 'Choose a directory: ',
      defaultPath = os.getcwd(),
      style = wx.DD_DEFAULT_STYLE,
      pos = (60, 220)
    )

    if dirDialog.ShowModal() == wx.ID_OK:
      self.selectedPath = dirDialog.GetPath()

    dirDialog.Destroy()
    return self.selectedPath;

  def OpenFileDialog(self, event):
    fileDialog = wx.FileDialog(
      self,
      message = 'Choose a file: ',
      defaultDir = os.getcwd(),
      style = wx.OPEN | wx.MULTIPLE | wx.CHANGE_DIR
    )

    if fileDialog.ShowModal() == wx.ID_OK:
      paths = fileDialog.GetPaths()
      for path in paths:
        print path
    fileDialog.Destroy()

  def OnClick(self, event):
    print self.selectedPath;
    # imgHelper = helpers.ImageHelper();
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
    # self.pathTxt.SetValue('button clicked')

# run the app
def main():
  app = wx.App(False)
  frame = MainWindow(None, "GUI for thumb creation")
  app.MainLoop()

if __name__ == '__main__':
  main()
