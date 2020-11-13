#Computer date and time format consists only of numbers, for example: 21.05.2018 16:30
#Humans prefer to see something like this: 21 May 2018 year, 16 hours 30 minutes
#Your task is simple - convert the input date and time from computer format into a "human" format.

def date_time(time):
    year = {'01':'January', '02':'February', '03':'March', '04':'April', '05':'May', '06':'June',
    '07':'July', '08': 'August', '09': 'September', '10': 'October', '11':'November', '12':'December'}
    if time[3:5] in year:
        mes = year[time[3:5]]
    if int(time[:2])<10:
        dia = time[1:2]
    else:
        dia = time[:2]
    ano = time[6:10]
    if int(time[11:13])<10:
        hora = time[12:13]
    else:
        hora = time[11:13]
    if int(time[14:16])<10:
        minuto = time[15:16]
    else:
        minuto = time[14:16]
        
    if hora=='1' and minuto=='1':
        return f'{dia} {mes} {ano} year {hora} hour {minuto} minute'
    elif hora == '1':
       return f'{dia} {mes} {ano} year {hora} hour {minuto} minutes'
    elif minuto =='1':
        return f'{dia} {mes} {ano} year {hora} hours {minuto} minute'
    else: 
        return f'{dia} {mes} {ano} year {hora} hours {minuto} minutes'
        

if __name__ == '__main__':
    print("Example:")
    print(date_time("01.01.2000 00:00")) == "1 January 2000 year 0 hours 0 minutes", "Millenium"
    print(date_time("09.05.1945 06:30")) == "9 May 1945 year 6 hours 30 minutes", "Victory"
    print(date_time("20.11.1990 03:55")) == "20 November 1990 year 3 hours 55 minutes", "Somebody was born"
    print(date_time("04.11.1812 01:01"))