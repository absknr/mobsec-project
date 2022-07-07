import os
import subprocess

from os.path import join
from glob import glob

APKS_DIR = "./apks"
APPS_DIR = "./apps"

def disassemble(apks_path):
    apks = [apk for apk in os.listdir(apks_path) if apk.endswith(".apk")]

    for apk in apks:
        subprocess.run(
            ["apktool", "d", join(apks_path, apk), "-o", join("apps", apk[:-4]), "-f"]
        )


def main():
    disassemble(join(".", "apks"))

    apps_dirpath = [
        os.path.join(APPS_DIR, app_dirname)
        for app_dirname in next(os.walk(APPS_DIR))[1]
    ]

    for app_dirpath in apps_dirpath:
        for smali_filepath in glob(join(app_dirpath, "smali", "**", "*.smali")):
            print(smali_filepath)


if __name__ == "__main__":
    main()
