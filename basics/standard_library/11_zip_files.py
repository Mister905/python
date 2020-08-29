# Zipfile Module
# Linux CLI
# zip archivename.zip 11_purchased.txt 11_wishlist.txt

import zipfile

# Open and List
zip = zipfile.ZipFile('11_archive.zip', 'r')
print(zip.namelist())

# Metadata in the zip folder
for meta in zip.infolist():
    print(meta)

info = zip.getinfo("11_purchased.txt")
print(info)

# Access to files in zip folder
print(zip.read("11_wishlist.txt"))
with zip.open('11_wishlist.txt') as f:
    print(f.read())

# Extracting files
#zip.extract("purchased.txt")
zip.extractall()

# Closing the zip
zip.close()

