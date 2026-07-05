"""
sun_altaz.py

Calcule la hauteur (altitude) et l'azimut du Soleil pour un lieu et un
instant donnes, exprime en temps universel (UTC).

Dependances principales: astropy (coordinates, time, units).
"""

from astropy.coordinates import EarthLocation, AltAz, get_sun
from astropy.time import Time
import astropy.units as u

# ARRAS
latitude = 50.33        # degrés, positif au nord
longitude = 2.77        # degrés, positif à l'est
elevation = 60           # mètres au dessus du niveau de la mer

date_heure_utc = "2026-08-12T17:30:00"  # format ISO, en UTC

# Construction du lieu et de l'instant
lieu = EarthLocation(lat=latitude * u.deg, lon=longitude * u.deg, height=elevation * u.m)
instant = Time(date_heure_utc, scale="utc")

# Calcul de la position du Soleil dans le référentiel local (horizon)
repere_altaz = AltAz(obstime=instant, location=lieu)
soleil_altaz = get_sun(instant).transform_to(repere_altaz)

print(f"Date/heure UTC : {instant.iso}")
print(f"Lieu : latitude {latitude}°, longitude {longitude}°, altitude {elevation} m")
print(f"Hauteur du Soleil : {soleil_altaz.alt:.3f}")
print(f"Azimut du Soleil : {soleil_altaz.az:.3f}")
