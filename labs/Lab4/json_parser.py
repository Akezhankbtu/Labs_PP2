import json
import os#это помогает избежать ошибок при открытии JSON.


current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "sample-data.json")

with open(file_path, "r") as file:
    data = json.load(file)#лежит содержимое JSON в виде словаря Python.

interfaces = data.get("imdata", [])

print("Interface Status")
print("=" * 84)
print(f"{'DN':50} {'Description':20} {'Speed':7} {'MTU':7}")
print("-" * 84)

for item in interfaces:
    attr = item["l1PhysIf"]["attributes"]
    dn = attr.get("dn", "")
    descr = attr.get("descr", "")
    speed = attr.get("speed", "inherit")
    mtu = attr.get("mtu", "")

    print(f"{dn:50} {descr:20} {speed:7} {mtu:7}")
