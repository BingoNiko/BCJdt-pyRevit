from Autodesk.Revit.UI import TaskDialog

name = __revit__.Application.Username
output = 'Good job %s !!  You can go home now.' % name
print(output)
