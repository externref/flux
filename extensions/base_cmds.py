from wyvern import CommandsClient, Event, as_listener, models, utils


@as_listener(Event.MESSAGE_CREATE)
async def ping(msg: models.Message) -> None:
    if msg.content == ".ping":
        await msg.respond(f"Pong!: `{msg.client.latency*1000:.2f}ms`")


@as_listener(Event.MESSAGE_CREATE)
async def echo(msg: models.Message) -> None:
    if msg.content.startswith(".echo"):
        await msg.respond(msg.content[5:])


@as_listener(Event.MESSAGE_CREATE)
async def avatar(msg: models.Message) -> None:
    if msg.content.startswith(".avatar"):
        args: list[str] = msg.content.split(" ")[1:]
        if len(args) > 0:
            member = msg.client.users.parse_from_string(" ".join(args))
            response = (
                member.display_avatar.url
                if member is not None
                else f"Member named {' '.join(args)} not found."
            )
        else:
            response = msg.author.display_avatar.url
        await msg.respond(response, reply=True)


@utils.as_hook()
def base(client: CommandsClient) -> None:
    for lsnr in (ping, echo, avatar):
        client.event_handler.add_listener(lsnr)
