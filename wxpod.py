#!/usr/bin/python
# coding: utf-8
""" A gui for POD """

from mainframe import MainWindow
import wx

app = wx.App(False)
frame = MainWindow(None, "wxPOD")
app.MainLoop()
