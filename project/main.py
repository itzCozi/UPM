# Version control system like git using scoop to implement as a terminal app
# Using CMD args: https://www.geeksforgeeks.org/command-line-arguments-in-python/#
import hashlib
import os, sys


class globals:
  user = 'Coope'  #os.getlogin()
  scoop_Dir = str(f'C:/{user}/scoop')
  scoopApp_Dir = str(f'{scoop_Dir}/')
  CC = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
  debug = True


class _upm():

  def setup():
    if os.path.exists(_2PT.scoop_Dir):
      if debug:
        print("Scoop is already installed. ")
      pass
    else:
      subprocess.call(_2PT.powershell + 'iwr -useb get.scoop.sh | iex')

    if not os.path.exists(_2PT.main_Dir):
      os.mkdir(_2PT.main_Dir)
    else:
      pass
    if not os.path.exists(_2PT.scoopApp_Dir):
      os.mkdir(_2PT.scoopApp_Dir)
    else:
      pass

    if not os.path.exists(_2PT.scoopShim_File):
      with open(_2PT.scoopShim_File, 'w') as file:
        file.write(
          f'@"{_2PT.python_Path + "/Python311/python.exe"}" "{_2PT.scoopApp_File}" %*'
        )
      if debug:
        print("Program file " + _2PT.scoopShim_File + " !MISSING!")

    if not os.path.exists(_2PT.scoopApp_File):
      _2PT.utility.install(_2PT.console_WebFile, _2PT.scoopApp_Dir, "2PT",
                           ".py")
      if debug:
        print("Program file " + _2PT.scoopApp_File + " !MISSING!")
