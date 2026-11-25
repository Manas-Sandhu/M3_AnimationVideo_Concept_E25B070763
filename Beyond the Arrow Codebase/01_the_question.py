
from manim import *
import numpy as np


# ============================================================
# BEYOND THE ARROWS
# PALAK EDITION
# SCENE 01 — THE QUESTION
#
# Visual identity: Editorial Mathematical Documentary
# Palette: Charcoal / Cream / Lime / Coral
# Format: 16:9
# ============================================================


class BeyondTheArrowsOpening(Scene):

    # --------------------------------------------------------
    # DESIGN SYSTEM
    # --------------------------------------------------------

    BG = "#20201E"
    CREAM = "#F2EBDD"
    LIME = "#C6F277"
    CORAL = "#FF765E"
    GREY = "#A8A69F"
    PANEL = "#30302C"
    GRID = "#77776F"

    # --------------------------------------------------------
    # BACKGROUND DEPTH
    # --------------------------------------------------------

    def create_depth_background(self):

        grid = NumberPlane(
            x_range=[-8, 8, 0.5],
            y_range=[-4.5, 4.5, 0.5],
            background_line_style={
                "stroke_color": self.GRID,
                "stroke_opacity": 0.09,
                "stroke_width": 0.6,
            },
            axis_config={
                "stroke_opacity": 0,
            },
        )

        rings = VGroup(*[
            Circle(
                radius=r,
                color=self.LIME,
                stroke_width=0.7,
                stroke_opacity=0.09,
            ).move_to(RIGHT * 4.8 + UP * 1.8)
            for r in [1.2, 1.8, 2.4]
        ])

        label = Text(
            "VECTOR STORIES  /  FIELD NOTES 01",
            font_size=11,
            color=self.GREY,
            weight=BOLD,
        ).to_corner(UR, buff=0.35)

        grid.set_z_index(-3)
        rings.set_z_index(-2)

        self.add(grid, rings, label)

        return VGroup(grid, rings, label)

    # --------------------------------------------------------
    # VECTOR SYSTEM
    # --------------------------------------------------------

    def vector(self, start, end, color):

        shadow = Arrow(
            start + DOWN * 0.035,
            end + DOWN * 0.035,
            buff=0,
            color="#000000",
            stroke_width=11,
            max_tip_length_to_length_ratio=0.13,
        ).set_opacity(0.20)

        core = Arrow(
            start,
            end,
            buff=0,
            color=color,
            stroke_width=5,
            max_tip_length_to_length_ratio=0.13,
        )

        endpoint = Dot(
            end,
            radius=0.065,
            color=color,
        )

        return VGroup(shadow, core, endpoint)

    # --------------------------------------------------------
    # SUBTITLE SYSTEM
    # --------------------------------------------------------

    def subtitle(self, message, duration=2.4):

        text = Text(
            message,
            font="DejaVu Sans",
            font_size=19,
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

        text.move_to(panel.get_center())
        marker.move_to(panel.get_left() + RIGHT * 0.28)

        group = VGroup(panel, marker, text)
        group.to_edge(DOWN, buff=0.18)

        if hasattr(self, "active_subtitle"):
            self.play(
                FadeOut(self.active_subtitle),
                FadeIn(group, shift=UP * 0.06),
                run_time=0.25,
            )
        else:
            self.play(
                FadeIn(group, shift=UP * 0.06),
                run_time=0.25,
            )

        self.active_subtitle = group
        self.wait(duration)

    # --------------------------------------------------------
    # MAIN SCENE
    # --------------------------------------------------------

    def construct(self):

        self.camera.background_color = self.BG

        self.background = self.create_depth_background()

        self.opening()
        self.reconstruction()
        self.title_card()

    # ========================================================
    # PART 1 — OPENING QUESTION
    # ========================================================

    def opening(self):

        index = Text(
            "MATHEMATICS / 01",
            font_size=14,
            color=self.LIME,
            weight=BOLD,
        ).to_corner(UL, buff=0.55)

        headline = Text(
            "CAN YOU",
            font_size=65,
            color=self.CREAM,
            weight=BOLD,
        )

        headline2 = Text(
            "RECREATE A DIRECTION?",
            font_size=39,
            color=self.LIME,
            weight=BOLD,
        )

        heading = VGroup(
            headline,
            headline2,
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.12)

        heading.move_to(UP * 0.65)

        underline = Line(
            LEFT * 2.8,
            LEFT * 0.8,
            color=self.CORAL,
            stroke_width=7,
        ).next_to(heading, DOWN, buff=0.4)

        self.play(
            FadeIn(index),
            FadeIn(heading, shift=RIGHT * 0.2),
            run_time=0.7,
        )

        self.play(
            Create(underline),
            run_time=0.3,
        )

        self.subtitle(
            "Imagine being given a target vector.",
            duration=2.2,
        )

        self.subtitle(
            "Could other vectors combine to recreate it?",
            duration=2.5,
        )

        self.play(
            FadeOut(VGroup(index, heading, underline)),
            run_time=0.35,
        )

    # ========================================================
    # PART 2 — VECTOR RECONSTRUCTION
    # ========================================================

    def reconstruction(self):

        plane = NumberPlane(
            x_range=[-1, 4, 1],
            y_range=[-2, 3, 1],
            x_length=5.8,
            y_length=4.7,
            background_line_style={
                "stroke_color": self.GRID,
                "stroke_opacity": 0.3,
                "stroke_width": 0.8,
            },
            axis_config={
                "stroke_color": self.GREY,
                "stroke_width": 1,
                "stroke_opacity": 0.7,
            },
        ).move_to(LEFT * 2.5 + UP * 0.1)

        self.play(
            Create(plane),
            run_time=0.8,
        )

        # Exact coordinate positions
        O = plane.c2p(0, 0)
        A = plane.c2p(1, 1)
        B = plane.c2p(1, -1)
        R = plane.c2p(2, 0)

        # Original vectors
        u = self.vector(O, A, self.LIME)
        v = self.vector(O, B, self.CORAL)

        label_u = MathTex(
            r"\vec{u}",
            color=self.LIME,
        ).scale(0.8).next_to(A, UP, buff=0.1)

        label_v = MathTex(
            r"\vec{v}",
            color=self.CORAL,
        ).scale(0.8).next_to(B, DOWN, buff=0.1)

        self.subtitle(
            "Take two vectors with different directions.",
            duration=2.2,
        )

        self.play(
            GrowArrow(u[1]),
            FadeIn(u[0]),
            FadeIn(u[2]),
            FadeIn(label_u),
            run_time=0.85,
        )

        self.play(
            GrowArrow(v[1]),
            FadeIn(v[0]),
            FadeIn(v[2]),
            FadeIn(label_v),
            run_time=0.85,
        )

        # ----------------------------------------------------
        # PROJECTION GUIDES
        # ----------------------------------------------------

        guide_y = DashedLine(
            A,
            plane.c2p(1, 0),
            color=self.LIME,
            dash_length=0.08,
            stroke_opacity=0.7,
        )

        projection = DashedLine(
            R,
            plane.c2p(2, -0.8),
            color=self.CORAL,
            dash_length=0.08,
            stroke_opacity=0.5,
        )

        self.play(
            Create(guide_y),
            Create(projection),
            run_time=0.45,
        )

        # ----------------------------------------------------
        # TRANSLATION
        # ----------------------------------------------------

        translated_v = self.vector(A, R, self.CORAL)

        translated_label = MathTex(
            r"\vec{v}",
            color=self.CORAL,
        ).scale(0.8).next_to(R, RIGHT, buff=0.15)

        self.subtitle(
            "Place the second vector at the first vector's endpoint.",
            duration=2.5,
        )

        self.play(
            TransformFromCopy(v, translated_v),
            FadeIn(translated_label),
            run_time=0.85,
        )

        # ----------------------------------------------------
        # RESULTANT
        # ----------------------------------------------------

        result = self.vector(O, R, self.LIME)

        self.subtitle(
            "Their combined displacement gives the resultant.",
            duration=2.2,
        )

        self.play(
            GrowArrow(result[1]),
            FadeIn(result[0]),
            FadeIn(result[2]),
            run_time=0.85,
        )

        # ----------------------------------------------------
        # MATHEMATICAL EQUATION
        # ----------------------------------------------------

        equation = MathTex(
            r"\begin{pmatrix}1\\1\end{pmatrix}"
            r"+"
            r"\begin{pmatrix}1\\-1\end{pmatrix}"
            r"="
            r"\begin{pmatrix}2\\0\end{pmatrix}",
            color=self.CREAM,
        ).scale(0.65)

        equation.to_corner(UR, buff=0.45)

        equation_label = Text(
            "VECTOR ADDITION",
            font_size=12,
            color=self.LIME,
            weight=BOLD,
        ).next_to(equation, DOWN, buff=0.2)

        self.play(
            FadeIn(equation, shift=LEFT * 0.15),
            FadeIn(equation_label),
            run_time=0.55,
        )

        self.subtitle(
            "We have reconstructed a vector using a combination of two others.",
            duration=2.8,
        )

        # ----------------------------------------------------
        # CLEAN TRANSITION
        # ----------------------------------------------------

        self.play(
            FadeOut(
                VGroup(
                    plane,
                    u,
                    v,
                    translated_v,
                    result,
                    label_u,
                    label_v,
                    translated_label,
                    guide_y,
                    projection,
                    equation,
                    equation_label,
                    self.active_subtitle,
                ),
                run_time=0.45,
            )
        )

    # ========================================================
    # PART 3 — TITLE CARD
    # ========================================================

    def title_card(self):

        number = Text(
            "A LINEAR ALGEBRA FILM",
            font_size=14,
            color=self.LIME,
            weight=BOLD,
        )

        title = Text(
            "BEYOND THE ARROWS",
            font_size=48,
            color=self.CREAM,
            weight=BOLD,
        )

        description = Text(
            "THE HIDDEN LOGIC OF LINEAR INDEPENDENCE",
            font_size=17,
            color=self.CORAL,
        )

        line = Line(
            LEFT * 2.4,
            RIGHT * 2.4,
            color=self.LIME,
            stroke_width=4,
        )

        composition = VGroup(
            number,
            title,
            line,
            description,
        ).arrange(DOWN, buff=0.3)

        composition.move_to(ORIGIN)

        self.play(
            FadeIn(number),
            run_time=0.3,
        )

        self.play(
            FadeIn(title, shift=UP * 0.15),
            run_time=0.8,
        )

        self.play(
            Create(line),
            FadeIn(description),
            run_time=0.6,
        )

        self.subtitle(
            "The real question is whether every vector contributes something new.",
            duration=2.8,
        )

        self.wait(0.5)
