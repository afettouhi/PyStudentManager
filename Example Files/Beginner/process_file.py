import os

p = '/path/to/datafile.dat'

# if os.path.exists(p):
#    process_file(p)
# else:
#    print('No such file as {}'.format(p))

try:
    process_file(f)
except OSError as e:
    print('Could not process file because {}'.format(str(e)))
