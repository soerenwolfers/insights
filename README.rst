quickedit: Non-intrusive notetaking
==========================================
:Author: Soeren Wolfers <soeren.wolfers@gmail.com>
:Organization: King Abdullah University of Science and Technology (KAUST) 

This tool allows one to take quick notes of sudden realizations or small insights with a few key strokes, thus without much disturbing work on something else. 

Installation:

Relies on package :code:`swutil`, which can be installed with :code:`pip install swutil`. 

Usage:

1) Create a keyboard shortcut, e.g. :code:`<Super-I>` to :code:`quickedit.py` e.g. with :code:`compizconfigsettingsmanager` on Ubuntu. 
2) Change value of :code:`ROOT_DIR` in :code:`quickedit` to location of insight files (currently it is assumed these are :code:`.tex` files)
3) Whenever an insight occurs, press :code:`<Super-I>`, type the initial letters of a file that you want to write, e.g. :code:`g` to edit :code:`git.tex` in Vim (this can obviously be changed to the editor of your liking)
