import physicalCalculator
import windowObject
import objects

window = windowObject.window()

main = window.create2dPlane()

Main = objects.triangle(250, 250, (0, 0, 0), (150, 100), 0, resolution=100)
Main2 = objects.square(250, 450, (0, 0, 0), (50, 50), resolution=100)
Main3 = objects.circle(250, 250, (0, 0, 0), 100, 1)

physicalCalculator.physics.createCollisionTag(Main3)
physicalCalculator.physics.createGravityTag(Main3)

main.objects.append(Main2)
main.objects.append(Main3)

while True:
    physicalCalculator.physics.calc()
    window.update()
