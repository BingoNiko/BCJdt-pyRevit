"""Opens the BCJ Slack group. Talk to your Office Coordinator if you do not have login information."""

__context__ = 'zerodoc'


#old non-functioning code
# from scriptutils import open_url
#open_url('http://bcj.slack.com')

import webbrowser

url = 'http://bcj.slack.com'

webbrowser.open_new(url)