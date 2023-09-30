import datetime
import requests

def newuser(name,dob):
    f = open("User.txt", "w")
    f.write(name+'\n'+dob+'\n')
    f.close()


def calculate_zodiac_sign(dob):
    month=int(dob[5:7])
    day=int(dob[8:])

    if (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Aquarius"
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return "Pisces"
    elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Aries"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Taurus"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Gemini"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Cancer"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Leo"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Virgo"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Libra"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Scorpio"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "Sagittarius"
    else:
        return "Capricorn"






def get_daily_horoscope(zs):
    if (zs=="Aquarius"):
        return "Today will bring you new opportunities and exciting adventures!"
    elif (zs=="Pisces"):
        return "Your creativity will be at its peak today. Embrace your imagination!"
    elif (zs=="Aries"):
        return "You have the energy and determination to achieve great things today. Go for it!"
    elif (zs=="Taurus"):
        return "Take some time today to appreciate the beauty around you. It will bring you joy."
    elif (zs=="Gemini"):
        return "Your communication skills will shine today. Engage in meaningful conversations!"
    elif (zs=="Leo"):
        return "Your confidence will be at its peak today. Step forward and show the world your brilliance!"   
    elif (zs=="Cancer"):
        return "Focus on self-care today. Nurture yourself and recharge your energy."
    elif (zs=="Virgo"):
        return "You have the ability to organize and accomplish tasks efficiently today. Make the most of it!"
    elif (zs=="Libra"):
        return "Seek harmony and balance in all aspects of your life today. It will bring you peace."
    elif (zs=="Scorpio"):
        return "Trust your instincts today. Your intuition will guide you towards success."
    elif (zs=="Sagittarius"):
        return "Embrace your adventurous spirit today. Engage in new experiences and expand your horizons!"
    else:
        return "Your hard work and dedication will pay off today. Keep pushing forward"
