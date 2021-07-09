# f = 'jobs.csv'
# csv = open('./{}'.format(f), mode="w")
# csv.write('')
# csv.close
import csv

with open('jobs.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['企業名', '仕事内容', '初年度年収'])
