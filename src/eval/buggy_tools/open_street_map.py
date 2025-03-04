import time

import requests
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from pydantic.v1 import BaseModel, Field

OPEN_STREET_SEARCH = 'https://nominatim.openstreetmap.org/search.php?q='
OPEN_STREET_ROUTES = 'https://routing.openstreetmap.de/routed-car/route/v1/driving/'

# Define the custom user agent string
custom_user_agent = "MasterThesis/2.0"

# Set up the headers with the custom user agent
headers = {
    'User-Agent': custom_user_agent
}


def request(url, retry=3):
    time.sleep(1)
    response = requests.get(url, headers=headers)
    if response.status_code == 400:
        raise ValueError(f"Couldn't locate {url}")
    if response.status_code != 200 and retry > 0:
        print(f"RETRY in 1 min. {response.text}, {response.status_code}")
        time.sleep(60)
        return request(url, retry - 1)
    if response.status_code == 403:
        print(response.text)
        raise TimeoutError("Cannot get response got timed out.")
    return response


class OpenStreetMapSearchInput(BaseModel):
    query: str = Field(
        description="Search query for locating places on a map. The query can be a place directly like Zurich, "
                    "Sofia and so on or a query like libraries in Zurich or coffee shops in San Francisco")


@tool('open-street-map-search', args_schema=OpenStreetMapSearchInput, return_direct=True)
def open_street_map_search(query: str) -> str:
    """
    Tool to query a map. This tool can locate places by name and simple queries such as: libraries in San Francisco.
    The idea of the tool is to locate places like coffe shops offices etc.
    """
    assert len(query) < 100, 'Query is too long. Query must be less than 100 characters'
    try:
        response = request(f"{OPEN_STREET_SEARCH}{query}&polygon_geojson=1&format=jsonv2")
        response_json = response.json()
        results = []
        for item in response_json:
            item_str = ''
            if 'display_name' in item:
                item_str += f"{item['name']}"
            elif 'name' in item:
                item_str += f"{item['name']}"

            if 'category' in item:
                item_str += f" of category {item['category']}"
            if 'type' in item:
                item_str += f" and type {item['type']}"

            if 'lat' in item and 'lon' in item:
                item_str += f" at latitude: {item['lat']} and longitude: {item['lon']}"

            if len(item_str) != 0:
                results.append(item_str)

            if len(results) >= 10:
                break
        return f"The top {len(results)} results for the query are: {'. '.join(results)}.\n"
    except Exception as e:
        return f"Error while using tool {e}"


def get_location(search_query: str):
    response = request(f"{OPEN_STREET_SEARCH}{search_query}&polygon_geojson=1&format=jsonv2")
    if len(response.json()) == 0:
        raise ValueError(f"No location found for {search_query}")
    first_location = response.json()[0]
    return f"{first_location['lon']},{first_location['lat']}", first_location['name']


class OpenStreetMapRouteInput(BaseModel):
    from_location_query: str = Field(
        description='Starting location query. The query is for locating places on a map. The query can be a place '
                    'directly like Zurich, Sofia and so on or a query like libraries in Zurich or coffee shops in San '
                    'Francisco')
    to_location_query: str = Field(
        description='Destination location query. The query is for locating places on a map. The query can be a place '
                    'directly like Zurich, Sofia and so on or a query like libraries in Zurich or coffee shops in San '
                    'Francisco')


@tool('open-street-map-route-distance', args_schema=OpenStreetMapRouteInput, return_direct=True)
def open_street_map_distance(from_location_query: str, to_location_query: str):
    """
    Tool which can find a route between two locations and give back the distance in km of that route. The route is on
    rodes that can be driven with car. The tool provides route distance in km for car trip between the two locations.
    The two locations can be cities or concrete places i.e. office buildings, shops, parks and so on.
    Tool arguments with cities must always include the full names and countries i.e. NYC -> New York City, USA or Paris -> Paris, France
    """
    try:
        from_lat_long, from_loc = get_location(from_location_query)
        to_lat_long, to_loc = get_location(to_location_query)
        response = request(f"{OPEN_STREET_ROUTES}{from_lat_long};{to_lat_long}")
        if 'routes' not in response.json():
            return "No route available."
        if len(response.json()['routes']) == 0:
            return "No route available"
        distance = response.json()['routes'][0]['distance']
        return f"The distance between {from_loc} to {to_loc} is {distance} meters"
    except Exception as e:
        return f"Error while using the tool {e}"
