import os


def space_occupied(path='C:\\Users\szere\OneDrive'):
    size = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for x in filenames:
            xy = os.path.join(dirpath, x)
            size = size + os.path.getsize(xy)

    return size


print('Total space occupied by this directory is: ', space_occupied(), 'bytes')
