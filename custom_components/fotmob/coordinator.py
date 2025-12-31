

from datetime import timedelta, date
import aiohttp
import logging

from homeassistant.helpers.update_coordinator import DataUpdateCoordinator

_LOGGER = logging.getLogger(__name__)

API_URL = f"https://v3.football.api-sports.io/fixtures?date={date.today()}"
API_HEADERS = {
    "X-RapidAPI-Key": "94ef4ba0647ea3e47b957dbc4e9ac5d5",
    "X-RapidAPI-Host": "v3.football.api-sports.io"
}

class FotMobCoordinator(DataUpdateCoordinator):
    def __init__(self, hass):
        super().__init__(
            hass,
            logger=_LOGGER,
            name="FotMob",
            update_interval=timedelta(minutes=15)
        )

    async def _async_update_data(self):
        """Busca partidas do dia da API-Football v3."""
        try:
            async with aiohttp.ClientSession(headers={"User-Agent": "HomeAssistant/1.0"}) as session:
                async with session.get(API_URL, headers=API_HEADERS) as resp:
                    resp.raise_for_status()
                    data = await resp.json()
                    # Retorna apenas lista de partidas
                    return data.get("response", [])
        except Exception as e:
            _LOGGER.error("Erro ao buscar partidas: %s", e)
            raise

