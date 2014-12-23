import requests
import pygeoip
from classes.logger import logger


class GeoIpProvider:
    _geo_ip_service = pygeoip.GeoIP("/var/geo_ip/GeoIP.dat", pygeoip.MEMORY_CACHE)

    def __init__(self, ip):
        self._ip = ip

    def get_ip_info(self):
        result = \
            {
                "ip": self._ip,
                "country_code": "---",
                "country_name": "---",
                "region_code": "---",
                "region_name": "---",
                "city": "---",
                "zipcode": "---",
                "latitude": 0,
                "longitude": 0,
                "metro_code": "0",
                "areacode": "0"
            }
        try:
            result["country_code"] = self._get_ip_info_local()
        except Exception, e:
            logger.exception(e)
        return result

    def get_ip_country_code(self):
        country_code = "XX"
        try:
            country_code = self._get_ip_info_local()
            if country_code == "":
                country_code = "XX"
        except Exception, e:
            logger.exception(e)
        return country_code

    def _get_ip_info_web(self):
        result = requests.get("http://freegeoip.net/json/{0}".format(self._ip), timeout=30)
        result = result.json()
        return result

    def _get_ip_info_local(self):
        country_code = GeoIpProvider._geo_ip_service.country_code_by_addr(self._ip)
        return country_code
