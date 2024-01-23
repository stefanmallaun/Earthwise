from flask import Flask, render_template, request, send_file, url_for, jsonify
from libr.worldmap.worldmap import plot
#import worldmap as wm
import libr.worldmap.worldmap.worldmap as wm
import io
import os
import shutil
from matplotlib.colors import ListedColormap
import json

app = Flask(__name__)

# Sample data
county_names = wm.list_county_names(map_name='world')


selected_countries = [' ']
selected_country = [' ']
opacity = 0.5
single_color_cmap = ListedColormap(['#06d009'])  
filename='World\static\selected_countries.txt'
is_reset = True
# Nutzerfreundlicher -> immer den ersten Buchstaben capital
def capitalize_first_letter(text):
    return text.capitalize()



# Function to save selected_countries to a text file
def save_selected_countries():
    with open(filename, 'w') as f:
        json.dump(selected_countries, f)

# Function to load selected_countries from a text file
def load_selected_countries():
    global selected_countries
    global selected_country
    try:
        with open(filename, 'r') as f:
            selected_countries = json.load(f)
    except FileNotFoundError:
        selected_countries = [' ']
    selected_country = [' ']

def generate_empty_svg_map():
    try:
        # Pass None as selected_countries to create an empty map
        svg_map_tuple = plot(None, opacity=opacity, cmap='Set1')
        return svg_map_tuple
    except Exception as e:
        return None

# Function to delete the SVG file and reset selected_countries
def delete_svg_file():
    global selected_countries
    global selected_country
    os.remove("World\static\custom_map.svg")
    with open(filename, 'w') as f:
        json.dump([" "], f)
    
    selected_countries = [' ']
    selected_country = [' ']
    return jsonify({'success': True})


load_selected_countries()

@app.route('/', methods=['GET', 'POST'])
def index():
    global selected_countries
    global is_reset
    message = ""

    map_exists = False

    if request.method == 'POST':
        if(is_reset):
            try:
                svg_map_tuple = plot([' '], opacity=opacity * len(selected_countries), cmap='ocean')
                is_reset = False
            except Exception as e:
                message = f"An error occurred while generating the map: {e}"
        else:
            
            selected_country = capitalize_first_letter(request.form.get('country'))
            
            for _ in range(10):
                print(selected_country)
            if selected_country in county_names:
                print(selected_country)
                if selected_country not in selected_countries:
                    selected_countries.append(selected_country)
                    message = f"{selected_country} added."
                    try:
                        svg_map_tuple = plot(selected_countries, opacity=opacity * len(selected_countries), cmap='Green')
                    except Exception as e:
                        message = f"An error occurred while generating the map: {e}"
                else:
                    message = f"{selected_country} is already selected."
            else:
                message = f"{selected_country} is not a valid country."


    # Save selected_countries to the text file before rendering the template
    save_selected_countries()
    return render_template('index.html', map_exists=map_exists, message=message, selected_countries=selected_countries)

@app.route('/reset', methods=['GET', 'POST'])
def reset():
    global selected_countries
    global is_reset 
    is_reset = True
    if(delete_svg_file()):
        return jsonify({'success': True})
    else: 
        return False



if __name__ == '__main__':
    app.run(debug=True)