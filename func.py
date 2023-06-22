import requests

def request_from_pribate_EC2(prompt):
    # 发起对服务A的POST请求
    # url = 'http://0.0.0.0:8888/'
    url = 'http://10.10.1.141:8888'
    data = {'prompt': prompt}  # 传递的数据示例
    response = requests.post(url, json=data)
    response_data = response.json()

    return response_data['answer']


