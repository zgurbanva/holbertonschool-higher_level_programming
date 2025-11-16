import os

def generate_invitations(template, attendees):
    """
    Generates personalized invitation files based on a text template and
    a list of attendee dictionaries.
    """

    # --------------------------
    # Validate input types
    # --------------------------
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return

    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return

    # --------------------------
    # Handle empty template
    # --------------------------
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    # --------------------------
    # Handle empty attendee list
    # --------------------------
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    # --------------------------
    # Process each attendee
    # --------------------------
    for index, attendee in enumerate(attendees, start=1):
        # Replace placeholders with values or N/A if missing
        processed = template
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(key)
            if not value:  
                value = "N/A"
            processed = processed.replace("{" + key + "}", value)

        # Output filename
        output_filename = f"output_{index}.txt"

        try:
            # Write the file
            with open(output_filename, "w", encoding="utf-8") as f:
                f.write(processed)
        except Exception as e:
            print(f"Error writing file {output_filename}: {e}")
            continue  # Continue generating other files if one fails

