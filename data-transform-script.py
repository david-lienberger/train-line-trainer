import json

def transform_json(input_json):
    # Load the JSON data
    with open(input_json, 'r') as file:
        data = json.load(file)

    # Initialize the transformed structure
    transformed_data = {
        "origins": [],
        "general": {
            "all_lines": []
        }
    }

    # Populate the 'origins' part
    for station_key, station_info in data.get('origins', {}).items():
        transformed_data['origins'].append({
            station_key: {
                "label": station_info.get("label", "")
            }
        })

    # Populate the 'general' -> 'all_lines' part
    for line in data.get('general', {}).get('all_lines', []):
        new_line = {
            "label": line.get("label", ""),
            "color": line.get("color", ""),
            "station_code_max_stretch_1": line.get("station_code_max_stretch_1", ""),
            "station_code_max_stretch_2": line.get("station_code_max_stretch_2", ""),
            "basetacts": []
        }

        for basetact in line.get("basetacts", []):
            new_basetact = {
                "interval_minutes": basetact.get("interval_minutes", 0),
                "departure_minutes": basetact.get("departure_minutes", ""),
                "lineflowstops": []
            }

            for stop in basetact.get("lineflowstops", []):
                new_stop = {
                    "station_code": stop.get("station_code", ""),
                    "station_label": stop.get("station_label", ""),
                    "departure_minute": stop.get("departure_minute", ""),
                    "arrival_minute": stop.get("arrival_minute", ""),
                    "is_origin": stop.get("is_origin", False),
                    "is_departure": stop.get("is_departure", False)
                }
                new_basetact['lineflowstops'].append(new_stop)

            new_line['basetacts'].append(new_basetact)

        transformed_data['general']['all_lines'].append(new_line)

    return transformed_data

def main():
    input_json = 'input.json'  # Replace with your input JSON file path
    output_json = 'output.json'  # Replace with your desired output JSON file path

    transformed_data = transform_json(input_json)

    # Write the transformed JSON data to a file
    with open(output_json, 'w') as file:
        json.dump(transformed_data, file, indent=4)

if __name__ == "__main__":
    main()
