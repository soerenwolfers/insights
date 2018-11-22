#! /usr/bin/python3
import os
import subprocess
import re
import shlex
import sys
from swutil.aux import string_dialog
from tkinter import messagebox
from swutil.files import find_directories,find_files, start_file
DIR = '.'
EDITOR = 'gvim'
EDITOR = 'gnome-terminal -- bash -c "stty -ixon; vim {}"'
TYPE = 'tex'
if not os.path.isdir(DIR):
    messagebox.showerror('Insights','DIR does not exist')
    sys.exit()
name = string_dialog('Insights','Enter filename')
show = name[-1]=='!'
if show:
    name=name[0:-1]
regexp = re.compile(name+'.*',re.IGNORECASE)
dir_choices = find_directories(pattern=regexp,path = DIR, match_name = True)
if not dir_choices:
    file_choices = find_files(path = DIR,pattern = name + '.' + TYPE,match_name=True)
else:
    dir_path = os.path.join(DIR,min(dir_choices,key = lambda choice:len(choice)))
    file_choices = find_files(path = dir_path, pattern ='*.'+TYPE,match_name=True)
if not file_choices:
    messagebox.showerror('Insights','Could not find matching insight file')
    sys.exit()
file_path = file_choices[0]
dir_path = os.path.split(file_path)[0]
os.chdir(dir_path)
if show:
    subprocess.run(['pdflatex','-interaction=nonstopmode',file_path])
    pdf = file_path[:-4]+'.pdf'
    start_file(pdf)
else:
    if '{}' in EDITOR:
        EDITOR = EDITOR.format(file_path)
    else:
        EDITOR = EDITOR+' '+file_path
    subprocess.call(shlex.split(EDITOR))
