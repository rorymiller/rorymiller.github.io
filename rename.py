__author__ = 'rorymiller'

import os
import re


# duplicate folder
# Traverse folders
# add YAML infromation to each .md file
# add index to each folder
# add index to first page
# make web friendly file names


# YAML for individual pages

## need to remove all non digit from yaml
## can perhaps try to add back in links.

def YAML(name):
    line1 = "-" * 3 + "\n"
    line2 = "title: " + name
    line3 = 'layout: page \n'
    line4 = line1 + "\n"
    return line1 + line2 + line3 + line4

def YAMLi(name1):
    line1 = "-" * 3 + "\n"
    line2 = "title: " + name1 +'\n'
    line3 = 'layout: index' + '\n'
    line4 = 'content: \n'
    return line1+line2+line3+line4

# add YAML

def individual(rootdir):
    title = ""
    infile = ""
    outfile = ""

    for subdir, dirs, files in os.walk(rootdir):
        # open file

        for f in files:
            if ".md" in f and "_" not in f:
                infile = open(subdir + "/" + f, 'r')
                fl = f.lower()
                outfile = open(subdir + "/" + "a" + fl.replace(" ","_").replace('(',"_").replace(')',""), 'w') # can change subdir if needed

                # find title
                for line in infile:
                    if re.match("^[#]{1} [a-zA-Z]",line):
                        title = line
                        break
                title = title.replace('# ','').replace(":","")

                    #write YAML information to top of file
                outfile.write(YAML(title))

                    # copy rest of document into new file
                for line in infile:
                    outfile.write(line.replace("[","").replace("]","") + '\n') # try and take out any reference links as seems to be causing an error
                outfile.write("end")

                print('done' , fl)
                    # close files
                infile.close()
                outfile.close()
    print("finished YAML individual files")

def index(rootdir): # must match outfile directory
    ind = "index.md"

    for subdir, dirs, files in os.walk(rootdir):

        indexfile = open(subdir + '/' + ind,"w")
        title = subdir.split('/')[-1]

        indexfile.write(YAMLi(title))

        if dirs:
            for f in dirs:
               print(f)
               indexfile.write("    - " + f + " " + "\n" + "")


        if files:
            for file in files:
                if ".md" in file and "index" not in file and file.islower() and " " not in file and file[0] == "a":
                    indexfile.write("    - " + file.replace(".md","") + "\n")


        indexfile.write("-" * 3 + "\n") # close YAML
    print("done with index files")


individual("/Users/rorymiller/Dropbox/GP_exp/notes")
index("/Users/rorymiller/Dropbox/GP_exp/notes")


