import re
from fractions import Fraction


s = input()
fracs = [_[0] for _ in re.findall(r"(\d+(\.\d*)?|\.\d+)|\d+/\d+", s)]
s = re.sub(r"(\d+(\.\d*)?|\.\d+)|\d+/\d+", "{}", s)
print(eval(s.format(*[repr(Fraction(frac)) for frac in fracs])))
