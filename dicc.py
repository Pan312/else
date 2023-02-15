capitals = {'USA':'Washington DC','India':'New Dehli'}
capitals.update({'Germany':'Berlin'})
#print(capitals.keys())
#print(capitals.values())
capitals.update({'USA':'Moscow'})

for key,value in capitals.items():
    print(key,value)