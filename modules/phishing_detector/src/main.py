import joblib
import pandas as pd
from feature_extractor import extract_features


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

    result = 'PHISHING ALERT!!!' if prediction[0] ==1 else 'just for testing' #put continue

    print(result)

if __name__ == '__main__':
    url = input('put the url: ')
    detect_phishing(url)

