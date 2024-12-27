from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from ctransformers import AutoModelForCausalLM
from huggingface_hub import hf_hub_download
import os
import logging
from tqdm import tqdm

load_dotenv()
logging.basicConfig(level=logging.INFO)

MAX_TOKENS = 2048

def get_api_token():
    while True:
        token = input("Please enter your Telegram Bot API token: ").strip()
        if token and " " not in token:
            return token
        print("Invalid token. The token should not contain spaces. Please try again.")

def getLLamaresponse(text):
    try:
        model_name = "TheBloke/MythoMax-L2-13B-GGUF"
        model_file = "mythomax-l2-13b.Q5_K_S.gguf"
        
        model_path = os.path.join(os.getcwd(), "models", model_file)
        
        if not os.path.exists(model_path):
            print(f"Model not found. Downloading {model_name}...")
            try:
                model_path = hf_hub_download(
                    repo_id=model_name,
                    filename=model_file,
                    local_dir=os.path.join(os.getcwd(), "models"),
                    local_dir_use_symlinks=False
                )
                print(f"Model downloaded to {model_path}")
            except Exception as download_error:
                logging.error(f"Error downloading model: {str(download_error)}")
                return "Sorry, I encountered an error while downloading the model. Please try again later."
            print(f"Model downloaded to {model_path}")
        
        llm = AutoModelForCausalLM.from_pretrained(model_path, model_type="llama", gpu_layers=50)

        template = "You are a helpful assistant skilled in mathematics and general knowledge. Please answer the following question or respond to the following statement: {question}"
        prompt = PromptTemplate(input_variables=["question"], template=template)
        response = llm(prompt.format(question=text))
        print(f"Full model response: {response}")
        return response
    except Exception as e:
        logging.error(f"Error in getLLamaresponse: {str(e)}")
        return "Sorry, I encountered an error while processing your request. Please try again or ask a different question."

# Get the API token
API_TOKEN = get_api_token()

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start','help'])
async def command_start_handler(message: types.Message):
    await message.reply("Hello! I'm a bot that can help with mathematical questions. Ask me anything!")

@dp.message_handler()
async def echo(message: types.Message):
    logging.info(f"Received message: {message.text}")
    response = getLLamaresponse(message.text)
    logging.info(f"Model response: {response}")
    await message.reply(response)

if __name__ == "__main__":
    print("Bot is starting...")
    executor.start_polling(dp, skip_updates=True)
