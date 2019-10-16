"""
  Автор: Уклейкин Артем, группа №p42551
  Ссылка на сайт-портфолио: https://artemukl.github.io/firstrepo/
"""

import random

class SumOfTwo():
  def randNum():
    return random.randint(0, 79)

  def find_sum(data, targetSum):
    targetListOfIndexes = []
    i = 0
    while (i < len(data)-1):
      if data[i] + data[i+1] == targetSum:
        # print('\t fit!', data[i], '+', data[i+1], '\t[', i, ',', i+1, ']')
        coupleOfIndex = (i, i+1)
        targetListOfIndexes.append(coupleOfIndex)
      i += 2  
    if not targetListOfIndexes:
      return 'coupleOfIndex is not found'
    return targetListOfIndexes   


if __name__ == '__main__': 
  cortegePi = (4,2,3,2,8,6,3,5,1,2,7,9,2,3,4,5,6,3,2,8,6,9,1,2,2,3,4,5,6,7,8,0,9,2,3,5,7,1,6,1,5,2,4,1,3,5,2,7,5,0,8,1,3,2,1,8,8,5,2,9)
  randList = [5,3,2,1,4,8,7,6,5,4,2,1,8,9,7,6,5,2,1,6,9,0,2,1,2,5,8,9,1,2,6,0,7,6,8,5,4,3,5,3,2,1,2,3,7,8,9,0,2,1,3,4,5,7,8,2,2,3,1,9]

  """ Test #1 """
  targetSum = 9
  res1 = SumOfTwo.find_sum(cortegePi, targetSum)
  print('targetSum=',targetSum)
  print('res1',res1)
  assert res1 == [(4, 5), (21, 22), (54, 55), (62, 63)], 'test #1 passed'

  """ Test #2 """
  targetSum = 4
  res1 = SumOfTwo.find_sum(randList, targetSum)
  print('\ntargetSum=',targetSum)
  print('res1',res1)
  assert res1 == [(22, 23), (36, 37)], 'test #2 passed'

  """ Test #3 """
  targetSum = 32
  res1 = SumOfTwo.find_sum(cortegePi, targetSum)
  print('\ntargetSum=',targetSum)
  print('res1',res1)
  assert res1 == 'coupleOfIndex is not found', 'test #3 passed'

  """ Test #4 """
  targetSum = 9
  res1 = SumOfTwo.find_sum(cortegePi, targetSum)
  print('\ntargetSum=',targetSum)
  print('res1',res1)
  assert res1 == [(4, 5), (21, 22), (54, 55), (62, 63)], 'test #4 failed'
