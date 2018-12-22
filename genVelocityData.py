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

def randomRot():
    rotAxis = randomPos()#numpy.normalize(randomPos)
    angle = numpy.random.uniform(0.0, 2.0 * 3.14159)
    bpy.ops.transform.rotate(value=angle, axis=rotAxis)
    
def resetScene():
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False, confirm=False)

# create random geometry
def generateGeo():
    for i in range(0, OBJECT_COUNT):
        bpy.ops.mesh.primitive_cube_add(size=2, location=randomPos())
        randomRot()

def setupCamera():
    bpy.ops.object.camera_add(location=(0.0, 0.0, 10.0))
    bpy.context.scene.render.resolution_x = RENDER_RESOLUTION
    bpy.context.scene.render.resolution_y = RENDER_RESOLUTION
    bpy.context.scene.camera = bpy.context.object
    
def setupLighting():
    for i in range(0, LIGHT_COUNT):
        bpy.ops.object.light_add(type='AREA', radius=numpy.random.uniform(0, 5), location=randomPos())
        randomRot()


# add random keyframes
def animateGeo():
    for obj in bpy.context.scene.objects:
        # add a keframe @ t = 0
        f = 1
        obj.location = randomPos()
        #bpy.context.scene.frame_set(1)
        obj.keyframe_insert(data_path="location", frame=f)
        
        obj.location = randomPos()
        
        #bpy.context.scene.frame_set(numpy.random.uniform(5, 20))
        f = numpy.random.uniform(50, 100)
        obj.keyframe_insert(data_path="location", frame=f)
        bpy.ops.screen.frame_jump(end=False)

def renderFrames():
    f = int(numpy.random.uniform(5, 10))
    bpy.context.scene.frame_set(f)
    
    bpy.context.scene.render.filepath = "C:\\Users\\chandra\\desktop\\testPrev.png"
    bpy.ops.render.render(write_still=True)
    
    bpy.context.scene.render.filepath = "C:\\Users\\chandra\\desktop\\testNext.png"
    bpy.context.scene.frame_set(f + 1)
    bpy.ops.render.render(write_still=True)
    

def main():
    resetScene()
    generateGeo()
    animateGeo()
    setupCamera()
    setupLighting()
    renderFrames()
    
main()