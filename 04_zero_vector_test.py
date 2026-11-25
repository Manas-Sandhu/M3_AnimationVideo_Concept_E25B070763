
from manim import *
import numpy as np

# ============================================================
# BEYOND THE ARROWS
# VECTOR STORIES / STUDIO EDITION
#
# SCENE 04 — THE ZERO-VECTOR TEST
#
# A mathematical proof of linear independence and dependence.
#
# Visual direction:
# Charcoal / Ivory / Lime / Coral / Gold
# Editorial mathematical documentary
#
# Estimated duration: 75–90 seconds
# ============================================================


# -------------------- DESIGN SYSTEM -------------------------

BG = "#20201E"
CREAM = "#F2EBDD"
LIME = "#C6F277"
CORAL = "#FF765E"
GOLD = "#F2BE69"
GREY = "#A8A69F"
PANEL = "#30302C"
GRID = "#77776F"


class BeyondTheArrowsProof(Scene):

    def construct(self):

        self.camera.background_color = BG

        self.create_background()

        self.opening()
        self.independent_proof()
        self.dependent_proof()
        self.final_comparison()
        self.closing()

    # ========================================================
    # BACKGROUND
    # ========================================================

    def create_background(self):

        self.grid = NumberPlane(
            x_range=[-8, 8, 1],
            y_range=[-5, 5, 1],
            background_line_style={
                "stroke_color": GRID,
                "stroke_width": 0.7,
                "stroke_opacity": 0.10,
            },
            axis_config={
                "stroke_color": GREY,
                "stroke_opacity": 0.12,
            },
        )

        self.header = Text(
            "VECTOR STORIES   /   STUDIO EDITION",
            font="DejaVu Sans",
            font_size=15,
            color=GREY,
        ).to_corner(UL, buff=0.35)

        self.scene_label = Text(
            "04  —  THE ALGEBRAIC TEST",
            font="DejaVu Sans",
            font_size=14,
            color=LIME,
        ).to_corner(UR, buff=0.35)

        self.add(self.grid, self.header, self.scene_label)

    # ========================================================
    # SUBTITLE SYSTEM
    # ========================================================

    def subtitle(self, dialogue, duration=2.5, color=CREAM):

        panel = RoundedRectangle(
            corner_radius=0.12,
            width=12.0,
            height=0.85,
            fill_color=PANEL,
            fill_opacity=0.97,
            stroke_color=GREY,
            stroke_opacity=0.18,
            stroke_width=1,
        )

        accent = RoundedRectangle(
            corner_radius=0.025,
            width=0.055,
            height=0.48,
            fill_color=LIME,
            fill_opacity=1,
            stroke_width=0,
        )

        words = Text(
            dialogue,
            font="DejaVu Sans",
            font_size=19,
            color=color,
            weight=MEDIUM,
        )

        if words.width > 10.8:
            words.scale_to_fit_width(10.8)

        accent.move_to(panel.get_left() + RIGHT * 0.35)
        words.move_to(panel.get_center() + RIGHT * 0.1)

        group = VGroup(panel, accent, words)
        group.to_edge(DOWN, buff=0.22)

        self.play(
            FadeIn(group, shift=UP * 0.08),
            run_time=0.25,
        )

        self.wait(duration)

        self.play(
            FadeOut(group),
            run_time=0.2,
        )

    # ========================================================
    # REUSABLE ELEMENTS
    # ========================================================

    def heading(self, number, title, color=LIME):

        number_text = Text(
            number,
            font="DejaVu Sans",
            font_size=18,
            color=color,
            weight=BOLD,
        )

        title_text = Text(
            title,
            font="DejaVu Sans",
            font_size=25,
            color=CREAM,
            weight=BOLD,
        )

        group = VGroup(number_text, title_text)
        group.arrange(RIGHT, buff=0.22)
        group.to_corner(UL, buff=0.55)
        group.shift(DOWN * 0.48)

        return group

    def equation(self, tex, color=CREAM, size=40):

        return MathTex(
            tex,
            color=color,
            font_size=size,
        )

    def clear_objects(self, *objects):

        self.play(
            *[FadeOut(obj) for obj in objects],
            run_time=0.45,
        )

    # ========================================================
    # ACT 1 — THE QUESTION
    # ========================================================

    def opening(self):

        title = Text(
            "THE ZERO-VECTOR TEST",
            font="DejaVu Sans",
            font_size=43,
            color=CREAM,
            weight=BOLD,
        )

        subtitle_text = Text(
            "A diagram suggests. An equation proves.",
            font="DejaVu Sans",
            font_size=25,
            color=LIME,
        ).next_to(title, DOWN, buff=0.35)

        self.play(
            FadeIn(title, shift=UP * 0.2),
            run_time=0.6,
        )

        self.play(
            FadeIn(subtitle_text),
            run_time=0.5,
        )

        self.subtitle(
            "We have seen what independent and dependent vectors look like. Now we need a mathematical test.",
            duration=3.1,
        )

        self.subtitle(
            "The test begins by asking whether a linear combination of the vectors can equal zero.",
            duration=3.0,
            color=GOLD,
        )

        zero_equation = self.equation(
            r"c_1\vec v_1+c_2\vec v_2=\vec 0",
            CREAM,
            46,
        )

        zero_equation.next_to(subtitle_text, DOWN, buff=0.9)

        self.play(
            Write(zero_equation),
            run_time=0.8,
        )

        self.subtitle(
            "The coefficients decide whether the zero vector can be formed in a trivial or non-trivial way.",
            duration=3.1,
        )

        self.clear_objects(
            title,
            subtitle_text,
            zero_equation,
        )

    # ========================================================
    # ACT 2 — INDEPENDENT PAIR
    #
    # v1 = (1,1)
    # v2 = (1,-1)
    #
    # c1(1,1) + c2(1,-1) = (0,0)
    #
    # c1 + c2 = 0
    # c1 - c2 = 0
    #
    # Therefore c1 = c2 = 0.
    # ========================================================

    def independent_proof(self):

        heading = self.heading(
            "01",
            "TESTING INDEPENDENCE",
            LIME,
        )

        self.play(
            FadeIn(heading),
            run_time=0.4,
        )

        pair = self.equation(
            r"\vec v_1=(1,1),\qquad \vec v_2=(1,-1)",
            CREAM,
            34,
        ).move_to(UP * 1.55)

        self.play(
            Write(pair),
            run_time=0.7,
        )

        self.subtitle(
            "First, take our independent pair: one, one and one, minus one.",
            duration=2.8,
        )

        starting = self.equation(
            r"c_1(1,1)+c_2(1,-1)=(0,0)",
            GOLD,
            38,
        ).move_to(UP * 0.35)

        self.play(
            Write(starting),
            run_time=0.75,
        )

        self.subtitle(
            "We multiply each vector by its coefficient and add the components.",
            duration=2.7,
        )

        component_equations = VGroup(
            self.equation(
                r"c_1+c_2=0",
                CREAM,
                42,
            ),
            self.equation(
                r"c_1-c_2=0",
                CREAM,
                42,
            ),
        ).arrange(DOWN, buff=0.38)

        component_equations.move_to(DOWN * 0.85)

        self.play(
            FadeIn(component_equations, shift=UP * 0.15),
            run_time=0.65,
        )

        self.subtitle(
            "Equating the first and second components gives us these two equations.",
            duration=2.7,
        )

        # Add the two equations.
        addition = self.equation(
            r"(c_1+c_2)+(c_1-c_2)=0+0",
            GOLD,
            33,
        ).move_to(DOWN * 2.0)

        self.play(
            Write(addition),
            run_time=0.7,
        )

        self.subtitle(
            "Add the equations. The c2 terms cancel, leaving two c1 equal to zero.",
            duration=3.0,
            color=GOLD,
        )

        result_one = self.equation(
            r"2c_1=0\quad\Longrightarrow\quad c_1=0",
            LIME,
            38,
        ).move_to(DOWN * 2.0)

        self.play(
            Transform(addition, result_one),
            run_time=0.65,
        )

        result_two = self.equation(
            r"c_1+c_2=0\quad\Longrightarrow\quad c_2=0",
            LIME,
            35,
        ).next_to(result_one, DOWN, buff=0.35)

        self.play(
            Write(result_two),
            run_time=0.65,
        )

        self.subtitle(
            "Substituting c1 equal to zero into the first equation gives c2 equal to zero.",
            duration=3.0,
        )

        conclusion = Text(
            "ONLY THE TRIVIAL SOLUTION",
            font="DejaVu Sans",
            font_size=24,
            color=LIME,
            weight=BOLD,
        ).move_to(DOWN * 2.9)

        self.play(
            FadeIn(conclusion, shift=UP * 0.12),
            run_time=0.5,
        )

        self.subtitle(
            "Both coefficients must be zero. Therefore, this pair is linearly independent.",
            duration=3.2,
            color=LIME,
        )

        self.clear_objects(
            heading,
            pair,
            starting,
            component_equations,
            addition,
            result_two,
            conclusion,
        )

    # ========================================================
    # ACT 3 — DEPENDENT PAIR
    #
    # w1 = (1,2)
    # w2 = (2,4)
    #
    # c1(1,2) + c2(2,4) = (0,0)
    #
    # c1 + 2c2 = 0
    # 2c1 + 4c2 = 0
    #
    # Choose c2 = 1:
    # c1 = -2
    #
    # Non-trivial solution exists.
    # ========================================================

    def dependent_proof(self):

        heading = self.heading(
            "02",
            "TESTING DEPENDENCE",
            CORAL,
        )

        self.play(
            FadeIn(heading),
            run_time=0.4,
        )

        pair = self.equation(
            r"\vec w_1=(1,2),\qquad \vec w_2=(2,4)",
            CREAM,
            34,
        ).move_to(UP * 1.55)

        self.play(
            Write(pair),
            run_time=0.7,
        )

        self.subtitle(
            "Now consider our second pair: one, two and two, four.",
            duration=2.7,
        )

        starting = self.equation(
            r"c_1(1,2)+c_2(2,4)=(0,0)",
            GOLD,
            38,
        ).move_to(UP * 0.35)

        self.play(
            Write(starting),
            run_time=0.75,
        )

        self.subtitle(
            "Again, we multiply each vector by its coefficient and compare the components.",
            duration=2.8,
        )

        component_equations = VGroup(
            self.equation(
                r"c_1+2c_2=0",
                CREAM,
                42,
            ),
            self.equation(
                r"2c_1+4c_2=0",
                CREAM,
                42,
            ),
        ).arrange(DOWN, buff=0.38)

        component_equations.move_to(DOWN * 0.85)

        self.play(
            FadeIn(component_equations, shift=UP * 0.15),
            run_time=0.65,
        )

        self.subtitle(
            "Notice something important. The second equation is exactly twice the first.",
            duration=3.0,
            color=CORAL,
        )

        duplicate = self.equation(
            r"2(c_1+2c_2=0)",
            GOLD,
            36,
        ).move_to(DOWN * 2.0)

        self.play(
            Write(duplicate),
            run_time=0.65,
        )

        self.subtitle(
            "These equations do not give us two independent restrictions on the coefficients.",
            duration=3.0,
        )

        choice = self.equation(
            r"c_2=1",
            CORAL,
            42,
        ).move_to(DOWN * 2.0)

        self.play(
            Transform(duplicate, choice),
            run_time=0.55,
        )

        self.subtitle(
            "We are free to choose a non-zero value for c2. Let us choose one.",
            duration=2.7,
            color=CORAL,
        )

        solution = self.equation(
            r"c_1+2(1)=0\quad\Longrightarrow\quad c_1=-2",
            CORAL,
            36,
        ).next_to(duplicate, DOWN, buff=0.4)

        self.play(
            Write(solution),
            run_time=0.7,
        )

        self.subtitle(
            "The first equation then gives c1 equal to minus two.",
            duration=2.6,
        )

        nontrivial = self.equation(
            r"(c_1,c_2)=(-2,1)",
            LIME,
            43,
        ).move_to(DOWN * 2.9)

        self.play(
            Write(nontrivial),
            run_time=0.7,
        )

        self.subtitle(
            "We have found a solution where the coefficients are not both zero. This is a non-trivial solution.",
            duration=3.4,
            color=LIME,
        )

        conclusion = Text(
            "A NON-TRIVIAL SOLUTION EXISTS",
            font="DejaVu Sans",
            font_size=22,
            color=CORAL,
            weight=BOLD,
        ).move_to(DOWN * 3.55)

        self.play(
            FadeIn(conclusion),
            run_time=0.45,
        )

        self.subtitle(
            "Therefore, this pair is linearly dependent.",
            duration=2.5,
            color=CORAL,
        )

        self.clear_objects(
            heading,
            pair,
            starting,
            component_equations,
            duplicate,
            solution,
            nontrivial,
            conclusion,
        )

    # ========================================================
    # ACT 4 — COMPARISON
    # ========================================================

    def final_comparison(self):

        heading = self.heading(
            "03",
            "THE RESULT",
            GOLD,
        )

        self.play(
            FadeIn(heading),
            run_time=0.4,
        )

        left_title = Text(
            "INDEPENDENT",
            font="DejaVu Sans",
            font_size=23,
            color=LIME,
            weight=BOLD,
        ).move_to(UP * 1.65 + LEFT * 3.0)

        right_title = Text(
            "DEPENDENT",
            font="DejaVu Sans",
            font_size=23,
            color=CORAL,
            weight=BOLD,
        ).move_to(UP * 1.65 + RIGHT * 3.0)

        left_equation = self.equation(
            r"c_1=c_2=0",
            LIME,
            42,
        ).move_to(UP * 0.5 + LEFT * 3.0)

        right_equation = self.equation(
            r"(c_1,c_2)=(-2,1)",
            CORAL,
            38,
        ).move_to(UP * 0.5 + RIGHT * 3.0)

        left_note = Text(
            "Only the trivial solution",
            font="DejaVu Sans",
            font_size=18,
            color=CREAM,
        ).move_to(DOWN * 0.4 + LEFT * 3.0)

        right_note = Text(
            "A non-trivial solution exists",
            font="DejaVu Sans",
            font_size=18,
            color=CREAM,
        ).move_to(DOWN * 0.4 + RIGHT * 3.0)

        divider = Line(
            UP * 1.0,
            DOWN * 1.0,
            color=GREY,
            stroke_opacity=0.5,
        )

        self.play(
            FadeIn(left_title),
            FadeIn(right_title),
            Write(left_equation),
            Write(right_equation),
            Create(divider),
            run_time=0.9,
        )

        self.play(
            FadeIn(left_note),
            FadeIn(right_note),
            run_time=0.5,
        )

        self.subtitle(
            "The rule is simple: only the trivial solution means independence; a non-trivial solution means dependence.",
            duration=3.5,
            color=GOLD,
        )

        self.clear_objects(
            heading,
            left_title,
            right_title,
            left_equation,
            right_equation,
            left_note,
            right_note,
            divider,
        )

    # ========================================================
    # ACT 5 — CLOSING
    # ========================================================

    def closing(self):

        statement = Text(
            "FROM GEOMETRY TO ALGEBRA.",
            font="DejaVu Sans",
            font_size=36,
            color=CREAM,
            weight=BOLD,
        )

        statement_two = Text(
            "ONE EQUATION. TWO POSSIBILITIES.",
            font="DejaVu Sans",
            font_size=25,
            color=LIME,
            weight=BOLD,
        ).next_to(statement, DOWN, buff=0.35)

        self.play(
            FadeIn(statement, shift=UP * 0.15),
            FadeIn(statement_two, shift=UP * 0.15),
            run_time=0.65,
        )

        self.subtitle(
            "We can now distinguish independent and dependent vectors using a precise algebraic test.",
            duration=3.2,
        )

        self.wait(0.5)

        self.play(
            FadeOut(VGroup(statement, statement_two)),
            run_time=0.5,
        )
