import datetime
import pandas as pd
import smtplib, ssl

#---------------------------- EMAIL CONFIG ----------------------------#
port = 465  # For SSL
server = "smtp.gmail.com" # Locaweb server
email = "sergio.guerrato@gmail.com" # Email sender
password = "1234" # It's password

# Create a secure SSL context
context = ssl.create_default_context()

# Create a smtp object
smtpObj = smtplib.SMTP_SSL("smtp.gmail.com", port, context=context)
smtpObj.connect(host=server, port = port)
smtpObj.login(email, password)

sender_email = "ocs.bot@company.com.br"
receiver_email = "atendimento-chamados@company.com.br"
#----------------------------------------------------------------------#

# Read the csv file only columns Last inventory and Computer (name) - Using Pandas
df = pd.read_csv("C:\\Users\\supor\\Downloads\\export.csv", sep=';', on_bad_lines='skip')

# Set date as 30 days ago
date = datetime.date.today() - datetime.timedelta(days=30)

# Function to search for computers that have not been inventoried for a long time
def func(fetchComp):
    
    # Variables for each columns
    li = fetchComp['Last inventory']
    cn = fetchComp['Computer']
    tag = fetchComp['Account info : TAG']
    ip = fetchComp['IP address']
    mac = fetchComp['MAC address']
    mf = fetchComp['Manufacturer']
    model = fetchComp['Model']
    sn = fetchComp['Serial number']
    
    

    # Condition to send a ticket (more than 30 days)
    if li < str(date):
        
        # Check for store code in the computer name
        ### On my company, for default, we use the 4th and 5th characters to identify each store. ###
        store = cn[3] + cn[4]
        match store:
            case "00":
                storeName = "COMPANY 1"
            case "01":
                storeName = "COMPANY 2"
            case "02":
                storeName = "COMPANY 3"
            case "03":
                storeName = "COMPANY 4"
            case "04":
                storeName = "COMPANY 5"
            case "05":
                storeName = "COMPANY 6"
            case "06":
                storeName = "COMPANY 7"
            case "07":
                storeName = "COMPANY 8"
            case "08":
                storeName = "COMPANY 9"
            case "09":
                storeName = "COMPANY 10"
            case "10":
                storeName = "COMPANY 11"
            case "11":
                storeName = "COMPANY 12"
            case "12":
                storeName = "COMPANY 1A"
            case "13":
                storeName = "COMPANY 2B"
            case "14":
                storeName = "COMPANY 3C"

        txt1 = "Subject: OCS Inventory BOT Alert - "+ cn +"\n\nOlá,\n\nO computador a seguir deixou de inventariar no OCS.\n"
        txt2 = "\n Nome do Computador: " + cn + "\n Loja: " + storeName + "\n Depart./TAG: " + tag + "\n Último IP: " + ip + "\n MAC: " + mac + "\n Fabricante: " + mf + "\n Modelo: "+ model + "\n Serial N.: " + sn + "\n Última vez inventariado: " + li
        txt3 = "\n\nAtt,\nOCS Inventory Bot"
        message = (txt1 + txt2 + txt3).encode('utf8')
        smtpObj.sendmail(sender_email, receiver_email, message)
        print("Email sent: ", cn, li)

# Using Pandas, the ".apply" applys a function along an axis of the DataFrame (axis = 1 set columns)
df.apply(func,axis=1)
