import os, glob
from PIL import Image
TARGET="1100100001111000011100110101100100101110001101110010010110010010"
def dhash(path, size=8):
 img=Image.open(path).convert("L").resize((size+1,size))
 px=list(img.getdata()); bits=[]
 for r in range(size):
  row=px[r*(size+1):(r+1)*(size+1)]
  for c in range(size): bits.append("1" if row[c]>row[c+1] else "0")
 return "".join(bits)
def ham(a,b): return sum(x!=y for x,y in zip(a,b))
dirs=["/mnt/workspace/ComfyUI/input/wangfu_input","/mnt/workspace/wangfu/input"]
res=[]
for d in dirs:
 for p in glob.glob(d+"/*.png"):
  try:
   h=dhash(p); res.append((ham(h,TARGET),os.path.basename(p),d,h==TARGET))
  except Exception as e:
   print("ERR",p,e)
res.sort()
for dist,name,d,exact in res[:10]:
 print("DIST",dist,"EXACT" if exact else "",name,d)
print("TOTAL",len(res))
