import sublime, sublime_plugin, os, json
class InitialiseCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		file_name = str(self.view.file_name())
		index = file_name.rfind('.')
		file_type = file_name[index + 1:len(file_name)]
		print(file_type)
		decoder = json.JSONDecoder()
		path = sublime.cache_path() + '\CodeIniter\config.json'
		fobj = open(path, 'r')
		s = fobj.read()
		db = decoder.decode(s)
		file_name = self.view.file_name()
		index = int(file_name.rfind('.')) + 1
		file_type = file_name[index:]
		fobj.close()
		self.view.insert(edit, 0, db[file_type])

class FileListener(sublime_plugin.EventListener):
	def on_load_async(self, view):
		path = sublime.cache_path()
		path = path + '\CodeIniter'
		print(path)
		if os.path.exists(path):
			print()
		else:
			os.makedirs(path)
		path = path + '\config.json'
		print(path)
		if os.path.isfile(path):
			print()
		else:
			fobj = open(path, 'w')
			data = {}
			data['cpp'] = '#include <iostream>\nusing namespace std\nint main() {\n}'
			data['java'] = 'import java.util.*;\nimport java.io.*;\nclass {\npublic static void main(String[] args) {\n}'
			data['py'] = 'import os'
			fobj.write(json.dumps(data))
			fobj.close()