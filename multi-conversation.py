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



llm_config = llm_config
user_proxy = autogen.UserProxyAgent(
    name="User_proxy",
    system_message="A human admin.",
    code_execution_config={
        "last_n_messages": 2,
        "work_dir": "groupchat",
        "use_docker": True,
    },  # Please set use_docker=True if docker is available to run the generated code. Using docker is safer than running the generated code directly.
    human_input_mode="TERMINATE",
)
coder = autogen.AssistantAgent(
    name="Coder",
    llm_config=llm_config,
)
pm = autogen.AssistantAgent(
    name="Product_manager",
    system_message="Discuss and finalize diagnotic and treatment plan.",
    llm_config=llm_config,
)
groupchat = autogen.GroupChat(agents=[user_proxy, coder, pm], messages=[], max_round=12)
manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=llm_config)



user_proxy.initiate_chat(
    manager, message="A 65-year-old patient with a history of smoking and construction \
          work presents with progressive breathlessness, a dry cough, and unexplained weight loss.\
            Physical examination reveals digital clubbing and bilateral basal crackles. \
            Laboratory tests show elevated inflammatory markers, and a chest X-ray \
            suggests interstitial lung disease. As the Medical AI Bayesian Programmer, \
            integrate inputs from the Pulmonology, Rheumatology, Cardiology, Nephrology, \
            and General Internal Medicine Specialist Agents to developne a treatment plan. \
            Begin by establishing a list of potential diagnoses. \
            Update these diagnosis based on additional findings from HRCT, \
            pulmonary function tests, serological markers, and other suggested diagnostic tests.\
            Conduct a cross-specialty validation phase for feedback and adjust the disgnosis \
            to achieve a consensus. Propose a comprehensive treatment plan, referencing current \
            medical guidelines and patient history. Ensure all diagnostic and treatment \
            recommendations are supported by evidence-based information from reputable \
            medical databases such as PubMed and Cochrane Library. Conclude the task by \
            presenting the final diagnosis with a detailed \
            treatment plan.."
)
# type exit to terminate the chat