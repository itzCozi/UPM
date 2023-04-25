import os, sys

current_Dir = os.getcwd()
current_repository = 'upm'
repository = str(f'{current_Dir}/{current_repository}')
tracked_Dir = str(f'{repository}/tracked_files')
encoded_Dir = str(f'{repository}/encoded')
commits = str(f'{repository}/commits')
builds = str(f'{repository}/builds')
changes_File = str(f'{repository}/changes.txt')

  
class encode_decode:
  
  def detick(letter):
    if 'a01' or 'A11' in letter:
      if 'a' in letter:
        return 'a'
      if 'A' in letter:
        return 'A'
    if 'b02' or 'B21' in letter:
      if 'b' in letter:
        return 'b'
      if 'B' in letter:
        return 'B' 
    if 'c03' or 'C31' in letter:
      if 'c' in letter:
        return 'c'
      if 'C' in letter:
        return 'C'
    if 'd04' or 'D41' in letter:
      if 'd' in letter:
        return 'd'
      if 'D' in letter:
        return 'D'
    if 'e05' or 'E51' in letter:
      if 'e' in letter:
        return 'e'
      if 'E' in letter:
        return 'E'
    if 'f06' or 'F61' in letter:
      if 'f' in letter:
        return 'f'
      if 'F' in letter:
        return 'F'
    if 'g07' or 'G71' in letter:
      if 'g' in letter:
        return 'g'
      if 'G' in letter:
        return 'G'
    if 'h08' or 'H81' in letter:
      if 'h08' in letter:
        return 'h'
      if 'H' in letter:
        return 'H'
    if 'i09' or 'I91' in letter:
      if 'i' in letter:
        return 'i'
      if 'I' in letter:
        return 'I'
    if 'j10' or 'J11' in letter:
      if 'j' in letter:
        return 'j'
      if 'J' in letter:
        return 'J'
    if 'k20' or 'K21' in letter:
      if 'k' in letter:
        return 'k'
      if 'K' in letter:
        return 'K'
    if 'l30' or 'L31' in letter:
      if 'l' in letter:
        return 'l'
      if 'L' in letter:
        return 'L'
    if 'm40' or 'M41' in letter:
      if 'm' in letter:
        return 'm'
      if 'M' in letter:
        return 'M'
    if 'n50' or 'N51' in letter:
      if 'n' in letter:
        return 'n'
      if 'N' in letter:
        return 'N'
    if 'o60' or 'O61' in letter:
      if 'o' in letter:
        return 'o'
      if 'O' in letter:
        return 'o'
    if 'p70' or 'P71' in letter:
      if 'p' in letter:
        return 'p'
      if 'P' in letter:
        return 'P'
    if 'q80' or 'Q81' in letter:
      if 'q' in letter:
        return 'q'
      if 'Q' in letter:
        return 'Q'
    if 'r90' or 'R91' in letter:
      if 'r' in letter:
        return 'r'
      if 'R' in letter:
        return 'R'  
    if 's10' or 'S11' in letter:
      if 's' in letter:
        return 's'
      if 'S' in letter:
        return 'S'
    if 't20' or 'T21' in letter:
      if 't' in letter:
        return 't'
      if 'T' in letter:
        return 'T'
    if 'u30' or 'U31' in letter:
      if 'u' in letter:
        return 'u'
      if 'U' in letter:
        return 'U'
    if 'v40' or 'V41' in letter:
      if 'v' in letter:
        return 'v'
      if 'V' in letter:
        return 'V'
    if 'w51' or 'W50' in letter:
      if 'w' in letter:
        return 'w'
      if 'W' in letter:
        return 'W'
    if 'x60' or 'X' in letter:
      if 'x' in letter:
        return 'x'
      if 'X' in letter:
        return 'X'
    if 'y70' or 'Y' in letter:
      if 'y' in letter:
        return 'y'
      if 'Y' in letter:
        return 'Y'
    if 'z80' or 'Z81' in letter:
      if 'z' in letter:
        return 'z'
      if 'Z' in letter:
        return 'Z'
    
    if '10' in letter:
      return '1'
    if '20' in letter:
      return '2'
    if '30' in letter:
      return '3'
    if '40' in letter:
      return '4'
    if '50' in letter:
      return '5'
    if '60' in letter:
      return '6'
    if '70' in letter:
      return '7'
    if '80' in letter:
      return '8'
    if '90' in letter:
      return '9'
    
    if ';' in letter:
      return '!'
    if '*' in letter:
      return '@'
    if ':-' in letter:
      return '#'
    if '::' in letter:
      return '$'
    if '&*' in letter:
      return '%'
    if '@-' in letter:
      return '^'
    if '!<' in letter:
      return '&'
    if '_-_' in letter:
      return '*'
    if '|' in letter:
      return '('
    if '--' in letter:
      return '-'
    if '++' in letter:
      return '+'
    if '=' in letter:
      return '='
   
  def tick(letter):
    if 'a' or 'A' in letter:
      if 'a' in letter:
        return 'a01'
      if 'A' in letter:
        return 'A11'
    if 'b' or 'B' in letter:
      if 'b' in letter:
        return 'b02'
      if 'B' in letter:
        return 'B21' 
    if 'c' or 'C' in letter:
      if 'c' in letter:
        return 'c03'
      if 'C' in letter:
        return 'C31'
    if 'd' or 'D' in letter:
      if 'd' in letter:
        return 'd04'
      if 'D' in letter:
        return 'D41'
    if 'e' or 'E' in letter:
      if 'e' in letter:
        return 'e05'
      if 'E' in letter:
        return 'E51'
    if 'f' or 'F' in letter:
      if 'f' in letter:
        return 'f06'
      if 'F' in letter:
        return 'F61'
    if 'g' or 'G' in letter:
      if 'g' in letter:
        return 'g07'
      if 'G' in letter:
        return 'G71'
    if 'h' or 'H' in letter:
      if 'h' in letter:
        return 'h08'
      if 'H' in letter:
        return 'H81'
    if 'i' or 'I' in letter:
      if 'i' in letter:
        return 'i09'
      if 'I' in letter:
        return 'I91'
    if 'j' or 'J' in letter:
      if 'j' in letter:
        return 'j10'
      if 'J' in letter:
        return 'J11'
    if 'k' or 'K' in letter:
      if 'k' in letter:
        return 'k20'
      if 'K' in letter:
        return 'K21'
    if 'l' or 'L' in letter:
      if 'l' in letter:
        return 'l30'
      if 'L' in letter:
        return 'L31'
    if 'm' or 'M' in letter:
      if 'm' in letter:
        return 'm40'
      if 'M' in letter:
        return 'M41'
    if 'n' or 'N' in letter:
      if 'n' in letter:
        return 'n50'
      if 'N' in letter:
        return 'N51'
    if 'o' or 'O' in letter:
      if 'o' in letter:
        return 'o60'
      if 'O' in letter:
        return 'O61'
    if 'p' or 'P' in letter:
      if 'p' in letter:
        return 'p70'
      if 'P' in letter:
        return 'P71'
    if 'q' or 'Q' in letter:
      if 'q' in letter:
        return 'q80'
      if 'Q' in letter:
        return 'Q81'
    if 'r' or 'R' in letter:
      if 'r' in letter:
        return 'r90'
      if 'R' in letter:
        return 'R91'  
    if 's' or 'S' in letter:
      if 's' in letter:
        return 's10'
      if 'S' in letter:
        return 'S11'
    if 't' or 'T' in letter:
      if 't' in letter:
        return 't20'
      if 'T' in letter:
        return 'T21'
    if 'u' or 'U' in letter:
      if 'u' in letter:
        return 'u30'
      if 'U' in letter:
        return 'U31'
    if 'v' or 'V' in letter:
      if 'v' in letter:
        return 'v40'
      if 'V' in letter:
        return 'V41'
    if 'w' or 'W' in letter:
      if 'w' in letter:
        return 'w50'
      if 'W' in letter:
        return 'W51'
    if 'x' or 'X' in letter:
      if 'x' in letter:
        return 'x60'
      if 'X' in letter:
        return 'X61'
    if 'y' or 'Y' in letter:
      if 'y' in letter:
        return 'y70'
      if 'Y' in letter:
        return 'Y71'
    if 'z' or 'Z' in letter:
      if 'z' in letter:
        return 'z80'
      if 'Z' in letter:
        return 'Z81'
    
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
    
    if '!' in letter:
      return ';'
    if '@' in letter:
      return '*'
    if '#' in letter:
      return ':-'
    if '$' in letter:
      return '::'
    if '%' in letter:
      return '&*'
    if '^' in letter:
      return '@-'
    if '&' in letter:
      return '!<'
    if '*' in letter:
      return '_-_'
    if '(' or ')' in letter:
      return '|'
    if '-' or '_' in letter:
      return '--'
    if '+' in letter:
      return '++'
    if '=' in letter:
      return '=?'


  def decode_file(file):
    if not os.path.exists(f'{encoded_Dir}/{file}'):
      print('ERROR: File not in encoded folder.')
      sys.exit(1)
    if os.path.getsize(file) == 0:
      print('ERROR: Given file is to small.')
      sys.exit(1)
    
    with open(file, 'r+') as File:
      file_name = os.path.basename(file).split('/')[-1]
      write_back = File.read()
      for line in write_back:

        for word in line.split(' '):
          word_list = list(word)
          
          for letter in word_list:
            if letter.isalpha():
              write_back = write_back.replace(str(letter), str(encode_decode.detick(letter)))

      with open(f'{tracked_Dir}/{file}', 'w') as Fout:
        print(f'Decoded {file_name} and created tracked file.')
        Fout.write(write_back)
        File.close()


  def encode_file(file):
    if not os.path.exists(f'{tracked_Dir}/{file}'):
      print('ERROR: File not tracked.')
      sys.exit(1)
    if os.path.getsize(file) == 0:
      print('ERROR: Given file is to small.')
      sys.exit(1)
    
    with open(file, 'r+') as File:
      file_name = os.path.basename(file).split('/')[-1]
      write_back = File.read()
      for line in write_back:

        for word in line.split(' '):
          word_list = list(word)
          
          for letter in word_list:
            if letter.isalpha():
              write_back = write_back.replace(str(letter), (encode_decode.tick(letter)))

      with open(f'{encoded_Dir}/{file}', 'w') as Fout:
        print(f'Encoded {file_name} and created encoded file.')
        Fout.write(write_back)
        File.close()


try:
  if sys.argv[1] == 'encode':
    encode_decode.encode_file(sys.argv[2])
    sys.exit(0)
  if sys.argv[1] == 'decode':
    encode_decode.decode_file(sys.argv[2])
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
  