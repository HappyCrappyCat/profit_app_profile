from csv import reader

# with open('AppleStore.csv') as a_opener:
#     reader = reader(a_opener)
#     apple = list(reader)
#     app_headers = apple[:1]
#     app_data = apple[1:]

with open('googleplaystore.csv', encoding="utf8") as g_opener:
    reader2 = reader(g_opener)
    google = list(reader2)
    google_headers = google[:1]
    google_data = google[1:]

def explore_data(dataset, start, end, rows_and_columns=False):
    dataset_slice = dataset[start:end]    
    for row in dataset_slice:
        print(row)
        print('\n') # adds a new (empty) line after each row

    if rows_and_columns:
        print('Number of rows:', len(dataset))
        print('Number of columns:', len(dataset[0]))
        

        
for i in range(0,len(google_data)-1):
    if len(google_data[i]) != len(google_headers[0]):
        print(i, google_data[i])
        del google_data[i]
        print("row {} has been deleted".format(i))
    
# print(len(google_headers[0]))        
# app_first_5_rows = explore_data(google_data, 0, 5, rows_and_columns = True)
dup_apps = []
unique_apps = []
        
for app in google_data:
    name = app[0]
    if name not in unique_apps:
        unique_apps.append(name)
    else:
        dup_apps.append(name)

print("Number of dup apps: ",len(dup_apps))

for pp in dup_apps:
    name = pp[0]
    if name == 'Instagram':
        print(pp)

print("Number of unique apps: ", len(unique_apps))        

reviews_max = {}
for row in google_data:
    app_name = row[0]    
    n_reviews = float(row[3])
#     if n_reviews.isdigit() == False:
#         print(row)
    if app_name not in reviews_max:
        reviews_max[app_name] = n_reviews
    elif app_name in reviews_max and reviews_max[app_name] < n_reviews:
        reviews_max[app_name] = n_reviews

# print(len(reviews_max))

android_clean = []
already_added = []

for app in google_data:
    name = app[0]
    n_reviews = float(app[3])    
    for i in reviews_max:
        if n_reviews == reviews_max[name] and name not in already_added:
            android_clean.append(app)
            already_added.append(name)
        

print(len(android_clean))
