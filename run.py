from demo.demo_loader import demoLoader

newDemo = demoLoader(3, 10, 5)
newDemo.initRandomUsersAndMovies()
newDemo.generateUserRatingMatrix()
newDemo.showResult()
