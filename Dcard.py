import pandas as pd
import requests
import json
import re
import csv

'''
    使用DcardAPI : API: https://www.dcard.tw/service/api/v2/posts
    從Dcard
'''

if __name__ == '__main__':
    response = requests.get('https://www.dcard.tw/service/api/v2/posts')
    data = json.loads(response.text)

#轉換成dataframe
    df = pd.DataFrame(data)
    # 印出資料前三行，確認資料載入如同預期
    #print(df.head(3))

    with open('Dcard_articles.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2,
                  sort_keys=True, ensure_ascii=False)


    f = open('result.json', 'a+')
    result = []
    temp = {}
    # temp['name'] = 'Tony'
    # temp['age'] = '21'
    # temp['hobbies'] = ['basketball', 'tennis']
    temp['score'] = 'ddaff'
    result.append(temp)

    f.write(json.dumps(result, ensure_ascii=False))

#json檔 轉存成 csv檔
    df = pd.read_json(r'C:\Python_CFI102\Dcard\Dcard_articles.json')
    df.to_csv(r'C:\Python_CFI102\Dcard\Dcard_articles.csv',encoding='utf-8', index=None)

    # print(json_resp[1]['excerpt'])
    #
    # for i in range(0,10):
    #     print(json_resp[i]['excerpt'])


# def convertScore(score):
#     if score >= 4:
#         return 'good'
#     elif score == 3:
#         pass
#     else:
#         return 'bad'
#
#
# def Convert(google):
#     google['status'] = google['評等'].map(lambda e: convertScore(e))
#     google = google[google['status'].isin(['good', 'bad'])]
#     google['status'] = google['status'].replace({'good': 1, 'bad': 0})
#     google = google.drop(columns=['評等', '評論者'])
#     return google