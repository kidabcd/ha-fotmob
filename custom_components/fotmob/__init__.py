from .coordinator import FotMobCoordinator

async def async_setup_entry(hass, entry):
    coordinator = FotMobCoordinator(hass)
    await coordinator.async_config_entry_first_refresh()

    hass.data.setdefault("fotmob", {})
    hass.data["fotmob"][entry.entry_id] = coordinator

    hass.async_create_task(
        hass.config_entries.async_forward_entry_setup(entry, "sensor")
    )

    return True
