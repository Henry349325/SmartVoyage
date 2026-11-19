dockerfile
# 使用轻量级 Python 镜像
FROM python:3.10-slim

# 设置工作目录
WORKDIR /app

# 先拷贝依赖文件并安装，利用 Docker 缓存
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 拷贝所有代码
COPY . .

# 默认启动命令（会被 docker-compose 覆盖）
CMD ["python", "main.py"]
