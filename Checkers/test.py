import datetime
now = datetime.datetime.now()
print(str(now.today().strftime('%d-%m-%Y %H:%M.%S %p')))