L = [[1,2,3,4],
     [4,1,2,3],
     [3,4,1,2],
     [2,3,4,1]]

L2 = [1,2,3,4,
     4,1,2,3,
     3,4,2,2,
     2,3,4,1]

for i in range(4):
     lst = []
     n = i
     for row in L:
          if n > 0:
               lst.append(row[n])
               n = 1
     print(lst)