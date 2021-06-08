import requests
import json

headers = {
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",
    "Referer":"https://www.itjuzi.com/bulletin",
    "Cookie":"juzi_user=946027; juzi_token=bearer%20eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvd3d3Lml0anV6aS5jb21cL2FwaVwvYXV0aG9yaXphdGlvbnMiLCJpYXQiOjE2MTg0MDIxNzQsImV4cCI6MTYxODQwOTM3NCwibmJmIjoxNjE4NDAyMTc0LCJqdGkiOiJpMHk5MXpxRG5TbVRoaTZTIiwic3ViIjo5NDYwMjcsInBydiI6IjIzYmQ1Yzg5NDlmNjAwYWRiMzllNzAxYzQwMDg3MmRiN2E1OTc2ZjciLCJ1dWlkIjoiQ0VKc2pCIn0.3nWU1QOYo93YHG_lWDp__u4rXYer3bZoBia82cvDOU4",
}

n=2
data ={
    "page": n,
}
url = "https://www.itjuzi.com/api/companys"

response = requests.post(url,headers=headers, data=data, verify=False)
print(response.text)

# res = json.loads(response.text)
# for i in res.get("data")['info']:
#     print(i.get('title'))