from spotapi.public import Public
import json

episode_id = "5CZlLoGOibAGX9oLh26YEk"
episode_info = Public.podcast_episode_info(episode_id)
print(json.dumps(episode_info, indent=2))
