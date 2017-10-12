# aiorequests
[requests](https://github.com/kennethreitz/requests) wrapper for asyncio (based on [run_in_executor](https://docs.python.org/3/library/asyncio-eventloop.html?highlight=run_in_executor#asyncio.BaseEventLoop.run_in_executor)).

## Reasons
* [aiohttp](https://github.com/KeepSafe/aiohttp) have no https proxy support.

## License
aiorequests is offered under the WTFPL license.

## Features
* Same as requests.
* Source code is [short and simple](https://github.com/pohmelie/aiorequests/blob/master/aiorequests.py).

## Usage
```python
import asyncio

import aiorequests


async def yoba():

    r = await aiorequests.get("https://google.com")
    print(r.status_code)
    print(len(r.content))


if __name__ == "__main__":

    loop = asyncio.get_event_loop()
    aiorequests.set_async_requests(loop=loop)
    loop.run_until_complete(yoba())
```
