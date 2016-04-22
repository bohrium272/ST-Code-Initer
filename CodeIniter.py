import sublime, sublime_plugin
class InitialiseCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		file_name = str(self.view.file_name())
		index = file_name.rfind('.')
		file_type = file_name[index:len(file_name)]
		print(file_type)
		if file_type == '.py':
			self.view.insert(edit, 0, "Hello, Python!")
		elif file_type == '.cpp':
			self.view.insert(edit, 0, "#include <iostream>\nusing namespace std\nint main() {\n}")
		else:
			self.view.insert(edit, 0, "Hello!!!")	