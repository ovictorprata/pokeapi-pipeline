def categorize_base_experience(base_experinece):
    category =  None
    if base_experinece < 50:
        category = 'Fraco'
    elif base_experinece <= 100:
        category = 'Médio'
    else:
        category = 'Forte'
    return category