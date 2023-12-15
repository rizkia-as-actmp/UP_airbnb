def findOut(objectData) :
    try:
        # Try using vars() to get the dictionary of object attributes
        tes_attributes = vars(objectData)
        
        # Print all fields and their values
        for field, value in tes_attributes.items():
            print(f"{field}: {value}")

    except Exception as e:
        print(f"Error retrieving object attributes: {e}") 