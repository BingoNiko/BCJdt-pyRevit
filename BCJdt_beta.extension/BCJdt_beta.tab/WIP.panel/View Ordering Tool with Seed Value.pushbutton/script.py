from pyrevit import revit, DB, UI
from pyrevit import forms
from rpw.ui.forms import TextInput


__doc__ = 'Run this tool in a sheet view and click on viewports one '\
          'by one and this tool will change the detail number sequencially.'


curview = revit.activeview

if not isinstance(curview, DB.ViewSheet):
    forms.alert('You must be on a sheet to use this tool.')

viewports = []
for vpId in curview.GetAllViewports():
    viewports.append(revit.doc.GetElement(vpId))

# TODO: Exclude legends.
# Can you give a warning if you are trying to renumber a legend?
vports = {(vp.LookupParameter('Detail Number').AsString()): vp
          for vp in viewports if vp.LookupParameter('Detail Number')}

maxNum = max(vports.keys())

with revit.Transaction('Re-number Viewports'):
    '''
    TODO: Is it better to ask for the starting value first, or to select the viewports first?
   '''
    # Popup Textbox for starting value
    value = TextInput(
        'Starting Value',
        description='Begin renumbering with:',
        default="1",
        )

    # Convert starting value to an integer so it can be added to
    v = int(value)

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

    # Instead of enumerating the iteration, run through list and set value to string of 'v' and then iterate for the next selection
    for el in sel:
        el.LookupParameter('Detail Number').Set(str(v))
        v += 1
