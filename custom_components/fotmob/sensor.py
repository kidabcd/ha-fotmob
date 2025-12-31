from homeassistant.components.sensor import SensorEntity

class FotMobLiveMatchesSensor(SensorEntity):
    _attr_has_entity_name = True

    def __init__(self, coordinator):
        self.coordinator = coordinator
        self._attr_unique_id = "fotmob_live_matches"
        self._attr_name = "Jogos ao Vivo"
