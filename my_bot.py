from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from ctransformers import AutoModelForCausalLM
import os
import logging

load_dotenv()
API_TOKEN="put token here"
logging.basicConfig(level=logging.INFO)

MAX_TOKENS = 2048

def getLLamaresponse(text):
    try:                                             # if you use a different model then 
        llm = AutoModelForCausalLM.from_pretrained("TheBloke/MythoMax-L2-13B-GGUF", model_file="path\\to\\model\\.gguf", model_type="llama", gpu_layers=50) # change layers for less or more capable gpus
        template="You are a helpful agent. Reply to the following message to the best of your knowledge. {question}"
        prompt=PromptTemplate(input_variables=["question"],template=template)
        response = llm(prompt.format(question=text))
        print(f"Full model response: {response}")
        return response
    except Exception as e:
        logging.error(f"Error in getLLamaresponse: {str(e)}")
        return "Sorry, I encountered an error while processing your request."

bot=Bot(token=API_TOKEN)
dp=Dispatcher(bot)

@dp.message_handler(commands=['start','help'])
async def command_start_handler(message: types.Message):
    await message.reply("")

@dp.message_handler()
async def echo(message: types.Message):
    logging.info(f"Received message: {message.text}")
    response = getLLamaresponse(message.text)
    logging.info(f"Model response: {response}")
    await message.reply(response)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
