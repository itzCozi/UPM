# Version control system like git using scoop to implement as a terminal app
import hashlib
import os, sys
import requests
import subprocess

debug = True


class globals:
  version = '0.1 - Pre-release'
  user = os.getlogin()
  powershell = str('C:/Windows/System32/powershell.exe')
  web_file = str(f'https://github.com/itzCozi/UPM/blob/main/UPM-source/win-version/{__file__}')
  python_Path = str(f'C:/Users/{user}/AppData/Local/Programs/Python/Python311')
  main_Dir = str(f'C:/Users/{user}/upm')
  scoop_Dir = str(f'C:/Users/{user}/scoop')
  scoopApp_Dir = str(f'{scoop_Dir}/apps/upm')
  scoopShim_File = str(f'{scoop_Dir}/shims/upm.cmd')
  scoopApp_File = str(f'{scoopApp_Dir}/upm.py')
  CC = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

  class upm_files:
    current_Dir = os.getcwd()
    repository = str(current_Dir + '/upm')
    tracked_Dir = str(repository + '/tracked_files')
    commits = str(repository + '/commits')
    changes_File = str(repository + '/changes.txt')


class commands:

  def about():
    # Simply prints the version and github
    print('----- Universal Program Manager -----\n')
    print(f'Version: {globals.version}')
    print(f'Github: https://github.com/itzCozi/UPM')
    return True

  def init():
    # Creates and sets up the folder system in current folder that archives changes
    try:
      os.mkdir(globals.upm_files.repository)
      os.mkdir(globals.upm_files.tracked_Dir)
      os.mkdir(globals.upm_files.commits)
      open(globals.upm_files.changes_File, 'w')
      print(f'{globals.upm_files.current_Dir} | Repository successfully created!')
      return True
    except:
      print('ERROR: An error occured, repository not created.')
      sys.exit(1)

  def commit(dir, message):
    # Commit a draft as a folder
    if os.path.exists(dir):
      formatted_msg = message.replace(' ', '-')
      commit_Dir = f'{globals.upm_files.commits}/{formatted_msg}'
      if not os.path.exists(commit_Dir):
        os.mkdir(commit_Dir)
      else:
        print("ERROR: A commit with the same message is already made.")
        sys.exit(1)
    else:
      print('ERROR: Given directory can not be found.')
      sys.exit(1)

    for r, d, f in os.walk(dir):
      # Works but spits out the files in the commit_dir not there folders
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
        file_name = os.path.basename(file).split("/")[-1]
        new_Dir = str(f'{globals.upm_files.tracked_Dir}/{file_name}')
        with open(new_Dir, 'w') as Fout:
          Fout.write(file_content)
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
        print(f'{file_name} | Has been untracked.')
        return True
      except:
        print('ERROR: Could not access tracked file.')
        sys.exit(1)
    else:
      print('Given file does not exists.')
      sys.exit(1)

  def update(file):
    # Updates the saved file with the given file
    file_name = os.path.basename(file).split('/')[-1]
    if os.path.exists(f'{globals.upm_files.tracked_Dir}/{file_name}'):
      try:
        with open(file, 'r') as Fout:
          file_content = Fout.read()
          with open(f'{globals.upm_files.tracked_Dir}/{file_name}','w') as Fin:
            Fin.write(str(file_content))
          print(f'{file_name} | Saved file has been updated.')
          return True
      except:
        print('ERROR: Counld not access files, Maybe try as admin.')
        sys.exit(1)
    else:
      print('ERROR: Given file is not being tracked.')
      sys.exit(1)


class _upm:

  @staticmethod
  # Returns all files in the baseDir
  def get_files(baseDir):
    files = []
    for r, d, f in os.walk(baseDir):
      for file in f:
        filepath = os.path.join(r, file)
      if os.path.exists(filepath):
        files.append(filepath)

    return files

  class utility:

    @staticmethod
    def setup():
      # Setup program files and dependencies
      if os.path.exists(globals.scoop_Dir):
        if debug:
          print('Scoop is already installed. ')
        pass
      else:
        subprocess.call(globals.powershell + 'iwr -useb get.scoop.sh | iex')

      if not os.path.exists(globals.main_Dir):
        os.mkdir(globals.main_Dir)
      else:
        pass
      if not os.path.exists(globals.scoopApp_Dir):
        os.mkdir(globals.scoopApp_Dir)
      else:
        pass

      if not os.path.exists(globals.python_Path):
        python_install = 'https://www.python.org/downloads/release/python-3110/'
        print(f'Python3.11 not installed please download it here: {python_install}')

      if not os.path.exists(globals.scoopShim_File):
        with open(globals.scoopShim_File, 'w') as file:
          file.write(f'@"{globals.python_Path + "/python.exe"}" "{globals.scoopApp_File}" %*')
      if debug:
        print('Program file ' + globals.scoopShim_File + ' !MISSING!')

      if not os.path.exists(globals.scoopApp_File):
        try:
          _upm.utility.install(globals.web_file, globals.scoopApp_Dir, '/upm.py')
        except:
          print('ERROR: Cant install file from web, Did you change the name of the file?')
        if debug:
          print('Program file ' + globals.scoopApp_File + ' !MISSING!')

    def hashfile(file):
      # Hash the contents of the file
      BUF_SIZE = os.path.getsize(file)
      sha256 = hashlib.sha256()
      with open(file, 'rb') as f:
        while True:
          data = f.read(BUF_SIZE)
          if not data:
            break

        f.close()

        sha256.update(data)
        return sha256.hexdigest()

    def install(URL, Destination, NewName):
      # Download and write to file
      file_content = requests.get(URL)
      open(Destination + '/' + NewName, 'wb').write(file_content.content)
      if debug:
        print('Downloaded file to: ' + Destination)


class driver:

  def arg_handler():
    if sys.argv[1] == 'about':
      commands.about()
    if sys.argv[1] == 'init':
      commands.init()
    if sys.argv[1] == 'commit':
      try:
        commands.commit(str(sys.argv[2]), str(sys.argv[3]))
      except IndexError:
        print("Please provide proper parameters : commit 'C:/project/source' Bug Fix #69")
    if sys.argv[1] == 'track':
      try:
        commands.track(sys.argv[2])
      except:
        print("Please provide proper parameters : track 'C:/project/users.txt'")
    if sys.argv[1] == 'untrack':
      try:
        commands.untrack(sys.argv[2])
      except:
        print("Please provide proper parameters : untrack 'test/lol.py'")
    if sys.argv[1] == 'update':
      try:
        commands.update(sys.argv[2])
      except:
        print("Please provide proper parameters : update 'C:/test.txt'")


driver.arg_handler()
