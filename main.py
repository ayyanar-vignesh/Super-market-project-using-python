import pandas as pd  
import smtplib 
import random 
view_data=pd.read_csv('data_new.csv')
def email_sending():
    try:
        for i in view_data["emailid"]:
            otp_number=random.randint(0000,9999)
            print(i,otp_number)
            s=smtplib.SMTP('smtp.gmail.com',587)
            s.starttls()
            s.login("sender_mailid","sender_encrypt password")
            message=f"your otp number is {otp_number}"
            s.sendmail("sendeer_mailid",i,message)
            s.quit()
            print("mail sent successfully")
    except:
        print("mail not sent")
email_sending()