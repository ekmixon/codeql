import pkg # $ use=moduleImport("pkg")

async def foo():
    coro = pkg.async_func() # $ use=moduleImport("pkg").getMember("async_func").getReturn()
    coro # $ use=moduleImport("pkg").getMember("async_func").getReturn()
    result = await coro # $ use=moduleImport("pkg").getMember("async_func").getReturn().getAwaited()
    result # $ use=moduleImport("pkg").getMember("async_func").getReturn().getAwaited()
    return result # $ use=moduleImport("pkg").getMember("async_func").getReturn().getAwaited()

async def bar():
    result = await pkg.async_func() # $ use=moduleImport("pkg").getMember("async_func").getReturn().getAwaited()
    return result # $ use=moduleImport("pkg").getMember("async_func").getReturn().getAwaited()

def check_annotations():
    return pkg.sync_func()
