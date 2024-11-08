#%%
import folium
import pandas as pd
from folium.plugins import HeatMap

dirfile = 'C:/Users/e_par/Downloads/BaseHYD.xlsx'
df = pd.read_excel(dirfile, sheet_name="eng")

#%%
lat_KHH = 22.620550
long_KHH = 120.312050

m = folium.Map(location=[lat_KHH, long_KHH], zoom_start=12)



# %%
#pedest = folium.FeatureGroup("pedestrian").add_to(m)
#moped = folium.FeatureGroup("moped").add_to(m)
jan = folium.FeatureGroup("january").add_to(m)
feb = folium.FeatureGroup("february").add_to(m)
mar = folium.FeatureGroup("march").add_to(m)
apr = folium.FeatureGroup("april").add_to(m)
may = folium.FeatureGroup("may").add_to(m)
jun = folium.FeatureGroup("june").add_to(m)
jul = folium.FeatureGroup("july").add_to(m)
aug = folium.FeatureGroup("august").add_to(m)
sep = folium.FeatureGroup("september").add_to(m)
oct = folium.FeatureGroup("october").add_to(m)
nov = folium.FeatureGroup("november").add_to(m)
dec = folium.FeatureGroup("december").add_to(m)


for i in range(len(df)):
    lat = df.loc[i,'Lat']
    long = df.loc[i,'Long']

    ## color

    if df.loc[i,'Deaths'] == 0:
        color_icon = 'orange'
    else:
        color_icon = 'red'


    #icon type

    type_icon = df.loc[i,'MopedPedestrian']

    match type_icon:
        case "Moped":
            icon_fig = "motorcycle"
        case "Pedestrian":
            icon_fig = "user"
        case "Both":
            icon_fig = "user-plus"
        case "No":
            icon_fig = 'minus-square'

    #month layer
    month = df.loc[i,'Month']
    match month:
        case 1:
            folium.Marker(location=[lat, long],
                            popup=df.loc[i,"D_I"],
                            icon=folium.Icon(color=color_icon,
                                                icon=icon_fig,
                                                prefix='fa'
                                                )).add_to(jan)
        case 2:
            folium.Marker(location=[lat, long],
                popup=df.loc[i,"D_I"],
                icon=folium.Icon(color=color_icon,
                                    icon=icon_fig,
                                    prefix='fa'
                                    )).add_to(feb)
        case 3:
            folium.Marker(location=[lat, long],
                popup=df.loc[i,"D_I"],
                icon=folium.Icon(color=color_icon,
                                    icon=icon_fig,
                                    prefix='fa'
                                    )).add_to(mar)
        case 4:
            folium.Marker(location=[lat, long],
                popup=df.loc[i,"D_I"],
                icon=folium.Icon(color=color_icon,
                                    icon=icon_fig,
                                    prefix='fa'
                                    )).add_to(apr)
        case 5:
            folium.Marker(location=[lat, long],
                popup=df.loc[i,"D_I"],
                icon=folium.Icon(color=color_icon,
                                    icon=icon_fig,
                                    prefix='fa'
                                    )).add_to(may)
        case 6:
            folium.Marker(location=[lat, long],
                popup=df.loc[i,"D_I"],
                icon=folium.Icon(color=color_icon,
                                    icon=icon_fig,
                                    prefix='fa'
                                    )).add_to(jun)
        case 7:
            folium.Marker(location=[lat, long],
                popup=df.loc[i,"D_I"],
                icon=folium.Icon(color=color_icon,
                                    icon=icon_fig,
                                    prefix='fa'
                                    )).add_to(jul)
        case 8:
            folium.Marker(location=[lat, long],
                popup=df.loc[i,"D_I"],
                icon=folium.Icon(color=color_icon,
                                    icon=icon_fig,
                                    prefix='fa'
                                    )).add_to(aug)
        case 9:
            folium.Marker(location=[lat, long],
                popup=df.loc[i,"D_I"],
                icon=folium.Icon(color=color_icon,
                                    icon=icon_fig,
                                    prefix='fa'
                                    )).add_to(sep)
        case 10:
            folium.Marker(location=[lat, long],
                popup=df.loc[i,"D_I"],
                icon=folium.Icon(color=color_icon,
                                    icon=icon_fig,
                                    prefix='fa'
                                    )).add_to(oct)
        case 11:
            folium.Marker(location=[lat, long],
                popup=df.loc[i,"D_I"],
                icon=folium.Icon(color=color_icon,
                                    icon=icon_fig,
                                    prefix='fa'
                                    )).add_to(nov)
        case 12:
            folium.Marker(location=[lat, long],
                popup=df.loc[i,"D_I"],
                icon=folium.Icon(color=color_icon,
                                    icon=icon_fig,
                                    prefix='fa'
                                    )).add_to(dec)

# %%
# Display the map
folium.LayerControl().add_to(m)
m.save("map2.html")

# %%
# Prepare the heatmap data
heat_data = [[row['Lat'], row['Long']] for index, row in df.iterrows()]

m = folium.Map(location=[lat_KHH, long_KHH], zoom_start=12)

# Add heatmap layer
HeatMap(heat_data, radius=15, blur=10, min_opacity=0.5).add_to(m)

# Save and display the map
m.save("binned_heatmap.html")


# %%
#! heatmap
bin_size = 0.001  # Adjust based on desired granularity

# Round the latitude and longitude to the nearest bin size
df['lat_bin'] = (df['Lat'] // bin_size) * bin_size
df['lon_bin'] = (df['Long'] // bin_size) * bin_size

# Group by the binned latitude and longitude, then count the occurrences
binned_data = df.groupby(['lat_bin', 'lon_bin']).size().reset_index(name='count')


# Prepare the heatmap data
heat_data = [[row['lat_bin'], row['lon_bin'], row['count']] for index, row in binned_data.iterrows()]

m = folium.Map(location=[lat_KHH, long_KHH], zoom_start=12)

# Add heatmap layer
HeatMap(heat_data, radius=15, blur=10, min_opacity=0.5).add_to(m)
