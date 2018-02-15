# BCJdt - Bohlin Cywinski Jackson designtech
# Copyright(c) 2018
# Author: Jon Szczesniak - @jonszcz
"""
Toggles the side of a Grid or Level bubble in the active view based on the current selection
"""
# Import necessary classes
from rpw import revit, db, ui
from Autodesk.Revit.DB import DatumEnds

# Shortcut variables
uidoc = revit.uidoc
v = uidoc.ActiveView

# RPW way of instantiating a transaction within Revit
with db.Transaction('Swap Grid Heads'):
    # Grab selected elements in the active view
    selection = ui.Selection()

    # Iterate through the list of selected items
    # Look at each end of the plane/line and see if the Bubble is on
    # Set the bubble to be off if it's on, and on if it's off
    for i in selection:
        i.HideBubbleInView(DatumEnds.End0, v) if i.IsBubbleVisibleInView(DatumEnds.End0, v) else i.ShowBubbleInView(DatumEnds.End0, v)
        i.HideBubbleInView(DatumEnds.End1, v) if i.IsBubbleVisibleInView(DatumEnds.End1, v) else i.ShowBubbleInView(DatumEnds.End1, v)
