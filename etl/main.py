from etl import truncate_and_etl


def send_email():
    from email.mime.text import MIMEText
    from phila_mail import server

    recipientslist = ['dani.interrante@phila.gov', 
                      'philip.ribbens@phila.gov',
                      'shannon.holm@phila.gov',
					  'jessica.bradley@phila.gov']
    sender = 'ligisteam@phila.gov'
    commaspace = ', '
    email = 'RENTAL_PAYMENTS_OPA_MVW in GISLNI failed to update properly and may be missing rows or empty. Please stand by for updates. The ETL process happens on the 131 VM.'
    text = f'AUTOMATIC EMAIL: \n {email}'
    msg = MIMEText(text)
    msg['To'] = commaspace.join(recipientslist)
    msg['From'] = sender
    msg['X-Priority'] = '2'
    msg['Subject'] = 'Important Email'
    server.server.sendmail(sender, recipientslist, msg.as_string())
    server.server.quit()

def main():
    try:
        truncate_and_etl()
    except:
        send_email()

if __name__ == '__main__':
    main()