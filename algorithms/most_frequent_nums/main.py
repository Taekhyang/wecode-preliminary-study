def top_k(nums, k):
  num_frequency = dict()
  for n in nums:
    num_frequency.setdefault(n, 0)
    num_frequency[n] += 1
  
  sorted_nums_by_val = sorted(num_frequency.items(), key= lambda x: -x[1])

  result = list()
  for i in range(k):
    result.append(sorted_nums_by_val[i][0])

  return result
