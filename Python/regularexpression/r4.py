
import json

student = [
            {'name': '鸡小萌', 'age': 18, 'flag': False},
            {'name': '兔八哥', 'age': 18, 'flag': True}
          ]


# 序列化
json_str = json.dumps(student)

print(type(json_str))
print(json_str)
