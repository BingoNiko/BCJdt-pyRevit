"""
Copyright (c) Ben Muller - @pix3lot
BCJdt - Bohlin Cywinski Jackson designtech
"""

__doc__ = 'This tool is to align a section or elevation to a wall. Run this tool in a Plan view.' \
          ' Pick the view to align, then pick the wall to align to.'

from Autodesk.Revit.DB import Transaction, FilteredElementCollector, View, ViewSection, Wall, XYZ, Line, Curve, ElementTransformUtils
from Autodesk.Revit.UI import TaskDialog
from Autodesk.Revit.UI.Selection import ObjectType

try:
    from revitutils import doc, uidoc, selection
except:
    from pyrevit import revit
    uidoc = revit.uidoc
    doc = revit.doc

from math import pi as PI

views = FilteredElementCollector(doc).OfClass(ViewSection)
view = []

try:
    view_el =  doc.GetElement(uidoc.Selection.PickObject(ObjectType.Element, 'Pick View to Align'))
    align_el = doc.GetElement(uidoc.Selection.PickObject(ObjectType.Element, 'Pick Wall to Align View to'))

#get view from view element
    for v in views:
        if v.Name == view_el.Name:
            view = v

	###--- Parameters ---###
    v_direction = view.ViewDirection
    v_origin = XYZ(view.Origin.X, view.Origin.Y, view.Origin.Z)#.ToPoint().ToXyz() #ISSUE IS HERE NO .ToPoint
    v_midpoint = XYZ(view.Origin.X, view.Origin.Y, 0)
        
    el_orientation = align_el.Orientation
    r_orientation = el_orientation.CrossProduct(XYZ.BasisZ)

    #axis of view for rotation, rotate about Z axis @ origin
    axis = Line.CreateBound(v_origin, v_origin + XYZ.BasisZ)

    #orientation of element to align to
    el_curve = align_el.Location.Curve
    el_midpoint = el_curve.Origin
    el_offset = el_curve.CreateOffset(-2, XYZ.BasisZ)
    el_flip = align_el.Flipped

    if el_flip:
        el_offset = el_curve.CreateOffset(2, XYZ.BasisZ)

    el_off_mid = el_offset.Evaluate(0.5, True)

    move = el_off_mid - v_midpoint

    #angle from element to view
    angle = el_orientation.AngleTo(v_direction)
    #angle from orientation to view
    angle_r = r_orientation.AngleTo(v_direction)

    #direction to rotate
    dir = 1.0

    #check the angle between to determin direction
    #used Degrees so we can use round() later
    #probably an easier way, but it works
    abs_angle = (abs(angle) - abs(angle_r)) * (180/PI)
    abs_angle_add = (abs(angle) + abs(angle_r)) * (180/PI)

    if round(abs_angle) == -90:
        dir = -1.0
        
    if round(abs(abs_angle)) != 90:
        dir = -1.0
        
    if round(abs_angle_add) == 90:
        dir = 1.0

    #apply the direction for rotation
    angle *= dir

    #rotate to perpendicular
    angle += (PI/2)

    with Transaction(doc, 'Update Section') as t:
        t.Start()
        ###--- Rotate marker to match element ---###
        ElementTransformUtils.RotateElement(doc, view_el.Id, axis, angle)
        doc.Regenerate()

        ###--- Move marker to align element ---###
        ElementTransformUtils.MoveElement(doc, view_el.Id, move)
        doc.Regenerate()

        t.Commit()

except:
	pass
