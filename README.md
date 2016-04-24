CodeIniter - Sublime Text 3
===========================

This extension allows you to initialise files of various formats with snippets of code.
<br>Currently tested for Sublime Text 3 on Windows 10.

Inspiration
--------------------
Since I do not use an IDE while doing competitive programming, I would constantly write obvious code like ```int main()``` and 
```public static void main(String[] args)```. This is an attempt to reduce that effort by doing the same task with a single command.

Steps to Use/Install
--------------------
1. Clone the repo
2. Go to The Sublime Text Packages Directory (```/Packages```) and paste this folder over there.
<br>Basically it should be like this ```/Packages/CodeIniter/```
3. The config file is stored in the Sublime Text 3's cache directory.
<br>Open the console in Sublime Text and type <br>
```import sublime```
<br>```print(sublime.cache_path())```
4. The config.json file can be found in ```*cache_path*/CodeIniter/config.json```
5. Here you can add your own snippets for various file formats. The format is the key and the snippet is the value.
6. After doing this, open a file in Sublime of one of the formats.
7. Open the command palette (```Ctrl + Shift + P```) and type initialise, select the open ```File: Initialise```. Alternatively, use the console to write ```view.run_command('initialise')```.
8. Voila! Your file has been initialised with your custom snippet.

Plugin is still in testing and this page will soon be updated with screenshots and any changes for Mac and Linux platforms
<br>After proper testing I plan to upload this plugin at Package Control for public use.
