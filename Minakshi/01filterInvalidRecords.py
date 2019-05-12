"""
Write a program to filter out the invalid records and store invalid records in separate files.
"""

import pandas as pd


input_file_path = '/home/minal/githubcodes/data-analysis-tvsalesdata/television.txt'
output_file_path_invalidrecords = \
    '/home/minal/githubcodes/data-analysis-tvsalesdata/Minakshi/output/televisioninvalidrecords'
output_file_path_validrecords = \
    '/home/minal/githubcodes/data-analysis-tvsalesdata/Minakshi/output/televisionvalidrecords'
separator = '|'
is_header = None
tv_sales_columns = ['CompanyName','ProductName','Size in inches','State','Pin Code','Price']

tv_sales_data = pd.read_csv(input_file_path,header=is_header,sep= separator)

tv_sales_data.columns = tv_sales_columns

tv_sales_data_invalidrecords = \
    tv_sales_data[tv_sales_data['CompanyName'].isnull()| tv_sales_data['ProductName'].isnull()]
tv_sales_data_validrecords = \
    tv_sales_data[tv_sales_data['CompanyName'].notna() & tv_sales_data['ProductName'].notna()]

tv_sales_data_invalidrecords.to_csv(output_file_path_invalidrecords, header= None , sep= separator )
tv_sales_data_validrecords.to_csv(output_file_path_validrecords, header= None , sep= separator )


