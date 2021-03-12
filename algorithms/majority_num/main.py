def more_than_half(nums):
    # 아래 코드를 입력해주세요.
    nums_dict = dict()

    for n in nums:
      nums_dict.setdefault(n, 0)
      nums_dict[n] += 1

    for k, v in nums_dict.items():
      if v > len(nums) / 2:
        return k
