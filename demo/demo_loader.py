from .modal.user import user
from .modal.movie import movie
from random import uniform, shuffle


class demoLoader(object):
    def __init__(self, no_of_users, no_of_movies, no_of_features=4,
        random_rating_threshold = 0.5):
        self.no_of_users = no_of_users
        self.no_of_movies = no_of_movies
        self.no_of_features = no_of_features
        self.random_rating_threshold = random_rating_threshold

        self.user_rating_matrix = [[-1 for x in range(no_of_movies)]
            for y in range(no_of_users)]

    def initRandomUsersAndMovies(self):
        self.users = [user(id, "User:" + str(id),
            self.__createRandomFeatures(5)) for id in range(self.no_of_users)]
        self.movies = [movie(id, "Movie:" + str(id),
            self.__createRandomFeatures(1)) for id in range(self.no_of_movies)]

    def generateUserRatingMatrix(self):
        for user in self.users:
            for movie in self.movies:
                probability = uniform(0, 1)
                if(probability > self.random_rating_threshold):
                    self.user_rating_matrix[user.id][movie.id] = user.rateMovie(movie)

    def __createRandomFeatures(self, range):
        random_features = list(map(lambda x : uniform(0, range), range(self.no_of_features)))
        shuffle(random_features)
        return random_features

    def showResult(self):
        for user in self.users:
            print(f"{user.id} {user.name} {user.features}")

        for movie in self.movies:
            print(f"{movie.id} {movie.name} {movie.features}")

        for i in range(self.no_of_users):
            for j in range(self.no_of_movies):
                print(f"rating({i}, {j}) = {self.user_rating_matrix[i][j]}")

    def test(self):
        new_user = user(1, "Tanmay", [5, 1, 4, 0])
        new_movie = movie(1, "Moive", [4, 2, 5, 0])
        rating = new_user.rateMovie(new_movie)

        print(f"{new_user.name} rated {new_movie.name} {rating} starts.")
