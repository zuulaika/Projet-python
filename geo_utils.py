
import geopandas as gpd
from cartiflette import carti_download

def load_and_reproject_departements():
    """
    Télécharge les limites des départements français et les reprojette en Lambert 93 (EPSG:2154).

    Returns:
        geopandas.GeoDataFrame: GeoDataFrame des départements français reprojetés en Lambert 93.
    """
    # Télécharge les limites des départements français pour l'année 2022.
    departements = carti_download(
        values="France",
        crs=4326,
        borders="DEPARTEMENT",
        vectorfile_format="geojson",
        filter_by="FRANCE_ENTIERE_DROM_RAPPROCHES",
        source="EXPRESS-COG-CARTO-TERRITOIRE",
        year=2022,
    )
    # Reprojecte les données géographiques des départements vers le système de coordonnées Lambert 93 (EPSG:2154).
    departements_lambert93 = departements.to_crs(epsg=2154)
    return departements_lambert93

if __name__ == "__main__":
    # Exemple d'utilisation si le script est exécuté directement
    departements_lambert93_test = load_and_reproject_departements()
    print(f"CRS of 'departements_lambert93_test': {departements_lambert93_test.crs}")
    print(departements_lambert93_test.head())
