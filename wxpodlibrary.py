#!/usr/bin/python
# coding: utf-8
""" The Library tree """

import wx
import keyword
import string

class WxPodLibrary(wx.TreeCtrl):
    """ manage library tree """

    def __init__(self, parent):
        super(WxPodLibrary, self).__init__(parent, -1,
                             style=wx.TR_DEFAULT_STYLE |
                             wx.TR_FULL_ROW_HIGHLIGHT |
                             wx.TR_EDIT_LABELS)
        root = self.AddRoot("Library")
        # Add the tree root
        letters = []
        for kwd in keyword.kwlist:
            first = kwd[0]
            if first not in letters:
                letters.append(first)

        for letter in letters:
            item = self.AppendItem(root, letter)
            for kwd in keyword.kwlist:
                first = kwd[0]
                if first == letter:
                    sub_item = self.AppendItem(item, kwd)
                    
        self.ExpandAll()
 
