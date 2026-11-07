import json, urllib.request
d=json.load(urllib.request.urlopen("http://localhost:8188/object_info"))
names=list(d.keys())
for k in names:
 kl=k.lower()
 if "minimax" in kl or "h3" in kl or "videotile" in kl or "imagetovideo" in kl:
  print(k)
print("TOTAL_NODES",len(names))
