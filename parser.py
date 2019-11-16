#!/usr/bin/python3
import random
import sys
import re
import os

def expand(token):

    #basedir = "/home/mobaxterm/adatabletop/tables/lib/mazerats-"
    #basedir = "/home/mobaxterm/adatabletop/tables/lib/"
    basedir = sys.path[0] + "/lib/"
    tokensalt = token.strip('[').strip(']').lower().replace(" ", "-")

    testopen = basedir + tokensalt

    random.seed()

    with open(testopen, "r") as file:
        contents = file.readlines()
        token = contents[random.randrange(0, len(contents))].strip('\n')

    return token

def stitch(intext):
    intext = re.split(r'([\[\]])', intext)
    if intext[0] == "":
        del intext[0]

    while "]" in intext:
        # stitch together tokens here
        first = intext.index("[")
        
        second = intext.index("]")

        foo = intext[first:second+1]
        foo = ''.join(foo)

        del intext[first:second+1]

        intext.insert(first, foo)
        # end stitching

    return intext
    
def expandline(intextline):
    output = ""
    for j in range(0, len(intextline)):
        token = intextline[j]

        if "[" in token:
            token = expand(token)
        
        output = output + token

    if "[" in output:
        output = stitch(output)
        output = expandline(output)

    return output

def driver():
    readin = sys.stdin.readlines()

    output = ""
    for i in range(0, len(readin)):
        readinline = stitch(readin[i])
        output += expandline(readinline)
    
    print(output)

if __name__ == "__main__":
#    print(sys.path[0])
    driver()
