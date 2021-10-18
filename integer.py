""" 

Student: Hanna Sjöstrand
Mail: hannaa.sjostrand@hotmail.com
Reviewed by: Elias Estensen
Date reviewed: 18/10-2021
"""

""" Phyton interface to the C++ Integer class """
import ctypes
lib = ctypes.cdll.LoadLibrary('./libinteger.so')

class Integer(object):
	def __init__(self, val):
		lib.Integer_new.argtypes = [ctypes.c_int]
		lib.Integer_new.restype = ctypes.c_void_p
		lib.Integer_get.argtypes =[ctypes.c_void_p]
		lib.Integer_get.restype = ctypes.c_int
		lib.Integer_set.argtypes = [ctypes.c_void_p, ctypes.c_int]
		lib.Integer_delete.argtypes = [ctypes.c_void_p]
		lib.Integer_fib.argtypes = [ctypes.c_void_p]
		lib.Integer_fib.restypes = ctypes.c_int
		self.obj = lib.Integer_new(val)

	def get(self):
		return lib.Integer_get(self.obj)

	def set(self, val):
		lib.Integer_set(self.obj, val)

	def __del__(self):
		return lib.Integer_delete(self.obj)

	def fib(self):
		return lib.Integer_fib(self.obj)
