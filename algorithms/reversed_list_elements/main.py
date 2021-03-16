def reverse_string(s):
  for i in s[:]:
    s.pop()
    s.insert(0, i)
  return s

reverse_string(["h","e","l","l","o"])

# reversed 함수를 써서 바로 return 할 수도 있지만
# 안전하게 원래 list 인덱스에 영향을 주지 않도록 shallow copy 된 list 를 for 문을 돌았다.
# 맨 뒤에 요소를 pop 으로 없애고 다시 맨 앞으로 insert 해주었다.