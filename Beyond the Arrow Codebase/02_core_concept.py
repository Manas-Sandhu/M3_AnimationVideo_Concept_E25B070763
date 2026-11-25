
from manim import *
import numpy as np


# ============================================================
# BEYOND THE ARROWS
# PALAK EDITION
# SCENE 02 — THE RULES OF THE GAME
#
# Mathematical focus:
# Linear combinations
# Trivial and non-trivial solutions
# Linear independence and dependence
# ============================================================


class BeyondTheArrowsConcept(Scene):

    # --------------------------------------------------------
    # DESIGN SYSTEM
    # --------------------------------------------------------

    BG = "#20201E"
    CREAM = "#F2EBDD"
    LIME = "#C6F277"
    CORAL = "#FF765E"
    GOLD = "#F2BE69"
    GREY = "#A8A69F"
    PANEL = "#30302C"
    GRID = "#77776F"

    # --------------------------------------------------------
    # BACKGROUND
    # --------------------------------------------------------

    def background(self):

        grid = NumberPlane(
            x_range=[-8, 8, 0.5],
            y_range=[-4.5, 4.5, 0.5],
            background_line_style={
                "stroke_color": self.GRID,
                "stroke_opacity": 0.07,
                "stroke_width": 0.6,
            },
            axis_config={
                "stroke_opacity": 0,
            },
        )

        grid.set_z_index(-3)
        self.add(grid)

        header = Text(
            "VECTOR STORIES  /  02 — THE MATHEMATICS",
            font_size=12,
            color=self.LIME,
            weight=BOLD,
        ).to_corner(UL, buff=0.38)

        self.add(header)

    # --------------------------------------------------------
    # SUBTITLES
    # --------------------------------------------------------

    def subtitle(self, message, duration=2.5):

        caption = Text(
            message,
            font="DejaVu Sans",
            font_size=18,
            color=self.CREAM,
        ).set_max_width(11)

        panel = RoundedRectangle(
            corner_radius=0.08,
            width=12,
            height=0.72,
            stroke_width=0,
            fill_color=self.PANEL,
            fill_opacity=1,
        )

        marker = Rectangle(
            width=0.07,
            height=0.34,
            stroke_width=0,
            fill_color=self.LIME,
        )

        caption.move_to(panel.get_center())
        marker.move_to(panel.get_left() + RIGHT * 0.28)

        group = VGroup(panel, marker, caption)
        group.to_edge(DOWN, buff=0.18)

        if hasattr(self, "active_subtitle"):
            self.play(
                FadeOut(self.active_subtitle),
                FadeIn(group, shift=UP * 0.06),
                run_time=0.22,
            )
        else:
            self.play(
                FadeIn(group),
                run_time=0.22,
            )

        self.active_subtitle = group
        self.wait(duration)

    # --------------------------------------------------------
    # SECTION HEADING
    # --------------------------------------------------------

    def section_heading(self, number, heading, accent=None):

        number_text = Text(
            number,
            font_size=15,
            color=self.LIME,
            weight=BOLD,
        )

        title = Text(
            heading,
            font_size=31,
            color=self.CREAM,
            weight=BOLD,
        )

        group = VGroup(
            number_text,
            title,
        ).arrange(RIGHT, buff=0.25)

        group.to_corner(UL, buff=0.55)
        group.shift(DOWN * 0.5)

        line = Line(
            group.get_left(),
            group.get_right() + RIGHT * 0.5,
            color=accent or self.LIME,
            stroke_width=2,
        ).next_to(group, DOWN, buff=0.15)

        return VGroup(group, line)

    # ========================================================
    # MAIN
    # ========================================================

    def construct(self):

        self.camera.background_color = self.BG
        self.background()

        self.linear_combination()
        self.zero_vector_equation()
        self.definition()
        self.closing_question()

    # ========================================================
    # PART 1 — LINEAR COMBINATIONS
    # ========================================================

    def linear_combination(self):

        heading = self.section_heading(
            "01",
            "HOW VECTORS COMBINE",
        )

        self.play(
            FadeIn(heading, shift=RIGHT * 0.15),
            run_time=0.5,
        )

        self.subtitle(
            "Vectors can be scaled and then added together.",
            2.3,
        )

        # Two example vectors
        v1 = MathTex(
            r"\vec{v}_1=",
            r"\begin{pmatrix}1\\1\end{pmatrix}",
            color=self.CREAM,
        ).scale(0.8)

        v2 = MathTex(
            r"\vec{v}_2=",
            r"\begin{pmatrix}1\\-1\end{pmatrix}",
            color=self.CREAM,
        ).scale(0.8)

        vectors = VGroup(v1, v2).arrange(
            DOWN,
            aligned_edge=LEFT,
            buff=0.45,
        )

        vectors.move_to(LEFT * 3.7 + UP * 0.1)

        # Colour the vector symbols
        v1[0].set_color(self.LIME)
        v2[0].set_color(self.CORAL)

        self.play(
            FadeIn(vectors, shift=RIGHT * 0.2),
            run_time=0.7,
        )

        # Coefficient equation
        combination = MathTex(
            r"c_1\vec{v}_1+c_2\vec{v}_2",
            color=self.CREAM,
        ).scale(1.0)

        combination.move_to(RIGHT * 2.2 + UP * 0.7)

        combination[0][0:2].set_color(self.LIME)
        combination[0][3:5].set_color(self.CORAL)

        label = Text(
            "LINEAR COMBINATION",
            font_size=13,
            color=self.LIME,
            weight=BOLD,
        ).next_to(combination, DOWN, buff=0.25)

        self.subtitle(
            "The coefficients determine how much of each vector we use.",
            2.6,
        )

        self.play(
            Write(combination),
            FadeIn(label),
            run_time=0.8,
        )

        # Explain scalar coefficients
        coefficients = MathTex(
            r"c_1=2",
            r"\qquad",
            r"c_2=-1",
            color=self.CREAM,
        ).scale(0.85)

        coefficients.next_to(label, DOWN, buff=0.55)
        coefficients[0].set_color(self.LIME)
        coefficients[2].set_color(self.CORAL)

        self.play(
            FadeIn(coefficients, shift=UP * 0.12),
            run_time=0.6,
        )

        self.subtitle(
            "A negative coefficient reverses a vector's direction.",
            2.5,
        )

        # Numerical example
        numerical = MathTex(
            r"2\begin{pmatrix}1\\1\end{pmatrix}"
            r"-"
            r"\begin{pmatrix}1\\-1\end{pmatrix}"
            r"="
            r"\begin{pmatrix}1\\3\end{pmatrix}",
            color=self.CREAM,
        ).scale(0.68)

        numerical.move_to(DOWN * 1.45 + RIGHT * 0.4)

        numerical_label = Text(
            "AN EXAMPLE OF A LINEAR COMBINATION",
            font_size=12,
            color=self.GREY,
            weight=BOLD,
        ).next_to(numerical, UP, buff=0.2)

        self.play(
            FadeIn(numerical_label),
            Write(numerical),
            run_time=0.9,
        )

        self.subtitle(
            "The result is another vector in the same vector space.",
            2.5,
        )

        self.play(
            FadeOut(
                VGroup(
                    heading,
                    vectors,
                    combination,
                    label,
                    coefficients,
                    numerical,
                    numerical_label,
                    self.active_subtitle,
                ),
                run_time=0.4,
            )
        )

    # ========================================================
    # PART 2 — THE ZERO VECTOR EQUATION
    # ========================================================

    def zero_vector_equation(self):

        heading = self.section_heading(
            "02",
            "THE IMPORTANT QUESTION",
            self.CORAL,
        )

        self.play(
            FadeIn(heading),
            run_time=0.4,
        )

        self.subtitle(
            "To test independence, we examine a special combination.",
            2.5,
        )

        equation = MathTex(
            r"c_1\vec{v}_1+c_2\vec{v}_2=\vec{0}",
            color=self.CREAM,
        ).scale(1.05)

        equation.move_to(UP * 0.75)

        equation[0][0:2].set_color(self.LIME)
        equation[0][3:5].set_color(self.CORAL)
        equation[0][-1].set_color(self.GOLD)

        self.play(
            Write(equation),
            run_time=0.8,
        )

        zero_label = Text(
            "THE ZERO-VECTOR EQUATION",
            font_size=13,
            color=self.CORAL,
            weight=BOLD,
        ).next_to(equation, DOWN, buff=0.25)

        self.play(
            FadeIn(zero_label),
            run_time=0.35,
        )

        self.subtitle(
            "Can a combination of these vectors produce zero?",
            2.7,
        )

        # The zero vector is a special target
        zero_visual = Circle(
            radius=0.48,
            color=self.CORAL,
            stroke_width=2,
        )

        zero_dot = Dot(
            ORIGIN,
            color=self.CORAL,
            radius=0.07,
        )

        zero_text = MathTex(
            r"\vec{0}",
            color=self.CORAL,
        ).scale(1.0).next_to(zero_visual, DOWN, buff=0.2)

        visual_group = VGroup(
            zero_visual,
            zero_dot,
            zero_text,
        ).move_to(DOWN * 1.1)

        self.play(
            FadeIn(visual_group, scale=0.8),
            run_time=0.6,
        )

        # Two possible cases
        cases = VGroup(
            Text(
                "ONLY ZERO COEFFICIENTS",
                font_size=17,
                color=self.LIME,
                weight=BOLD,
            ),
            Text(
                "NON-ZERO COEFFICIENTS ALSO WORK",
                font_size=17,
                color=self.CORAL,
                weight=BOLD,
            ),
        ).arrange(
            DOWN,
            aligned_edge=LEFT,
            buff=0.38,
        )

        cases.move_to(DOWN * 2.45 + RIGHT * 0.3)

        self.play(
            FadeIn(cases, shift=UP * 0.12),
            run_time=0.65,
        )

        self.subtitle(
            "These two possibilities distinguish independence from dependence.",
            3,
        )

        self.play(
            FadeOut(
                VGroup(
                    heading,
                    equation,
                    zero_label,
                    visual_group,
                    cases,
                    self.active_subtitle,
                ),
                run_time=0.4,
            )
        )

    # ========================================================
    # PART 3 — FORMAL DEFINITION
    # ========================================================

    def definition(self):

        heading = self.section_heading(
            "03",
            "THE MATHEMATICAL RULE",
        )

        self.play(
            FadeIn(heading),
            run_time=0.4,
        )

        # Independent
        independent_title = Text(
            "LINEARLY INDEPENDENT",
            font_size=20,
            color=self.LIME,
            weight=BOLD,
        )

        independent_equation = MathTex(
            r"c_1\vec{v}_1+\cdots+c_n\vec{v}_n"
            r"=\vec{0}",
        ).scale(0.72)

        independent_result = MathTex(
            r"\Longrightarrow",
            r"c_1=\cdots=c_n=0",
            color=self.LIME,
        ).scale(0.85)

        independent_group = VGroup(
            independent_title,
            independent_equation,
            independent_result,
        ).arrange(
            DOWN,
            buff=0.28,
        )

        independent_group.move_to(UP * 0.65)

        # Dependent
        dependent_title = Text(
            "LINEARLY DEPENDENT",
            font_size=20,
            color=self.CORAL,
            weight=BOLD,
        )

        dependent_equation = MathTex(
            r"c_1\vec{v}_1+\cdots+c_n\vec{v}_n"
            r"=\vec{0}",
        ).scale(0.72)

        dependent_result = MathTex(
            r"\text{At least one }c_i\ne0",
            color=self.CORAL,
        ).scale(0.85)

        dependent_group = VGroup(
            dependent_title,
            dependent_equation,
            dependent_result,
        ).arrange(
            DOWN,
            buff=0.28,
        )

        dependent_group.move_to(DOWN * 1.45)

        separator = Line(
            LEFT * 5.2,
            RIGHT * 5.2,
            color=self.GREY,
            stroke_opacity=0.35,
        ).move_to(ORIGIN)

        self.play(
            FadeIn(independent_title),
            FadeIn(independent_equation),
            FadeIn(independent_result),
            run_time=0.9,
        )

        self.play(
            Create(separator),
            run_time=0.3,
        )

        self.subtitle(
            "Independent means the zero vector has only the trivial solution.",
            3,
        )

        self.play(
            FadeIn(dependent_group, shift=UP * 0.1),
            run_time=0.8,
        )

        self.subtitle(
            "Dependent means a non-zero coefficient solution exists.",
            3,
        )

        # Final conceptual distinction
        final_statement = Text(
            "THE DIFFERENCE IS IN THE COEFFICIENTS.",
            font_size=22,
            color=self.LIME,
            weight=BOLD,
        ).to_edge(DOWN, buff=1.15)

        self.play(
            FadeIn(final_statement),
            run_time=0.6,
        )

        self.wait(1)

        self.play(
            FadeOut(
                VGroup(
                    heading,
                    independent_group,
                    dependent_group,
                    separator,
                    final_statement,
                    self.active_subtitle,
                ),
                run_time=0.45,
            )
        )

    # ========================================================
    # PART 4 — CLOSING QUESTION
    # ========================================================

    def closing_question(self):

        title = Text(
            "ONE EQUATION.",
            font_size=35,
            color=self.CREAM,
            weight=BOLD,
        )

        title2 = Text(
            "TWO POSSIBILITIES.",
            font_size=35,
            color=self.LIME,
            weight=BOLD,
        )

        group = VGroup(
            title,
            title2,
        ).arrange(
            DOWN,
            buff=0.28,
        )

        group.move_to(ORIGIN)

        self.play(
            FadeIn(title, shift=RIGHT * 0.15),
            run_time=0.55,
        )

        self.play(
            FadeIn(title2, shift=LEFT * 0.15),
            run_time=0.55,
        )

        self.subtitle(
            "Now let's see what these two possibilities look like geometrically.",
            3,
        )

        self.wait(0.5)
