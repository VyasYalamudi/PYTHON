import Tkinter as tk
import tkMessageBox
from PIL import ImageTk, Image
import os
import random

class a():
    def __init__(self):
        self.Captcha = ''
        self.Window = ''
        self.CaptchaLabel = ''
        self.CaptchaImg = ''
        self.ReCaptchaButton = ''
        self.ReCaptchaImg = ''
        self.WrongCaptchaCount = 0
        self.ReCaptchaCount = 0
        self.WrongPasswordCount = 0
        self.Path = 'D:\Captchas'
        self.ReCaptchaPath = 'D:\Captchas/recaptcha.gif'
        self.BgImagePath = 'D:\Captchas/background.jpg'
        self.BgImage = ''
        self.CaptchaPath = ''
        self.BgLabel = ''
        self.CaptchaEntry = ''
        self.CLabel = ''
        self.UIDEntry = ''
        self.UIDLabel = ''
        self.CaptchaCode = ''
        self.UID = ''
        self.CaptchaCodeText = ''
        self.UIDText = ''
        self.PasswordLabel = ''
        self.PasswordEntry = ''
        self.NewWindow = ''


    def MainWindow(self):
        self.Window = tk.Tk()
        self.Window.title( 'Login' )
        self.BgImg()
        self.IPLabels()
        self.LoadCaptcha()
        self.Window.mainloop()

    def BgImg(self):
        self.BgImg = ImageTk.PhotoImage( Image.open( self.BgImagePath ) )
        self.BgLabel = tk.Label( self.Window, image=self.BgImg, width=444, height=250)
        self.BgLabel.grid(row=0,column=0)

    def IPLabels(self):
        self.UIDLabel = tk.Label( self.BgLabel, text = 'User ID ', relief = 'solid', font = 'Times 10 bold' )
        #self.UIDLabel.configure(highlightbackground='black',highlightthickness=2)
        self.UIDLabel.grid( row = 0, column = 0, padx=(10,25), pady=(5,10) )
        self.UID = tk.StringVar()
        self.UIDEntry = tk.Entry( self.BgLabel, textvariable = self.UID, bd=1 )
        self.UID.set(self.UIDText)
        self.UIDEntry.grid( row = 0, column = 1, padx=(30,50), pady=(5,10) )
        self.CLabel = tk.Label( self.BgLabel, text = 'Enter the text in above Captcha ')
        self.CLabel.grid( row = 2, column = 1, padx=(27,27), pady=(10,10) )
        self.CaptchaCode = tk.StringVar()
        self.CaptchaEntry = tk.Entry( self.BgLabel, textvariable = self.CaptchaCode, bd=1 )
        self.CaptchaEntry.grid( row = 3, column = 1, padx=(5,5) )
        self.Submit = tk.Button( self.BgLabel, text = 'Submit', command = self.VerifyCaptcha )
        self.Submit.grid( row = 4, column = 1, pady=(10,10))


    def VerifyCaptcha(self):
        self.UIDText = self.UID.get()
        CaptchaCodeText = self.CaptchaCode.get()
        if self.UIDText == '' :
            tkMessageBox.showinfo( 'Credentials', 'User ID can\'t be empty!!!' )
    
        elif CaptchaCodeText == '' :
            tkMessageBox.showinfo( 'Credentials', 'CAPTCHA can\'t be empty!!!' )
            
        elif CaptchaCodeText == self.Captcha[:-4] :
            tkMessageBox.showinfo( 'Sucess', 'Correct Captcha' )
            self.NewMainWindow()
            
        else :
            self.WrongCaptchaCount+=1
            tkMessageBox.showwarning( 'CAPTCHA', 'Wrong CAPTCHA' )
            if self.WrongCaptchaCount < 4 :
                self.CaptchaCodeText = ''
                self.LoadCaptcha()
                
            else :
                self.ExceededWrongCaptcha()

                
    def NewMainWindow(self):
        self.BgLabel.grid_forget()
        self.BgLabel = tk.Label( self.Window, image=self.BgImg, width=444, height=250)
        self.BgLabel.grid(row=0,column=0)
        self.UIDLabel = tk.Label( self.BgLabel, text = 'User ID', font = 'Times 10 bold', relief = 'solid' )
        self.UIDLabel.grid( row = 0, column = 0, padx=(10,25), pady=(10,15) )
        self.UIDEntry = tk.Label( self.BgLabel, text = self.UIDText, font = 'Times 10 bold', relief = 'solid' )
        self.UIDEntry.grid( row = 0, column = 1, padx=(30,50), pady=(10,15) )
        self.PasswordLabel = tk.Label( self.BgLabel, text = 'Password ')
        self.PasswordLabel.grid( row = 1, column = 0)
        self.Password = tk.StringVar()
        self.PasswordEntry = tk.Entry( self.BgLabel, show='*', textvariable = self.Password)
        self.Password.set('')
        self.PasswordEntry.grid( row = 1, column = 1)
        self.Submit = tk.Button( self.BgLabel, text = 'Login', command = self.VerifyPassword )
        self.Submit.grid( row = 2, column = 1)
        

    def VerifyPassword(self):
        Password = self.Password.get()
        if Password == '':
            tkMessageBox.showwarning( 'Credentials', 'Password can\'t be empty!!!' )
            
        elif Password == 'asdfg' :
            tkMessageBox.showinfo( 'Sucess', 'Login Successful' )

        else :
            self.WrongPasswordCount+=1
            tkMessageBox.showwarning( 'Password', 'Wrong Password!!!' )
            if self.WrongPasswordCount > 3 :
                tkMessageBox.showerror( 'Limit', 'Wrong Password Limit Exceeded' )
                self.Destroy()
            else :
                self.NewMainWindow()
                

    def LoadCaptcha(self):
        self.IPLabels()
        self.SelectCaptcha()
        self.CaptchaImg = ImageTk.PhotoImage( Image.open( self.CaptchaPath ) )
        self.CaptchaLabel = tk.Label( self.BgLabel, image = self.CaptchaImg, width=250, height=50 )
        self.CaptchaLabel.grid( row = 1, column = 1 )
        self.LoadReCaptcha()


    def SelectCaptcha(self):
        self.Captcha = random.choice( os.listdir( self.Path ) )
        self.CaptchaPath = self.Path + '/' + self.Captcha
        if self.Captcha == 'recaptcha.gif' :
            self.SelectCaptcha()


    def LoadReCaptcha(self):
        self.ReCaptchaImg = ImageTk.PhotoImage( Image.open(self.ReCaptchaPath ) )
        self.ReCaptchaButton = tk.Button( self.BgLabel, image = self.ReCaptchaImg, width=40, height=40, relief='raised', command=self.CheckReCaptcha )
        self.ReCaptchaButton.grid( row = 1, column = 2, padx=(5,5) )


    def CheckReCaptcha(self):
        self.ReCaptchaCount+=1
        if self.ReCaptchaCount>0 and self.ReCaptchaCount<4 :
            self.UIDText = self.UID.get()
            self.LoadCaptcha()
            
        else :
            self.ExceededReCaptcha()


    def ExceededReCaptcha(self):
        tkMessageBox.showerror( 'Limit', 'Recaptcha Limit Exceeded' )
        self.Destroy()


    def ExceededWrongCaptcha(self):
        tkMessageBox.showerror( 'CAPTCHA', 'Wrong Captcha Limit Exceeded!!!' )
        self.Destroy()


    def Destroy(self) :
        self.Window.destroy()

b=a()
b.MainWindow()
