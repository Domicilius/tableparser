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

def mathexpand(token):
    # assumption: token is of form {xdy+z}

    # get rid of the {
    token = token.strip("{").lower().strip("\n")
    token = token.strip(" ")
    token = token.strip("}")

    z = 0
    if "+" in token:
        token = token.split('+')
        z = token[1]
    elif "-" in token:
        token = token.split('-')
        z = token[1]
    bar = token[0].split("d")
    x = bar[0]
    y = bar[1]
    output = 0
    for i in range(0, int(x)):
        output += random.randrange(1, int(y)+1)

    return str(output+(int(z))) + " "

def stitch(intext):
    # pretty sure this function turns everything between two [] into one token
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
    # this function recursively fills in the contents of a line, expanding all [] to 
    # table entries
    output = ""
    for j in range(0, len(intextline)):
        token = intextline[j]

        if "[" in token:
            token = expand(token)

        if "{" in token:
            token = mathexpand(token)
        
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
