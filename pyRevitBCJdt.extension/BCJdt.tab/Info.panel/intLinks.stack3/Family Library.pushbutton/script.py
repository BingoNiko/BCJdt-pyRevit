"""Opens the current BCJ Revit Family library location."""

__context__ = 'zerodoc'

from pyrevit import coreutils


family_folder = 'L:/+Revit/3 Families/'
coreutils.open_folder_in_explorer(family_folder)
