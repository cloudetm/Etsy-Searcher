import random
import urllib2
import json
import webbrowser
from Tkinter import *


class Application(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):

        self.top_frame = Frame(self)
        self.my_button = Button(self.top_frame, text = 'Random Search', command = self.act)

        self.my_button.pack()

        self.top_frame.pack(side = 'top')

    def act(self):

        e = False

        data = getListing()

        while e == False:
        
            try:
                #print data['results'][0]['state']
                print "Wait for it..."
                while data['results'][0]['state'] == unicode('expired') or data['results'][0]['state'] == unicode('m_closed') or data['results'][0]['state'] == unicode('alchemy') or data['results'][0]['state'] == unicode('a_closed') or data['results'][0]['state'] == unicode('create') or data['results'][0]['state'] == unicode('edit') or data['results'][0]['state'] == unicode('removed') or data['results'][0]['state'] == unicode('sold_out') or data['results'][0]['state'] == unicode('unavailable') or data['results'][0]['state'] == unicode('draft'):

                    data = getListing()

            except:

                e = False
                data = getListing()


            else:
                e = True

        print data

        x = data['params']['listing_id']
        str(x)

        webbrowser.open('http://www.etsy.com/listing/' + x)





def main():

    app = Application()
    app.master.title("Random Search")
    app.mainloop()



def getListing():

    itemID = random.randint(1, 86600611)

    itemStr = str(itemID)

    data = urllib2.urlopen('http://openapi.etsy.com/v2/listings/' + itemStr + '?api_key=XXXXXXXXXXXXXXXXXXX')

    return json.load(data)





try:

    main()

except:

    main()

        
