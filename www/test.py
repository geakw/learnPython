import orm
from models import User, Blog, Comment
import asyncio


async def test(loop):
    await orm.create_pool(user='', password='', database='awesome', loop=loop)

    u = User(name='Test', email='test@example.com',
             passwd='1234567890', image='about:blank')

    await u.save()

loop = asyncio.get_event_loop()
test(loop)