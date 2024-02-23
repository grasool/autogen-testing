#autobuildworksrecent.p

import autogen
from autogen.agentchat.contrib.agent_builder import AgentBuilder


llm_config = {
    "config_list": [
        {
            "model": "mistral",
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




def start_task(execution_task: str, agent_list: list):
    group_chat = autogen.GroupChat(agents=agent_list, messages=[], max_round=12)
    manager = autogen.GroupChatManager(groupchat=group_chat, llm_config=llm_config)
    agent_list[0].initiate_chat(manager, message=execution_task)


builder = AgentBuilder(llm_config=llm_config)
