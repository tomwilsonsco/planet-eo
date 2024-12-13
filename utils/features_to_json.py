import geopandas as gpd
import json
from shapely.geometry import box


class SearchFeatures:
    """Prepare features for Planet api search and order"""

    def __init__(self, features_fp, bounding_box=False):
        """Initialize the SearchFeatures object."""
        self.features_fp = features_fp
        self.bounding_box = bounding_box
        self.gdf = gpd.read_file(features_fp)
        self.json_data = None

    def convert_to_wgs(self):
        """Convert the GeoDataFrame CRS to WGS84 (EPSG:4326)."""
        self.gdf = self.gdf.to_crs(epsg=4326)

    def geom_to_bbox(self):
        """Convert geometries to bounding boxes if specified."""
        if self.bounding_box:
            self.gdf["geometry"] = self.gdf.geometry.apply(
                lambda geom: box(*geom.bounds)
            )

    def features_to_json(self):
        """Convert features to GeoJSON format."""
        json_text = self.gdf.to_json()
        self.json_data = json.loads(json_text)

    def filter_json(self, id_col, id_val):
        """Filter the GeoJSON features based on a given column and value."""
        filtered = [
            d
            for d in self.json_data["features"]
            if d["properties"].get(id_col) == id_val
        ]
        return filtered[0] if filtered else None

    @staticmethod
    def json_to_bbox_string(feature):
        """Convert a GeoJSON feature to a bounding box string."""
        if feature["geometry"]["type"] != "Polygon":
            raise ValueError("The geometry type must be 'Polygon'.")
        coordinates = feature["geometry"]["coordinates"][0]
        lons, lats = zip(*coordinates)
        lon_min, lon_max = min(lons), max(lons)
        lat_min, lat_max = min(lats), max(lats)

        return f"{lon_min}, {lat_min}, {lon_max}, {lat_max}"

    def process(self):
        """Run all necessary processing and return GeoJSON."""
        self.convert_to_wgs()
        self.geom_to_bbox()
        self.features_to_json()
        return self.json_data
