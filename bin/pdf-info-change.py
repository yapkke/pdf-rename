#!/usr/bin/env python
import commands
import sys
import subprocess
import getopt
import tempfile
import pdfrename.pdftk as pdftk

#Print usage guide
def usage():
    """Display usage
    """
    print "Usage "+sys.argv[0]+" <current filename> <key> <value>"
    print "\tScript to update PDF meta-information"
    print  "Options:"
    print "-h/--help\n\tPrint this usage guide"

#Parse options and arguments
try:
    opts, args = getopt.getopt(sys.argv[1:], "h",
                               ["help"])
except getopt.GetoptError:
    print "Option error!"
    usage()
    sys.exit(2)
    
#Variables
MV = "mv"
filename =args[0]
key = args[1]
value = args[2]
outfile = tempfile.mktemp()

#Parse options
for opt,arg in opts:
    if (opt in ("-h","--help")):
        usage()
        sys.exit(0)
    else:
        print "Unhandled option :"+opt
        sys.exit(2)

pdftk_cmd = pdftk.cmd()
print pdftk_cmd.update_info(filename, key, value, outfile)
print commands.getoutput(MV+" \""+outfile+"\" \""+filename+"\"")

