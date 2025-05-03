import joblib
import pandas as pd
from colorama import init, Fore
from feature_extractor import extract_features
from time import time


init(autoreset=True)

def detect_phishing(url: str):

    model = joblib.load('../trained_model/trained_model.pk1')

    features = extract_features(url)

    features_list = [
            features['url_length'],
            features['has_at_symbol'],
            features['dot_count'],
            features['slash_count'],
            features['dash_count'],
            features['has_ip'],
            features['has_https'],
            features['subdomain_count'],
            features['has_suspicious_words'],
            features['has_valid_ssl'],
            ]

    features_df = pd.DataFrame([features_list], columns=[
        'url_length',
        'has_at_symbol',
        'dot_count',
        'slash_count',
        'dash_count',
        'has_ip',
        'has_https',
        'subdomain_count',
        'has_suspicious_words',
        'has_valid_ssl'
        ])

    prediction = model.predict(features_df)

    return prediction[0]

if __name__ == '__main__':
    while True:
        url = input('\nput the URL (or q to quit):  ').strip()
        if url.lower() == 'q':
            break
        if not url.startswith(('https://', 'http://')):
            print(Fore.YELLOW + 'PLEASE INSERT HTTP:// OR HTTPS://')
            continue

        start = time()
        result = detect_phishing(url)
        elapsed = time() - start

        if result == 1:
            print(Fore.RED + 'PHISHING ALERT!!!')
        else:
            print(Fore.GREEN + 'no phishing detected')

        print(Fore.CYAN + f'detection time {elapsed:.2f} seconds')

