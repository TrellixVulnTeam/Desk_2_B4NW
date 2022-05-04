import json, json_tools

data = {"name":"Jack Ma", "sex" : "男", "年龄" : 26, "age":26}

# with open('data_1.json', 'w', encoding="utf-8") as fout:
#     json.dump(data, fout, indent=4, separators=(",", " : "), ensure_ascii=False,sort_keys=True)
#
# with open('data_2.json', 'w', encoding="utf-8") as fout:
#     json.dump(data, fout, indent=4, separators=(",", " : "), ensure_ascii=False,sort_keys=True)

#json_tools.diff(old,new)
with open("data_1.json", encoding="utf-8") as f:
    data_1=json.load(f)
with open('data_2.json', encoding="utf-8") as f:
    data_2=json.load(f)

with open('compare.json','w', encoding='utf-8') as f:
    json.dump(json_tools.diff(data_1, data_2),f, ensure_ascii=False, indent=4)