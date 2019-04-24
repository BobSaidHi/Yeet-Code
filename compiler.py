#Yeet-Code Compiler
print("Starting Yeet-Code Compiler Version INDEV Version 1")
print("This version is propriatary.  ALL RIGHTS RESERVED, including distrabution and modification.")

#Imports
import py_compile
from os import rename as os_rename
from os import remove as os_remove
from os import chdir as os_chdir
import zipfile
import datetime

#Variables
statement = []
compatiblity = []
type_expect = 'skip'

#Open File
source = 'input/example-source.yeet'
f = open(source, mode='r', encoding='ascii')

#String Artist
statement = f.read()
statement = statement.split(' ')
f.close()
print(statement)

#Compatibilty Layer
for i in statement:
    if type_expect == 'command':
        if i == 'NULL':
            compatiblity.append('NULL')
            type_expect = 'NONE'
            print("statement:" + "  " + i + "    " + "next_type:" + "  " + type_expect)
            compatiblity.append('/na = input()')
        elif i == 'YEET':
            compatiblity.append('print(')
            type_expect = 'text'
            print("statement:" + "  " + i + "    " + "next_type:" + "  " + type_expect)
    elif type_expect == 'text':
        compatiblity.append(i)
        compatiblity.append(')')
        type_expect = 'command'
        print("statement:" + "  " + i + "    " + "next_type:" + "  " + type_expect)
    elif type_expect == 'skip':
        type_expect = 'command'
        print("statement:" + "  " + i + "    " + "next_type:" + "  " + type_expect)    
    else:
        print("Skipping bad satement" + " " + i)
        print("statement:" + "  " + i + "    " + "next_type:" + "  " + type_expect)

#Cache Compatibilty Layer's Code
g = open('cache/build.ytmp', mode='w')
#g = open('cache/build.py', mode='w')
for j in compatiblity:
    g.write(j)
g.close()

#Convert to Byte Code
name = 'example-compiled.pyc.yt'
try:
    os_remove('cache/__pycache__/' + name)
except(FileNotFoundError):
    pass
py_compile.compile('cache/build.ytmp')
os_rename('cache/__pycache__/build.cpython-37.pyc', str('cache/__pycache__/' + name))

package_name = 'example-package.zip'
#Zip file creation
os_chdir('cache/__pycache__/')
package = zipfile.ZipFile(package_name, mode='w')
package.write(name)
package.close()
os_chdir('..')
os_chdir('..')
os_rename('cache/__pycache__/' + package_name, str('output/' + package_name))

#Wait
print("Press any key to close...")
a = input()
