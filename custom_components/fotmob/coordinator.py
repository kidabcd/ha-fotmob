from datetime import timedelta
import aiohttp
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator

class FotMobCoordinator(DataUpdateCoordinator):
    def __init__(self, hass):
        super().__init__(
            hass,
            logger=None,
            name="FotMob",
            update_interval=timedelta(minutes=1),
        )

    async def _async_update_data(self):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://www.fotmob.com/api/matches") as resp:
                return await resp.json()
