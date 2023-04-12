# Version control system like git using scoop to implement as a terminal app
import os, sys
import requests
import shutil
import subprocess
from datetime import datetime

debug = True


class globals:
  version = '0.1 - Pre-release'
  user = os.getlogin()
  powershell = str('C:/Windows/System32/powershell.exe')
  web_file = str(f'https://github.com/itzCozi/UPM/blob/main/UPM-source/win-version/{__file__}')
  scoop_Dir = str(f'C:/Users/{user}/scoop')
  scoopApp_Dir = str(f'{scoop_Dir}/apps/upm')
  scoopShim_File = str(f'{scoop_Dir}/shims/upm.cmd')
  scoopApp_File = str(f'{scoopApp_Dir}/upm.py')
  now = datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '\n\n'

  class upm_files:
    current_Dir = os.getcwd()
    repository = str(f'{current_Dir}/upm')
    tracked_Dir = str(f'{repository}/tracked_files')
    commits = str(f'{repository}/commits')
    builds = str(f'{repository}/builds')
    changes_File = str(f'{repository}/changes.txt')


class commands:

  def about():
    # Simply prints the version and github
    print('----- Universal Program Manager -----\n')
    print(f'Version: {globals.version}')
    print(f'Current repository: {globals.upm_files.repository}')
    print('Github: https://github.com/itzCozi/UPM')
    return True

  def init():
    # Creates and sets up the folder system in current folder that archives changes
    try:
      os.mkdir(globals.upm_files.repository)
      os.mkdir(globals.upm_files.tracked_Dir)
      os.mkdir(globals.upm_files.commits)
      os.mkdir(globals.upm_files.builds)
      open(globals.upm_files.changes_File, 'w')
      with open(f'{globals.upm_files.changes_File}', 'a') as log:
        log.write(f'{globals.upm_files.current_Dir} | New repository created AT - {globals.now}')
      print(f'{globals.upm_files.current_Dir} | Repository successfully created!')
      return True
    except Exception as e:
      print(f'ERROR: An error occured, repository not created. \n{e}\n')
      sys.exit(1)

  def commit(dir, message):
    # Commit a draft as a folder
    if os.path.exists(dir):
      formatted_msg = message.replace(' ', '-')
      commit_Dir = f'{globals.upm_files.commits}/{formatted_msg}'
      if not os.path.exists(commit_Dir):
        os.mkdir(commit_Dir)
      else:
        print('ERROR: A commit with the same message is already made.')
        sys.exit(1)
    else:
      print('ERROR: Given directory can not be found.')
      sys.exit(1)

    for r, d, f in os.walk(dir):
      for folder in d or f:
        tracked_folder = os.path.join(r, folder)
        new_Dir = str(f'{commit_Dir}/{dir}')
        new_File = str(f'{commit_Dir}/{tracked_folder}')
        if not os.path.exists(new_Dir):
          os.mkdir(new_Dir)
        if not os.path.exists(new_File):
          if os.path.isdir(tracked_folder):
            os.mkdir(new_File)
          else:
            open(new_File, 'w')
      for file in f:
        tracked_path = os.path.join(r, file)
        if not os.path.exists(new_File):
          open(new_File, 'w')
        with open(f'{commit_Dir}/{tracked_path}', 'w') as _file:
          _file.write(open(tracked_path, 'r').read())
      print(f'{commit_Dir} | New commit has been made.')
      return True

  def track(file):
    # Starts tracking a file's changes
    if os.path.exists(file):
      with open(file, 'r') as Fin:
        file_content = Fin.read()
        file_name = os.path.basename(file).split('/')[-1]
        new_Dir = str(f'{globals.upm_files.tracked_Dir}/{file_name}')
        with open(new_Dir, 'w') as Fout:
          Fout.write(file_content)
      with open(f'{globals.upm_files.changes_File}', 'a') as log:
        log.write(f'{file_name} | New file has tracked AT - {globals.now}')
      print(f'{file_name} | Successfully tracked.')
      return True
    else:
      print('ERROR: File cannont be found.')
      sys.exit(1)

  def untrack(file):
    # Just untracks the file
    file_name = os.path.basename(file).split('/')[-1]
    tracked_file = f'{globals.upm_files.tracked_Dir}/{file_name}'
    if os.path.exists(tracked_file):
      try:
        os.remove(tracked_file)
        with open(f'{globals.upm_files.changes_File}', 'a') as log:
          log.write(f'{file_name} | File has been untracked AT - {globals.now}')
        print(f'{file_name} | Has been untracked.')
        return True
      except Exception as e:
        print(f'ERROR: Could not access tracked file. \n{e}\n')
        sys.exit(1)
    else:
      print('Given file does not exists.')
      sys.exit(1)

  def build(dir, name, version):
    # Creates a compiled version of the project
    if os.path.exists(dir):
      formatted_name = name.replace(' ', '-')
      build_Dir = f'{globals.upm_files.builds}/{formatted_name}-{version}'
      if not os.path.exists(build_Dir):
        os.mkdir(build_Dir)
      else:
        print('ERROR: A build with the same message is already made.')
        sys.exit(1)
    else:
      print('ERROR: Given directory can not be found.')
      sys.exit(1)

    for r, d, f in os.walk(dir):
      for folder in d or f:
        tracked_folder = os.path.join(r, folder)
        new_Dir = str(f'{build_Dir}/{dir}')
        new_File = str(f'{build_Dir}/{tracked_folder}')
        if not os.path.exists(new_Dir):
          os.mkdir(new_Dir)
        if not os.path.exists(new_File):
          if os.path.isdir(tracked_folder):
            os.mkdir(new_File)
          else:
            open(new_File, 'w')
      for file in f:
        tracked_path = os.path.join(r, file)
        if not os.path.exists(new_File):
          open(new_File, 'w')
        with open(f'{build_Dir}/{tracked_path}', 'w') as _file:
          _file.write(open(tracked_path, 'r').read())
      print(f'{build_Dir} | New build has been created.')
      return True

  def update(file):
    # Updates the saved file with the given file
    file_name = os.path.basename(file).split('/')[-1]
    if os.path.exists(f'{globals.upm_files.tracked_Dir}/{file_name}'):
      try:
        with open(file, 'r') as Fout:
          file_content = Fout.read()
          with open(f'{globals.upm_files.tracked_Dir}/{file_name}', 'w') as Fin:
            Fin.write(str(file_content))
          with open(f'{globals.upm_files.changes_File}', 'a') as log:
            log.write(f'{file_name} | Tracked file has been updated AT - {globals.now}')
          print(f'{file_name} | Saved file has been updated.')
          return True
      except Exception as e:
        print(f'ERROR: Counld not access files, Maybe try as admin. \n{e}\n')
        sys.exit(1)
    else:
      print('ERROR: Given file is not being tracked.')
      sys.exit(1)

  def clear_changes():
    # Clear the changes file
    changes_file = globals.upm_files.changes_File
    try:
      if os.path.exists(changes_file):
        with open(f'{changes_file}', 'a') as file:
          file.truncate(0)
          file.write('Changes file cleared! \n\n')
          file.close()
    except Exception as e:
      print(f'ERROR: Could not access changes file. \n{e}\n')
      sys.exit(1)

  def uninit():
    # Deletes the repository
    try:
      for d in os.walk(globals.upm_files.current_Dir):
        for folder in d:
          if str(folder) == 'upm':
            shutil.rmtree(folder)
          else:
            pass
    except Exception as e:
      print(f'ERROR: Could not access needed files. \n{e}\n')
      sys.exit(1)


class utility:

  @staticmethod
  def setup():
    # Setup program files and dependencies
    if os.path.exists(globals.scoop_Dir):
      if debug:
        print('Scoop is already installed. ')
      pass
    else:
      subprocess.call(f'{globals.powershell} iwr -useb get.scoop.sh | iex')
      print('We have installed scoop for you this is so you can use\
            \nour program with calling to it with `python upm.py`\
            \n instead try and use `upm` to call to the program.\n')

    if os.path.exists(globals.scoop_Dir):
      if not os.path.exists(globals.scoopApp_Dir):
        os.mkdir(globals.scoopApp_Dir)

      if not os.path.exists(globals.scoopShim_File):
        with open(globals.scoopShim_File, 'w') as file:
          file.write(f'@"{globals.scoopApp_File}" %*')
      if debug:
        print(f'Program file {globals.scoopShim_File} !MISSING!')

      if not os.path.exists(globals.scoopApp_File):
        try:
          utility.install(globals.web_file, globals.scoopApp_Dir, '/upm.py')
        except Exception as e:
          print(f'ERROR: Cant install file from web, Did you change the name of the file? \n{e}\n')
          sys.exit(1)
        if debug:
          print(f'Program file {globals.scoopApp_File} !MISSING!')
    else:
      pass

  def install(URL, destination, NewName):
    # Download and write to file
    file_content = requests.get(URL)
    open(f'{destination}/{NewName}', 'wb').write(file_content.content)
    if debug:
      print(f'Downloaded file to: {destination}')


class driver:

  def mercyHelper():
    # This creates a file called HELP.txt with helpful info
    if os.path.exists(globals.upm_files.repository):
      new_file = f'{globals.upm_files.repository}/HELP.txt'
    else:
      new_file = f'{globals.upm_files.current_Dir}/HELP.txt'
    if not os.path.exists(new_file):
      open(new_file, 'x')
    with open(new_file, 'w') as file:
      file.write('Github:https://github.com/itzCozi/UPM\n')
      file.write('Wiki: https://github.com/itzCozi/UPM/wiki\n')
      file.write('''
Commands | Description
init : Creates `upm` folder and repository
about : Displays relitive context
commit : Create a new commit with given name
track : Starts saving given file
untrack : Removes given save file
update : Update the given tracked file
build : Create a new build and store it in repository
clear_changes : Wipes the changes file
uninit : Deletes detected repository
      ''')
      file.close()

  def argHandler():
    if sys.argv[1] == 'init':
      commands.init()
    elif sys.argv[1] == 'about':
      commands.about()
    elif sys.argv[1] == 'uninit':
      commands.uninit()
    elif sys.argv[1] == 'clear_changes':
      commands.clear_changes()
    elif sys.argv[1] == 'commit':
      try:
        commands.commit(str(sys.argv[2]), str(sys.argv[3]))
      except IndexError:
        print("Please provide proper parameters : commit 'C:/project/source' Bug Fix #69")
    elif sys.argv[1] == 'track':
      try:
        commands.track(sys.argv[2])
      except Exception as e:
        print(f"Please provide proper parameters : track 'C:/project/users.txt' \n{e}\n")
    elif sys.argv[1] == 'untrack':
      try:
        commands.untrack(sys.argv[2])
      except Exception as e:
        print(f"Please provide proper parameters : untrack 'test/lol.py' \n{e}\n")
    elif sys.argv[1] == 'update':
      try:
        commands.update(sys.argv[2])
      except Exception as e:
        print(f"Please provide proper parameters : update 'C:/test.txt' \n{e}\n")
    elif sys.argv[1] == 'build':
      try:
        commands.build(sys.argv[2], sys.argv[3], sys.argv[4])
      except Exception as e:
        print(f"Please provide proper parameters : build 'C:/UPM.txt' TESTBUILD 1.0.0 \n{e}\n")

    else:
      print("To use UPM you must pass an argument via the command-line such as: \
        \npython upm.py track 'happy-420/snoop.cpp'")


try:
  driver.argHandler()
except Exception as e:
  print(f'CRIT-ERROR: A unkown runtime-error occurred. \n{e}\n')
  driver.mercyHelper()
  sys.exit(1)
