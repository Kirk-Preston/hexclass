class hexbytes():
    def __init__(self,string):
        self.string = string
    def lilendian(self):
        bytestring = []
        for char in self.string:
            hexchar = char.encode("hex")
            hexesc = ('\\x')
            hexconcat = (hexesc+hexchar)
            bytestring.append(hexconcat)
        return(''.join(reversed(bytestring)))
    def bigendian(self):
        bytestring = []
        for char in self.string:
            hexchar = char.encode("hex")
            hexesc = ('\\x')
            hexconcat = (hexesc+hexchar)
            bytestring.append(hexconcat)
        return(''.join(bytestring))
'''   
tobytes = hexbytes("test")
print(tobytes.lilendian())
print(tobytes.bigendian())
'''
