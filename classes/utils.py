from tldextract.tldextract import TLDExtract
from urlparse import urlparse


class Utils:
    _tld_extract = TLDExtract()

    @staticmethod
    def get_domain_from_url(url):
        if not url or url == "":
            return None
        parsed_url = urlparse(url)
        domain = Utils._tld_extract(parsed_url.netloc)
        domain = domain.domain + "." + domain.suffix
        return domain