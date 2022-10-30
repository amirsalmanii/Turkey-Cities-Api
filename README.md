# Turkey-Cities-Api
turkey cities regions quarters api 
turkie turkiye-il-ilce api

for run app just install requirements and run api.py --> python api.py

++++++++++++++++++++++++++
for get list cities (method get)

host/cities/

++++++++++++++++++++++++++

for get just one region (method get)

host/region/<city name>/

++++++++++++++++++++++++++

for get many regions (method post)

host/region/

{
  "cities": ["ADANA", "ANKARA"]
}

++++++++++++++++++++++++++

for get just one quarter (method get)

host/quarter/<city name>/<region name>/

+++++++++++++++++++++++++++

for get many quarter (method post)

{"cities_regions": {name_of_city: [region1, regions2, ...]}, {name_of_city: [region1, regions2, ...]}}

host/quarter/

+++++++++++++++++++++++++++

and you can see docs by -> host/docs
