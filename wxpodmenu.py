#!/usr/bin/python
# coding: utf-8
""" wxpod menu """

import wx

class WxPodMenu(wx.MenuBar):
    """ Manage wxpod menu """

    def __init__(self):
        super(WxPodMenu, self).__init__()
        self.dirname=''
        self.filemenu = wx.Menu()
        self.menuOpen = self.filemenu.Append(
                wx.ID_OPEN, "&Open",
                " Open a file to edit")
        self.menuAbout= self.filemenu.Append(
                wx.ID_ABOUT, "&About",
                " Information about this program")
        self.menuExit = self.filemenu.Append(
            wx.ID_EXIT, "E&xit",
            " Terminate the program")

        # Creating the menubar.
        self.Append(self.filemenu, "&File")

        # Events.
        self.Bind(wx.EVT_MENU, self.OnOpen, self.menuOpen)
        self.Bind(wx.EVT_MENU, self.OnExit, self.menuExit)
        self.Bind(wx.EVT_MENU, self.OnAbout, self.menuAbout)

    def OnAbout(self,e):
        # Create a message dialog box
        dlg = wx.MessageDialog(self,
                               " A sample editor \n in wxPython",
                               "About Sample Editor", wx.OK)
        dlg.ShowModal() # Shows it
        dlg.Destroy() # finally destroy it when finished.

    def OnExit(self,e):
        self.Close(True)  # Close the frame.

    def OnOpen(self,e):
        """ Open a file"""
        dlg = wx.FileDialog(self,
                            "Choose a file",
                            self.dirname,
                            "", "*.*", wx.OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            f = open(os.path.join(self.dirname, self.filename), 'r')
            self.control.SetValue(f.read())
            f.close()
        dlg.Destroy()
