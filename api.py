import uvicorn
from fastapi import FastAPI
from main4 import data


app = FastAPI()


@app.get("/cities/")
async def cities():
    cities = []
    for i in data.keys():
        cities.append(i)

    return {"cities": cities}


@app.get("/region/{city_name}")
async def cities(city_name):
    region = []
    for i in data.get(city_name):
        region.append(i)

    return {"regions": region}


@app.get("/quarter/{city_name}/{region_name}/")
async def cities(city_name, region_name):
    quarter = []
    for i in data.get(city_name).get(region_name):
        quarter.append(i)

    return {"quarter": quarter}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)