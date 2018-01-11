
from aiohttp import web
from allow_host import AllowedHosts
from aiohttp import hdrs
from ipaddress import ip_address

async def data_handler(aio_req):
    print(aio_req.__dict__,'11111')
    return web.Response(text='404')


app = web.Application()
app.router.add_get('/', data_handler)
web.run_app(app)