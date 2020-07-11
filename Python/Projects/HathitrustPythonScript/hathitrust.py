#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ONLY WORKS WITH FULL-TEXTS

import requests
import os
import img2pdf
import re

def main():

    # CAMBIA ESTO !! !!
    hathitrust_handle = 'https://hdl.handle.net/2027/uiuo.ark:/13960/t0wp9vx13'
    folder_name = 'Bulletin of the American Library Association 1908'
    pages = 132
    # CAMBIA ESTO !! !!

    file_id = re.match(r'^https\:\/\/hdl.handle.net/\d+\/(.+)$', hathitrust_handle).group(1)
    link = 'https://babel.hathitrust.org/cgi/imgsrv/image?id=' + file_id + ';seq={}'

    # Prepare new folder to store
    path = os.path.dirname( os.path.abspath(__file__) )
    new_folder = os.path.join(path, folder_name)
    try:
        os.mkdir(new_folder)
    except FileExistsError:
        print(f'[!] Folder {folder_name} already exists!')

    os.chdir(new_folder)
    width = len(str(pages))


    page = 1
    # Download images and store them
    for i in range(1, pages + 1):
        response = requests.get(link.format(page))
        file_name = os.path.join(new_folder, f'{str(page).zfill(width)}.jpg')

        if response.status_code == 200:
            with open(file_name, 'wb') as fp:
                fp.write(response.content)

            print(f'[✓] Found and downloaded page {page}. {file_name}')
        else:
            print(f'[✗] Could not find or download page {page}')

        page += 1


    # Get jpg images from current folder and convert them to pdf
    image_list = os.listdir()
    image_list = list(filter(lambda x: x.endswith('.jpg'), image_list))

    output_name = os.path.join(new_folder, f'{folder_name}.pdf')

    with open(output_name, 'wb') as fp:
        fp.write(img2pdf.convert(image_list))


if __name__ == "__main__":
    main()

