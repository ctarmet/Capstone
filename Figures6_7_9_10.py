from manim import *


class Figure6(Scene):
    def construct(self):
        self.camera.background_color = BLACK
        triangle = Triangle().scale(3)
        
        triangle.set_fill(BLUE, opacity=1).set_stroke(width=0)
        self.play(FadeIn(triangle))
        self.wait()
        self.play(triangle.animate.scale(0.5).move_to(ORIGIN))
        self.wait()
        t = Triangle().scale(3)
        t.set_fill(BLUE, opacity=1)
        t.set_color(BLUE)
        vertices = t.get_vertices()
        t1 = triangle.copy()
        t2 = triangle.copy()
        triangle.set_fill(BLUE, opacity=1).set_stroke(width=0)
        t1.set_fill(RED, opacity=1).set_stroke(width=0)
        
        t2.set_fill(YELLOW, opacity=1).set_stroke(width=0)
        
        
        self.play(AnimationGroup(triangle.animate.shift(0.5*vertices[0]),
                                t1.animate.shift(0.5*vertices[1]), t2.animate.shift(0.5*vertices[2])))
        
        self.wait()

        group = VGroup(triangle, t1, t2)
        self.play(group.animate.scale(0.5).move_to(ORIGIN))
        self.wait()

        g1 = group.copy()
        g2 = group.copy()

        g1.set_fill(RED, opacity=1).set_stroke(width=0)
        
        g2.set_fill(YELLOW, opacity=1).set_stroke(width=0)
        
        
        group.set_fill(BLUE, opacity=1).set_stroke(width=0)
        
        self.play(AnimationGroup(group.animate.shift(0.5*vertices[0]),
                                 g1.animate.shift(0.5*vertices[1]),
                                 g2.animate.shift(0.5*vertices[2])))
        
        self.wait()

        gr = VGroup(group, g1, g2)
        self.play(gr.animate.scale(0.5).move_to(ORIGIN))
        self.wait()

        gr1 = gr.copy()
        gr2 = gr.copy()

        gr1.set_fill(RED, opacity=1).set_stroke(width=0)
        
        gr2.set_fill(YELLOW, opacity=1).set_stroke(width=0)
        
        
        gr.set_fill(BLUE, opacity=1).set_stroke(width=0)
        
        self.play(AnimationGroup(gr.animate.shift(0.5*vertices[0]),
                                 gr1.animate.shift(0.5*vertices[1]),
                                 gr2.animate.shift(0.5*vertices[2])))
        
        self.wait()

        gro = VGroup(gr, gr1, gr2)
        self.play(gro.animate.scale(0.5).move_to(ORIGIN))
        self.wait()

        gro1 = gro.copy()
        gro2 = gro.copy()

        gro1.set_fill(RED, opacity=1).set_stroke(width=0)
        
        gro2.set_fill(YELLOW, opacity=1).set_stroke(width=0)
        
       
        
        gro.set_fill(BLUE, opacity=1).set_stroke(width=0)
        
        self.play(AnimationGroup(gro.animate.shift(0.5*vertices[0]),
                                 gro1.animate.shift(0.5*vertices[1]),
                                 gro2.animate.shift(0.5*vertices[2])))
        
        self.wait()

        grou = VGroup(gro, gro1, gro2)
        self.play(grou.animate.scale(0.5).move_to(ORIGIN))
        self.wait()

        grou1 = grou.copy()
        grou2 = grou.copy()

        grou1.set_fill(RED, opacity=1).set_stroke(width=0)
        
        grou2.set_fill(YELLOW, opacity=1).set_stroke(width=0)
        
        grou.set_fill(BLUE, opacity=1).set_stroke(width=0)
        
        self.play(AnimationGroup(grou.animate.shift(0.5*vertices[0]),
                                 grou1.animate.shift(0.5*vertices[1]),
                                 grou2.animate.shift(0.5*vertices[2])))
        
        self.wait(3)
        

class Figure7(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        c1 = 3 * 0.25 * (np.sqrt(5) - 1)
        c2 = 3 * 0.25 * (np.sqrt(5) + 1)
        s1 = 3 * 0.25 * (np.sqrt(10 + 2 * np.sqrt(5)))
        s2 = 3 * 0.25 * (np.sqrt(10 - 2 * np.sqrt(5)))
        p1 = np.array([-s2, -c2, 0])
        p2 = np.array([s2, -c2, 0])
        p3 = np.array([s1, c1, 0])
        p4 = np.array([0, 3, 0])
        p5 = np.array([-s1, c1, 0])

        a1 = Arrow(start=p1,end=p2)
        a2 = Arrow(start=p2,end=p3)
        a3 = Arrow(start=p3,end=p4)
        a4 = Arrow(start=p4,end=p5)
        a5 = Arrow(start=p5,end=p1)
        a6 = Arrow(start=p1,end=p3)
        a7 = Arrow(start=p1,end=p4)
        a8 = Arrow(start=p5,end=p3)
        a9 = Arrow(start=p5,end=p2)
        a10 = Arrow(start=p2,end=p4)

        l1 = Line(start=p1,end=p2,stroke_width=2)
        l2 = Line(start=p2,end=p3,stroke_width=2)
        l3 = Line(start=p3,end=p4,stroke_width=2)
        l4 = Line(start=p4,end=p5,stroke_width=2)
        l5 = Line(start=p5,end=p1,stroke_width=2)

        a1.color = RED
        a2.color = RED
        a3.color = RED
        a4.color = RED
        a5.color = RED
        a6.color = BLACK
        a7.color = BLACK
        a8.color = BLACK
        a9.color = BLACK
        a10.color = BLACK

        l1.color = BLACK
        l2.color = BLACK
        l3.color = BLACK
        l4.color = BLACK
        l5.color = BLACK

        self.add(a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,l1,l2,l3,l4,l5)


class Figure9(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        p1 = np.array([-2,-1,0])
        p2 = np.array([2,-1,0])

        yellow_color = rgb_to_color([254, 204, 0])
        blue_color = rgb_to_color([0, 106, 167])

        l1 = Line(start=p1, end=p2, color = blue_color, stroke_width = 7)

        p3 = np.array([-2,1,0])
        p4 = np.array([0,1,0])

        l2 = Line(start=p3, end=p4, color = yellow_color, stroke_width = 7)

        p5 = np.array([0,-1,0]) # Middle bottom

        self.add(l1)
        self.add(l2)

        self.add(Dot(p1, color=BLACK), Dot(p2, color=BLACK), Dot(p3, color=BLACK), 
                 Dot(p4, color=BLACK), Dot(p5, color=BLACK)) 
                 
        lab1 = MathTex("A").next_to(p1, DOWN)
        lab2 = MathTex("B").next_to(p5, DOWN)
        lab3 = MathTex("C").next_to(p2, DOWN)
        lab4 = MathTex("D").next_to(p4, UP)
        lab5 = MathTex("E").next_to(p3, UP)
        
        lab1.color = BLACK
        lab2.color = BLACK
        lab3.color = BLACK
        lab4.color = BLACK
        lab5.color = BLACK
        

        self.add(lab1, lab2, lab3, lab4, lab5)


class Figure10(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        p1 = np.array([-3,-1,0])
        p2 = np.array([3,-1,0])

        yellow_color = rgb_to_color([254, 204, 0])
        blue_color = rgb_to_color([0, 106, 167])

        l1 = Line(start=p1, end=p2, color = blue_color, stroke_width = 7)

        p3 = np.array([-4,1,0])
        p4 = np.array([0,1,0])

        l2 = Line(start=p3, end=p4, color = yellow_color, stroke_width = 7)

        p5 = np.array([0,1,0]) # Middle top
        p6 = np.array([0,-1,0]) # Middle bottom
        p7 = np.array([-3,1,0]) # F
        p8 = np.array([1,-1,0]) # K
        p9 = np.array([-1,-1,0]) # J
        p10 = np.array([-1,1,0]) # G


        dl1 = DashedLine(
            start=p1,
            end=p7,
            color=BLACK,
            dashed_ratio=0.5,  # Ratio of dash length to gap length
            dash_length=0.1    # Length of each dash
        )

        dl2 = DashedLine(
            start=p9,
            end=p10,
            color=BLACK,
            dashed_ratio=0.5,  # Ratio of dash length to gap length
            dash_length=0.1    # Length of each dash
        )

        self.add(l1)
        self.add(l2)
        self.add(dl1,dl2)

        self.add(Dot(p1, color=BLACK), Dot(p2, color=BLACK), Dot(p3, color=BLACK), 
                 Dot(p4, color=BLACK), Dot(p5, color=BLACK), Dot(p6, color=BLACK), 
                 Dot(p7, color=BLACK), Dot(p9, color=BLACK), Dot(p10, color=BLACK))
        
        lab1 = MathTex("A").next_to(p1, DOWN)
        lab2 = MathTex("B").next_to(p9, DOWN)
        lab3 = MathTex("C").next_to(p6, DOWN)
        lab4 = MathTex("D").next_to(p5, UP)
        lab5 = MathTex("E").next_to(p10, UP)
        lab6 = MathTex("F").next_to(p7, UP)
        lab7 = MathTex("G").next_to(p3, UP)
        lab8 = MathTex("H").next_to(p2, DOWN)
        lab1.color = BLACK
        lab2.color = BLACK
        lab3.color = BLACK
        lab4.color = BLACK
        lab5.color = BLACK
        lab6.color = BLACK
        lab7.color = BLACK
        lab8.color = BLACK

        self.add(lab1, lab2, lab3, lab4, lab5, lab6, lab7, lab8)
        

