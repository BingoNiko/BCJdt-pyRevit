from rpw.ui.forms import TextInput


value = TextInput(
	'Starting Value',
	description='Begin renumbering with:',
	default="1",
	)
print('Starting renumbering with detail ' + value)
