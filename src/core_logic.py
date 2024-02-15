def execute_core_logic(categories, descriptions):
    # Initialize an empty dictionary to hold the category as key and descriptions as values
    category_dict = {category: [] for category in categories}

    # Variable to track the current category for descriptions that span multiple entries
    current_category = None

    # Iterate through each description in the descriptions array
    for description in descriptions:
        # Split the description by newline to analyze its components
        description_parts = description.split('\n')

        # Assume the first part is always the category or part of the description of the current category
        # Check if the first part of the description matches any category
        is_category_found = False
        for category in categories:
            if description_parts[0] == category:
                current_category = category
                is_category_found = True
                break

        # If a current category is found or we are continuing with the previous category
        if current_category and is_category_found:
            # Add the entire description excluding the category part to the new category
            category_dict[current_category].append('\n'.join(description_parts[1:]))
        elif current_category and not is_category_found:
            # Add the entire description to the current category
            category_dict[current_category].append(description)

    return category_dict
