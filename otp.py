from twilio.rest import Client
import random
from tkinter import *
from tkinter import messagebox
import webbrowser

class otp_generate(Tk):
    def __init__(self):
        super().__init__()

        self.geometry("600x550")
        self.resizable(False, False)
        self.n = random.randint(1000, 9999)
        self.client = Client("AC115cb240b37565457f7340c8c3f451b0", "b34da79d39db3a9ea5fb731accd5bc4c")

        self.Labels()
        self.Entry()
        self.Buttons()

        self.client.messages.create(to=["+917063762843"], from_="+18288091595", body=str(self.n))

    def Labels(self):
        self.c = Canvas(self, bg="white", width=400, height=280)
        self.c.place(x=100, y=60)

        self.Login_Title = Label(self, text="OTP Verification", font="bold, 20", bg="white")
        self.Login_Title.place(x=218, y=98)

    def Entry(self):
        self.User_Name = Entry(self, font=("Helvetica", 16), show='•')
        self.User_Name.place(x=190, y=160)

    def Buttons(self):
        self.submitButtonImage = PhotoImage(file="D:\Python OTP Generator\submit.png")
        self.submitButton = Button(self, image=self.submitButtonImage, command=self.checkOTP, border=0, width=240, height=70)
        self.submitButton.place(x=195, y=240)

        self.resendOTPImage = PhotoImage(file="D:\Python OTP Generator\otpresend.png")
        self.resendOTPButton = Button(self, image=self.resendOTPImage, command=self.resendOTP, border=0, width=240,height=70)
        self.resendOTPButton.place(x=195, y=400)
        
        

    def checkOTP(self):
        try:
            userInput = int(self.User_Name.get())
            if userInput == self.n:
                messagebox.showinfo("Success", "Login Success")
                webbrowser.open("file:///D:/Banking/index.html")
                self.n = "done"
            elif self.n == "done":
                messagebox.showinfo("Info", "Already entered the OTP")
            else:
                messagebox.showinfo("Info", "Wrong OTP")
        except ValueError:
            messagebox.showinfo("Info", "Invalid OTP")

    def resendOTP(self):
        self.n = random.randint(1000, 9999)
        self.client = Client("AC115cb240b37565457f7340c8c3f451b0", "b34da79d39db3a9ea5fb731accd5bc4c")
        self.client.messages.create(to=["+917063762843"], from_="+18288091595", body=str(self.n))

if __name__ == "__main__":
    window = otp_generate()
    window.mainloop()
