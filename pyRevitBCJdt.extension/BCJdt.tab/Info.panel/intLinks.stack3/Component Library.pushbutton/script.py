"""Opens the current BCJ Revit Detail Component library location."""

__context__ = 'zerodoc'

from pyrevit import coreutils


component_folder = 'L:/+Revit/2 Detail Components/'
coreutils.open_folder_in_explorer(component_folder)
