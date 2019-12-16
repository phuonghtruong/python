#!/usr/bin/env python3
import os
import stat
import subprocess
import shutil
from os import path

working_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(working_dir)
print(working_dir)

folderName = 'cproject'
url_clone = 'https://github.com/phuonghtruong/cproject.git'


def del_rw(action, name, exc):
    os.chmod(name, stat.S_IWRITE)
    os.remove(name)


def clone_repo():
    cmd = 'git clone ' + url_clone
    pipe = subprocess.Popen(cmd, shell=True)
    pipe.wait()


def is_dir_existed(folder):
    return True if os.path.exists(folder) else False


def is_git_valid(folder: str) -> bool:
    git_head_file = '/.git/HEAD'
    git_ref_folder = '/.git/refs/'
    git_obj_folder = '/.git/objects/'

    is_head_existed = os.path.exists(folder + git_head_file)  # check head file existence
    is_obj_existed = os.path.exists(folder + git_obj_folder)  # check object folder => give up
    is_ref_existed = os.path.exists(folder + git_ref_folder)  # check ref folder => contains all branch, tags
    return True if (is_head_existed & is_obj_existed & is_ref_existed) else False


def is_git_aborted(folder: str) -> bool:
    git_index_file = '/.git/index'
    return False if os.path.exists(folder + git_index_file) else True


def is_git_dirty(folder: str) -> bool:
    output = subprocess.check_output(["git", "status", "-uno", "--porcelain"], cwd=folder)
    print("status output: " + output)
    return output.strip() != b""


if __name__ == '__main__':
    if is_dir_existed(folderName):
        if is_git_valid(folderName):
            print(folderName + " is a valid git")
        else:
            print(folderName + " is NOT a valid git")
            print("Delete " + folderName)
            shutil.rmtree(folderName, onerror=del_rw)
            print("Start clone " + folderName)
            clone_repo()
    else:
        print("Start clone " + folderName)
        clone_repo()
