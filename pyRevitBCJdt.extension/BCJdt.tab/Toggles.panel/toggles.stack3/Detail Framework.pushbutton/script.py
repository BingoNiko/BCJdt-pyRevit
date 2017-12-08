# BCJdt - Bohlin Cywinski Jackson designtech
# Copyright(c) 2017
# Author: Jon Szczesniak - @jonszcz
"""
Toggles visibility of Detail Sheet Framework Annotation Symbol in Current View
"""

from revitutils import doc, uidoc
from Autodesk.Revit.DB import Transaction, View, BuiltInCategory

# activate the show hidden so we can collect all elements (visible and hidden)
activeview = uidoc.ActiveView
# FIXME: Would like the option of using the current sheet or all the sheets

# define a transaction variable and describe the transaction
t = Transaction(doc, 'Toggle Detail Framework')

# start a transaction in the Revit database
t.Start()

# If the Detail Sheet Framework Generic Annotation subcategory is shown
# Then turn it off. If it's hidden, then turn it on.

GA = doc.Settings.Categories.get_Item(BuiltInCategory.OST_GenericAnnotation)
subcat = GA.SubCategories

for sub in subcat:
    if sub.Name == "Detail Sheet Framework":
        i = (sub.Id)

if View.GetCategoryHidden(activeview, i):
    View.SetCategoryHidden(activeview, i, False)
else:
    View.SetCategoryHidden(activeview, i, True)

# commit the transaction to the Revit database
t.Commit()
