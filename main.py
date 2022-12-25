import os

import dotenv
import wyvern

dotenv.load_dotenv()

intents = (
    wyvern.Intents.GUILDS
    | wyvern.Intents.DIRECT_MESSAGES
    | wyvern.Intents.GUILD_MESSAGES
    | wyvern.Intents.MESSAGE_CONTENT
    | wyvern.Intents.GUILD_MEMBERS
    | wyvern.Intents.GUILD_PRESENCES
)

client = wyvern.CommandsClient(
    os.environ["TOKEN"],
    intents=intents,
    allowed_mentions=wyvern.AllowedMentions(users=True),
)
client.load_hooks("extensions.base_cmds")
client.load_hooks("extensions.tasks")


@client.with_listener(wyvern.Event.STARTING)
async def setups(client: wyvern.CommandsClient) -> None:
    client.hooks["base"](client)
    client.hooks["tasks"](client)


@client.with_listener(wyvern.Event.STARTED)
async def ready(client: wyvern.CommandsClient) -> None:
    print("Bot is online!")


client.run(
    activity=wyvern.Activity(name="hello, world!", type=wyvern.ActivityType.LISTENING),
    status=wyvern.Status.IDLE,
)
