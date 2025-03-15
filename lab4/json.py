import json

data = open('sample-file.json').read()
object = json.loads(data)

print("======================================================================================")
print(f"{'DN':<50} {'Description':<20} {'Speed':<10} {'MTU':<6}")
print("-------------------------------------------------- -------------------  -------  -----")

data = object.get("imdata", [])
#If "imdata" is missing, it returns an empty list ([]) instead of causing an error.

for i in data:     #Each i is a dictionary 
    l1_Phys_If = i.get('l1PhysIf', {}).get('attributes', {})
    dn = l1_Phys_If.get('dn', '')
    desc = l1_Phys_If.get('descr', '')
    speed = l1_Phys_If.get('speed', '')     #(inherit, auto, fixed)
    mtu = l1_Phys_If.get('mtu', '')         #(Maximum Transmission Unit)

    print(f"{dn:<50}{desc:<22}{speed:<10}{mtu:<6}")


# .get = Ensures missing values don’t break the program.
