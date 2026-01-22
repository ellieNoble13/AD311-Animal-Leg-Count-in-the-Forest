def countLegs(animals):
    count = 0
    fourLegs = ['lion', 'deer', 'elephant', 'horse', 'dog', 'cat']
    for animal in animals:
        if animal.lower()  in fourLegs:
            count +=1
    return count