import pandas as pd

read_file = pd.read_csv (r'test_list_category_img.txt')
read_file.to_csv (r'test_list_category_img.csv', index=None)