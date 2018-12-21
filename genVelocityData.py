import bpy
import numpy

numSamples = 100

def generateGeo():
    x = 20.0 * numpy.random.uniform() - 10.0
    y = 20.0 * numpy.random.uniform() - 10.0
    z = 20.0 * numpy.random.uniform() - 10.0
    
    bpy.ops.mesh.primitive_cube_add(size=2, location=(x,y,z))

def main():
    for i in range(0, numSamples):
        generateGeo()
        #animateGeo()
        
        #renderFrame(i)
    
main()