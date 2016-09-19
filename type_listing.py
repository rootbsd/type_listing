import json
import sys
from pprint import pprint

class MyType():
  def __init__(self, arch):
    self.arch = arch
    self.d = ""
    if self.arch == "x86":
      self.d = open('struct_x86.json').read()
    elif self.arch == "x64":
      self.d = open('struct_x64.json').read()
    else:
      print "Wrong arch..."  

  def get(self, word):
    js = json.loads(self.d)
    for entry in js:
      if word == entry.lower():
        print entry
        return js[entry]
    return []
      
  def search(self, word):
    js = json.loads(self.d)
    l = []
    for entry in js:
      if word in entry.lower():
        l.append(entry)
    return l
    
MT = MyType(sys.argv[2])
entries = MT.search(sys.argv[1].lower())
print "List:"
for entry in entries:
  print entry
print ""
a = MT.get(sys.argv[1].lower())
if len(a) != 0:
  print "Description of "+sys.argv[1]
  pprint(a)