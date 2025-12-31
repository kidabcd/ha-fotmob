from homeassistant.components.sensor import SensorEntity
from homeassistant.helpers.update_coordinator import CoordinatorEntity

async def async_setup_entry(hass, entry, async_add_entities):
    coordinator = hass.data["fotmob"][entry.entry_id]
    async_add_entities([FotMobLiveMatchesSensor(coordinator)])

class FotMobLiveMatchesSensor(CoordinatorEntity, SensorEntity):
    _attr_has_entity_name = True

    def __init__(self, coordinator):
        super().__init__(coordinator)
        self._attr_unique_id = "fotmob_live_matches"
        self._attr_name = "Jogos ao Vivo"

    @property
    def native_value(self):
        if not self.coordinator.data:
            return 0
        return len(self.coordinator.data.get("liveMatches", []))
