from langchain_groq import ChatGroq
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory,InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.messages import HumanMessage,AIMessage
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
import os
from dotenv import load_dotenv
load_dotenv()
groq_api_key=os.getenv("GROUGE_API_KEY")
model=ChatGroq(model="gemma2-9b-it",groq_api_key=groq_api_key)

store = {}

store["num"] =  InMemoryChatMessageHistory(messages=[HumanMessage(content='play 7th video from youtube', additional_kwargs={}, response_metadata={}), AIMessage(content='7 \n', additional_kwargs={}, response_metadata={'token_usage': {'completion_tokens': 5, 'prompt_tokens': 35, 'total_tokens': 40, 'completion_time': 0.009090909, 'prompt_time': 0.000349088, 'queue_time': 0.02239037, 'total_time': 0.009439997}, 'model_name': 'gemma2-9b-it', 'system_fingerprint': 'fp_10c08bf97d', 'finish_reason': 'stop', 'logprobs': None}, id='run-feb57d61-64a6-4985-bd8a-7bd423c29aed-0', usage_metadata={'input_tokens': 35, 'output_tokens': 5, 'total_tokens': 40}), HumanMessage(content='my name is pratik', additional_kwargs={}, response_metadata={}), AIMessage(content='1 \n', additional_kwargs={}, response_metadata={'token_usage': {'completion_tokens': 5, 'prompt_tokens': 53, 'total_tokens': 58, 'completion_time': 0.009090909, 'prompt_time': 0.001826954, 'queue_time': 0.020554703, 'total_time': 0.010917863}, 'model_name': 'gemma2-9b-it', 'system_fingerprint': 'fp_10c08bf97d', 'finish_reason': 'stop', 'logprobs': None}, id='run-b42a0893-2482-470d-b777-5ab268ffafac-0', usage_metadata={'input_tokens': 53, 'output_tokens': 5, 'total_tokens': 58}), HumanMessage(content='play seven video', additional_kwargs={}, response_metadata={}), AIMessage(content='7 \n', additional_kwargs={}, response_metadata={'token_usage': {'completion_tokens': 5, 'prompt_tokens': 69, 'total_tokens': 74, 'completion_time': 0.009090909, 'prompt_time': 0.001838304, 'queue_time': 0.021289953, 'total_time': 0.010929213}, 'model_name': 'gemma2-9b-it', 'system_fingerprint': 'fp_10c08bf97d', 'finish_reason': 'stop', 'logprobs': None}, id='run-3bb6c15b-d7d3-4b58-aa37-77e29a64c6eb-0', usage_metadata={'input_tokens': 69, 'output_tokens': 5, 'total_tokens': 74})])
store["search"] = InMemoryChatMessageHistory(messages=[HumanMessage(content='karen search on youtube what is machne learning', additional_kwargs={}, response_metadata={}), AIMessage(content='"What is machine learning" \n', additional_kwargs={}, response_metadata={'token_usage': {'completion_tokens': 10, 'prompt_tokens': 46, 'total_tokens': 56, 'completion_time': 0.018181818, 'prompt_time': 0.000584077, 'queue_time': 0.02114043, 'total_time': 0.018765895}, 'model_name': 'gemma2-9b-it', 'system_fingerprint': 'fp_10c08bf97d', 'finish_reason': 'stop', 'logprobs': None}, id='run-d9e84faf-ef47-4563-ba79-ef045a9d4e37-0', usage_metadata={'input_tokens': 46, 'output_tokens': 10, 'total_tokens': 56}), HumanMessage(content='search on youtube bbkivines', additional_kwargs={}, response_metadata={}), AIMessage(content='bbkivines \n', additional_kwargs={}, response_metadata={'token_usage': {'completion_tokens': 7, 'prompt_tokens': 70, 'total_tokens': 77, 'completion_time': 0.012727273, 'prompt_time': 0.004840448, 'queue_time': 0.050787737, 'total_time': 0.017567721}, 'model_name': 'gemma2-9b-it', 'system_fingerprint': 'fp_10c08bf97d', 'finish_reason': 'stop', 'logprobs': None}, id='run-0011f8e3-5564-4ee3-b249-0f090755cca5-0', usage_metadata={'input_tokens': 70, 'output_tokens': 7, 'total_tokens': 77})])
store["classify"] = InMemoryChatMessageHistory(messages=[HumanMessage(content='karen search on youtube what is machne learning', additional_kwargs={}, response_metadata={}), AIMessage(content='1 \n\n', additional_kwargs={}, response_metadata={'token_usage': {'completion_tokens': 6, 'prompt_tokens': 114, 'total_tokens': 120, 'completion_time': 0.010909091, 'prompt_time': 0.003549202, 'queue_time': 0.020691006999999997, 'total_time': 0.014458293}, 'model_name': 'gemma2-9b-it', 'system_fingerprint': 'fp_10c08bf97d', 'finish_reason': 'stop', 'logprobs': None}, id='run-debb5644-bf75-4693-b5be-936846fe5abb-0', usage_metadata={'input_tokens': 114, 'output_tokens': 6, 'total_tokens': 120}), HumanMessage(content='open google', additional_kwargs={}, response_metadata={}), AIMessage(content='2 \n', additional_kwargs={}, response_metadata={'token_usage': {'completion_tokens': 5, 'prompt_tokens': 129, 'total_tokens': 134, 'completion_time': 0.009090909, 'prompt_time': 0.003663181, 'queue_time': 0.019620548999999998, 'total_time': 0.01275409}, 'model_name': 'gemma2-9b-it', 'system_fingerprint': 'fp_10c08bf97d', 'finish_reason': 'stop', 'logprobs': None}, id='run-83f22bb4-0a4c-47d5-8c81-e0ca0665cd02-0', usage_metadata={'input_tokens': 129, 'output_tokens': 5, 'total_tokens': 134}), HumanMessage(content='open arduino ide', additional_kwargs={}, response_metadata={}), AIMessage(content='3 \n', additional_kwargs={}, response_metadata={'token_usage': {'completion_tokens': 5, 'prompt_tokens': 145, 'total_tokens': 150, 'completion_time': 0.009090909, 'prompt_time': 0.004213598, 'queue_time': 0.020193551, 'total_time': 0.013304507}, 'model_name': 'gemma2-9b-it', 'system_fingerprint': 'fp_10c08bf97d', 'finish_reason': 'stop', 'logprobs': None}, id='run-b21832ff-db30-4460-9b10-59bb48a6aee5-0', usage_metadata={'input_tokens': 145, 'output_tokens': 5, 'total_tokens': 150}), HumanMessage(content="what's the time", additional_kwargs={}, response_metadata={}), AIMessage(content='4 \n', additional_kwargs={}, response_metadata={'token_usage': {'completion_tokens': 5, 'prompt_tokens': 163, 'total_tokens': 168, 'completion_time': 0.009090909, 'prompt_time': 0.008361158, 'queue_time': 0.020513041, 'total_time': 0.017452067}, 'model_name': 'gemma2-9b-it', 'system_fingerprint': 'fp_10c08bf97d', 'finish_reason': 'stop', 'logprobs': None}, id='run-df4ed3c1-567a-4d62-8026-28e0c0d5a765-0', usage_metadata={'input_tokens': 163, 'output_tokens': 5, 'total_tokens': 168}), HumanMessage(content="what's general theory of relativity", additional_kwargs={}, response_metadata={}), AIMessage(content='5 \n', additional_kwargs={}, response_metadata={'token_usage': {'completion_tokens': 5, 'prompt_tokens': 183, 'total_tokens': 188, 'completion_time': 0.009090909, 'prompt_time': 0.005496292, 'queue_time': 0.021131376, 'total_time': 0.014587201}, 'model_name': 'gemma2-9b-it', 'system_fingerprint': 'fp_10c08bf97d', 'finish_reason': 'stop', 'logprobs': None}, id='run-87f5fa35-b3c2-4f1d-9d66-9991fec8b3f7-0', usage_metadata={'input_tokens': 183, 'output_tokens': 5, 'total_tokens': 188}), HumanMessage(content='bye, quit', additional_kwargs={}, response_metadata={}), AIMessage(content='6 \n', additional_kwargs={}, response_metadata={'token_usage': {'completion_tokens': 5, 'prompt_tokens': 199, 'total_tokens': 204, 'completion_time': 0.009090909, 'prompt_time': 0.010083559, 'queue_time': 0.020448939, 'total_time': 0.019174468}, 'model_name': 'gemma2-9b-it', 'system_fingerprint': 'fp_10c08bf97d', 'finish_reason': 'stop', 'logprobs': None}, id='run-fd5f282f-1751-4b8e-b8b1-a7ed01728956-0', usage_metadata={'input_tokens': 199, 'output_tokens': 5, 'total_tokens': 204})])


def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in store :
        store[session_id] = ChatMessageHistory()
    return store[session_id]

with_message_history=RunnableWithMessageHistory(model,get_session_history)

def extractnum(query) :
    prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a number extract from a query return what numbered video does user wants to play,like in history only respond with number, if not get it return 1"),
        MessagesPlaceholder(variable_name="messages")
    ]
    )

    chain=prompt|model

    with_message_history=RunnableWithMessageHistory(chain,get_session_history)

    config = {"configurable": {"session_id": "num"}}
    response=with_message_history.invoke(
        [HumanMessage(content=query)],
        config=config
    )

    return int(response.content)


def extractsearch(query) :
    prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a search query extractor, where user will give you a query and you have to return just what does the user want to search"),
        MessagesPlaceholder(variable_name="messages")
    ]
    )

    chain=prompt|model

    with_message_history=RunnableWithMessageHistory(chain,get_session_history)

    config = {"configurable": {"session_id": "search"}}
    response=with_message_history.invoke(
        [HumanMessage(content=query)],
        config=config
    )

    return response.content

def classify(query) :
    prompt=ChatPromptTemplate.from_messages(
    [
        ("system","""You are a classification bot, where you have 5 catogories :
         option1:user wants to play any video or song on youtube
         option2:user wants to open google or classroom appliaction
         option3:user wamts to open another application
         option4:user wants to know time
         option5:user wants to know something just an query
         option6:user wants to quit
         return only option number
         """),
        MessagesPlaceholder(variable_name="messages")
    ]
    )

    chain=prompt|model

#chain.invoke({"messages":[HumanMessage(content="karen search on youtube what is machne learning")]})

    with_message_history=RunnableWithMessageHistory(chain,get_session_history)

    config = {"configurable": {"session_id": "classify"}}
    response=with_message_history.invoke(
        [HumanMessage(content=query)],
        config=config
    )

    return response.content

def ytclassify(query) :
    prompt=ChatPromptTemplate.from_messages(
    [
        ("system","""You are a yotube classification bot, where you have 5 catogories :
         optionA :user wants just open youtube
         optionB:user wants just search something on youtube
         optionC:user wants to open youtube and serach something
         optionD:user wants to play a video
         return only option Variable just a, b or c
         """),
        MessagesPlaceholder(variable_name="messages")
    ]
    )

    chain=prompt|model

#chain.invoke({"messages":[HumanMessage(content="karen search on youtube what is machne learning")]})

    with_message_history=RunnableWithMessageHistory(chain,get_session_history)

    config = {"configurable": {"session_id": "ytclass"}}
    response=with_message_history.invoke(
        [HumanMessage(content=query)],
        config=config
    )

    return response.content