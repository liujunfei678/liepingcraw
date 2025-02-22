import requests
import json
import time
import random
from pprint import pprint
url='https://api-c.liepin.com/api/com.liepin.searchfront4c.pc-search-job'

headers = {
    # 接受的响应类型
    'accept': 'application/json, text/plain, */*',
    # 压缩类型
    'accept-encoding': 'gzip, deflate, br, zstd',
    # 语言偏好
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    # 保持连接
    'connection': 'keep-alive',
    # 请求体长度
    'content-length': '406',
    # 请求体类型
    'content-type': 'application/json;charset=UTF-8',
    # 用户 cookies
    'cookie': '__uuid=1736816341742.29; __gc_id=6c6cf53cdb2c44179b708c4c7146d767; need_bind_tel=false; new_user=false; c_flag=3c79ea3f1c5759b7fb9fbab286252f7c; _ga=GA1.1.1098197003.1736816526; imId=9eea429fc1bfbaa8f261c95be713ae5f; imId_0=9eea429fc1bfbaa8f261c95be713ae5f; imClientId=9eea429fc1bfbaa8357e636e1fc5d0d1; imClientId_0=9eea429fc1bfbaa8357e636e1fc5d0d1; _uetvid=bf2d3370d21211ef9301f3402a63ff63; _uetmsclkid=_uet1d1b208023511208a984473087665cf1; _clck=1i1i6f1%7C2%7Cftg%7C0%7C1872; XSRF-TOKEN=m11W2bRzTNOAKJaPmjypGA; __tlog=1740139290677.04%7C00000000%7C00000000%7C00000000%7C00000000; acw_tc=1a0c660317401392922503521e0100ecbbe3123f7fa590bc2aeec6a0920056; Hm_lvt_a2647413544f5a04f00da7eee0d5e200=1740139291; HMACCOUNT=EEF82B6C1EE7924F; Hm_lpvt_a2647413544f5a04f00da7eee0d5e200=1740139708; __session_seq=6; __tlg_event_seq=24; _ga_54YTJKWN86=GS1.1.1740139290.2.1.1740139734.0.0.0',
    # 目标主机
    'host': 'api-c.liepin.com',
    # 请求来源
    'origin': 'https://www.liepin.com',
    # 引用页
    'referer': 'https://www.liepin.com/',
    # 浏览器标识
    'sec-ch-ua': '"Not(A:Brand";v="99", "Microsoft Edge";v="133", "Chromium";v="133"',
    # 移动标识
    'sec-ch-ua-mobile': '?0',
    # 平台标识
    'sec-ch-ua-platform': '"Windows"',
    # 请求目标类型
    'sec-fetch-dest': 'empty',
    # 请求模式
    'sec-fetch-mode': 'cors',
    # 请求站点
    'sec-fetch-site': 'same-site',
    # 用户代理
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0',
    # 客户端类型
    'x-client-type': 'web',
    # 统计信息
    'x-fscp-bi-stat': '{"location": "https://www.liepin.com/zhaopin/?inputFrom=campus_index&workYearCode=1&key=python&scene=input&ckId=u0c4gomgc5fcrz4qt71th9si85etwbt9&"}',
    # 前端版本
    'x-fscp-fe-version': '',
    # 标准信息
    'x-fscp-std-info': '{"client_id": "40108"}',
    # 请求追踪ID
    'x-fscp-trace-id': '954e3c00-1b36-4d3e-9313-f853b589cf5a',
    # 版本号
    'x-fscp-version': '1.1',
    # 请求方式
    'x-requested-with': 'XMLHttpRequest',
    # XSRF令牌
    'x-xsrf-token': 'm11W2bRzTNOAKJaPmjypGA',
}
get_job_list=[]
for i in range(10):
    print(f'正在爬取第{i}页')
    time.sleep(random.randint(1,3))

    data={
        "data": {
            "mainSearchPcConditionForm": {
                "city": "410",
                "dq": "410",
                "pubTime": "",
                "currentPage": i,
                "pageSize": 40,
                "key": "python",
                "suggestTag": "",
                "workYearCode": "1",
                "compId": "",
                "compName": "",
                "compTag": "",
                "industry": "",
                "salary": "",
                "jobKind": "",
                "compScale": "",
                "compKind": "",
                "compStage": "",
                "eduLevel": ""
            },
            "passThroughForm": {
                "scene": "input",
                "skId": "",
                "fkId": "",
                "ckId": "zboqc4bxjj1lckuifa9jcdpllqy3hfua",
                "suggest": None
            }
        }
    }
    res=requests.post(url,headers=headers,data=json.dumps(data))
    print(res.status_code)
    # print(res.text)
    # pprint(res.json())
    job_data=res.json()
    job_list=job_data['data']['data']['jobCardList']
    
    for job in job_list:
        # print(job['comp']['compName'])
        comName=job['comp']['compName']
        compIndustrys=job['comp']['compIndustry']
        complink=job['comp']['link']
        title=job['job']['title']
        dq=job['job']['dq']
        salary=job['job']['salary']
        labels=job['job']['labels']
        try:
            jobkind=job['job']['campusJobKind']
        except:
            jobkind='无'
        get_job_list.append({
            'comName':comName,
            'compIndustrys':compIndustrys,
            'complink':complink,
            'title':title,
            'dq':dq,
            'salary':salary,
            'labels':labels,
            'jobkind':jobkind
        })

with open('job.csv','w',encoding='utf-8') as f:
    f.write('公司名称,公司行业,公司链接,职位,地区,薪资,标签,职位类型\n')
    for job in get_job_list:
        f.write(f"{job['comName']},{job['compIndustrys']},{job['complink']},{job['title']},{job['dq']},{job['salary']},{job['labels']},{job['jobkind']}\n")




