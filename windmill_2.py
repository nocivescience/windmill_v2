from manim import *
import itertools as it
class WindmillData(Scene):
    CONFIG0={
        'dot_config':{
            'radius':0.07,
        },
        'color_dots':[GREEN,YELLOW,RED],
        'windmill_length':2*config['frame_width'],
        'windmill_rotation_speed':0.25,
        'style_windmill':{
            'style_stroke':RED,
            'stroke_width':2,
        }
    }
    def get_random_points_set(self,n_points=11,width=12,height=6):
        return np.array([
            [
                -width/2+np.random.random()*width,
                -height/2+np.random.random()*height,
                0
            ]
            for n in range(n_points)
        ])
    def get_dots(self,points):
        color_dot=it.cycle(self.CONFIG0['color_dots'])
        return VGroup(*[
            Dot(color=next(color_dot),**self.CONFIG0['dot_config']).move_to(point) for point in points
        ])
    def get_windmill(self,points,pivot=None,angle=TAU/6):
        line=Line(LEFT,RIGHT)
        line.set_angle(angle)
        line.set_length(self.CONFIG['windmill_length'])
        line.set_style(**self.CONFIG['windmill_style'])
        line.pivot_set=points
        if pivot is not None:
            line.pivot=pivot
        else:
            line.pivot=points[0]
class WindmillScene(WindmillData):
    CONFIG={
        'final_run_time':60,
        'windmill_rotation_speed':0.5
    }
    def construct(self):
        self.add_points()
    def add_points(self):
        points=self.get_random_points_set(40)
        dots=self.get_dots(points=points)
        self.play(
            LaggedStartMap(DrawBorderThenFill,dots)
        )
        self.wait()