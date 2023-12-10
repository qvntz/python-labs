import asyncio
import os

import aiofiles
import aiohttp


async def download_image(url, folder, number):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                filepath = os.path.join(folder, f"image_{number}.jpg")
                async with aiofiles.open(filepath, mode="wb") as file:
                    await file.write(await response.read())
                    print(f"Downloaded image {number} at {filepath}.")
            else:
                print(
                    f"Error downloading image {number}. Status code: {response.status}"
                )


async def download_images(quantity, folder):
    url = "https://thispersondoesnotexist.com/"
    if not os.path.exists(folder):
        os.makedirs(folder)

    tasks = []
    for i in range(quantity):
        tasks.append(asyncio.ensure_future(download_image(url, folder, i)))

    await asyncio.gather(*tasks)


def main():
    folder = "artifacts"
    quantity = 10
    loop = asyncio.get_event_loop()
    loop.run_until_complete(download_images(quantity, folder))
    loop.close()


if __name__ == "__main__":
    main()
