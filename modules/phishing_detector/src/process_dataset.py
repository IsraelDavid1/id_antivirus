import pandas as pd
from feature_extractor import extract_features

def process_dataset(input_csv: str, output_csv: str):
    df = pd.read_csv(input_csv)
    
    features_list = []

    for index, row in df.iterrows():
        url = row['url']
        label = row['label']
        features = extract_features(url)
        features['label'] = label
        features_list.append(features)

    processed_df = pd.DataFrame(features_list)
    processed_df.to_csv(output_csv, index=False)
    print(f'Features salvas em: {output_csv}')

if __name__ == '__main__':
    input_csv = '../dataset/urls.csv'
    output_csv = '../dataset/features.csv'
    process_dataset(input_csv, output_csv)

