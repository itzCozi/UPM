import os, sys
import shutil
from datetime import datetime

class globals:
  version = '0.1 - Pre-release'
  now = datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '\n\n'

  class upm_files:
    current_Dir = os.getcwd()
    repository = str(f'{current_Dir}/upm')
    tracked_Dir = str(f'{repository}/tracked_files')
    commits = str(f'{repository}/commits')
    builds = str(f'{repository}/builds')
    changes_File = str(f'{repository}/changes.txt')


class test:
  def zip_repo(name):
    zip_location = f'{globals.upm_files.current_Dir}/{name}'
    zip_obj = shutil.make_archive(zip_location, 'zip', globals.upm_files.repository)
    
    if not os.path.exists(zip_location):
      print(zip_obj)
    else:
      print('Oops')
      
      
given = input('Name: ')
test.zip_repo(given)