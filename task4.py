import asyncio
import time

async def call_external_api(service_name):
    print(f"Calling {service_name} API..")
    await asyncio.sleep(2)
    print(f"{service_name} responce is received ")



async def main():
    start = time.time()
    await asyncio.gather(
        call_external_api("service 1"),
        call_external_api("service 2"),
        call_external_api("service 3")
    )        

    end = time.time()
    print(f"total time taken: {end-start:.2f} seconds")


asyncio.run(main()) 