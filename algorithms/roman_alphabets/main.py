def roman_to_num(s):
  # 여기에 코드를 작성해주세요.
    romans = dict(I=1,
                  V=5,
                  X=10,
                  L=50,
                  C=100,
                  D=500,
                  M=1000)

    roman_alphabets = [i for i in s]
    
    sum = 0
    length = len(roman_alphabets)

    for i in range(length):
      if i == length - 1:
        sum += romans[roman_alphabets[i]]
        return sum

      roman_before = romans[roman_alphabets[i]]
      roman_after = romans[roman_alphabets[i+1]]

      if roman_before >= roman_after:
        sum += roman_before
      else:
        sum -= roman_before
