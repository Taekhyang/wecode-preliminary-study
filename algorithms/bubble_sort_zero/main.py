def move_zeroes(nums):
  for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
      if nums[i] == 0:
        if nums[j] != 0:
          nums[i], nums[j] = nums[j], nums[i]
  return nums
move_zeroes([0,1,0,3,12])

## 0 1, 0 2, 0 3 이런식으로 인덱스 3 4 까지 비교 

## 시간복잡도 O(n) 모범답안
## 이해 완벽히 못함
def move_zeroes(nums):
    i = 0
    for j in range(len(nums)):
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1

move_zeroes([0,1,0,3,12])
