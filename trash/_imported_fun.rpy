init python:
    def silhouette_matrix (r,g,b,a):
        return im.matrix((0, 0, 0, 0, r,
                    0, 0, 0, 0, g,
                    0, 0, 0, 0, b,
                    0, 0, 0, a, 0,))
    def silhouetted (filename, r,g,b, a = 1.0):
        return im.MatrixColor (Image (filename), silhouette_matrix (r,g,b,a))

    def sss(filename):
        return im.MatrixColor(filename, im.matrix.brightness(0.0))
define foto = "friz/main/friz_otoja.png"
define heh = "background/bedroom.png"
image ii = sss(heh)

image glowing= silhouetted(foto, 0.872,0.66,0.128)

init python:
    import math
    import pygame
    class BoxBlur(im.ImageBase):
        def __init__(self, imname, r, **properties):
            image = im.image(imname)
            super(BoxBlur, self).__init__(image, r, **properties)
            self.image = image
            if isinstance(r, (int, long, float)):
                r = (r, r)
            self.r = r
        def get_mtime(self):
            return self.image.get_mtime()
        def load(self):
            # Collect metrics
            origsurf = im.cache.get(self.image)
            size = origsurf.get_size()
            hr, vr = self.r[0], self.r[1]
            hrate = math.ceil(256.0 / (hr * 2 + 1))
            vrate = math.ceil(256.0 / (vr * 2 + 1))

            # Create buffer
            fracsurf = renpy.display.pgrender.surface(size, True)
            retsurf = renpy.display.pgrender.surface(size, True)

            # Vertical blur
            renpy.display.module.linmap(
                origsurf, fracsurf, vrate, vrate, vrate, vrate)
            retsurf.fill(0)
            for y in range(-vr, vr + 1):
                retsurf.blit(fracsurf, (0, y), None, pygame.BLEND_RGBA_ADD)

            # Horizontal blur
            renpy.display.module.linmap(
                retsurf, fracsurf, hrate, hrate, hrate, hrate)
            retsurf.fill(0)
            for x in range(-hr, hr + 1):
                retsurf.blit(fracsurf, (x, 0), None, pygame.BLEND_RGBA_ADD)

            return retsurf
        def predict_files(self):
            return self.image.predict_files()
    a=Fade(.25, 0, .75, color="#fff")

image glo = BoxBlur(foto,3)
