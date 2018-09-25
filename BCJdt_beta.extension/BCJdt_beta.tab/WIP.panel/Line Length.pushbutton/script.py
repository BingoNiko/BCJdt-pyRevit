"""Counts all lines in the model with matching style to the selected line.

CTRL-Click: Lists every matching line
"""

from pyrevit import script
from pyrevit import revit, DB


__context__ = 'selection'


logger = script.get_logger()
selection = revit.get_selection()


cl = DB.FilteredElementCollector(revit.doc)
cllines = cl.OfCategory(DB.BuiltInCategory.OST_Lines
                        or DB.BuiltInCategory.OST_SketchLines)\
            .WhereElementIsNotElementType()

for c in cllines:
    line = c.LookupParameter('Length').AsString()
    if line != 'None':
        print(line)
