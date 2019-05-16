import pandas as pd
import matplotlib.pyplot as plt

inputfilePath= "/home/minal/githubcodes/data-analysis-tvsalesdata/Minakshi/output/televisionvalidrecords"
outputfilePath = "/home/minal/githubcodes/data-analysis-tvsalesdata/Minakshi/output/TotalSalesPlot"
tv_sales_data = pd.read_csv(inputfilePath,sep='|')
columnlist = ['CompanyName','ProductName','Size in inches','State','Pin Code','Price']

total_sales = tv_sales_data.loc[:,['CompanyName','ProductName']]
total_sales_perunit = total_sales.groupby('CompanyName').count()
total_sales_perunit.rename(columns={'ProductName':'Total Sales'},inplace=True)
print(total_sales_perunit)
total_sales_perunit.plot(kind='bar')
plt.ylabel("Total Sales")
#plt.xlabel("Listed Companies")
plt.savefig(outputfilePath)


