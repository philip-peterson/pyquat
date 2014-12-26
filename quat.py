from math import sqrt

class Quaternion(object):

   def __init__(self, w, x, y, z):
      try:
         w = float(w)
         x = float(x)
         y = float(y)
         z = float(z)
      except TypeError:
         raise TypeError('Quaternion() arguments must be real numbers')
      self.w = w
      self.x = x
      self.y = y
      self.z = z
   
   def conjugate(self):
      return Quaternion(
         self.w,
         -self.x,
         -self.y,
         -self.z,
      )

   def __abs__(self):
      return sqrt(
         self.w * self.w,
         self.x * self.x,
         self.y * self.y,
         self.z * self.z
      )

   def __sub__(self, other):
      return self + other*-1

   def __add__(self, other):
      t = type(other)
      if t == Quaternion:
         return Quaternion(*[self[i]*other[i] for i in range(4)])
      elif t in (float, int, complex):
         other = complex(other)
         return Quaternion(real(other), imag(other), 0, 0) + self
      else:
         raise TypeError('Quaternions cannot be added to or subtracted from anything except complex numbers (including scalars) and other quaternions')
            
   def __repr__(self):
      return str(self)

   def __str__(self):
      return ("%g+%gi+%gj+%gk" % tuple(self)).replace('+-', '-')

   def __bool__(self):
      return abs(self) != 0

   def __gt__(self, other):
      raise TypeError('no ordering relation is defined for quaternions')

   def __gte__(self, other):
      return self.__gt__(other)

   def __lt__(self, other):
      return self.__gt__(other)

   def __lte__(self, other):
      return self.__gt__(other)

   def __getitem__(self, index):
      return (self.w, self.x, self.y, self.z)[index]

   def __iter__(self):
      yield self.w
      yield self.x
      yield self.y
      yield self.z

   def rank(self):
      return len([c for c in self if c != 0])

   def __mul__(self, other):
      t = type(other)
      print t
      if t == Quaternion:
         # quaternion * quaternion
         # Note: this is just the distributive law, taking
         # into account the following properties of hypercomplex numbers:
         #  ii = jj = kk = -1
         #  ij = k = -ji
         #  jk = i = -kj
         #  ki = j = -ik
         return Quaternion(
            self.w*other.w - self.x*other.x - self.y*other.y - self.z*other.z
            , self.w*other.x + self.x*other.w + self.y*other.z - self.z*other.y
            , self.w*other.y - self.x*other.z + self.y*other.w + self.z*other.x
            , self.w*other.z + self.x*other.y - self.y*other.x + self.z*other.w
         )
      elif t in (float, complex):
         # quaternion * scalar
         return Quaternion(*[comp*other for comp in self])
      elif t in (tuple, list) and len(other) == 3:
         # quaternion * vector
         equivalent_q = Quaternion(0, *other)
         return self * equivalent_q * self.conjugate()
      else:
         raise TypeError('Quaternions cannot be multiplied by anything except real numbers and other quaternions')

Quaternion.i = Quaternion(0,1,0,0)
Quaternion.j = Quaternion(0,0,1,0)
Quaternion.k = Quaternion(0,0,0,1)
