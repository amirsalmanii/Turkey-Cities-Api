import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from tr_json import data
from typing import List, Dict
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder


class Item(BaseModel):
    cities: List[str] = []


class Item2(BaseModel):
    cities_regions: Dict = {}


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/cities/")
async def cities():
    cities = []
    for i in data.keys():
        cities.append(i)

    return {"cities": cities}


@app.post("/region/")
async def region(city_names: Item):
    result = {}
    regions = []
    city_names = jsonable_encoder(city_names)
    city_names = city_names["cities"]
    if city_names:
        for city_name in city_names:
            cities_regions = data.get(city_name)
            if cities_regions:
                for i in cities_regions:
                    regions.append(i)
                result[city_name] = regions
                regions = [] # reset when region city is done and going to another city

    return result


@app.post(
    "/quarter/",
    description='{"cities_regions": {name_of_city: [region1, regions2, ...]}, {name_of_city: [region1, regions2, ...]}}',
)
async def quarter(city_names: Item2):
    city_names = jsonable_encoder(city_names)["cities_regions"]
    final_cities_regions_quarter = {}
    res = []
    for city_name, region_names in city_names.items():
        for region_name in region_names:
            try:
                d2 = data.get(city_name).get(region_name)
            except AttributeError:
                d2 = []
            for i in d2:
                res.append(i)
            final_cities_regions_quarter[region_name] = res
            res = [] # reset when region city is done and going to another city

    return final_cities_regions_quarter


@app.get("/region/c/{city_name}")
async def cities(city_name):
    region = []
    for i in data.get(city_name):
        region.append(i)

    return {"regions": region}


@app.get("/quarter/c/{city_name}/{region_name}/")
async def cities(city_name, region_name):
    quarter = []
    for i in data.get(city_name).get(region_name):
        quarter.append(i)

    return {"quarter": quarter}


if __name__ == "__main__":
    uvicorn.run("api:app", host="0.0.0.0", port=8001, debug=True, reload=True)
