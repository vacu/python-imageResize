#!/usr/bin/env python
import wx

import sys, os, Image, string
import helpers

class MainWindow(wx.Frame):
  def __init__(self, parent, title):
    # main window
    wx.Frame.__init__(self, parent, title = title, size = (800, 600));
    self.selectedPath = [];
    self.InitUI();
    # render the frame
    self.Center();
    self.Show();

  def InitUI(self):
    # type folder / image
    self.fileRadio = wx.RadioButton(self, label = 'Single file', pos = (20, 0));
    self.fileRadio.SetValue(True);
    self.Bind(wx.EVT_RADIOBUTTON, self.changeDialogTypeFile, self.fileRadio);

    self.folderRadio = wx.RadioButton(self, label = 'Folder', pos = (120, 0));
    self.Bind(wx.EVT_RADIOBUTTON, self.changeDialogTypeDir, self.folderRadio);

    # directory dialog
    self.openDirBrowser = wx.Button(self, label = 'Search for file or folder', pos = (20, 30));
    # open file dialog by default
    self.Bind(wx.EVT_BUTTON, self.OpenFileDialog, self.openDirBrowser);

    # path control (input)
    self.stringLabel = wx.StaticText(self, label = 'Append to end of file: ', pos = (20, 60));
    self.stringTxt = wx.TextCtrl(self, pos = (300, 60));

    # size of thumb
    self.sizeLabel = wx.StaticText(self, label = 'Size of thumb: ', pos = (20, 90));
    self.sizeTxt = wx.TextCtrl(self, pos = (300, 90));

    # button
    self.applyBtn = wx.Button(self, label = 'Create thumbs', pos = (500, 120));
    self.Bind(wx.EVT_BUTTON, self.OnClick, self.applyBtn);

    # status text
    self.console = wx.TextCtrl(self, style = wx.TE_MULTILINE | wx.TE_READONLY, size = (600, 300), pos = (20, 150));

  def changeDialogTypeFile(self, event):
    self.Bind(wx.EVT_BUTTON, self.OpenFileDialog, self.openDirBrowser);

  def changeDialogTypeDir(self, event):
    self.Bind(wx.EVT_BUTTON, self.OpenDirDialog, self.openDirBrowser);

  def OpenDirDialog(self, event):
    self.selectedPath = [];

    dirDialog = wx.DirDialog(
      self,
      message = 'Choose a directory: ',
      defaultPath = os.getcwd(),
      style = wx.DD_DEFAULT_STYLE,
      pos = (60, 220)
    );

    if dirDialog.ShowModal() == wx.ID_OK:
      self.selectedPath.append(dirDialog.GetPath());

    dirDialog.Destroy();
    return self.selectedPath;

  def OpenFileDialog(self, event):
    self.selectedPath = [];

    fileDialog = wx.FileDialog(
      self,
      message = 'Choose a file: ',
      defaultDir = os.getcwd(),
      style = wx.OPEN | wx.MULTIPLE | wx.CHANGE_DIR
    );

    if fileDialog.ShowModal() == wx.ID_OK:
      paths = fileDialog.GetPaths();

      for path in paths:
        self.selectedPath.append(path);

    fileDialog.Destroy();
    return self.selectedPath;

  def OnClick(self, event):
    imgHelper = helpers.ImageHelper();

    if self.selectedPath:
      # if more than one than they are files
      # act accordingly
      if len(self.selectedPath) > 1:
        print len(self.selectedPath);
      # if less than 2 than it can be file or folder
      elif len(self.selectedPath) < 2:
        pathParts = string.split(self.selectedPath[0], '/');
        lastPathPart = pathParts[len(pathParts) - 1];
        checkType = string.split(lastPathPart, '.');

        # if it's a file
        if len(checkType) > 1:
          imageFile = Image.open(self.selectedPath[0]);
          imageX = imageFile.size[0] / 2;
          imageY = imageFile.size[1] / 2;

          imgHelper.createThumb(imageFile, self.sizeTxt.GetValue());
          imgHelper.saveFile(imageFile, self.selectedPath[0], self.stringTxt.GetValue());
        # if it's a folder
        else:
          for root, dirs, files in os.walk(self.selectedPath[0]):
            for file in files:
              if file.endswith('.jpg') or file.endswith('.png'):
                imageFile = Image.open(self.selectedPath[0] + '/' + file);
                imgHelper.createThumb(imageFile, self.sizeTxt.GetValue());
                imgHelper.saveFile(imageFile, self.selectedPath[0], self.stringTxt.GetValue(), file);
    # array is empty
    else:
      print 'Please select a file or folder.';

    # write the status of the current operation
    # self.pathTxt.SetValue('button clicked')

# run the app
def main():
  app = wx.App(False);
  frame = MainWindow(None, "GUI for thumb creation");
  app.MainLoop();

if __name__ == '__main__':
  main();
