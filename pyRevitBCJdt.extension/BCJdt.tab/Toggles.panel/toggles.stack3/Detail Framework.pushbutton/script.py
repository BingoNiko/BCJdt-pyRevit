# BCJdt - Bohlin Cywinski Jackson designtech
# Copyright(c) 2017
# Author: Jon Szczesniak - @jonszcz
"""
Toggles visibility of Detail Sheet Framework Annotation Symbol in Current View
"""

from pyrevit import revit
from Autodesk.Revit.DB import Transaction, View, BuiltInCategory

doc = revit.doc
uidoc = revit.uidoc

# activate the show hidden so we can collect all elements (visible and hidden)
activeview = uidoc.ActiveView
# FIXME: Would like the option of using the current sheet or all the sheets

GA = doc.Settings.Categories.get_Item(BuiltInCategory.OST_GenericAnnotation)
subcat = GA.SubCategories

# Preset id to compare to after going through the subcategories.
id = 0

for sub in subcat:
    if sub.Name == "Detail Sheet Framework":
        id = sub.Id

# TODO: How do you add an output to break and warn if the framework isn't loaded? Currently handled with comparing the id to a preset value.

with Transaction(doc, 'Toggle Detail Framework') as t:
    t.Start()

    if id == 0:
        print("Detail Framework isn't loaded into the project.")
        # TODO: Give a better output window rather than a print dialog.
    elif View.GetCategoryHidden(activeview, id):
        View.SetCategoryHidden(activeview, id, False)
    else:
        View.SetCategoryHidden(activeview, id, True)

    t.Commit()
