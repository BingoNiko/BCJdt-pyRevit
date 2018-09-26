'''
Copyright(c) 2017, Jon Szczesniak - @jonszcz
BCJdt - Bohlin Cywinski Jackson designtech
'''

__doc__ = 'This tool will isolate any walls that have painted faces'

import System
from System.Collections.Generic import *
# from revitutils import doc, uidoc, selection
from Autodesk.Revit.DB import *
from pyrevit import revit

doc = revit.doc
uidoc = revit.uidoc
elements = []
view = uidoc.ActiveView
painted = []

collector = FilteredElementCollector(doc, view.Id).WhereElementIsNotElementType()#WherePasses(ElementClassFilter(Wall))

for e in collector:
	if (e.Category != None and e.Category.HasMaterialQuantities):
		elements.append(e)

for el in elements:
	geom = el.get_Geometry(Options())

	for g in geom:

		for f in g.Faces:

			if doc.IsPainted(el.Id, f):
				painted.append(el.Id)

ids = List[ElementId](painted)

with Transaction(doc, 'Isolate Elements') as t:
	t.Start()
	view.IsolateElementsTemporary(ids)
	t.Commit()
