import requests

API_KEY = "yourAPIkey"
function = ""
urlbase = "https://api.n2yo.com/rest/v1/satellite{}&apiKey={}"
observer_lat = -6.21462	
observer_long = 106.84513
observer_alt = 0

NORAD_Ids = [43678,43017,27607,40908,40931,22825,25544,7530]
NOAA = [33591]

def GetURL(function):
    url = urlbase.format(function,API_KEY)
    return url

def GetTLEData(NORADId):
    function = "/tle/{}".format(NORADId)
    url = GetURL(function)
    res = requests.get(url=url)
    data = res.json()
    return data

def GetSatId(data):
    SatId = data['info']['satname']
    return SatId

def GetSatName(data):
    SatName = data['info']['satname']
    return SatName

def GetTLE(data):
    TLE = data['tle']
    return TLE

def GetSatPosData(NORAId, observer_lat, observer_long, observer_alt, seconds):
    function = "/positions/{}/{}/{}/{}/{}".format(NORAId, observer_lat, observer_long, observer_alt, seconds)
    url = GetURL(function)
    res = requests.get(url=url)
    data = res.json()
    return data

def GetSatLat(data):
    lat = data['positions'][0]['satlatitude']
    return lat

def GetSatLong(data):
    long = data['positions'][0]['satlongitude']
    return long

def GetSatAlt(data):
    alt = data['positions'][0]['sataltitude']
    return alt

def GetSatAz(data):
    az = data['positions'][0]['azimuth']
    return az

def GetSatEl(data):
    el = data['positions'][0]['elevation']
    return el

def GetSatRa(data):
    ra = data['positions'][0]['ra']
    return ra

def GetSatDec(data):
    dec = data['positions'][0]['dec']
    return dec

def GetSatTimeStamp(data):
    timestamp = data['positions'][0]['timestamp']
    return timestamp

def GetRadioPasses(NORAId, observer_lat, observer_long, observer_alt, days, min_elevation):
    function = "/radiopasses/{}/{}/{}/{}/{}/{}".format(NORAId, observer_lat, observer_long, observer_alt, days, min_elevation)
    url = GetURL(function)
    res = requests.get(url=url)
    data = res.json()
    return data

def ReportRadioPasses(NORAId, observer_lat, observer_long, observer_alt, days, min_elevation):
    import datetime
    data = GetRadioPasses(NORAId, observer_lat, observer_long, observer_alt, days, min_elevation)
    res = "Radio Passes Report\n"
    res = res + "{} [{}]\n".format(data['info']['satname'],data['info']['satid'])
    for d in data['passes']:
        res = res + "-"*30+"\n"
        res = res + "AOS\tTime: {}\n".format(datetime.datetime.utcfromtimestamp(d["startUTC"]))
        res = res +"\tAzimuth: {} ({})\n\n".format(d['startAz'],d['startAzCompass'])
        res = res +"Max\tAzimuth: {} ({})\n".format(d['maxAz'],d['maxAzCompass'])      
        res = res +"\tElevation: {}\n\n".format(d['maxEl'])      
        res = res + "LOS\tTime: {}\n".format(datetime.datetime.utcfromtimestamp(d["endUTC"]))
        res = res + "\tAzimuth: {} ({})\n".format(d['endAz'],d['endAzCompass'])
    res = res + "-"*30+"\n"
    return res

if __name__ == "__main__":
    observer_lat = -6.21462	
    observer_long = 106.84513
    observer_alt = 0
    #print(GetTLEData("1293"))
    #print(GetSatLat(GetSatPosData("25544",observer_lat, observer_long, observer_alt,1)))
    print(ReportRadioPasses("33591",observer_lat, observer_long, observer_alt,1, 10))
