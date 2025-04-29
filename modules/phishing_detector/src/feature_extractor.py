import ipaddress
import socket
import ssl
import tldextract
from urllib.parse import urlparse

    
def extract_features(url: str) -> dict:
    features = {}

    features['url_length'] = len(url)

    features['has_at_symbol'] = '@' in url

    features['dot_count'] = url.count('.')

    features['slash_count'] = url.count('/')

    features['dash_count'] = url.count('-')

    # instead of true and false, i will be using 1/0 because it hells the machine learning
    try:
        ipaddress.ip_address(urlparse(url).netloc)
        features['has_ip'] = 1
    except ValueError:
        features['has_ip'] = 0

    secure_protocol = urlparse(url).scheme
    features['has_https'] = 1 if secure_protocol == 'https' else 0

    extracted = tldextract.extract(url)
    features['subdomain_count'] = extracted.subdomain.count('.') + 1 if extracted.subdomain else 0

    suspicious_words = ['login', 'verify', 'update', 'free', 'security', 'ebayisapi', 'banking']
    features['has_suspicious_words'] = int(any(word in url.lower() for word in suspicious_words))

    def is_ssl_valid(domain) -> bool:
        try:
            context = ssl.create_default_context()
            with socket.create_connection((domain, 443), timeout=5) as sock:
                with context.wrap_socket(sock, server_hostname=domain) as ssock:
                    cert = ssock.getpeercert()
                    return True 
        except Exception as e:
            return False
    
    domain = urlparse(url).netloc
    features["has_valid_ssl"] = int(is_ssl_valid(domain))

    return features

