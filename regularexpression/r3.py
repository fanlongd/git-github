
import json

json_str = '{"name":"鸡小萌", "age":18, "flag":false}'

# 反序列化
student = json.loads(json_str)
print(type(student))
print(student)
print(student['name'])
print(student['age'])