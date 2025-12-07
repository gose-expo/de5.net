# 子域名批量注册工具

这是一个用于批量注册 de5.net 子域名的 Python 脚本，通过自动化的方式向 dnshe.com 提交子域名注册请求。

## 功能说明

- 从文本文件读取子域名列表
- 批量向 dnshe.com 发送注册请求
- 自动检测域名是否已被注册
- 实时输出注册结果

## 环境要求

- Python 3.6+
- requests 库

## 安装依赖

```bash
pip install requests
```

## 配置说明

在使用脚本之前，需要修改以下配置参数：

### 1. 根域名 (ROOT_DOMAIN)

```python
ROOT_DOMAIN = "de5.net"  # 修改为你的根域名
```

### 2. CSRF Token (CSRF_TOKEN)

从浏览器开发者工具中获取最新的 CSRF token：

1. 登录 https://my.dnshe.com
2. 打开浏览器开发者工具（F12）
3. 进入 Network 标签页
4. 手动注册一个子域名
5. 找到对应的请求，查看 Form Data 中的 `cfmod_csrf_token` 值
6. 复制该值并替换脚本中的 `CSRF_TOKEN`

### 3. Cookies

从浏览器中获取你的登录 Cookie：

1. 在开发者工具的 Network 标签页中
2. 找到任意请求的 Request Headers
3. 复制 Cookie 值
4. 更新脚本中的 `COOKIES` 字典

```python
COOKIES = {
    "fc_fp": "你的值",
    "fc_tz": "Asia/Shanghai",
    "fc_lang": "zh-CN",
    "WHMCSUser": "你的值",
    "WHMCSy551iLvnhYt7": "你的会话ID",
    "disable_renewal_token": "你的值",
}
```

## 使用方法

### 1. 准备子域名列表

创建 `subdomain.txt` 文件，每行一个子域名（不包含根域名部分）：

```
test
demo
app
www
blog
```

### 2. 运行脚本

```bash
python 1.py
```

### 3. 查看结果

脚本会实时输出每个子域名的注册结果：

```
test.de5.net → 注册成功
demo.de5.net → 已被注册
app.de5.net → 注册成功
```

## 文件说明

- `1.py` - 主程序脚本
- `subdomain.txt` - 子域名列表文件（每行一个子域名）
- `README.md` - 使用说明文档

## 注意事项

1. **Cookie 时效性**：Cookie 和 CSRF Token 有时效性，如果脚本运行失败，请更新这些值
2. **请求频率**：建议在子域名之间添加适当的延迟，避免请求过于频繁
3. **账号安全**：不要将包含真实 Cookie 的脚本分享给他人
4. **合法使用**：请确保你有权限注册这些子域名，遵守服务条款

## 常见问题

### Q: 提示"已被注册"但实际未注册？

A: 可能是 Cookie 或 CSRF Token 过期，请重新获取并更新配置。

### Q: 所有请求都失败？

A: 检查以下几点：
- 网络连接是否正常
- Cookie 是否有效（尝试在浏览器中重新登录）
- CSRF Token 是否最新
- 目标网站是否可访问

### Q: 如何添加请求延迟？

A: 在 `main()` 函数的循环中添加 `time.sleep()`：

```python
import time

for sub in subs:
    success, msg = register_subdomain(sub)
    print(f"{sub}.{ROOT_DOMAIN} → {msg}")
    time.sleep(1)  # 每个请求间隔1秒
```

## 免责声明

本工具仅供学习和个人使用，使用者需遵守相关网站的服务条款。使用本工具产生的任何后果由使用者自行承担。
