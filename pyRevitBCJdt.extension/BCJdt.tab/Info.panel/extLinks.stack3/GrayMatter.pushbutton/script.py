"""Opens the BCJ Intranet. Refer to your New Employee documentation for login information."""

__context__ = 'zerodoc'

#old non-functioning code
#from scriptutils import open_url
#open_url('https://graymatter.bcj.com/Default.aspx')

import webbrowser

url = 'https://graymatter.bcj.com/technology/default.aspx'

webbrowser.open_new(url)
