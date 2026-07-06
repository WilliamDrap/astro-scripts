from astropy.time import Time
from astropy.coordinates import get_body_barycentric
from astropy import units as u

def distance_terre_lune(instant_utc):
    """
    Calcule la distance Terre-Lune (centre à centre) pour un instant UTC donné.

    instant_utc : str au format ISO, ex "2026-08-12T10:30:00"
    """
    t = Time(instant_utc, scale="utc")

    # On récupère les positions barycentriques de la Terre et de la Lune via les
    # éphémérides intégrées à astropy (basées sur les données JPL par défaut),
    # on calcule le vecteur entre les deux, puis sa norme donne la distance centre à centre.
    pos_terre = get_body_barycentric("earth", t)
    pos_lune = get_body_barycentric("moon", t)

    vecteur = pos_lune - pos_terre
    distance = vecteur.norm().to(u.km)

    return distance

if __name__ == "__main__":
    instant = "2026-08-12T10:30:00"
    d = distance_terre_lune(instant)
    print(f"Distance Terre-Lune le {instant} UTC : {d:.1f}")
    print(f"Soit environ {d.to(u.au):.6f} unités astronomiques")
