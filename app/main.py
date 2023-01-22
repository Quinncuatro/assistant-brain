from typing import Union
from fastapi import FastAPI

# import json
import requests

app = FastAPI()

class BearerAuth(requests.auth.AuthBase):
  def __init__(self, token):
    self.token = token
  def __call__(self, r):
    r.headers["authorization"] = "Bearer " + self.token
    return r

@app.get("/")
def read_root():
  return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
  return {"item_id": item_id, "q": q}

@app.get("/light-on")
def light_on():
  """
  Turn on the light.
  """

  data = {"entity_id": "light.office_light"}

  url = "http://192.168.0.59:8123/api/services/light/turn_on"

  try:
    response = requests.post(url, json=data, auth=BearerAuth('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJkZTRmMzM1N2I1OWM0ZmUxYjM0MmI4MDFlNDBlOGEwYyIsImlhdCI6MTY3NDMxMjQwMiwiZXhwIjoxOTg5NjcyNDAyfQ.8bTSpE2kx8b5SSnSrgi0WFZkfaVSZaP9_Hbkr9UljtE'))

    return {"Hopefully the light turned on! Response: ", response.text}
  except Exception as err:
    return {"Error: ", err}

@app.get("/light-off")
def light_on():
  """
  Turn off the light.
  """

  data = {"entity_id": "light.office_light"}

  url = "http://192.168.0.59:8123/api/services/light/turn_off"

  try:
    response = requests.post(url, json=data, auth=BearerAuth('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJkZTRmMzM1N2I1OWM0ZmUxYjM0MmI4MDFlNDBlOGEwYyIsImlhdCI6MTY3NDMxMjQwMiwiZXhwIjoxOTg5NjcyNDAyfQ.8bTSpE2kx8b5SSnSrgi0WFZkfaVSZaP9_Hbkr9UljtE'))

    return {"Hopefully the light turned on! Response: ", response.text}
  except Exception as err:
    return {"Error: ", err}