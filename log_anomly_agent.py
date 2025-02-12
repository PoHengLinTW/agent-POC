from dotenv import load_dotenv
from smolagents import tool
# Required for HuggingFace API key
load_dotenv()

# Envvar
USE_LOCAL_MODEL=False
LOCAL_MODEL=''
# LOCAL_MODEL="ollama/llama3.1:8b-instruct-q8_0"
# LOCAL_MODEL="ollama/deepseek-coder-v2:16b-lite-instruct-q2_K"
# LOCAL_MODEL="ollama/qwen2.5-coder:7b-instruct-q2_K"
# LOCAL_MODEL="ollama/qwen2.5-coder:32b-instruct-q2_K"

@tool
def getServerLogs() -> str:
    """
    Allows you to get the server logs. Returns a string representation of the result.
    Each row contains 
    IP, 
    timestamp, 
    HTTP method and route, 
    HTTP response status code, 
    domain name, 
    and the device users use.
    Here is a few examples:
    192.168.1.109 - - [05/Feb/2025:08:01:50 +0000] "POST /api/cart/remove HTTP/1.1" 200 124 "https://example.com/cart" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"
    10.0.0.34 - - [05/Feb/2025:08:01:51 +0000] "GET /robots.txt HTTP/1.1" 200 67 "-" "Googlebot/2.1"
    172.16.0.59 - - [05/Feb/2025:08:01:52 +0000] "GET /api/featured HTTP/1.1" 200 2341 "https://example.com" "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    192.168.1.110 - - [05/Feb/2025:08:01:53 +0000] "GET /support HTTP/1.1" 301 185 "-" "Mozilla/5.0 (Android 13; Mobile)"
    """
    with open("web-server-logs.txt", "r") as file:
        content = file.read()
        return content
    

from smolagents import CodeAgent, HfApiModel, LiteLLMModel

if USE_LOCAL_MODEL is True:
    model = LiteLLMModel(
        api_key="",
        api_base="http://localhost:11434",
         model_id=LOCAL_MODEL,
        num_ctx=16384
    )
else:
    model=HfApiModel("Qwen/Qwen2.5-Coder-32B-Instruct")

agent = CodeAgent(
    tools=[getServerLogs],
    model=model,
    max_steps=10
)

agent.run("Today is 10/Feb/2025, inspect the web server web log and extract all errors (400 - 500), give me a summary of who last login errors in last two days")
