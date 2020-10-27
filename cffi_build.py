from cffi import FFI
ffibuilder = FFI()

ffibuilder.cdef("""

struct us_lnk_lst {
  char *data;
  struct us_lnk_lst *previous;
};

extern int unishox1_compress(const char *in, int len, char *out, struct us_lnk_lst *prev_lines);
extern int unishox1_decompress(const char *in, int len, char *out, struct us_lnk_lst *prev_lines);

""")

ffibuilder.set_source(
    '_unishox_cffi',
    '#include "unishox1.h"',
    sources=['Unishox/unishox1.c'],
    include_dirs=['Unishox/'],
)

ffibuilder.compile(verbose=True)
