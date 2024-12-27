from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from ctransformers import AutoModelForCausalLM
from huggingface_hub import hf_hub_download
import os
import logging
from tqdm import tqdm

load_dotenv()
API_TOKEN="put token here"
logging.basicConfig(level=logging.INFO)

MAX_TOKENS = 2048

def getLLamaresponse(text):
    try:
        model_name = "TheBloke/MythoMax-L2-13B-GGUF"
        model_file = "mythomax-l2-13b.Q5_K_S.gguf"
        
        model_path = os.path.join(os.getcwd(), "models", model_file)
        
        if not os.path.exists(model_path):
            print(f"Model not found. Downloading {model_name}...")
            model_path = hf_hub_download(
                repo_id=model_name,
                filename=model_file,
                local_dir=os.path.join(os.getcwd(), "models"),
                local_dir_use_symlinks=False,
                force_download=True,
                force_filename=model_file,
                progress_bar_class=tqdm
            )
            print(f"Model downloaded to {model_path}")
        
        llm = AutoModelForCausalLM.from_pretrained(model_path, model_type="llama", gpu_layers=50)

        template = "You are a helpful assistant skilled in mathematics. Please answer the following question: {question}"
        prompt = PromptTemplate(input_variables=["question"], template=template)
        response = llm(prompt.format(question=text))
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
