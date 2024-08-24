## Overview
input: xlsx file with multiple worksheets inside of it

user interaction: add/edit patient info which is then saved to the original xlsx file

output: formatted text for printing (doc or md etc)


## Resources & Ideas
- [pandas ExcelFile](https://pandas.pydata.org/docs/dev/reference/api/pandas.ExcelFile.html) - for parsing the original .xlsx file
- [python-docx](https://python-docx.readthedocs.io/en/latest/index.html#) - for outputting to word doc 
- GUI Libraries
  - [PySimpleGUI](https://docs.pysimplegui.com/en/latest/) - simpler/faster but some limitations
  - [tkinter](https://docs.python.org/3/library/tkinter.html) - bit slower but more potential
