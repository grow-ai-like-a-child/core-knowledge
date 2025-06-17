import pandas as pd
import yaml

for mode in ['image_only', 'single', 'total']:
    df3 = pd.read_csv(f'/Users/kaiagao/Documents/top_{mode}_models_by_concept.csv')
    print(df3.columns)
    df3.loc[:, df3.columns[1:]] *= 100  # Scale columns from index 1 onwards by 100
    df3.rename(columns={'true_mean': 'mean'}, inplace=True)

    # Convert to list of dictionaries
    records3 = df3.to_dict(orient='records')

    # Save to YAML
    yaml_file_path3 = f"_data/leaderboard_{mode}.yml"
    with open(yaml_file_path3, 'w') as file:
        yaml.dump(records3, file, sort_keys=False)