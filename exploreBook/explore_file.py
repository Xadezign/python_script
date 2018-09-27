import os
import csv

#Test
with open('csvFold.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['path','name','file_ext']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for dirname, dirnames, filenames in os.walk(r"C:/Users/Utilisateur/Google Drive/Books"):
        for filename in filenames:
            pathname = os.path.join(dirname, filename)
            name, file_ext = os.path.splitext(filename)
            writer.writerow({'path': pathname, 'name':name, 'file_ext':file_ext})
            print (name, file_ext)

        