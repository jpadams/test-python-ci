import anyio
import dagger

async def main():
    async with dagger.Connection() as client:
        ctr = (
            client.container()
            .from_("alpine")
            .with_exec(["apk", "add", "curl"])
            .with_exec(["curl", "https://dagger.io"])
        )
        output = await ctr.stdout()
        print(output[:300])

anyio.run(main)
