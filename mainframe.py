#!/usr/bin/python
# coding: utf-8
""" The main frame """

import wx
import os
import podcork
from wxpodlibrary import WxPodLibrary
from wxpodmenu import WxPodMenu

class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(200,-1))
        self.CreateStatusBar()  

        # Setting up the menu.
        self.SetMenuBar(WxPodMenu())  # Adding the MenuBar to the Frame content.
        self.control = WxPodLibrary(self) 

        self.sizer2 = wx.BoxSizer(wx.HORIZONTAL)
        self.buttons = []
        for i in range(0, 6):
            self.buttons.append(wx.Button(self, -1, "Button &"+str(i)))
            self.sizer2.Add(self.buttons[i], 1, wx.EXPAND)

        # Use some sizers to see layout options
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.control, 1, wx.EXPAND)
        self.sizer.Add(self.sizer2, 0, wx.EXPAND)

        #Layout sizers
        self.SetSizer(self.sizer)
        self.SetAutoLayout(1)
        self.sizer.Fit(self)
        self.Show()
