'''
root@kali:~/Documents# pydoc3 base64
Help on module base64:

NAME
    base64 - Base16, Base32, Base64 (RFC 3548), Base85 and Ascii85 data encodings

MODULE REFERENCE
    https://docs.python.org/3.7/library/base64
    
    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.
'''

import base64

a="Nm@rmLsBy{Nm5u-K{iZKPgPMzS2I*lPc%_SMOjQ#O;uV{MM*?PPFhk|Hd;hVPFhq{HaAH<"
b=base64.b85decode(a)
print(base64.b32decode(b))
