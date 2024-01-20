# Syntax: "python addexpex.py <input> <output>

# This function takes an <input> text file with multiple glosses. Each gloss
# shall be broken up into blocks, divided into two or three lines, with the
# first line being the \gla line, the second being the \glb line, and the third
# being an optional \glft line. Each block is seperated by two newlines. 

# This function will parse the file, and adorn all the glosses formatted as
# above with the necessary syntax to run as an expex gloss. 

import sys

text = ''
glosses = []
newglosses = []

with open(sys.argv[1], encoding='utf8') as file:
  for line in file:
    text += line

glosses = text.split('\n\n')

for gloss in glosses:
  gloss = gloss.splitlines()
  gloss[0] = '''
\ex
\\begingl
\\gla ''' + gloss[0] + '//'
  
  gloss[1] = '\\glb ' + gloss[1] + '//'
  try:
     glft = '\n' + '\\glft ' + gloss[2] + '//'
  except:
     glft = ''
     
  tempgloss = gloss[0] + '\n' + gloss[1] + glft + '''
\\endgl
\\xe'''
  newglosses.append(tempgloss)

with open(sys.argv[2], 'w+', encoding='utf8') as out:
  tempfile = ''
  for gloss in newglosses:
    tempfile += gloss + '\n'
  out.write(tempfile)
print("Done")