from models import Task
from aiogram import types


async def start_command(message: types.Message):
    reply_text = "Привет! Я бот для управления списком задач. Вот доступные команды:\n" \
                 "/add <задача> - добавление новой задачи\n" \
                 "/done <индекс> - отметка задачи как выполненной\n" \
                 "/list - вывод списка задач\n" \
                 "/delete <индекс> - удаление задачи\n"
    await message.reply(reply_text)


async def add_task_command(message: types.Message):
    task_text = message.text[5:].strip() # Получаем текст задачи после команды "/add "
    if not task_text:   
        await message.reply('Вы не указали тект задачи')
        return
    
    task = Task(task_text, "", "невыполнена")
    task.save()
    await message.reply("Задача успешно добавлена!")


async def done_command(message: types.Message):
    task_id = int(message.text[6:])  # Получаем индекс задачи после команды "/done "
    tasks = Task.get_all()

    if task_id < 1 or task_id > len(tasks):
        await message.reply("Некорректный индекс задачи!")
        return

    task = tasks[task_id - 1]
    Task.mark_as_done(task_id)
    await message.reply(f"Задача '{task.title}' отмечена как выполненная!")


async def list_command(message: types.Message):
    tasks = Task.get_all()

    if not tasks:
        await message.reply("Список задач пуст!")
        return

    reply_text = "Список задач:\n"
    for i, task in enumerate(tasks):
        status = "✅" if task.status == "выполнена" else "❌"
        reply_text += f"{i + 1}. {status} {task.title}\n"

    await message.reply(reply_text)


async def delete_command(message: types.Message):
    task_id = int(message.text[8:])  # Получаем индекс задачи после команды "/delete "
    tasks = Task.get_all()

    if task_id < 1 or task_id > len(tasks):
        await message.reply("Некорректный индекс задачи!")
        return

    task = tasks[task_id - 1]
    Task.delete(task_id)
    await message.reply(f"Задача '{task.title}' удалена!")


async def unknown_command(message: types.Message):
    await message.reply("Неизвестная команда. Введите /help для получения списка команд.")