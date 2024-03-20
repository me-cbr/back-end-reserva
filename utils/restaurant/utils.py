def calculate_classification(restaurant):
    avaliations = restaurant.restaurant_classification.all()
    if avaliations:
        total_avaliation = sum([classification.classification for classification in avaliations])
        return total_avaliation / len(avaliations)
    else:
        return 0