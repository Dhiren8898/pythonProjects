#matrix problem
import numpy as np

#matrix creation
a=[[2,2,2],[9,8,-1],[4,6,1]]
b=[[2,4,2],[2,8,-1],[4,5,0]]
result=[[0,0,0],[0,0,0],[0,0,0]]
#matrix addition
# for i in range(len(a)): #for row
#     for j in range(len(a[0])):  #for column
#         result[i][j]=a[i][j]+b[i][j]
# for r in result:
#     print(r)


#matrix  multiplication
# for i in range(len(a)): #row of first matrix
#     for j in range(len(b[0])): #column of second matrix
#         for k in range(len(b)):  #row of second matrix
#             result[i][j]+=a[i][k]*b[k][j]
# for r in result:
#     print(r)
# importing numpy as np

a=[[2,2,2],[9,8,-1],[4,6,1]]
b=[[2,4,2],[2,8,-1],[4,5,0]]
print(np.add(a,b))
print(np.dot(a,b))


