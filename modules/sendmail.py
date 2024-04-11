import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate

# Creating the email - to, from, subject, body and attachment
def mail(nome,email,arq,from_email,info) -> MIMEMultipart:
    
    # Unpacking variables
    simulado,dia = info
    
    msg: MIMEMultipart = MIMEMultipart()
   
   # From 
    msg['From'] = from_email
    
    # To
    msg['To'] = email
    
    # Date
    msg['Date'] = formatdate(localtime=True)
    
    # Subject
    msg['Subject'] = f"Resultados Simulado {simulado} {dia} - Cursinho Popular FFLCH"
    
    # Body
    msg.attach(MIMEText(f"Olá, {nome} \n \n Segue em anexo o resultado do seu simulado {simulado} do dia {dia}."))

    # File attachment
    with open(arq, "rb") as file:
        part = MIMEApplication(file.read(),Name=basename(arq))
        part['Content-Disposition'] = 'attachment; filename="%s"' % basename(arq)
        msg.attach(part)

    return msg

# Sending the email created by mail() function. Returns True if it was not possible to send the email
def send_email(login,destinatario,arq,info) -> bool:
    
    # Unpacking variables
    id,nome,email = destinatario
    usuario,senha = login
    
    # Error flag
    erro: bool = False
    
    # Conecting to server
    smtp: smtplib.SMTP = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.starttls()
    smtp.login(usuario,senha)
    
    # Creating email and checking for error
    msg: MIMEMultipart = mail(nome,email,arq,usuario,info)
    try:
        smtp.sendmail(msg['From'], msg['To'], msg.as_string())
    except OSError as e:
        erro = True
        with open("erro.txt","a") as arq:
            arq.write(f"{nome},{email},{e}")
            
    smtp.close()
    
    return erro