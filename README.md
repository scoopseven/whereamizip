Python function to get city/state from Google Maps API when provided a valid zip/postal code.

A new city/state is only returned from the API when they're not passed in or blank ones are passed
in, to prevent over-writing existing data.

Replace GetYourOwnGoogleMapsApiKey with a Google API key from https://developers.google.com/maps/signup

Accepts:
zip - string (required) Any valid postal code.
city - string (optional) Won't be overwritten if provided.
country - string, 2 letter iso code
state - string (optional) Won't be overwritten if provided.

Returns:
zip - unmodified
city - string from Google API
country - unmodified
state - string from Google API