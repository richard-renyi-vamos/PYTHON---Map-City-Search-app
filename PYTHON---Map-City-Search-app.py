import folium
import tkinter as tk
from geopy.geocoders import Nominatim

def search_city():
    city = entry.get()
    geolocator = Nominatim(user_agent="map_app")
    location = geolocator.geocode(city)
    
    if location:
        map = folium.Map(location=[location.latitude, location.longitude], zoom_start=10)
        folium.Marker([location.latitude, location.longitude], popup=city).add_to(map)
        
        map.save('map.html')  # Save map to a HTML file
        
        # Open the map in a web browser
        import webbrowser
        webbrowser.open('map.html')
    else:
        result_label.config(text="City not found")

# GUI setup
root = tk.Tk()
root.title("City Map App")

label = tk.Label(root, text="Enter city name:")
label.pack()

entry = tk.Entry(root)
entry.pack()

search_button = tk.Button(root, text="Search", command=search_city)
search_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
