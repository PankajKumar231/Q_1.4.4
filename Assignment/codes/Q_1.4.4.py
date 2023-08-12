import numpy as np
A = np.array([1, -1])
B = np.array([-4, 6])
C = np.array([-3, -5])

#O is perpendicular bisector of AB and AC
O = np.array([-53/12, 5/12])

#to find OA, OB and OC
OA = int(np.linalg.norm(A-O))
OB = int(np.linalg.norm(B-O))
OC = int(np.linalg.norm(C-O))

#Verification part
if (OA == OB == OC):
  print("OA = OB = OC")
  print("Hence verified")
else:
  print("wrong")
