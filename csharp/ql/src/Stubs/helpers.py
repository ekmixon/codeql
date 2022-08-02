import sys
import os
import subprocess


def run_cmd(cmd, msg="Failed to run command"):
    print('Running ' + ' '.join(cmd))
    if subprocess.check_call(cmd):
        print(msg)
        exit(1)


def get_argv(index, default):
    return sys.argv[index] if len(sys.argv) > index else default


def trim_output_file(file):
    # Remove the leading and trailing bytes from the file
    length = os.stat(file).st_size
    if length < 20:
        contents = b''
    else:
        f = open(file, "rb")
        try:
            pre = f.read(2)
            print("Start characters in file skipped.", pre)
            contents = f.read(length - 5)
            post = f.read(3)
            print("End characters in file skipped.", post)
        finally:
            f.close()

    with open(file, "wb") as f:
        f.write(contents)


# remove all files with extension
def remove_files(path, ext):
    for file in os.listdir(path):
        if file.endswith(ext):
            os.remove(os.path.join(path, file))
