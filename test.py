from __future__ import print_function
import os

print('\n'.join(
    '{}: {}'.format(k, v)
    for k, v in os.environ.items()
))

assert '42' == os.environ['SECRET']"
