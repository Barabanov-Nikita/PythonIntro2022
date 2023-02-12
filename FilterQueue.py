import asyncio


class FilterQueue(asyncio.Queue):
    @property
    def window(self):
        return self._queue[0] if self._queue else None

    def __contains__(self, filter):
        for elem in self._queue:
            if filter(elem):
                return True
        return False

    def later(self):
        item = self.get_nowait()
        self.put_nowait(item)

    async def get(self, filter=None):
        if filter and filter in self:
            while not filter(self.window):
                self.later()

        return await super().get()
