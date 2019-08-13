import os
import sys

from cx_Freeze import setup, Executable

Path = str(os.getcwd())
distr = Path + '\\distr'

executables = [
		Executable('mainOR.pyw',
                        base="Win32GUI",
                        targetName='OpenRoller.exe',
                        icon = distr + '\\iconOR.ico',),
		Executable('mainOC.pyw',
                        base="Win32GUI",
                        targetName='OpenCrafter.exe',
                        icon = distr + '\\iconCR.ico',),
		]

include_files = ['BluePrints',
                 'Crafters',
                 'Bugs.gdoc',
                 'Правила ремесла.docx',
                 'Правила бросков и действий.docx',
                 'Условные обозначения.gdoc',
                 'distr'
                 ]

options = {'build_exe': {
            'include_files': include_files,
	      'build_exe': Path[0]+':\\Drive\\OGall\\'
           }}

setup(name = 'OGall',
      version = '0.95',
      description = 'Support progs for OG',
      executables = executables,
      options = options,
      )
