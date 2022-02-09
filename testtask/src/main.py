import os

def generate_file(filename, filesize):
    command = 'head -c {0} < /dev/urandom > {1}'.format(filesize, filename)

    print('Generating new random file with:')
    print(command)

    os.system(command)

if __name__ == "__main__":
    generate_file('name', 128)