import os
import json
from collections import OrderedDict

source_path = "wavout/"
target_data = OrderedDict()
target_arr = sorted([int(filename.replace(".wav", "")) for filename in os.listdir(source_path)])

for filename in target_arr:
    target_data[source_path + str(filename) + ".wav"] = ""

print(json.dumps(target_data, ensure_ascii=False, indent="\t"))

with open('script.json', 'w', encoding ="utf-8") as make_file:
    json.dump(target_data, make_file, ensure_ascii=False, indent="\t")