from openai import OpenAI

API_KEY=''


def gpt(text):
  client= OpenAI(api_key=API_KEY)
  completition = client.chat.completions.create(
      model='gpt-3.5-turbo',
      messages = [
            {"role": "system", "content" : "You are a polite guide for Astana who answer only on questions that are related with the Astana and Kazakhstan in generall"},        # В поле content указываем "личность" бота на английском языке
            {'role': 'user', 'content': f'{text}'},        # Здесь передаётся сам запрос
        ],
      temperature = 0.9        # Значение от 0 до 1. Отвечает за количество выразительности
  )
  return completition.choices[0].message.content
