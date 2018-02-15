#!/usr/bin/python3

# -*- coding: utf-8 -*- 

# https://automatetheboringstuff.com/chapter16/
# https://stackoverflow.com/questions/45385894/python-smtp-send-email-from-gmail

##################################################################################
#         ATENCIO																 #
#     Teniu en compte que per que funcioni necessitam							 #
#     "permitir acceso a aplicaciones menos seguras" en la configuració del	 	 #
#     correu de Gmail. Millor utilitzar un compte de proves i no el personal.	 #
##################################################################################

##################################################################################
#         ATENCIO																 #
#     Si utilitzau aquesta funció heu de llegir              					 #
#     l'usuari i password des d'un fitxer							 			 #
#     Aquest fitxer només ha de tenir permís de lectura per el vostre usuari	 #
#	  Si no podria ser un error greu de seguretat ... 							 #
#	  pensau quedarà al vostre servidor	, ningú més ha de poder accedir			 #
##################################################################################

import smtplib
import sys

def send_email(user, pwd, recipient, subject, body):
    import smtplib

    FROM = user
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    
    ServerConnect = False
    try:
        smtp_server = smtplib.SMTP('smtp.gmail.com',587)
        smtp_server.starttls()
        smtp_server.login(user, pwd)
        ServerConnect = True
    except smtplib.SMTPHeloError as e:
        print ("Server did not reply")
    except smtplib.SMTPAuthenticationError as e:
        print ("Incorrect username/password combination")
    except smtplib.SMTPException as e:
        print ("Authentication failed")

    if ServerConnect == True:
        try:
            smtp_server.sendmail(user, recipient, message)
            print ("Successfully sent email")
        except SMTPException as e:
            print ("Error: unable to send email", e)
        finally:
            smtp_server.quit()

