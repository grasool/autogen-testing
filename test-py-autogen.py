#test-py-autogen.py

from autogen import AssistantAgent, UserProxyAgent, config_list_from_json
import autogen

llm_config = {
    "config_list": [
        {
            "model": "llama2",
            "api_key": 'ollama',
            "base_url": 'http://localhost:11434/v1/',
        },
        # {
        #     "model": "llama-7B",
        #     "base_url": "http://localhost:11434/v1/",
        #     "api_type": "openai",
        #     "api_key": 'ollama',
        # },
    ],
    "temperature": 0.9,
    "timeout": 300,
}

# print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
# assistant = AssistantAgent("assistant", llm_config=llm_config)
# user_proxy = UserProxyAgent("user_proxy", code_execution_config={"work_dir": "coding", "use_docker": "python:3"}) # IMPORTANT: set to True to run code in docker, recommended
# user_proxy.initiate_chat(assistant, message="Plot a chart of NVDA and TESLA stock price change YTD.")
# # This initiates an automated chat between the two agents to solve the task

# create an AssistantAgent named "assistant"
assistant = autogen.AssistantAgent(
    name="assistant",
    llm_config=llm_config,
)
# create a UserProxyAgent instance named "user_proxy"
user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=10,
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
    code_execution_config={
        "work_dir": "coding",
        "use_docker": False,  # Please set use_docker=True if docker is available to run the generated code. Using docker is safer than running the generated code directly.
    },
)
# the assistant receives a message from the user_proxy, which contains the task description
chat_res = user_proxy.initiate_chat(
    assistant,
    message="""What date is today? Compare the year-to-date gain for META and TESLA.""",
    summary_method="reflection_with_llm",
)