async def async_setup_entry(hass, entry):
    from .coordinator import FotMobCoordinator

    coordinator = FotMobCoordinator(hass)
    await coordinator.async_config_entry_first_refresh()

    hass.data.setdefault("fotmob", {})
    hass.data["fotmob"][entry.entry_id] = coordinator

    await hass.config_entries.async_forward_entry_setups(entry, ["sensor"])

    return True
