import json
import urllib2

GEO_API_URL = 'http://maps.google.com/maps/geo?key=GetYourOwnGoogleMapsApiKey&sensor=false'

def clean_zip(zip=None):
    return zip.replace(' ', '')

def google_whereami_zip(zip, city='', country='', state=''):
    zip = clean_zip(zip)

    # Create the geocoding url from settings
    geo_url = '%s&q=%s' %(GEO_API_URL, zip)

    # If we don't have a zip, don't bother processing
    if len(zip):

        # Don't bother making the api call if we already have a city/region
        if not len(city) or not len(state):
            try:
                data_string = urllib2.urlopen(geo_url).read()
                data = json.loads(data_string)
            except urllib2.HTTPError:
                data = ''

            if len(data):
                # Get the country code for our results
                try:
                    api_country_iso = data['Placemark'][0]['AddressDetails']['Country']['CountryNameCode']
                except KeyError:
                    api_country_iso = ''

                # Make sure we have results for the same country, we're not replacing US city/region with Europe
                if country.iso == api_country_iso:

                    # Only set the city if we passed in a blank one.
                    if not len(city):
                        try:
                            city = data['Placemark'][0]['AddressDetails']['Country']['AdministrativeArea']['Locality']['LocalityName']
                        except KeyError:
                            pass

                    # Only set the state if we passed in a blank one.
                    if not len(state):
                        try:
                            state = data['Placemark'][0]['AddressDetails']['Country']['AdministrativeArea']['AdministrativeAreaName']
                        except KeyError:
                            pass

    return zip, city, country, state
