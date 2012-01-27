import tempfile
import commands
import os

PDFTK = "pdftk"

class cmd:
    """Commands for pdftk

    @author ykk
    @date Jan 2012
    """
    def update_info(self,filename, key, value, output):
        """Generate command to update meta data
        """
        mfile = self.tmp_meta_file(key,value)
        ret = commands.getoutput(PDFTK+" \""+filename+"\""+\
                                 " update_info "+mfile+\
                                 " output \""+output+"\"")
        os.remove(mfile)
        return ret

    def tmp_meta_file(self,key,value):
        filename = tempfile.mktemp()
        fileRef = open(filename, "w")
        fileRef.write("InfoKey: "+key+"\n")
        fileRef.write("InfoValue: "+value+"\n") 
        fileRef.close()

        return filename
