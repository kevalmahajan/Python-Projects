import os
import requests # to sent GET requests
from bs4 import BeautifulSoup # to parse HTML
from tkinter import *
import tkinter as tk
from tkinter import messagebox as m_box
from tkinter import filedialog
from PIL import Image
import youtube_dl
from PIL import ImageTk

root = Tk()
root.title("Media Downloader")

   
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
    
    f1=Frame(root)
    z = Canvas(f1, width=400,height=280,bg='#0B3680')  #2367FA

    z.create_text(195,50, text="What are you looking for?", fill = "White",font = ('Verdana'))
    

    e1=Entry(f1)
    e1.place(x=90,y=70)
    z.create_text(225,120, text="How many images do you want?", fill = "White",font = ('Verdana'))
    
   
    e2=Entry(f1)
    e2.place(x=90,y=140)
           
    button4 = tk.Button(f1, text='Download', width=17,
                        bg="#D3D3D3",fg='black',
                        command=lambda:download_images(e1,e2))
    button4.place(x=90,y=190)
    
    button5 = tk.Button(f1, text='Back', width=10,
                        bg="#D3D3D3",fg='black',
                        command=lambda:[f1.destroy(),main()]).place(x=225,y=190)
       
    z.pack()
    f1.pack()
    
    
    
def download_images(e1,e2):
    try:

        data=e1.get()
        n_images=e2.get()
        if data=='' or n_images=='':

            m_box.showerror('Error','Please fill both entries ')
        else:
            data=str(data)
            n_images=int(n_images)
            print('Start searching...')
           
       
                   
            # get url query string
            searchurl = yahoo_img + 'p=' + data
               
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
            print('Start downloading...')
               
            for i, imagelink in enumerate(imagelinks):
                # open image link and save as file
                response = requests.get(imagelink)
                       
                imagename = save_folder + '/' + data + str(i+1) + '.jpg'
                with open(imagename, 'wb') as file:
                    file.write(response.content)
               
            print('Done')

            m_box.showinfo(title='Done', message=f'found {len(imagelinks)} images \nDownloading Complete')   
            
    except ValueError:
        m_box.showwarning('Error','Enter a Valid Number')

#------------------------------------------------------------------------------------


def url_n():
    f2=Frame(root)
    z = Canvas(f2, width=400,height=280,bg='#0B3680')
    
    z.create_text(135,50, text="Enter Url : ", fill = "White",font = ('Verdana'))
    e1=Entry(f2,width=35)
    e1.place(x=90,y=70)
    
    
    z.create_text(225,120, text="Name of the image to be saved :", fill = "White",font = ('Verdana'))
    e2=Entry(f2)
    e2.place(x=90,y=140)
           
   
    button4 = tk.Button(f2, text='Download', width=17,
                        bg="#D3D3D3",fg='black',
                        command=lambda:url_images(e1,e2)).place(x=90,y=190)
    button5 = tk.Button(f2, text='Back', width=10,
                        bg="#D3D3D3",fg='black',
                        command=lambda:[f2.destroy(),main()]).place(x=225,y=190)
       
       
    z.pack()
    f2.pack()
    
def url_images(e1,e2):
    try:
        
        imagelink=e1.get()
        data=e2.get()
        if imagelink=='' or data=='':
            m_box.showerror('Error','Please fill both entries ')
        else:
            response = requests.get(imagelink)
            imagename = save_folder + '/' + data +  '.jpg'
            with open(imagename, 'wb') as file:
                file.write(response.content)
            print('Done')
            m_box.showinfo(title='Done', message='Downloading Complete')   

    except :

        m_box.showwarning('Invalid Url','Enter a Valid URL')
   
       
       
#------------------------------------------------------------------------------------------
   
def insta_n():
    f3=Frame(root)
   
    z = Canvas(f3, width=400,height=280,bg = '#0B3680')
    z.create_text(210,50, text="Enter Instagram Image link : ", fill = "White",font = ('Verdana'))
    

    e1=Entry(f3,width=35)
    e1.place(x=90,y=70)

    z.create_text(225,120, text="Name of the image to be saved :", fill = "White",font = ('Verdana'))
    
   
    e2=Entry(f3)
    e2.place(x=90,y=140)
           
    button4 = tk.Button(f3, text='Download', width=17,
                        bg="#D3D3D3",fg='black',
                        command=lambda:insta_images(e1,e2)).place(x=90,y=190)
    button5 = tk.Button(f3, text='Back', width=10,
                        bg="#D3D3D3",fg='black',
                        command=lambda:[f3.destroy(),main()]).place(x=225,y=190)
       
    z.pack()
    f3.pack()
def insta_images(e1,e2):
    try:
      
        url=e1.get()
        data=e2.get()
        
        if data=='' or url=='':

            m_box.showerror('Error','Please fill both entries ')
        else:
            usr_agent = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
            'Accept-Encoding': 'none',
            'Accept-Language': 'en-US,en;q=0.8',
            'Connection': 'keep-alive',}
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
            m_box.showinfo(title='Done', message='Downloading Complete')  
        

    except :
        m_box.showwarning('Invalid Instagram Link','Enter a Valid URL')

       
#--------------------------------------------------------------------------------
def yt_n():
    f4=Frame(root)

    z = Canvas(f4, width=400,height=280,bg='#0B3680')

    z.create_text(175,90, text="Enter Youtube link :", fill = "White",font = ('Verdana'))
    

    e1=Entry(f4,width=35)
    e1.place(x=90,y=110)
           
   
    button4 = tk.Button(f4, text='Download', width=17,
                        bg="#D3D3D3",fg='black',
                        command=lambda:yt_videos(e1)).place(x=90,y=170)
    button5 = tk.Button(f4, text='Back', width=10,
                        bg="#D3D3D3",fg='black',
                        command=lambda:[f4.destroy(),main()]).place(x=225,y=170)
    z.pack()
    f4.pack()
   
def yt_videos(e1):
    try:
    
        url=e1.get()
        if url=='' :
        
            m_box.showerror('Error','Please enter url ')
        else:
            ydl_opts = {}
            f=filedialog.askdirectory(initialdir='C:/')
            os.chdir(f)
            
            
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            m_box.showinfo(title='Done', message='Downloading Complete')

    except:

        m_box.showwarning('Invalid Youtube Link','Enter a Valid URL')
       
       
#-----------------------------------------------------------------------------------------  
   

def main():
    if not os.path.exists(save_folder):
        os.mkdir(save_folder)
       
    f=Frame(root)
    
    
    w = Canvas(f, width=400,height=280,bg = "black")
    
    image = ImageTk.PhotoImage(file = "page.jpeg")
    w.create_image(1, 1, image = image, anchor = NW)


    w.create_text(200,50, text="Media Downloader", fill = "White",font = ('Verdana', '18'))
    
    button1 = tk.Button(f, text='Download n required images', width=35,
                        command=lambda: [download_n(),f.destroy()]).place(x=75,y=100)
    button2 = tk.Button(f, text='Download via url', width=35,
                        command=lambda: [url_n(),f.destroy()]).place(x=75,y=140)
    button3 = tk.Button(f, text='Download instagram images', width=35,
                        command=lambda: [insta_n(),f.destroy()]).place(x=75,y=180)
    button4 = tk.Button(f, text='Download youtube videos', width=35,
                       command=lambda: [yt_n(),f.destroy()]).place(x=75,y=220)

    w.pack()
    f.pack()
    mainloop()
 
        
if __name__ == '__main__':
    main()
    

