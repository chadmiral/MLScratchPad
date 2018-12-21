import bpy
import numpy

OBJECT_COUNT = 100
LIGHT_COUNT = 10
RENDER_RESOLUTION = 512

def randomPos():
    x = numpy.random.uniform(-10, 10)
    y = numpy.random.uniform(-10, 10)
    z = numpy.random.uniform(-10, 10)
    return (x,y,z)

# create random geometry
def generateGeo():
    for i in range(0, OBJECT_COUNT):
        
        bpy.ops.mesh.primitive_cube_add(size=2, location=randomPos())

def setupCamera():
    bpy.ops.object.camera_add(location=(0.0, 0.0, 10.0))
    bpy.context.scene.render.resolution_x = RENDER_RESOLUTION
    bpy.context.scene.render.resolution_y = RENDER_RESOLUTION
    
def setupLighting():
    for i in range(0, LIGHT_COUNT):
        bpy.ops.object.light_add(type='AREA', radius=numpy.random.uniform(0, 5), location=randomPos())

# add random keyframes
def animateGeo():
    for obj in bpy.context.scene.objects:
        # add a keframe @ t = 0
        f =1
        obj.location = randomPos()
        #bpy.context.scene.frame_set(1)
        obj.keyframe_insert(data_path="location", frame=f)
        
        obj.location = randomPos()
        
        #bpy.context.scene.frame_set(numpy.random.uniform(5, 20))
        f = numpy.random.uniform(5, 100)
        obj.keyframe_insert(data_path="location", frame=f)
        bpy.ops.screen.frame_jump(end=False)

def main():
    generateGeo()
    animateGeo()
    setupCamera()
    setupLighting()
    
    #renderFrames(i)
    
main()