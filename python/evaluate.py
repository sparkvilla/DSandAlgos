from mytimer import Timer
from bigO.has_duplicate_value import has_dupl_val1, has_dupl_val2

t = Timer()

t.start()
has_dupl_val1(range(10000))
t.stop()

print('')

t.start()
has_dupl_val2(range(10000))
t.stop()


