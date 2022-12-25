from wyvern import (Activity, ActivityType, CommandsClient, Status, extensions,
                    utils)


@extensions.tasks.task(m=2)
async def status_task(client: CommandsClient) -> None:
    if not getattr(client.gateway, "_socket", None):
        return
    await client.gateway.update_presence(
        status=Status.DND,
        activity=Activity(
            name=f"Latency: {client.gateway.latency*1000:.2f}ms.",
            type=ActivityType.GAME,
        ),
    )


@utils.as_hook()
def tasks(client: CommandsClient) -> None:
    status_task.run(client)
