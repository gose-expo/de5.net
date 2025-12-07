import requests

# 目标 URL
URL = "https://my.dnshe.com/index.php?m=domain_hub"

# 固定参数
ROOT_DOMAIN = "de5.net"
CSRF_TOKEN = "ab7d7e53bea9c9c099688f85ef59c375b979cdc59fc19db75d1c551664d8a192"

# 请求头（你提供的，可直接使用）
HEADERS = {
    "Host": "my.dnshe.com",
    "Origin": "https://my.dnshe.com",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded",
    "Referer": "https://my.dnshe.com/index.php?m=domain_hub",
}

# Cookie（⚠️ 请替换成你自己的）
COOKIES = {
    "fc_fp": "2039668840",
    "fc_tz": "Asia/Shanghai",
    "fc_lang": "zh-CN",
    "WHMCSUser": "",
    "WHMCSy551iLvnhYt7": "",
    "disable_renewal_token": "",
}

def register_subdomain(subdomain: str):
    """尝试注册一个子域名并返回结果"""
    data = {
        "action": "register",
        "rootdomain": ROOT_DOMAIN,
        "subdomain": subdomain,
        "cfmod_csrf_token": CSRF_TOKEN
    }

    resp = requests.post(URL, headers=HEADERS, cookies=COOKIES, data=data)

    # 网站通常返回 HTML，因此用 text
    text = resp.text

    error_str = f"域名 '{subdomain}.{ROOT_DOMAIN}' 已被注册"

    if error_str in text or "已被注册" in text:
        return False, "已被注册"
    else:
        # 说明没有出现报错，就认为成功
        return True, "注册成功"

def main():
    # 从 txt 文件读取子域名，一行一个
    with open("subdomain.txt", "r", encoding="utf-8") as f:
        subs = [line.strip() for line in f if line.strip()]

    for sub in subs:
        success, msg = register_subdomain(sub)
        print(f"{sub}.{ROOT_DOMAIN} → {msg}")

if __name__ == "__main__":
    main()

