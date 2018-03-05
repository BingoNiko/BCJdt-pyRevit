'''
Copyright(c) 2017, Jon Szczesniak - @jonszcz
BCJdt - Bohlin Cywinski Jackson designtech
'''

__doc__ = 'Reload the keynote file'

from Autodesk.Revit.DB import Transaction, KeynoteTable
from pyrevit import revit

doc = revit.doc

t = Transaction(doc, 'Reload Keynote File')
t.Start()
KeynoteTable.GetKeynoteTable(doc).Reload(None)
t.Commit()
