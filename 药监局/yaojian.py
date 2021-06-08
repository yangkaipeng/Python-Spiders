import requests

from user_agent import generate_user_agent

headers = {
    'User-Agent':"SFDANewVerison/3.4.1 (iPad; iOS 14.2; Scale/2.00)",
    'tzRgz52a':'BntpPfYtzEY-sCenF7VZtDncs4-JBZFjkd6MokZyqT3eUlnE6lWep3IbFGLLAHrWF-Yc4CiRfCU5Z1ABucXRjVkCy7USRsEkHHy6fD13Dc6kEKwZ8mtBQyCOCRxo_huSlYm8A2i1uhUw1_IC0J8S8OPVz2CbSrU51X8Rv8V1Krc6a6NhRKj9GU4kkWVH.dbzR4cr8gkwSWb45HMHKyYI679WzPo5BtVClgatQF4CTMWKKC4tNf1UjoFLe-Pyb_U_vKv1R72mls5C9DFlSoseIfa80p2bUWlxpnAAHfV371zSJeyNxSRM97JTKgYhq8Iejxg2OD6tktD0EuEJOruJIws1R7Ig0r2M4iMnxDx5rRwnPk2dn4gMEXvuHTv-KDPr90iK2uVym39mdF3lvAljt_cBDXXKBSloyhC33kdvtseNYiRQUPpNIveeqHHxrDKsiPRN64T5PzBKoBU3gYNhxiz7Ij6qzV9RBFBa1yL06Wx0VTDPzPgXkBa_50nDXW-y-PkT3CkO0xvKTIFeD9LFrq73lq-78fcv8oCmL7dfmgy0W_Tu5xR56whA-rkyLZDA73ukaTgnc1KJ643VFTjtufIYOSyoG3TfXpGwxqqqEFredfsA8rQeCM_VPfRRkZJPR4Q10R3',
    'Cookie':'JSESSIONID=F4D5AD583CBD41CCF84E4872F9131E28;acw_tc=3ccdc16a16173651816028767e159394a4aa9ae6286243b603592d0c9950c6',
    'Host':'mobile.nmpa.gov.cn'
}


url = 'http://mobile.nmpa.gov.cn/datasearch/QueryList?tableId=25&searchF=Quick%20Search&searchK=&pageIndex=4&pageSize=20'

response = requests.get(url,headers=headers)

print(response)