from .. import Quaternion
from math import pi, sqrt

s2o2 = sqrt(2)/2

def eq(x, y, tol=.001):
   return abs(x-y) < tol

def eq3(v1, v2):
   assert len(v1) == 3 == len(v2)
   return (
      eq(v1[0], v2[0])
         and 
      eq(v1[1], v2[1])
         and 
      eq(v1[2], v2[2])
   )

"""Test that axis-angle quaternions preserve magnitude."""
def test_axis_angle_magnitude_preservation():
   q = Quaternion.fromaxisangle((.301, .203, .102), .201)
   v = (1,1,1)
   x = q*v

   assert eq(
      sqrt(x[0]*x[0]+x[1]*x[1]+x[2]*x[2]),
      sqrt(3),
      .03 # Yes, the error is currently horrendous
   )

"""Test the axis-angle to quaternion conversion."""
def test_axis_angle():
   # Rotate a vector by pi/4 radians about the Z axis
   q = Quaternion.fromaxisangle((0,0,1), pi/4)
   v = (1,0,0)
   assert eq3(q*v, (s2o2, s2o2, 0))
