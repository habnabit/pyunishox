from _unishox_cffi import ffi, lib

MAXALLOC = 1024


def compress(in_):
    out = bytearray(len(in_))
    N = lib.unishox1_compress(in_, len(in_), ffi.from_buffer(out), ffi.NULL)
    del out[N:]
    return out

def decompress(in_):
    out = bytearray(MAXALLOC)
    N = lib.unishox1_decompress(
        ffi.from_buffer(in_), len(in_),
        ffi.from_buffer(out), ffi.NULL)
    del out[N:]
    return out
