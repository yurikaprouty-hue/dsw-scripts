import json, urllib.request
d=json.load(urllib.request.urlopen("http://localhost:8188/object_info"))
for k,n in d.items():
 dn=n.get("display_name","")
 if "minimax" in (k+dn).lower() and ("image to video" in dn.lower() or "i2v" in k.lower() or "image to video" in k.lower()):
  print("KEY",k)
  print(" DISPLAY",dn)
  req=n["input"].get("required",{})
  opt=n["input"].get("optional",{})
  for f,v in req.items():
   t=v[0]
   extra=v[1] if len(v)>1 else {}
   print(" REQ",f,t,extra if not isinstance(t,list) else ("ENUM",len(t)))
  for f,v in opt.items():
   print(" OPT",f,v[0])
  print(" OUT",n.get("output"),n.get("output_name"))
