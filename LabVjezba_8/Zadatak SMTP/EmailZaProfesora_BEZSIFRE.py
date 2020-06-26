import smtplib


mojmail ='vedphone@gmail.com'
prima ='anteprojic@gmail.com'
sifra ='----------'

smtpserver = smtplib.SMTP("smtp.gmail.com",587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo()

smtpserver.login(mojmail,sifra)
poruka='Subject:Osmi_Zadatak_Email\nPostovanje profesore saljem vam email iz pythona kao sto trazite u zadatku, ovo je s google accounta jer mi je bilo lakse, lp Vedran Katavic'
smtpserver.sendmail(mojmail,prima,poruka)

print('Sent')
smtpserver.close()