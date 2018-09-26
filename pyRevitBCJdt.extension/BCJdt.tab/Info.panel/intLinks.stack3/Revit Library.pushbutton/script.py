"""Opens the current BCJ Revit Family library location."""

__context__ = 'zerodoc'

from pyrevit import coreutils


revit_folder = 'L:/+Revit'
coreutils.open_folder_in_explorer(revit_folder)
