# Create FrozenSet
fs1 = frozenset([1,2,3,4])
fs2 = frozenset([4,5,6,7])
fs = fs1 & fs2
print(fs)

# what works and what does not
# works -> all read fumctions 
# does not work -> write function bcoz frozenstes are immutable
# 2D frozensets are possible

fs = frozenset([1,2,3,frozenset[4,5,6]])
print(fs)