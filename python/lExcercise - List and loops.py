countries = ["India","united states","australia","srilanka","cuba","Iran","poland"]
#count all the countries which are starting with 'I'
# ["India","Iran"]

counter = 0
for country in countries:
    if country[0]== 'I':
        counter = counter + 1

print(counter)





##OTHER METHOD OF THIS
##also print all these countries as a list 
countries = ["India","united states","australia","srilanka","cuba","Iran","poland"]

counter = 0
output = []

for country in countries:
    if country.startswith('I'):
        counter = counter + 1
        output.append(country)

print(counter)
print(output)