from pyarr import SonarrAPI
import config

host_url = "http://sonarr.anime.burrard"
api_key = config.SONARR_API_KEY

sonarr = SonarrAPI(host_url, api_key)
print(sonarr.get_series())
