"""
geolocation services - no api key required - normalized output

    sample = {
        "url": "http://xxx.com/json",
        "city": "",
        "region": "",
        "country": "",
        "latitude": "0.0000",
        "longitude": "0.0000",
    }
    
services utilized:
    ip-api.com
    ipapi.co
    free.ipwhois.io
    ipvigilante.com
"""

# STANDARD PYTHON MODULES
from pprint import pprint

# THIRD PARTY MODULES
import requests


def geolocate(location=""):
    """
    attempt to contact multiple geolocation services
    format first response to standardized dictionary
    default to request for client IP address
    """
    try:
        url = f"http://ip-api.com/json/{location}"
        ret = requests.get(url).json()
        data = {
            "url": url,
            "city": str(ret["city"]),
            "region": str(ret["regionName"]),
            "country": str(ret["country"]),
            "latitude": "%.4f" % float(ret["lat"]),
            "longitude": "%.4f" % float(ret["lon"]),
        }
    except:
        try:
            url = f"https://ipapi.co/{location}/json/"
            ret = requests.get(url).json()
            data = {
                "url": url,
                "city": str(ret["city"]),
                "region": str(ret["region"]),
                "country": str(ret["country_name"]),
                "latitude": "%.4f" % float(ret["latitude"]),
                "longitude": "%.4f" % float(ret["longitude"]),
            }
        except:
            try:
                url = f"http://free.ipwhois.io/json/{location}"
                ret = requests.get(url).json()
                data = {
                    "url": url,
                    "city": str(ret["city"]),
                    "region": str(ret["region"]),
                    "country": str(ret["country"]),
                    "latitude": "%.4f" % float(ret["latitude"]),
                    "longitude": "%.4f" % float(ret["longitude"]),
                }
            except:
                try:
                    url = f"https://ipvigilante.com/json/{location}"
                    ret = requests.get(url).json()
                    data = {
                        "url": url,
                        "city": str(ret["data"]["city_name"]),
                        "region": str(ret["data"]["subdivision_1_name"]),
                        "country": str(ret["data"]["country_name"]),
                        "latitude": "%.4f" % float(ret["data"]["latitude"]),
                        "longitude": "%.4f" % float(ret["data"]["longitude"]),
                    }
                except:
                    data = {
                        "url": "WARN: NO RESPONSE",
                        "city": "null",
                        "region": "null",
                        "country": "null",
                        "latitude": "0.0000",
                        "longitude": "0.0000",
                    }

    return data


def main():

    pprint(geolocate())


if __name__ == "__main__":

    main()
