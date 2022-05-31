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

eng_apps = []

def eng_str_check(strng):
    non_eng_chr = 0
    for char in strng:
        if ord(char) > 127 or ord(char) < 0:
            non_eng_chr += 1
            if non_eng_chr > 3:
                return False
    return True

for app in google_data:
    if eng_str_check(app[0]) == True:
        eng_apps.append(app)
        
print('Number of English apps: ',len(eng_apps))

free_apps = []

for app in eng_apps:
    if app[6].lower() == 'free':
        free_apps.append(app)

print('Number of free apps: ',len(free_apps))


def freq_table(dataset, index):
    freq_tbl = {}
    for row in dataset:
        if row[index] not in freq_tbl:
            freq_tbl[row[index]] = 1
        else:
            freq_tbl[row[index]] += 1
    return freq_tbl        


def display_table(dataset, index):
    table = freq_table(dataset, index)
    table_display = []
    for key in table:
        key_val_as_tuple = (table[key], key)
        table_display.append(key_val_as_tuple)

    table_sorted = sorted(table_display, reverse = True)
    for entry in table_sorted:
        print(entry[1], ':', entry[0])
        
