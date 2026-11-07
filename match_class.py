import json, urllib.request
d=json.load(urllib.request.urlopen("http://localhost:8188/object_info"))
need={"first_frame","unet_name","lora_name","vae_name_1","noise_seed"}
for k,n in d.items():
 fields=set(n["input"].get("required",{}).keys())|set(n["input"].get("optional",{}).keys())
 if need.issubset(fields):
  print("KEY",k,"DISPLAY",n.get("display_name"))
  print(" FIELDS",sorted(fields))
  print(" OUT",n.get("output_name"))
