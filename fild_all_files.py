# -*- coding: utf-8 -*-

import os

# 指定されたディレクトリ配下のファイルを列挙する
def fild_all_files(directory):
  for root, dirs, files in os.walk(directory):
    #yield root
    for file in files:
    yield os.path.join(root, file)
    
def main():
  for filename in fild_all_files("C:/windows"):
    print(filename)
    
if __name__ == '__main__': main()
