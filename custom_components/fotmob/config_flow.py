from homeassistant import config_entries

class FotMobConfigFlow(config_entries.ConfigFlow, domain="fotmob"):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        if user_input is not None:
            return self.async_create_entry(
                title="FotMob",
                data={}
            )

        return self.async_show_form(step_id="user")
