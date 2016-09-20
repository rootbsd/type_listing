import json
import sys
from pprint import pprint

class MyType():
  def __init__(self, arch):
    self.arch = arch
    self.d = ""
    self.block_size = 0
    if self.arch == "x86":
      self.d = open('struct_x86.json').read()
      self.block_size = 4
    elif self.arch == "x64":
      self.d = open('struct_x64.json').read()
      self.block_size = 8
    else:
      print "Wrong arch..."  

  def get(self, word):
    js = json.loads(self.d)
    for entry in js:
      if word == entry.lower():
        return js[entry]
    return []
      
  def search(self, word):
    js = json.loads(self.d)
    l = []
    for entry in js:
      if word in entry.lower():
        l.append(entry)
    return l
    
  def display_hex(self, word, data):
    array = []
    for i in xrange(0, len(data), 2):
      array.append(data[i:i+2])
    a = self.get(word.lower())
    le = len(a)
    cpt = 0
    o = ""
    for i in a:
      if "+0x" in i[0]:
        if cpt == le-1:
          continue
        start = int(i[0].replace("+",""), 16)
        size = int(a[cpt+1][0].replace("+",""), 16)-start
        data = array[start:start+size]
        data = self.padding(data, self.block_size)
        result = []
        for item in self.chunks(data,self.block_size):
          result.append(''.join(item[0:self.block_size][::-1]))
        try:
          o = o + i[0]+" = "+(hex(int(''.join(result),16)))+ " ("+i[1]+" "+i[2]+")\n"
        except:
          o = o + i[0]+" = "+"0x00"+ " ("+i[1]+" "+i[2]+")\n"
      cpt = cpt  + 1
    return o
    
  def padding(self, l,block_size):
    pad = len(l) % block_size
    for i in range(0,pad):
      l.append('00')
    return l
    
  def chunks(self, l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
      yield l[i:i + n]
    
MT = MyType(sys.argv[2])
entries = MT.search(sys.argv[1].lower())
try:
  data = sys.argv[3]
except:
  data = ""
#data = "680002020000000000000000000000001082010000000000f013010000000000b014010000000000d014010000000000f014010000000000f014010000000000"

print "List:"
for entry in entries:
  print entry
print ""

a = MT.get(sys.argv[1].lower())
if len(a) != 0:
  print "Description of "+sys.argv[1]
  pprint(a)
  
  if data != "":
    print ""
    print MT.display_hex(sys.argv[1], data)
