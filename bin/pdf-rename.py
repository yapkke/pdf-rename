#!/usr/bin/env python
import commands
import sys
import getopt
import pdfrename.pdfinfo as pdfinfo

#Print usage guide
def usage():
    """Display usage
    """
    print "Usage "+sys.argv[0]+" [options] <current filename>"
    print "\tScript to rename PDF using meta-information (if any)"
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
PDFINFO = "pdfinfo"
MV = "mv"
filename =args[0]

#Parse options
for opt,arg in opts:
    if (opt in ("-h","--help")):
        usage()
        sys.exit(0)
    else:
        print "Unhandled option :"+opt
        sys.exit(2)

pinfo = pdfinfo.pdfinfo(commands.getoutput(PDFINFO+" \""+filename+"\""))
newfilename = pinfo.filename()
if ((newfilename != None) and (filename != newfilename)):
    print "Renaming \""+filename+"\" to\n\t\""+newfilename+"\"..."
    print commands.getoutput(MV+" \""+filename+"\" \""+newfilename+"\"")
