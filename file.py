import subprocess
import sys

def openFile(filename):

    subprocess.run(['start', filename], shell=True)  # 在Windows上