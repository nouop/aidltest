def ds_api(text_question,systext,models):
    from openai import OpenAI

    client = OpenAI(api_key="sk-fd831b63ed7040fdbdd899ba8d83a859", base_url="https://api.deepseek.com")

    response = client.chat.completions.create(
        model= models,
        messages=[
            {"role": "system", "content": str(systext)},
            {"role": "user", "content": str(text_question)},
        ],
        temperature=0.0,
        stream=False,
    )
    
    return response.choices[0].message.content



def cz_api(text_question):
    from cozepy import COZE_CN_BASE_URL

    coze_api_token = 'pat_1ojRbQlri96kSyFmm2Raj25x2LDt1ZIyKItVREE2iWzTkJYWqQV6nMPVVreFazcz'
    coze_api_base = COZE_CN_BASE_URL

    from cozepy import Coze, TokenAuth, Message, ChatStatus, MessageContentType  # noqa

    coze = Coze(auth=TokenAuth(token=coze_api_token), base_url=coze_api_base)
    bot_id = '7489105213002416164'
    user_id = '43455'
    chat_poll = coze.chat.create_and_poll(
        bot_id=bot_id,
        user_id=user_id,
        additional_messages=[
            Message.build_user_question_text(text_question),
        ],
    )
    for message in chat_poll.messages:
        return message.content


def silconflow_api(text_question,systext,models):
    import requests

    url = "https://api.siliconflow.cn/v1/chat/completions"

    payload = {
        "model": models,
        "messages": [
            {
                "role": "system", 
                "content": str(systext)
            },
            
            {
                "role": "user",
                "content": str(text_question)
            }
        ],

        "stream": False,
        "temperature": 0.0,
        "top_p": 0.7,
        "top_k": 39,
        "n": 1

    }
    headers = {
        "Authorization": "Bearer sk-krmrmjbonusebpikbwiizkicencqbwthtxnbtzvdewgiybmm",
        "Content-Type": "application/json"
    }

    response = requests.request("POST", url, json=payload, headers=headers)
    response.raise_for_status()
    print(response.text)
    return response.json()["choices"][0]["message"]["content"]