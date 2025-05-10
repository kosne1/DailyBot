from apscheduler.schedulers.asyncio import AsyncIOScheduler

from app import bot

# import app.handlers
scheduler = AsyncIOScheduler()

def example_function():
    print(123)


if __name__ == '__main__':
    scheduler.add_job(example_function, 'cron', hour='1, 9, 12, 20')
    scheduler.start()

    bot.polling(none_stop=True)
