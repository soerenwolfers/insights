insights: quick note taking
==========================================
:Author: Soeren Wolfers <soeren.wolfers@gmail.com>
:Organization: King Abdullah University of Science and Technology (KAUST) 

Take notes of sudden realizations and small insights without disturbing your workflow

Installation:

1) :code:`pip install swutil`. 
2) Download :code:`insights.py`
3) Create a keyboard shortcut that runs :code:`<PYTHON> <INSIGHTS>`, where :code:`<PYTHON>` is your Python3 executable and :code:`<INSIGHTS>` is the full path of :code:`insights.py` (:code:`compizconfigsettingsmanager` can be used on Ubuntu).

If desired:

1) Edit :code:`ROOT_DIR` to parent directory of notes files (default: parent directory of :code:`insights.py`)
2) Edit :code:`ENDING` to change the type of your note files (default: :code:`tex`)
3) Edit :code:`EDITOR` to change editor (default: :code:`vim`) 

Usage:

1) Whenever an insight occurs, press the shortcut, type the initial letters of a file that you want to edit, e.g. :code:`g`, to edit :code:`git.tex`, and press Enter
2) If you are using tex files and want to see the compiled pdf instead of editing, append an exclamation mark, e.g. :code:`g!`, to compile the tex and open the pdf
