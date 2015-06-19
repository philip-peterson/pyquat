Pyternion
=========

[![Build Status](https://travis-ci.org/philip-peterson/pyternion.svg?branch=master)](https://travis-ci.org/philip-peterson/pyternion)

Introduction
------------

A quaternion is, informally, a group of four numbers. Each represents the magnitude of a vector in "hypercomplex" space.
Just imagine that instead of one imaginary number (i), there are three (i, j, and k), each of which when squared equals -1.

So one component of a quaternion represents the quaternion's "real" component, and the other three represent its components in the
i, j, and k directions.

Quaternions are used a lot in 3D applications (to represent rotations), as well as hardcore math areas. This library attempts
to be more of a piece of code that you'd read to understand the math of Quaternions, rather than something super performant. So,
it tries to be very Pythonic, sometimes perhaps at the expense of speed.

Usage
-----
You can construct a quaternion like so:

```
>>> from pyternion import Quaternion
>>> q = Quaternion(3,3,2,5)
>>> q
3+3i+2j+5k
```

Addition and subtraction are handled in the usual way
```
>>> q
3+3i+2j+5k
>>> q-q
0+0i+0j+0k
>>> q+q
6+6i+4j+10k
```

More to come later about multiplication, particularly between two quaternions.

Running tests
-----------
You'll need `nose` (`pip install nose`), but after that, simply run:

```
nosetests
```
