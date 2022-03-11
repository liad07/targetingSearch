import webbrowser
city=input('enter a city\n')
street=input('enter a street\n')
numhouse=input('enter num of the house\n')
join=input('Enter login\n')
webbrowser.open(f"https://services.israelpost.co.il/zip_data.nsf/SearchZip?OpenAgent&Location={city}&POB=&Street={street}&House={numhouse}&Entrance={join}")
print(city,street,numhouse,join)
