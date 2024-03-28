from openai import OpenAI
from dotenv import load_dotenv

def getQuestion():
  load_dotenv()
  client = OpenAI()

  completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    temperature= 1.3,
    messages=[
      {"role": "system", "content": """You are a assistant for creating questions for creative writing section 
       of 11 plus exam for UK students. Don't repeat your questions and target age group is 11-12 years old. 
       Output the single unique question without any additional data. Make it as close as possible to a question that a 11 yearold can understand."""},
      {"role": "user", "content": "give a question."}
    ]
  )

  question = completion.choices[0].message.content if completion.choices else "What does success mean to you?"  # Fallback question

  print(completion.choices[0].message)
  return question

def getAnalysis(question,answer):
  load_dotenv()
  client = OpenAI()

  completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    temperature= 1.3,
    max_tokens= 1500,
    messages=[
      {"role": "system", "content": """You are a organisation for analyzing and evaluating answers for provided 
       creative writing question of 11 plus exam for UK students. The main factors need to be evaluated 
       are plot development, vocabulary usage, incorporation of literary techniques, 
       grammar and spelling proficiency. Suggest more detailed approach for improvement other than these factors.
       Don't respond in first person and grade the answers according to 11 plus exam standards in new line at end"""},
      {"role": "assistant", "content": question},
      {"role": "user", "content": answer}
    ]
  )

  analysis = completion.choices[0].message.content if completion.choices else "Thank you for your response. We are experiencing some issues. If you don't get answers in some time. Please connect with our support team"  # Fallback analysis

  print(completion.choices[0].message)
  return analysis