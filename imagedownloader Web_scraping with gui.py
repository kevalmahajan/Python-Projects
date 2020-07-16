import os
import requests # to sent GET requests
from bs4 import BeautifulSoup # to parse HTML
from tkinter import *
import tkinter as tk
import traceback
from tkinter import messagebox as m_box

yahoo_img = \
    'https://in.images.search.yahoo.com/search/images;_ylt=AwrwJSJD2Q1fTlkATCK8HAx.;_ylc=X1MDMjExNDcyMzAwNARfcgMyBGZyAwRncHJpZAN6VDFjeUl0WlFfLnRqMGU1YlNTTGVBBG5fc3VnZwMxMARvcmlnaW4DaW4uaW1hZ2VzLnNlYXJjaC55YWhvby5jb20EcG9zAzAEcHFzdHIDBHBxc3RybAMEcXN0cmwDNARxdWVyeQNkb2dzBHRfc3RtcAMxNTk0NzQzMTEw?fr2=sb-top-in.images.search&'

user_agent = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive',
}
save_folder = 'images'

#---------------------------------------------------------------------------------
def download_n():
    root1 = Tk()
    z = Canvas(root1, width=400,height=250)
    root1.title("Download n Images")
    Label(root1, text="What are you looking for?", fg = "Black",
		 font = "Verdana 10").place(x=90,y=20) 

    e1=Entry(root1)
    e1.place(x=90,y=50)
    
    Label(root1, text="How many images do you want? ", fg = "Black",
		 font = "Verdana 10").place(x=90,y=90) 
    
    e2=Entry(root1)
    e2.place(x=90,y=120)
            
    button4 = tk.Button(root1, text='Download', width=17,
                        bg="#D3D3D3",fg='black',
                        command=lambda:download_images(e1,e2))
    button4.place(x=90,y=160)

    
    
    button5 = tk.Button(root1, text='Back', width=10,
                        bg="#D3D3D3",fg='black',
                        command=lambda:[root1.destroy(),main()]).place(x=225,y=160)
        
    z.pack()
    
         
        
        
def download_images(e1,e2):
    try:
        root1 = Tk()
        root1.title("Done")
        data=e1.get()
        n_images=e2.get()
        if data=='' or n_images=='':
            root1.withdraw()
            m_box.showerror('Error','Please fill both entries ')
        else:
            data=str(data)
            n_images=int(n_images)
        #    print(data,n_images) 

            z = Canvas(root1, width=260,height=110)
            
            print('Start searching...')
            
        
                    
            # get url query string
            searchurl = yahoo_img + 'p=' + data
                    #print(searchurl)
                
                    # request url, without user_agent the permission gets denied
            response = requests.get(searchurl, headers=user_agent)
            html = response.text
            
            soup = BeautifulSoup(html, 'html.parser')
            results = soup.find_all('img',class_= 'process',limit=n_images)
                
                    # extract the link from the img tag
            imagelinks= []
                    
            for re in results:
                url1=re.attrs.get('data-src')
                imagelinks.append(url1)
            
            print(f'found {len(imagelinks)} images')
            Label(root1, text=f'found {len(imagelinks)} images', fg = "Black",
        		 font = "Verdana 10").place(x=70,y=20) 
            print('Start downloading...')
        #    Label(root1, text="Start downloading...", fg = "Black",
        #		 font = "Verdana 10").pack()
                
            for i, imagelink in enumerate(imagelinks):
                # open image link and save as file
                response = requests.get(imagelink)
                        
                imagename = save_folder + '/' + data + str(i+1) + '.jpg'
                with open(imagename, 'wb') as file:
                    file.write(response.content)
                
            print('Done')
            Label(root1, text="DOWNLOADING COMPLETE", fg = "Black",
        		 font = "Verdana 10").place(x=40,y=40) 
            button5 = tk.Button(root1, text='OK', width=10,
                                bg="#D3D3D3",fg='black',
                                command=root1.destroy).place(x=90,y=70)
                
            z.pack()
    except ValueError:
        root1.withdraw()
        m_box.showwarning('Error','Enter a Valid Number')
#        print("enter valid number")
#        root2 = Tk()
#        z = Canvas(root2, width=260,height=110)
#        Label(root2, text="Enter a valid Number", fg = "Black",
#		 font = "Verdana 10").place(x=60,y=30) 
#        button5 = tk.Button(root2, text='OK', width=10,
#                        bg="#D3D3D3",fg='black',
#                        command=root2.destroy).place(x=90,y=70)
#        
#        z.pack()
#------------------------------------------------------------------------------------


def url_n():
    root1 = Tk()
    root1.title("Download Image using url")
    z = Canvas(root1, width=400,height=250)
    Label(root1, text="Enter Url : ", fg = "Black",
		 font = "Verdana 10").place(x=90,y=20) 

    e1=Entry(root1,width=35)
    e1.place(x=90,y=50)
    
    Label(root1, text="Name of the image to be saved :", fg = "Black",
		 font = "Verdana 10").place(x=90,y=90) 
    
    e2=Entry(root1)
    e2.place(x=90,y=120)
            
    
    button4 = tk.Button(root1, text='Download', width=17,
                        bg="#D3D3D3",fg='black',
                        command=lambda:url_images(e1,e2)).place(x=90,y=160)
    button5 = tk.Button(root1, text='Back', width=10,
                        bg="#D3D3D3",fg='black',
                        command=lambda:[root1.destroy(),main()]).place(x=225,y=160)
        
        
    z.pack()
    
def url_images(e1,e2):
    try:
    
        root1 = Tk()
        root1.title("Done")

        z = Canvas(root1, width=260,height=110)
        
        imagelink=e1.get()
        data=e2.get()
        if imagelink=='' or data=='':
            root1.withdraw()
            m_box.showerror('Error','Please fill both entries ')
        else:
            response = requests.get(imagelink)
            imagename = save_folder + '/' + data +  '.jpg'
            with open(imagename, 'wb') as file:
                file.write(response.content)
            print('Done')
            Label(root1, text="IMAGE DOWNLOADED", fg = "Black",
        		 font = "Verdana 10").place(x=60,y=30) 
            button5 = tk.Button(root1, text='OK', width=10,
                                bg="#D3D3D3",fg='black',
                                command=root1.destroy).place(x=90,y=70)
                
            z.pack()
    except :
        root1.withdraw()
        m_box.showwarning('Invalid Url','Enter a Valid URL')
    
        
       
#------------------------------------------------------------------------------------------
    
def insta_n():
    root1 = Tk()
    root1.title("Download Instagram Image ")
    z = Canvas(root1, width=400,height=250)
    Label(root1, text="Enter Instagram Image link : ", fg = "Black",
		 font = "Verdana 10").place(x=90,y=20) 

    e1=Entry(root1,width=35)
    e1.place(x=90,y=50)
    
    Label(root1, text="Name of the image to be saved :", fg = "Black",
		 font = "Verdana 10").place(x=90,y=90) 
    
    e2=Entry(root1)
    e2.place(x=90,y=120)
            
    button4 = tk.Button(root1, text='Download', width=17,
                        bg="#D3D3D3",fg='black',
                        command=lambda:insta_images(e1,e2)).place(x=90,y=160)
    button5 = tk.Button(root1, text='Back', width=10,
                        bg="#D3D3D3",fg='black',
                        command=lambda:[root1.destroy(),main()]).place(x=225,y=160)
        
    z.pack()
    
def insta_images(e1,e2):
    try:
        root1 = Tk()
        root1.title("Done")
        z = Canvas(root1, width=260,height=110)
        
        url=e1.get()
        data=e2.get()
        if data=='' or n_images=='':
            root1.withdraw()
            m_box.showerror('Error','Please fill both entries ')
        else:
            usr_agent = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
            'Accept-Encoding': 'none',
            'Accept-Language': 'en-US,en;q=0.8',
            'Connection': 'keep-alive',
        }
            response = requests.get(url, headers=usr_agent)
            html = response.text
            #soup = BeautifulSoup(html, 'html.parser')
        
            soup = BeautifulSoup(html,'html.parser')
            metaTag = soup.find_all('meta', {'property':'og:image'})
            imagelink = metaTag[0]['content']
            
            response = requests.get(imagelink)
            imagename = save_folder + '/' + data +  '.jpg'
            with open(imagename, 'wb') as file:
                file.write(response.content)
            print('Done')
            Label(root1, text="IMAGE DOWNLOADED", fg = "Black",
        		 font = "Verdana 10").place(x=60,y=30) 
            button5 = tk.Button(root1, text='OK', width=10,
                                bg="#D3D3D3",fg='black',
                                command=root1.destroy).place(x=90,y=70)
                
            z.pack()

    except :
        root1.withdraw()
        m_box.showwarning('Invalid Instagram Link','Enter a Valid URL')
#        print("Invalid Image Url")
#        root2 = Tk()
#        z = Canvas(root2, width=260,height=110)
#        Label(root2, text="Invalid Image Url", fg = "Black",
#		 font = "Verdana 10").place(x=60,y=30) 
#        button5 = tk.Button(root2, text='OK', width=10,
#                        bg="#D3D3D3",fg='black',
#                        command=root2.destroy).place(x=90,y=70)
#        
#        z.pack()
        


def main():
    if not os.path.exists(save_folder):
        os.mkdir(save_folder)
        
    
    root = Tk()
    
    root.title("Image Downloader")
    w = Canvas(root, width=400,height=250) 
    Label(root, text="Image Downloader", fg = "Black",
		 font = "Verdana 14",pady=10,padx=10,bg = "LightGrey").place(x=100,y=20) 

    button1 = tk.Button(root, text='Download n required images', width=35,
                        command=lambda: [download_n(),root.destroy()]).place(x=75,y=100)
    button2 = tk.Button(root, text='Download via url', width=35,
                        command=lambda: [url_n(),root.destroy()]).place(x=75,y=140)
    button3 = tk.Button(root, text='Download instagram images', width=35,
                        command=lambda: [insta_n(),root.destroy()]).place(x=75,y=180)
 
    w.pack()
    mainloop()

    
    
if __name__ == '__main__':
    main()
    


