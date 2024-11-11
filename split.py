filename = 'xp.img'

ext = filename.split('.')[-1]
no_ext = filename[:-len(ext) - 1]

opened = open(filename, 'rb')

readf = opened.read()

file_length = len(readf)

step = 204800
i = 0

while i < file_length - step:
    temp_file = open(f'xp/{no_ext}-{i}-{i + step}.{ext}', 'wb')
    temp_file.write(readf[i:i + step])
    temp_file.close()
    i += step


temp_file = open(f'xp/{no_ext}-{i}-{file_length}.{ext}', 'wb')
temp_file.write(readf[i:i + file_length])
temp_file.close()

opened.close()
