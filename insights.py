#! /usr/bin/python3
import os
import subprocess
import re
import sys
from swutil.aux import string_dialog, warning_box
from swutil.files import find_directories,find_files, start_file
DIR = '.' 
EDITOR = 'gvim'
TYPE = 'tex'
if not os.path.isdir(DIR):
    warning_box('Insights','DIR does not exist')
    sys.exit()
project_name = string_dialog('Insights','Enter filename')
show = project_name[0]=='!'
if show:
    project_name=project_name[1:]
regexp = re.compile(project_name+'.*',re.IGNORECASE)
choices = find_directories(pattern=regexp,path = DIR, match_name = True,)
if not choices:
    warning_box('Insights','No matching insight file')
    sys.exit()
project_dir = os.path.join(DIR,min(choices,key = lambda choice:len(choice)))
project_tex = find_files(path = project_dir, pattern ='*.'+TYPE,match_name=True)[0]
os.chdir(project_dir)
if show:
    subprocess.run(['pdflatex','-interaction=nonstopmode',project_tex])
    project_pdf = project_tex[:-4]+'.pdf'
    start_file(project_pdf)
else:
    subprocess.call([EDITOR,project_tex])
