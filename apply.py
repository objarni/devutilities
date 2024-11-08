import os
import re

path = "src"


def file_matcher(filename):
    # TODO: implement
    if file.endswith(".test.tsx"):
        return False
    if file.endswith(".tsx"):
        return True
    return False


def change(content):
    return content  # TODO: implement


def run():
    for root, dirs, files in os.walk(path):
        for file in files:
            if not file_matcher(file):
                continue
            f = open(os.path.join(root, file), 'r')
            file_contents = f.read()
            f.close()
            modified = change(file_contents)
            if modified != file_contents:
                with open(os.path.join(root, file), 'w') as f:
                    f.write(modified)

run()
