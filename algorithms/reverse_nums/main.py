def reverse(number):
  if number == 0:
    return 0
  if number > 0:
    result = reverse_num(number)
  else:
    result = -(reverse_num(number))
  return result


def reverse_num(number):
  reversed_num = (str(abs(number)))[::-1]
  for num in reversed_num[:]:
    if num == 0:
      reversed_num.pop(0)
  return int(reversed_num)
