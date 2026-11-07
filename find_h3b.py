import json, urllib.request
d=json.load(urllib.request.urlopen("http://localhost:8188/object_info"))
for k,n in d.items():
 dn=n.get("display_name") or ""
 blob=(k+" "+dn).lower()
 if "minimax" in blob and ("image to video" in blob or "i2v" in blob or "fl2va" in blob or "fl2v" in blob):
  print("KEY",k)
  print(" DISPLAY",dn)
  for f,v in n["input"].get("required",{}).items():
   t=v[0]; extra=v[1] if len(v)>1 else {}
   print(" REQ",f,("ENUM"+str(len(t))) if isinstance(t,list) else t,extra)
  for f,v in n["input"].get("optional",{}).items():
   print(" OPT",f,v[0])
  print(" OUT",n.get("output_name"))
