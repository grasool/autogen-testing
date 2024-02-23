#test-py-autogen.py

from autogen import AssistantAgent, UserProxyAgent, config_list_from_json

llm_config = {
    "config_list": [
        {
            "model": "llama2",
            "api_key": 'ollama',
            "base_url": 'http://localhost:11434/v1/',
        },
        {
            "model": "llama-7B",
            "base_url": "http://localhost:11434/v1/",
            "api_type": "openai",
            "api_key": 'ollama',
        },
    ],
    "temperature": 0.9,
    "timeout": 300,
}

print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
assistant = AssistantAgent("assistant", llm_config=llm_config)
user_proxy = UserProxyAgent("user_proxy", code_execution_config={"work_dir": "coding", "use_docker": "python:3"}) # IMPORTANT: set to True to run code in docker, recommended
user_proxy.initiate_chat(assistant, message="Plot a chart of NVDA and TESLA stock price change YTD.")
# This initiates an automated chat between the two agents to solve the task