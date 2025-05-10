import asyncio

from apscheduler.schedulers.asyncio import AsyncIOScheduler

# from app import bot

# import app.handlers
scheduler = AsyncIOScheduler()


def example_function():
    print(123)


async def main():
    scheduler.add_job(example_function, 'cron', hour=13, minute=28)
    scheduler.start()
    await asyncio.Event().wait()


if __name__ == '__main__':
    asyncio.run(main())
