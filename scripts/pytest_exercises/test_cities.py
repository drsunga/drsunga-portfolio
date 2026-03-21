from city_functions import get_city_country_loc

def test_city_country():
        full_location = get_city_country_loc('manila', 'philippines')
        assert full_location == 'Manila, Philippines'

def test_city_country_population():
        full_location = get_city_country_loc('taguig', 'philippines', population=110_000_000)
        assert full_location == 'Taguig, Philippines - Population=110000000'