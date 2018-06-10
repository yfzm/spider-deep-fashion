import json
import os
import urllib.request

# break at 6950 243.json

JSON_FILE_ROOT = "../output/json"
img_num = 5706

for rt, dirs, files in os.walk(JSON_FILE_ROOT):
    for file in files:
        current_file = os.path.join(rt, file)
        # print(current_file)

        with open(current_file, encoding="utf-8") as f:
            obj = json.load(f)
            resultList = obj['result']['resultList']
            print("\n" + current_file + " loaded!")

            for index, entry in enumerate(resultList):
                img_url = entry['mediaUrl']

                response = urllib.request.urlopen(img_url)
                img = response.read()

                with open('../output/img/{}.jpg'.format(img_num), 'wb') as img_file:
                    img_file.write(img)

                if (img_num + 1) % 10 == 0:
                    print("{} complete.".format(img_num + 1))

                img_num += 1
    break




