class user(object):
    def __init__(self, id, name, features):
        self.id = id
        self.name = name
        self.features = features

    def rateMovie(self, movie):
        minFeaturesLength = len(movie.features)
        if(minFeaturesLength > len(self.features)):
            minFeaturesLength = len(self.features)

        ratings = list(map((lambda x, y: 5 - abs(x-y)),
            self.features, movie.features))

        return sum(ratings)/minFeaturesLength
