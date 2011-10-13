#!/usr/bin/env python
import commands
import sys
import getopt

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

class pdfinfo:
    """Class to hold information about PDF file
    """
    def __init__(self, info, parse=True):
        self.content = {}
        self.sanitization = { "/":"|",
                              "\"":"",
                              "'":"",
                              "`":""}
        
        if (parse):
            self.parse(info)

    def parse(self, info):
        #Parse result of pdfinfo
        lines = info.split("\n")
        for line in lines:
            items = line.split(":")
            if (len(items) >= 2):
                self.content[items[0].strip()] = items[1].strip()

    def filename(self, keys=["Author","Title"], musthave=["Title"], filename = "", quoted=False):
        #Check musthave information
        for k in musthave:
            if (k not in self.content):
                return None
            if (self.content[k] == ""):
                return None

        #Construct filename
        for k in keys:
            filename = self.__add_to_filename(filename, k)
            filename += ", "
        filename = filename[:-2]+".pdf"

        #Sanitize filename
        for k,v in self.sanitization.items():
            filename = filename.replace(k, v)

        if (quoted):
            filename = "\""+filename+"\""

        return filename
            
    def __add_to_filename(self, filename, key):
        try:
            if (self.content[key] != ""):
                filename += self.content[key]
        except KeyError:
            pass

        return filename

    def __str__(self):
        return str(self.content)

pinfo = pdfinfo(commands.getoutput(PDFINFO+" \""+filename+"\""))
newfilename = pinfo.filename()
if ((newfilename != None) and (filename != newfilename)):
    print "Renaming \""+filename+"\" to\n\t\""+newfilename+"\"..."
    print commands.getoutput(MV+" \""+filename+"\" \""+newfilename+"\"")
