import subprocess as sp
import re
from swutil.aux import string_dialog
from swutil.files import find_directories,find_files
import os.path
ROOT_DIR = os.path.expanduser('~')
project = string_dialog('Quickedit','Enter filename')
regexp = re.compile(project+'.*',re.IGNORECASE)
choices = find_directories(pattern=regexp,path = ROOT_DIR, match_name = True,)
projectdir = os.path.join(ROOT_DIR,choices[0])
projectfile = find_files(path = projectdir, pattern ='*.tex',match_name=True)[0]
sp.call(['gvim',os.path.join(projectdir,projectfile)])
