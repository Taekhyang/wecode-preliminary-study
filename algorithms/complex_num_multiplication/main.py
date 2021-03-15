def complex_number_multiply(a, b):
  fst = a.split('+')
  fst_real = complex(int(fst[0]))
  fst_img  = complex(fst[1].replace('i', 'j'))

  sec = b.split('+')
  sec_real = complex(int(sec[0]))
  sec_img  = complex(sec[1].replace('i', 'j'))

  fst_complex = complex(fst_real) + complex(fst_img)
  sec_complex = complex(sec_real) + complex(sec_img)

  multiplied = fst_complex * sec_complex
  multiplied_real = multiplied.real
  multiplied_img = multiplied.imag

  result = '{}+{}i'.format(int(multiplied_real), int(multiplied_img))

  return result

complex_number_multiply("1+-3i", "1+-2i")

# 파이썬에는 복소수 모듈 complex 가 있어서 복소수 끼리의 사칙연산이 가능하다.
# 먼저 문자열 split 으로 실수와 허수부분을 나눈다음 다시 complex 로 유효한 값을 만든다.
# 유효한 complex 끼리 곱한 뒤 계산된 값을 포매팅 한 뒤 리턴한다.
