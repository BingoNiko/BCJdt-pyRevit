"""
Copyright (c) 2014-2017 Ehsan Iran-Nejad
Python scripts for Autodesk Revit

This file is part of pyRevit repository at https://github.com/eirannejad/pyRevit

pyRevit is a free set of scripts for Autodesk Revit: you can redistribute it and/or modify
it under the terms of the GNU General Public License version 3, as published by
the Free Software Foundation.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

See this link for a copy of the GNU General Public License protecting this package.
https://github.com/eirannejad/pyRevit/blob/master/LICENSE
"""

from pyrevit import revit, DB, UI
from pyrevit import forms


__doc__ = 'Run this tool in a sheet view and click on viewports one '\
          'by one and this tool will change the detail number sequencially.'


curview = revit.activeview

if not isinstance(curview, DB.ViewSheet):
    forms.alert('You must be on a sheet to use this tool.')

viewports = []
for vpId in curview.GetAllViewports():
    viewports.append(revit.doc.GetElement(vpId))

vports = {(vp.LookupParameter('Detail Number').AsString()): vp
          for vp in viewports if vp.LookupParameter('Detail Number')}

maxNum = max(vports.keys())

with revit.Transaction('Re-number Viewports'):
    sel = []
    while len(sel) < len(vports):
        try:
            el = revit.doc.GetElement(
                revit.uidoc.Selection.PickObject(
                    UI.Selection.ObjectType.Element
                    )
                )

            if isinstance(el, DB.Viewport):
                sel.append(revit.doc.GetElement(el.ViewId))
        except Exception:
            break

    for i in range(1, len(sel) + 1):
        try:
            vports[i].LookupParameter('Detail Number').Set(str(maxNum + i))
        except KeyError:
            continue

    for i, el in enumerate(sel):
        el.LookupParameter('Detail Number').Set(str(i + 1))
