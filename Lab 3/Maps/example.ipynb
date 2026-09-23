

plt.rcParams["font.family"] = "DejaVu Serif"
plt.rcParams["font.serif"] = ["Nimbus Roman"]


#Cretaceous data from Matthews 2016, as provided in Cao et al. 2017 BG Supplement
cretaceouslm = gpd.read_file(
    "Assets/SHP/Cao_etal_2017_BG_Supplement/bg-2017-94-supplement/PresentDay_Palegeog_Matthews2016_Revised_402-2Ma/Revised_Palegeog_Matthews2016_ModernCoor_402-2Ma_Individually/PresentDay_Paleogeog_Matthews2016_76Ma/lm_fig52_81_58_76.00Ma.shp"
)

cretaceousmts = gpd.read_file(
    "Assets/SHP/Cao_etal_2017_BG_Supplement/bg-2017-94-supplement/PresentDay_Palegeog_Matthews2016_Revised_402-2Ma/Revised_Palegeog_Matthews2016_ModernCoor_402-2Ma_Individually/PresentDay_Paleogeog_Matthews2016_76Ma/m_fig52_81_58_76.00Ma.shp"
)

cretaceoussm = gpd.read_file(
    "Assets/SHP/Cao_etal_2017_BG_Supplement/bg-2017-94-supplement/PresentDay_Palegeog_Matthews2016_Revised_402-2Ma/Revised_Palegeog_Matthews2016_ModernCoor_402-2Ma_Individually/PresentDay_Paleogeog_Matthews2016_76Ma/sm_fig52_81_58_76.00Ma.shp"
)

#Jurassic data 
jurassiclm = gpd.read_file(
    "Assets/SHP/Cao_etal_2017_BG_Supplement/bg-2017-94-supplement/PresentDay_Palegeog_Matthews2016_Revised_402-2Ma/Revised_Palegeog_Matthews2016_ModernCoor_402-2Ma_Individually/PresentDay_Paleogeog_Matthews2016_152Ma/lm_fig42_166_146_152.00Ma.shp"
)

jurassicmts = gpd.read_file(
    "Assets/SHP/Cao_etal_2017_BG_Supplement/bg-2017-94-supplement/PresentDay_Palegeog_Matthews2016_Revised_402-2Ma/Revised_Palegeog_Matthews2016_ModernCoor_402-2Ma_Individually/PresentDay_Paleogeog_Matthews2016_152Ma/m_fig42_166_146_152.00Ma.shp"
)

jurassicsm = gpd.read_file(
    "Assets/SHP/Cao_etal_2017_BG_Supplement/bg-2017-94-supplement/PresentDay_Palegeog_Matthews2016_Revised_402-2Ma/Revised_Palegeog_Matthews2016_ModernCoor_402-2Ma_Individually/PresentDay_Paleogeog_Matthews2016_152Ma/sm_fig42_166_146_152.00Ma.shp"
)

#Natural Earth data
ne_rivers_url = (
    "https://naciscdn.org/naturalearth/50m/physical/ne_50m_rivers_lake_centerlines.zip"
)
rivers_temp_dir = tempfile.mkdtemp()
rivers_zip_path = os.path.join(
    rivers_temp_dir, "ne_rivers.zip"
)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}
response_rivers = requests.get(
    ne_rivers_url, headers=headers, stream=True
)
response_rivers.raise_for_status()
with open(rivers_zip_path, "wb") as f:
    for chunk in response_rivers.iter_content(chunk_size=8192):
        f.write(chunk)
with zipfile.ZipFile(rivers_zip_path, "r") as zip_ref:
    zip_ref.extractall(rivers_temp_dir)
rivers_shp_file = [f for f in os.listdir(rivers_temp_dir) if f.endswith(".shp")][
    0
]
rivers = gpd.read_file(
    os.path.join(rivers_temp_dir, rivers_shp_file)
)

countries_borders = gpd.read_file(
    "Assets/SHP/geoBoundariesCGAZ_ADM0/geoBoundariesCGAZ_ADM0.shp"
)

ne_countries_url = (
    "https://naciscdn.org/naturalearth/10m/cultural/ne_10m_admin_0_countries.zip"
)
countries_temp_dir = tempfile.mkdtemp()
countries_zip_path = os.path.join(
    countries_temp_dir, "ne_countries.zip"
)
response_countries = requests.get(
    ne_countries_url, headers=headers, stream=True
)
response_countries.raise_for_status()
with open(countries_zip_path, "wb") as f:
    for chunk in response_countries.iter_content(chunk_size=8192):
        f.write(chunk)
with zipfile.ZipFile(countries_zip_path, "r") as zip_ref:
    zip_ref.extractall(countries_temp_dir)
countries_shp_file = [f for f in os.listdir(countries_temp_dir) if f.endswith(".shp")][
    0
]
countries = gpd.read_file(
    os.path.join(countries_temp_dir, countries_shp_file)
)

state_borders_url = (
    "https://www2.census.gov/geo/tiger/GENZ2018/shp/cb_2018_us_state_500k.zip"
)
state_borders_temp_dir = tempfile.mkdtemp()
state_borders_zip_path = os.path.join(
    state_borders_temp_dir, "state_borders.zip"
)
response_state_borders = requests.get(
    state_borders_url, headers=headers, stream=True
)
response_state_borders.raise_for_status()
with open(state_borders_zip_path, "wb") as f:
    for chunk in response_state_borders.iter_content(chunk_size=8192):
        f.write(chunk)
with zipfile.ZipFile(state_borders_zip_path, "r") as zip_ref:
    zip_ref.extractall(state_borders_temp_dir)
state_borders_shp_file = [
    f for f in os.listdir(state_borders_temp_dir) if f.endswith(".shp")
][0]
state_borders = gpd.read_file(
    os.path.join(state_borders_temp_dir, state_borders_shp_file)
)

oceans_url = (
    "https://naciscdn.org/naturalearth/10m/physical/ne_10m_ocean.zip"
)
oceans_temp_dir = tempfile.mkdtemp()
oceans_zip_path = os.path.join(
    oceans_temp_dir, "ne_ocean.zip"
)
response_oceans = requests.get(
    oceans_url, headers=headers, stream=True
)
response_oceans.raise_for_status()
with open(oceans_zip_path, "wb") as f:
    for chunk in response_oceans.iter_content(chunk_size=8192):
        f.write(chunk)
with zipfile.ZipFile(oceans_zip_path, "r") as zip_ref:
    zip_ref.extractall(oceans_temp_dir)
oceans_shp_file = [f for f in os.listdir(oceans_temp_dir) if f.endswith(".shp")][
    0
]
oceans = gpd.read_file(
    os.path.join(oceans_temp_dir, oceans_shp_file)
)

ne_lakes_url = (
    "https://naciscdn.org/naturalearth/10m/physical/ne_10m_lakes.zip"
)
lakes_temp_dir = tempfile.mkdtemp()
lakes_zip_path = os.path.join(
    lakes_temp_dir, "ne_lakes.zip"
)  # we make a temporary directory to store the zip file with the lake locations
response_lakes = requests.get(
    ne_lakes_url, headers=headers, stream=True
)  # we download the zip file
response_lakes.raise_for_status()  # check that the download was successful
with open(lakes_zip_path, "wb") as f:
    for chunk in response_lakes.iter_content(chunk_size=8192):
        f.write(chunk)
with zipfile.ZipFile(lakes_zip_path, "r") as zip_ref:
    zip_ref.extractall(lakes_temp_dir)
lakes_shp_file = [f for f in os.listdir(lakes_temp_dir) if f.endswith(".shp")][
    0
]  # now find the lakes shapefile from the temporary directory
lakes = gpd.read_file(
    os.path.join(lakes_temp_dir, lakes_shp_file)
)  # read the lakes shapefile

ne_parks_url = (
    "https://naciscdn.org/naturalearth/10m/cultural/ne_10m_parks_and_protected_lands.zip"
)
parks_temp_dir = tempfile.mkdtemp()
parks_zip_path = os.path.join(
    parks_temp_dir, "ne_parks.zip"
)  # we make a temporary directory to store the zip file with the park locations
response_parks = requests.get(
    ne_parks_url, headers=headers, stream=True
)  # we download the zip file
response_parks.raise_for_status()  # check that the download was successful
with open(parks_zip_path, "wb") as f:
    for chunk in response_parks.iter_content(chunk_size=8192):
        f.write(chunk)
with zipfile.ZipFile(parks_zip_path, "r") as zip_ref:
    zip_ref.extractall(parks_temp_dir)
parks_shp_file = [f for f in os.listdir(parks_temp_dir) if f.endswith(".shp")][
    0
]  # now find the parks shapefile from the temporary directory
parks = gpd.read_file(
    os.path.join(parks_temp_dir, parks_shp_file)
)  # read the parks shapefile

# let's do the same exercise for state boundaries, so we can plot the location of Utah
# Download Natural Earth 110m admin level 1 (states/provinces) boundaries
ne_states_url = "https://naciscdn.org/naturalearth/10m/cultural/ne_10m_admin_1_states_provinces.zip"
temp_dir = tempfile.mkdtemp()
zip_path = os.path.join(temp_dir, "ne_states.zip")
response = requests.get(
    ne_states_url, headers=headers, stream=True
)  # note we're using the same header we already defined when getting the rivers shapefile
response.raise_for_status()
with open(zip_path, "wb") as f:
    for chunk in response.iter_content(chunk_size=8192):
        f.write(chunk)
with zipfile.ZipFile(zip_path, "r") as zip_ref:
    zip_ref.extractall(temp_dir)
states_shp_file = [f for f in os.listdir(temp_dir) if f.endswith(".shp")][0]
states = gpd.read_file(os.path.join(temp_dir, states_shp_file))

huajiyingfm = gpd.GeoDataFrame(
    {"geometry": [Point(117, 41)]}, crs=states.crs
)

jiufotangfm = gpd.GeoDataFrame(
    {"geometry": [Point(120, 41.4)]}, crs=states.crs
)

longjiefm = gpd.GeoDataFrame(
    {"geometry": [Point(100.6, 26.3)]}, crs=states.crs
)
