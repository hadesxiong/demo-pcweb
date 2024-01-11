# coding=utf8
import os
from dotenv import load_dotenv

# 读取配置
load_dotenv()

class CorsMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self,request):
        response = self.get_response(request)
        response["Access-Control-Allow-Origin"] = os.getenv('API_HOST')
        response["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
        response["Access-Control-Allow-Headers"] = "Content-Type"
        return response