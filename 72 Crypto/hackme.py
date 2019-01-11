import string
def rot25(s):
    return s.translate(string.maketrans(string.uppercase + string.lowercase,
        string.uppercase[1:] + string.uppercase[:1] +
        string.lowercase[1:] + string.lowercase[:1]))
a ="EKZF{Hs'r snnn dzrx, itrs bzdrzq bhogdq}"
print rot25(a)



