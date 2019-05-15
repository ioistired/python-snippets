import ctypes
import ctypes.util

libc = ctypes.CDLL(ctypes.util.find_library('c'))

malloc = libc.malloc
malloc.argtypes = [ctypes.c_size_t]
malloc.restype = ctypes.c_void_p

calloc = libc.calloc
# n, size
calloc.argtypes = [ctypes.c_size_t, ctypes.c_size_t]
calloc.restype = ctypes.c_void_p

free = libc.free
free.argtypes = [ctypes.c_void_p]
free.restype = None  # void
