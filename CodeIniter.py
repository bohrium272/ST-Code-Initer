import sublime
import sublime_plugin
import os
import json


class InitialiseCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        decoder = json.JSONDecoder()
        platform = sublime.platform()
        if platform == 'linux' or platform == 'osx':
            path = sublime.cache_path() + '/CodeIniter/config.json'
        else:
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
        if int(sublime.version()) > 3000: 
            path = sublime.cache_path()
        else:
            path = sublime.installed_packages_path()
        platform = sublime.platform()
        if platform == 'linux' or platform == 'osx':
            path = path + '/CodeIniter'
        else:
            path = path + '\CodeIniter'
        if os.path.exists(path):
            print()
        else:
            os.makedirs(path)
        if platform == 'linux' or platform == 'osx':
            path = path + '/config.json'
        else:
            path = path + '\config.json'
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