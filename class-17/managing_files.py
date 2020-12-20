from pathlib import Path

# Current dir
cwd = Path.cwd()
print(f'current working dir is \'{cwd}\'')

# create full path name by joining path and filename
file = Path(Path.joinpath(cwd, 'new_file.txt'))
print(f'Full path: \'{file}\'')
print(f'Does file exists? \'{file.exists()}\'')
print(f'file name: {file.name}')
print(f'file suffix: {file.suffix}')
print(f'file folder: {file.parent.name}')
print(f'file size: {file.stat().st_size}')

parent = cwd.parent
print(f'is this a dir? {parent.is_dir()}')
print(f'is this a file? {parent.is_file()}')

# list child directories
def list_dir(folder):
  for child in folder.iterdir():
    if child.is_dir():
      print(child)
list_dir(parent)

# Stream modes
# r - Read (default)
# w - Truncate and write
# a - Append if file exists
# x - Write, fail if file exists
# + - Updating (read/write)
# t - Text (default)
# b - Binary

# read file
stream = open('./new_file.txt', 'rt')
print(f'is this readable? {stream.readable()}')
print(f'read one character: {stream.read(1)}')
stream.seek(0)
print(f'read to end of line: {stream.readline()}')
stream.seek(0)
print(f'read all lines to end of file: {stream.readlines()}')
stream.seek(0)
stream.close()

# write to file
stream = open('./output.txt', 'wt')
print(f'\nis this file writable? {stream.writable()}')
stream.write('H')
stream.writelines(['ello', ' ', 'world'])
stream.write('\n')
names = ['rafael', 'ferreira']
stream.writelines(names)
stream.writelines('\n'.join(names))
stream.close()

# append to file
stream = open('./manage.txt', 'at')
stream.write('demo!')
stream.seek(0)
stream.write('cool')
stream.close()

try:
  s = open('./file.txt', 'wt')
  s.write('lorem ipsum')
finally:
  s.close()

# 'with' command closes the file after it was modified or if fails to open
# obs: does the same thing as 'try/finally'
with open('./file.txt', 'wt') as stream:
  stream.write('bla')