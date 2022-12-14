

from distutils import filelist
from doctest import OutputChecker
import pandas as pd
import os

def merge_csv():
    input_path = r'/Users/hongz/test_data/predict_data/'
    output_path = r'/Users/hongz/test_data/'
    result_name = 'merged_table.csv'

    os.chdir(input_path)
    file_list = os.listdir()
    df = pd.read_csv(input_path+file_list[0])
    df['CODE'] = file_list[0]
    df.to_csv(output_path+result_name, index=False)
    for i in range(1, len(file_list)):
        if not file_list[i].startswith('.'):
            df = pd.read_csv(input_path+file_list[i])
            df['CODE'] = file_list[i]
            df.to_csv(output_path+result_name, index=False, header=False, mode='a+')
merge_csv()
