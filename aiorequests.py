import asyncio
import functools

from requests import *


__version__ = "0.1.0"
version = tuple(map(int, str.split(__version__, ".")))


def executor_wrapper(f, *, loop=None, executor=None):

    loop = loop or asyncio.get_event_loop()

    @functools.wraps(f)
    async def function_with_async_executor(*args, **kwargs):

        return await loop.run_in_executor(
            executor,
            functools.partial(
                f,
                *args,
                **kwargs,
            )
        )

    return function_with_async_executor


def set_async_requests(*, loop=None, executor=None):

    setattr(
        Session,
        "request",
        executor_wrapper(
            Session.request,
            loop=loop,
            executor=executor,
        )
    )
