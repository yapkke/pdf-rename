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
    print "--mdate\n\tAppend filename with year in ModDate"
    print "--cdate\n\tAppend filename with year in CreationDate"
    
#Parse options and arguments
try:
    opts, args = getopt.getopt(sys.argv[1:], "h",
                               ["help","cdate","mdate"])
except getopt.GetoptError:
    print "Option error!"
    usage()
    sys.exit(2)
    
#Variables
PDFINFO = "pdfinfo"
MV = "mv"

#Parse options
for opt,arg in opts:
    if (opt in ("-h","--help")):
        usage()
        sys.exit(0)
    elif (opt in ("--mdate")):
        pass
    elif (opt in ("--cdate")):
        pass
    else:
        print "Unhandled option :"+opt
        sys.exit(2)

#Check number of arguments
if (len(args) < 1):
    print "Insufficient arguments!"
    usage()
    sys.exit(2)


filename =args[0]
pinfo = pdfinfo.pdfinfo(commands.getoutput(PDFINFO+" \""+filename+"\""))

year=None
for opt,arg in opts:
    if (opt in ("--mdate")):
        year=pinfo.content["ModDate"].split(" ")[-1]
    elif (opt in ("--cdate")):
        year=pinfo.content["CreationDate"].split(" ")[-1]

newfilename = pinfo.filename()
if (year != None):
    newfilename += ","+str(year).strip()

if ((newfilename != None) and (filename != newfilename)):
    print "Renaming \""+filename+"\" to\n\t\""+newfilename+"\"..."
    print commands.getoutput(MV+" \""+filename+"\" \""+newfilename+"\"")
