import json

# load file json ke dict
data = json.loads(open("data.json").read())

list_data = []

for i in data:
    name = i["name"]
    dart = i["dart"]
    list_data.append(f'"{name}": {dart}')
    print("list_data: ", list_data)

datas = ",\n".join(list_data)
print("datas: ", datas)
print("list_data: ", list_data)

with open("main.dart", "w") as f:
    f.write(
        f"""import 'package:flutter_lucide/flutter_lucide.dart';

// made with python script

Map<String, IconData> lucidMap = {{
    {datas}
}};
"""
    )
