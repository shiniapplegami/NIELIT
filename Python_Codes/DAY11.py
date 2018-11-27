import xml.sax

class ourhandler(xml.sax.ContentHandler):
    def __init__(self):
        self.title=""
        self.author=""
        self.year=""
        self.price=""
        self.cat=""
        self.currtag=""
        self.string = "The book"

    def startElement(self,tagname,attrs):
        self.currtag=tagname
        if tagname == 'book':
            self.cat=attrs['category']
            print "------"
            print "Category", attrs['category']
            t=attrs['category']
            global t
    
    def characters(self,content):
        if(self.currtag =='title'):
            self.title = content
        if(self.currtag =='author'):
            self.author = content
        if(self.currtag =='year'):
            self.year = content
        if(self.currtag=='price'):
            self.price = content  
    
    def endElement(self,tag):
        if tag=='title':
            print "The book ",self.title,"belongs to category",t
        if tag=='author':
            print "and is written by ",self.author
        if tag=='year':
            print "This book is published in the year ",self.year
        if tag=='price':
            print "with a price of ",self.price  
            

pobj = xml.sax.make_parser()
uhobj = ourhandler()
pobj.setContentHandler(uhobj)
pobj.parse("/home/ai7/Desktop/common/Python_Exercises/book.xml")
