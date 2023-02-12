import asyncio


class NotifyEvent(asyncio.Event):
    event = asyncio.Event()
    event.set()

    def set(self, name=None):
        self._name = name
        if self.is_set():
            self.clear()
        if NotifyEvent.event.is_set():
            NotifyEvent.event.clear()
        super().set()

    async def wait(self):
        await self.event.wait()
        await super().wait()
        return self._name

    def clear(self):
        NotifyEvent.event.set()
        NotifyEvent.event.clear()
        super().clear()
        NotifyEvent.event.clear()


async def task(name, notify):
    my, other = 0, 0
    while True:
        dest = await notify.wait()
        if dest is None:
            break
        elif dest == name:
            my += 1
            print(name, ": ", my, " / ", other, sep="")
        else:
            other += 1
