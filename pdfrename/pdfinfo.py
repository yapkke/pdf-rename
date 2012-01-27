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

    def filename(self, keys=["Author","Title"], musthave=["Title"],
                 filename = "", quoted=False):
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
