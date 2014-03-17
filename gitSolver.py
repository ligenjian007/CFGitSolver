__author__ = 'ligenjian'

import os
import re

vcapFile = '/Users/ligenjian/Programs/vcap'

gemCache = 'http://10.32.105.117:9000'
gitCache = 'git://10.32.105.117'

gitMatcher = re.compile(r'(?P<gitUrl>(https?|git)://github\.com)')
gemsMatcher = re.compile(r'http://rubygems.org')

def gitSubber(matched):
    gitUrl = matched.group('gitUrl')
    return gitCache

def replaceUrls():

    for fileTuple in os.walk(vcapFile):
        if 'Gemfile' in fileTuple[2]:
            gemFile = open(fileTuple[0] + '/Gemfile')
            gemContent = ''.join(gemFile.readlines())
            gemFile.close()
            gemBackup = open(fileTuple[0] + '/Gemfile_backup','w')
            gemBackup.write(gemContent)
            for found in gitMatcher.finditer(gemContent):
                #print found.group(0),' in file ', fileTuple[0]
                pass
            for found in gemsMatcher.finditer(gemContent):
                #print found.group(0),' in file ', fileTuple[0]
                pass
            gemContent = gitMatcher.sub(gitCache, gemContent)
            gemContent = gemsMatcher.sub(gemCache, gemContent)
            gemFile = open(fileTuple[0] + '/Gemfile','w')
            gemFile.write(gemContent)

def revertChange():
    for fileTuple in os.walk('/Users/ligenjian/Programs/vcap'):
        if 'Gemfile' in fileTuple[2]:
            os.remove(fileTuple[0] + '/Gemfile')
            os.rename(fileTuple[0] + '/Gemfile_backup', fileTuple[0] + '/Gemfile')

if __name__ == '__main__':
    replaceUrls()