import os, sys

current_Dir = os.getcwd()
current_repository = 'upm'
repository = str(f'{current_Dir}/{current_repository}')
tracked_Dir = str(f'{repository}/tracked_files')
encoded_Dir = str(f'{repository}/encoded')
commits = str(f'{repository}/commits')
builds = str(f'{repository}/builds')
changes_File = str(f'{repository}/changes.txt')

  
class encode:
   
  def tick(letter):
    if 'a' or 'A' in letter:
      if 'a' in letter:
        return '001'
      if 'A' in letter:
        return '011'
    if 'b' or 'B' in letter:
      if 'b' in letter:
        return '002'
      if 'B' in letter:
        return '021' 
    if 'c' or 'C' in letter:
      if 'c' in letter:
        return '003'
      if 'C' in letter:
        return '031'
    if 'd' or 'D' in letter:
      if 'd' in letter:
        return '004'
      if 'D' in letter:
        return '041'
    if 'e' or 'E' in letter:
      if 'e' in letter:
        return '005'
      if 'E' in letter:
        return '051'
    if 'f' or 'B' in letter:
      if 'f' in letter:
        return '006'
      if 'F' in letter:
        return '061'
    if 'g' or 'G' in letter:
      if 'g' in letter:
        return '007'
      if 'G' in letter:
        return '071'
    if 'h' or 'H' in letter:
      if 'h' in letter:
        return '008'
      if 'H' in letter:
        return '081'
    if 'i' or 'I' in letter:
      if 'i' in letter:
        return '009'
      if 'I' in letter:
        return '091'
    if 'j' or 'J' in letter:
      if 'j' in letter:
        return '100'
      if 'J' in letter:
        return '110'
    if 'k' or 'K' in letter:
      if 'k' in letter:
        return '200'
      if 'K' in letter:
        return '210'
    if 'l' or 'L' in letter:
      if 'l' in letter:
        return '300'
      if 'L' in letter:
        return '310'
    if 'm' or 'M' in letter:
      if 'm' in letter:
        return '400'
      if 'M' in letter:
        return '410'
    if 'n' or 'N' in letter:
      if 'n' in letter:
        return '500'
      if 'N' in letter:
        return '510'
    if 'o' or 'O' in letter:
      if 'o' in letter:
        return '600'
      if 'O' in letter:
        return '611'
    if 'p' or 'P' in letter:
      if 'p' in letter:
        return '700'
      if 'P' in letter:
        return '710'
    if 'q' or 'Q' in letter:
      if 'q' in letter:
        return '800'
      if 'Q' in letter:
        return '810'
    if 'r' or 'R' in letter:
      if 'r' in letter:
        return '900'
      if 'R' in letter:
        return '910'  
    if 's' or 'S' in letter:
      if 's' in letter:
        return '010'
      if 'S' in letter:
        return '101'
    if 't' or 'T' in letter:
      if 't' in letter:
        return '020'
      if 'T' in letter:
        return '201'
    if 'u' or 'U' in letter:
      if 'u' in letter:
        return '030'
      if 'U' in letter:
        return '301'
    if 'v' or 'V' in letter:
      if 'v' in letter:
        return '040'
      if 'V' in letter:
        return '401'
    if 'w' or 'W' in letter:
      if 'w' in letter:
        return '050'
      if 'W' in letter:
        return '501'
    if 'x' or 'X' in letter:
      if 'x' in letter:
        return '060'
      if 'X' in letter:
        return '601'
    if 'y' or 'Y' in letter:
      if 'y' in letter:
        return '070'
      if 'Y' in letter:
        return '701'
    if 'z' or 'Z' in letter:
      if 'z' in letter:
        return '080'
      if 'Z' in letter:
        return '801'
    
    if '1' in letter:
      return '10'
    if '2' in letter:
      return '20'
    if '3' in letter:
      return '30'
    if '4' in letter:
      return '40'
    if '5' in letter:
      return '50'
    if '6' in letter:
      return '60'
    if '7' in letter:
      return '70'
    if '8' in letter:
      return '80'
    if '9' in letter:
      return '90'

  
  def encode_file(file):
    if not os.path.exists(f'{tracked_Dir}/{file}'):
      print('ERROR: File not tracked.')
    
    with open(file, 'r+') as File:
      file_name = os.path.basename(file).split('/')[-1]
      write_back = File.read()
      for line in write_back:

        for word in line.split(' '):
          word_list = list(word)
          
          for letter in word_list:
            if letter.isalpha():
              write_back = write_back.replace(letter, encode.tick(letter))

      with open(f'{tracked_Dir}/{file}.enc', 'w') as Fout:
        print(f'Encoded {file_name} and created tracked file.')
        Fout.write(write_back)
        File.close()


try:
  if sys.argv[1] == 'encode':
    encode.encode_file(sys.argv[2])
    sys.exit(0)
  else:
    print('This program can only encode tracked files.')
    sys.exit(1)
except IndexError:
  print('You must pass `encode` argument followed by \
    \na file path to encode a tracked file.')
  sys.exit(1)
except Exception as e:
  print(f'CRIT-ERROR: A unkown runtime-error occurred. \n{e}\n')
  sys.exit(1)
  