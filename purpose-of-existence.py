#multi-conversation.py

from autogen import AssistantAgent, UserProxyAgent, config_list_from_json
import autogen

llm_config = {
    "config_list": [
        {
            "model": "mistral",
            "api_key": 'ollama',
            "base_url": 'http://localhost:11434/v1/',
        },
            ],
    "temperature": 0.5,
    "timeout": 300,
}



llm_config = llm_config
user_proxy = autogen.UserProxyAgent(
    name="User_proxy",
    system_message="A human admin.",
    code_execution_config={
        "last_n_messages": 2,
        "work_dir": "groupchat",
        "use_docker": False,
    },  # Please set use_docker=True if docker is available to run the generated code. Using docker is safer than running the generated code directly.
    human_input_mode="TERMINATE",
)

coder = autogen.AssistantAgent(
    name="Coder",
    llm_config=llm_config,
)

pm = autogen.AssistantAgent(
    name="Productmanager",
    system_message="Discuss the purpose of existeance.",
    llm_config=llm_config,
)
groupchat = autogen.GroupChat(agents=[user_proxy, coder, pm], messages=[], max_round=12)
manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=llm_config)



user_proxy.initiate_chat(
    manager, message=" Discuss the purpose of existence with focus on (1) life, (2) death. \
        (3) the universe, (4) the meaning of life, (5) the purpose of existence."
)
# type exit to terminate the chat