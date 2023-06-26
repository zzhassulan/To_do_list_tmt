from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from task import create_tasks_table
import controllers

API_TOKEN = '6242306680:AAH97ov5hgQ9fkoKGwZhhQ1-0rLYASHLnRs'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

dp.register_message_handler(controllers.start_command, commands=["start"])
dp.register_message_handler(controllers.add_task_command, commands=["add"])
dp.register_message_handler(controllers.done_command, commands=["done"])
dp.register_message_handler(controllers.list_command, commands=["list"])
dp.register_message_handler(controllers.delete_command, commands=["delete"])
dp.register_message_handler(controllers.unknown_command)

if __name__ == '__main__':
    from aiogram import executor
    create_tasks_table()
    
    executor.start_polling(dp, skip_updates=True)