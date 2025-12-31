from datetime import timedelta
import aiohttp
import logging

from homeassistant.helpers.update_coordinator import DataUpdateCoordinator

_LOGGER = logging.getLogger(__name__)

API_URL = "https://api-football-v1.p.rapidapi.com/v3/fixtures?live=all"
API_HEADERS = {
    "X-RapidAPI-Key": "94ef4ba0647ea3e47b957dbc4e9ac5d5",
    "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
}

class FotMobCoordinator(DataUpdateCoordinator):
    def __init__(self, hass):
        super().__init__(
            hass,
            logger=_LOGGER,
            name="FotMob",
            update_interval=timedelta(seconds=60),  # atualiza a cada minuto
        )

    async def _async_update_data(self):
        """Busca partidas ao vivo da API-Football."""
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(API_URL, headers=API_HEADERS) as resp:
                    resp.raise_for_status()
                    data = await resp.json()
                    # Retorna apenas lista de partidas
                    return data.get("response", [])
        except Exception as e:
            _LOGGER.error("Erro ao buscar partidas: %s", e)
            raise
