"""Build a Python script for the FreeMind to novelWriter converter.
        
Copyright (c) 2023 Peter Triesberger
For further information see https://github.com/peter88213/md2nw
Published under the MIT License (https://opensource.org/licenses/mit-license.php)
"""
import inliner

VERSION = '0.1.2'

SRC = '../src/'
BUILD = '../'
SOURCE_FILE = f'{SRC}md2nw_.py'
TARGET_FILE = f'{BUILD}md2nw.py'


def main():
    inliner.run(SOURCE_FILE, TARGET_FILE, 'md2nwlib', '../src/')
    inliner.run(TARGET_FILE, TARGET_FILE, 'yw2nwlib', '../src/')
    inliner.run(TARGET_FILE, TARGET_FILE, 'pywriter', '../src/')
    # inliner.run(TARGET_FILE, TARGET_FILE, 'pywriter', '../../PyWriter/src/', copyPyWriter=True)
    with open(TARGET_FILE, 'r', encoding='utf-8') as f:
        script = f.read()
    with open(TARGET_FILE, 'w', encoding='utf-8', newline='\n') as f:
        f.write(script.replace('@release', VERSION))
    print('Done.')


if __name__ == '__main__':
    main()
