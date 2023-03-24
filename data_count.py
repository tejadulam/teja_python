import csv
with open('data.csv', newline='\n') as csvfile:
    # datareader = csv.reader(csvfile, delimiter=';', quotechar='|')
    # data extracted to data reader and retruns a reader object
    
    datareader = csv.reader(csvfile, delimiter=',')
    
    data_iter = iter(datareader)
    col_names = next(data_iter)
    csv_data = []
    for x in data_iter:
        csv_data.append(x)
print(csv_data)

# country = {}
# for x in csv_data:
#     if country.get(x[5]):
#         country[x[5]] += 1
#     else:
#         country[x[5]] = 1
# print()
# print(country)
# print("Highest Population :",max(country,key=country.get))

country_c = {}
for x in csv_data:
    if x[5] not in country_c:
        country_c[x[5]] = 1
    else:
        country_c[x[5]]+=1
country = max(country_c,key=lambda x:country_c[x])
print(country_c)
print("Highest Population:",country,country_c[country])
