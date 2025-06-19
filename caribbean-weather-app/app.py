from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Caribbean cities (name, lat, lon)
CITIES = [
    {"name": "All Saints, Antigua and Barbuda", "lat": 17.0739, "lon": -61.7978},
    {"name": "Barrouallie, Saint Vincent and the Grenadines", "lat": 13.2245, "lon": -61.2583},
    {"name": "Basseterre, Saint Kitts and Nevis", "lat": 17.2955, "lon": -62.7266},
    {"name": "Belmopan, Belize", "lat": 17.2514, "lon": -88.7590},
    {"name": "Belize City, Belize", "lat": 17.5046, "lon": -88.1962},
    {"name": "Bridgetown, Barbados", "lat": 13.0975, "lon": -59.6177},
    {"name": "Brades, Montserrat", "lat": 16.7919, "lon": -62.2106},
    {"name": "Camagüey, Cuba", "lat": 21.3808, "lon": -77.9169},
    {"name": "Cap-Haïtien, Haiti", "lat": 19.7594, "lon": -72.2090},
    {"name": "Castries, Saint Lucia", "lat": 14.0101, "lon": -60.9875},
    {"name": "Charlestown, Saint Kitts and Nevis", "lat": 17.1200, "lon": -62.6252},
    {"name": "Charlotte Amalie, U.S. Virgin Islands", "lat": 18.3419, "lon": -64.9307},
    {"name": "Christiansted, U.S. Virgin Islands", "lat": 17.7466, "lon": -64.7025},
    {"name": "Cockburn Town, Turks and Caicos Islands", "lat": 21.4735, "lon": -71.1396},
    {"name": "Cruz Bay, U.S. Virgin Islands", "lat": 18.3333, "lon": -64.7936},
    {"name": "Fort-de-France, Martinique", "lat": 14.6161, "lon": -61.0588},
    {"name": "Freeport, Bahamas", "lat": 26.5333, "lon": -78.7000},
    {"name": "Georgetown, Guyana", "lat": 6.8013, "lon": -58.1552},
    {"name": "Georgetown, Saint Vincent and the Grenadines", "lat": 13.2656, "lon": -61.1819},
    {"name": "George Town, Cayman Islands", "lat": 19.2869, "lon": -81.3674},
    {"name": "Gouyave, Grenada", "lat": 12.1696, "lon": -61.7297},
    {"name": "Gustavia, Saint Barthélemy", "lat": 17.8962, "lon": -62.8501},
    {"name": "Gonaïves, Haiti", "lat": 19.4473, "lon": -72.6833},
    {"name": "Grenville, Grenada", "lat": 12.1310, "lon": -61.6888},
    {"name": "Havana, Cuba", "lat": 23.1136, "lon": -82.3666},
    {"name": "Kingstown, Saint Vincent and the Grenadines", "lat": 13.1600, "lon": -61.2248},
    {"name": "Kingston, Jamaica", "lat": 17.9642, "lon": -76.7923},
    {"name": "Kralendijk, Bonaire", "lat": 12.1443, "lon": -68.2655},
    {"name": "Lelydorp, Suriname", "lat": 5.7079, "lon": -55.2345},
    {"name": "Liberta, Antigua and Barbuda", "lat": 17.0564, "lon": -61.8093},
    {"name": "Linden, Guyana", "lat": 6.0081, "lon": -58.3075},
    {"name": "Marigot, Dominica", "lat": 15.5389, "lon": -61.3923},
    {"name": "Marigot, Saint Martin", "lat": 18.0663, "lon": -63.0822},
    {"name": "Mayagüez, Puerto Rico", "lat": 18.2016, "lon": -67.1396},
    {"name": "Montego Bay, Jamaica", "lat": 18.4762, "lon": -77.8939},
    {"name": "Nassau, Bahamas", "lat": 25.0343, "lon": -77.3963},
    {"name": "Nieuw Nickerie, Suriname", "lat": 5.9427, "lon": -56.9874},
    {"name": "Oistins, Barbados", "lat": 13.0650, "lon": -59.5338},
    {"name": "Oranjestad, Aruba", "lat": 12.5092, "lon": -70.0086},
    {"name": "Oranjestad, Sint Eustatius", "lat": 17.4890, "lon": -62.9736},
    {"name": "Paramaribo, Suriname", "lat": 5.8664, "lon": -55.1668},
    {"name": "Philipsburg, Sint Maarten", "lat": 18.0075, "lon": -63.0413},
    {"name": "Plymouth, Montserrat", "lat": 16.7050, "lon": -62.2129},
    {"name": "Pointe-à-Pitre, Guadeloupe", "lat": 16.2416, "lon": -61.5330},
    {"name": "Port-au-Prince, Haiti", "lat": 18.5944, "lon": -72.3074},
    {"name": "Port of Spain, Trinidad and Tobago", "lat": 10.6549, "lon": -61.5019},
    {"name": "Portsmouth, Dominica", "lat": 15.5838, "lon": -61.4744},
    {"name": "Providenciales, Turks and Caicos Islands", "lat": 21.7767, "lon": -72.2659},
    {"name": "Road Town, British Virgin Islands", "lat": 18.4260, "lon": -64.6208},
    {"name": "Roseau, Dominica", "lat": 15.3014, "lon": -61.3899},
    {"name": "San Ignacio, Belize", "lat": 17.1612, "lon": -89.0636},
    {"name": "San Juan, Puerto Rico", "lat": 18.4655, "lon": -66.1057},
    {"name": "San Nicolas, Aruba", "lat": 12.4205, "lon": -69.8806},
    {"name": "San Pedro de Macorís, Dominican Republic", "lat": 18.4508, "lon": -69.2963},
    {"name": "Santiago de Cuba, Cuba", "lat": 20.0247, "lon": -75.8214},
    {"name": "Santiago de los Caballeros, Dominican Republic", "lat": 19.4792, "lon": -70.6931},
    {"name": "Santo Domingo, Dominican Republic", "lat": 18.4861, "lon": -69.9312},
    {"name": "Sauteurs, Grenada", "lat": 12.2212, "lon": -61.6390},
    {"name": "Scarborough, Trinidad and Tobago", "lat": 11.1853, "lon": -60.7390},
    {"name": "Speightstown, Barbados", "lat": 13.2507, "lon": -59.6430},
    {"name": "Spanish Town, Jamaica", "lat": 17.9833, "lon": -76.9547},
    {"name": "St. George's, Grenada", "lat": 12.0561, "lon": -61.7488},
    {"name": "St. John's, Antigua and Barbuda", "lat": 17.1219, "lon": -61.8457},
    {"name": "The Bottom, Saba", "lat": 17.6261, "lon": -63.2402},
    {"name": "The Valley, Anguilla", "lat": 18.2170, "lon": -63.0578},
    {"name": "Victoria, Grenada", "lat": 12.1938, "lon": -61.7039},
    {"name": "Vieux Fort, Saint Lucia", "lat": 13.7166, "lon": -60.9471},
    {"name": "West End, Bahamas", "lat": 26.6861, "lon": -78.9964},
    {"name": "Willemstad, Curaçao", "lat": 12.1097, "lon": -68.9301}
]

@app.route('/cities')
def cities():
    return jsonify(CITIES)

@app.route('/forecast')
def forecast():
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    tz = request.args.get('tz', 'America/New_York')
    if lat is None or lon is None:
        return jsonify({"error": "Missing lat/lon"}), 400

    url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={lat}&longitude={lon}"
        "&daily=temperature_2m_max,temperature_2m_min,precipitation_sum,uv_index_max," 
        "wind_speed_10m_max,weathercode"
        f"&timezone={tz}"
    )
    response = requests.get(url)
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)