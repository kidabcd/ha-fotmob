from homeassistant.components.sensor import SensorEntity

class FotMobLiveMatchesSensor(SensorEntity):
    def __init__(self, coordinator):
        self.coordinator = coordinator
        self._attr_name = "Jogos ao Vivo"

    @property
    def native_value(self):
        return len(self.coordinator.data.get("liveMatches", []))
