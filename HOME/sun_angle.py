#Every true traveler must know how to do 3 things: fix the fire, find the water and extract useful information 
#from the nature around him. Programming won't help you with the fire and water, but when it comes to the 
#information extraction - it might be just the thing you need.
#Your task is to find the angle of the sun above the horizon knowing the time of the day. Input data: 
#the sun rises in the East at 6:00 AM, which corresponds to the angle of 0 degrees. At 12:00 PM the sun 
#reaches its zenith, which means that the angle equals 90 degrees. 6:00 PM is the time of the sunset so 
#the angle is 180 degrees. If the input will be the time of the night (before 6:00 AM or after 6:00 PM), 
#your function should return - "I don't see the sun!".

def sun_angle(hora):
    hora = hora.split(':')
    lista = []
    for c in hora:
        c = int(c)
        lista.append(c)
    if 6<=int(lista[0])<18:
        angulo = ((lista[0]-6)*15)+(lista[1]*0.25) 
    elif lista[0]==18 and lista[1]==00:
        angulo = ((lista[0]-6)*15)+(lista[1]*0.25) 
    else:
        return "I don't see the sun!"
    return angulo

if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))
    print(sun_angle("07:00")) == 15
    print(sun_angle("08:27"))
    print(sun_angle("06:00"))
    print(sun_angle("18:00"))
    print(sun_angle("12:00"))
    print(sun_angle("18:01"))
    print(sun_angle("18:02"))
    print(sun_angle("01:23")) == "I don't see the sun!"

