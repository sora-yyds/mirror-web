import datetime
import time
import requests
import os

# 获取时间戳
def get_time():
    t = datetime.datetime.now()
    end_time = int(t.timestamp() * 1000)
    start_time = int((t - datetime.timedelta(hours=6)).timestamp() * 1000)  # 时间范围为6小时前到现在
    return str(start_time), str(end_time)

# 下载 pic
def download_pic():
    grafana_server = "192.168.31.104:3000"  # 替换为你的 Grafana 服务器地址
    api_key = "xxxx"  # 替换为你的 API Key

    # 构建 Grafana 面板的 URL
    url = (
        f'http://{grafana_server}/render/d-solo/fdgbbcg2md3b4d/c0a88e3a-ff92-5c8a-a3af-c42614a4e1ad'
        f'?orgId=1&refresh=10s&var-datasource=sora-bucket&var-server=&var-inter=1s&from='
        f'{get_time()[0]}&to={get_time()[1]}&panelId=60200&width=546&height=399.81&tz=Asia%2FShanghai'
    )

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Accept": "application/json",
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        # 设置保存路径，确保 static/status 目录存在
        save_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../static/status")
        os.makedirs(save_path, exist_ok=True)  # 如果目录不存在，则创建

        img_name = os.path.join(save_path, "DiskIOBytes.png")
        
        # 保存图片
        with open(img_name, "wb") as f:
            f.write(response.content)
        
        print(f"图片已下载: {img_name}")
        return img_name
    else:
        print(f"下载失败，HTTP 状态码: {response.status_code}, 响应内容: {response.text}")
        return None

download_pic()
