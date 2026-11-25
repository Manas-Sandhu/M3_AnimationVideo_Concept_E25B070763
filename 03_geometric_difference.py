
from manim import *
import numpy as np

# ============================================================
# BEYOND THE ARROWS
# VECTOR STORIES / STUDIO EDITION
#
# SCENE 03 — WHEN DIRECTIONS BECOME FREEDOM
#
# Visual direction:
# Cinematic mathematical documentary
# Charcoal / Ivory / Lime / Coral
#
# Subtitles:
# Every narration beat has an on-screen subtitle.
# The displayed subtitle text is also the voiceover script.
#
# Estimated scene duration: 75–90 seconds
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


class BeyondTheArrowsGeometry(Scene):

    def construct(self):

        self.camera.background_color = BG

        self.create_background()

        self.opening_question()
        self.independent_geometry()
        self.dependent_geometry()
        self.geometric_comparison()
        self.mathematical_conclusion()
        self.transition_to_proof()

    # ========================================================
    # BACKGROUND AND VISUAL SYSTEM
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
            weight=MEDIUM,
        ).to_corner(UL, buff=0.35)

        self.scene_number = Text(
            "03  —  GEOMETRIC INTERPRETATION",
            font="DejaVu Sans",
            font_size=14,
            color=LIME,
        ).to_corner(UR, buff=0.35)

        self.add(self.grid, self.header, self.scene_number)

    # ========================================================
    # SUBTITLE SYSTEM
    # ========================================================

    def subtitle(self, dialogue, duration=2.5, emphasis=CREAM):

        """
        The displayed subtitle is the narration line.

        Timing:
        - Fade in: 0.25 seconds
        - Hold: duration
        - Fade out: 0.20 seconds

        Record the voiceover using the same dialogue and
        align it with these subtitle beats during editing.
        """

        background = RoundedRectangle(
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

        text = Text(
            dialogue,
            font="DejaVu Sans",
            font_size=20,
            color=emphasis,
            weight=MEDIUM,
            line_spacing=0.8,
        )

        if text.width > 10.8:
            text.scale_to_fit_width(10.8)

        accent.move_to(background.get_left() + RIGHT * 0.35)
        text.move_to(background.get_center() + RIGHT * 0.1)

        group = VGroup(background, accent, text)
        group.to_edge(DOWN, buff=0.22)

        self.play(
            FadeIn(group, shift=UP * 0.08),
            run_time=0.25,
        )

        self.wait(duration)

        self.play(
            FadeOut(group),
            run_time=0.20,
        )

        return group

    # ========================================================
    # REUSABLE ELEMENTS
    # ========================================================

    def section_heading(self, number, heading, color=LIME):

        number_text = Text(
            number,
            font="DejaVu Sans",
            font_size=18,
            color=color,
            weight=BOLD,
        )

        title = Text(
            heading,
            font="DejaVu Sans",
            font_size=25,
            color=CREAM,
            weight=BOLD,
        )

        group = VGroup(number_text, title)
        group.arrange(RIGHT, buff=0.22)
        group.to_corner(UL, buff=0.55)
        group.shift(DOWN * 0.48)

        return group

    def create_plane(self, x_range=(-3, 3), y_range=(-3, 3),
                     width=6.0, height=4.3, position=ORIGIN):

        plane = NumberPlane(
            x_range=[x_range[0], x_range[1], 1],
            y_range=[y_range[0], y_range[1], 1],
            x_length=width,
            y_length=height,
            background_line_style={
                "stroke_color": GRID,
                "stroke_width": 1,
                "stroke_opacity": 0.23,
            },
            axis_config={
                "stroke_color": GREY,
                "stroke_width": 1.5,
                "stroke_opacity": 0.65,
            },
        )

        plane.shift(position)

        return plane

    def make_arrow(self, plane, coordinates, color, label,
                   label_direction=UR, width=5):

        start = plane.c2p(0, 0)
        end = plane.c2p(*coordinates)

        shadow = Arrow(
            start + DOWN * 0.035,
            end + DOWN * 0.035,
            buff=0,
            color=BLACK,
            stroke_width=width + 3,
            max_tip_length_to_length_ratio=0.13,
        )

        arrow = Arrow(
            start,
            end,
            buff=0,
            color=color,
            stroke_width=width,
            max_tip_length_to_length_ratio=0.13,
        )

        label_object = MathTex(
            label,
            color=color,
            font_size=32,
        )

        label_object.next_to(
            end,
            label_direction,
            buff=0.13,
        )

        return VGroup(shadow, arrow, label_object)

    def add_small_label(self, text, position, color=GREY, size=19):

        label = Text(
            text,
            font="DejaVu Sans",
            font_size=size,
            color=color,
        )

        label.move_to(position)

        return label

    def clear_scene_objects(self, *objects):

        self.play(
            *[FadeOut(obj) for obj in objects],
            run_time=0.4,
        )

    # ========================================================
    # ACT 1 — OPENING QUESTION
    # ========================================================

    def opening_question(self):

        title = Text(
            "TWO VECTORS.",
            font="DejaVu Sans",
            font_size=48,
            color=CREAM,
            weight=BOLD,
        )

        second = Text(
            "TWO VERY DIFFERENT POSSIBILITIES.",
            font="DejaVu Sans",
            font_size=32,
            color=LIME,
            weight=BOLD,
        )

        second.next_to(title, DOWN, buff=0.3)

        self.play(
            FadeIn(title, shift=UP * 0.2),
            run_time=0.55,
        )

        self.subtitle(
            "Two vectors may look simple. But together, they can determine how much of a space we can reach.",
            duration=3.3,
        )

        self.play(
            Write(second),
            run_time=0.75,
        )

        self.subtitle(
            "The key is not simply their length. It is the directions they contribute.",
            duration=2.8,
            emphasis=LIME,
        )

        self.play(
            FadeOut(VGroup(title, second)),
            run_time=0.45,
        )

    # ========================================================
    # ACT 2 — INDEPENDENT VECTORS
    # ========================================================

    def independent_geometry(self):

        heading = self.section_heading(
            "01",
            "INDEPENDENT VECTORS",
            LIME,
        )

        plane = self.create_plane(
            x_range=(-2, 3),
            y_range=(-2, 3),
            width=6.0,
            height=4.4,
            position=LEFT * 1.45 + DOWN * 0.15,
        )

        self.play(
            FadeIn(heading),
            Create(plane),
            run_time=0.8,
        )

        self.subtitle(
            "Consider these two vectors: one points diagonally upward, while the other points diagonally downward.",
            duration=3.0,
        )

        v1 = self.make_arrow(
            plane,
            (1, 1),
            LIME,
            r"\vec{v}_1",
            UR,
        )

        v2 = self.make_arrow(
            plane,
            (1, -1),
            CORAL,
            r"\vec{v}_2",
            DR,
        )

        self.play(
            FadeIn(v1[0]),
            GrowArrow(v1[1]),
            FadeIn(v1[2]),
            run_time=0.7,
        )

        self.play(
            FadeIn(v2[0]),
            GrowArrow(v2[1]),
            FadeIn(v2[2]),
            run_time=0.7,
        )

        self.subtitle(
            "Neither vector can be obtained by simply multiplying the other by a scalar.",
            duration=2.9,
            emphasis=LIME,
        )

        # Show the parallelogram construction.
        origin = plane.c2p(0, 0)
        point_a = plane.c2p(1, 1)
        point_b = plane.c2p(1, -1)
        point_c = plane.c2p(2, 0)

        translated_v2 = Arrow(
            point_a,
            point_c,
            buff=0,
            color=CORAL,
            stroke_width=4,
            max_tip_length_to_length_ratio=0.13,
        )

        translated_v1 = Arrow(
            point_b,
            point_c,
            buff=0,
            color=LIME,
            stroke_width=4,
            max_tip_length_to_length_ratio=0.13,
        )

        parallelogram = Polygon(
            origin,
            point_a,
            point_c,
            point_b,
            color=GOLD,
            stroke_width=2,
            fill_color=GOLD,
            fill_opacity=0.12,
        )

        self.play(
            Create(parallelogram),
            run_time=0.55,
        )

        self.play(
            GrowArrow(translated_v2),
            GrowArrow(translated_v1),
            run_time=0.7,
        )

        self.subtitle(
            "By adding the vectors, we reach a new point. By changing their scalar multiples, we can reach many more.",
            duration=3.4,
        )

        # Explain the scalar multiples.
        combination = MathTex(
            r"a\vec{v}_1+b\vec{v}_2",
            color=GOLD,
            font_size=40,
        ).to_edge(RIGHT, buff=0.45).shift(UP * 1.25)

        combination_label = Text(
            "ALL LINEAR COMBINATIONS",
            font="DejaVu Sans",
            font_size=14,
            color=GREY,
        ).next_to(combination, DOWN, buff=0.2)

        self.play(
            Write(combination),
            FadeIn(combination_label),
            run_time=0.65,
        )

        self.subtitle(
            "The coefficients a and b control how far we move along each direction.",
            duration=2.7,
            emphasis=GOLD,
        )

        # Highlight the plane generated by the two directions.
        span = MathTex(
            r"\operatorname{span}\{\vec v_1,\vec v_2\}",
            color=LIME,
            font_size=29,
        ).to_edge(RIGHT, buff=0.3).shift(DOWN * 0.45)

        self.play(
            FadeIn(span, shift=UP * 0.15),
            run_time=0.5,
        )

        self.subtitle(
            "Because these two vectors provide independent directions, their linear combinations can cover the entire two-dimensional plane.",
            duration=3.7,
            emphasis=LIME,
        )

        self.clear_scene_objects(
            heading,
            plane,
            v1,
            v2,
            parallelogram,
            translated_v1,
            translated_v2,
            combination,
            combination_label,
            span,
        )

    # ========================================================
    # ACT 3 — DEPENDENT VECTORS
    # ========================================================

    def dependent_geometry(self):

        heading = self.section_heading(
            "02",
            "DEPENDENT VECTORS",
            CORAL,
        )

        plane = self.create_plane(
            x_range=(-2, 3),
            y_range=(-2, 5),
            width=6.0,
            height=4.5,
            position=LEFT * 1.45 + DOWN * 0.15,
        )

        self.play(
            FadeIn(heading),
            Create(plane),
            run_time=0.8,
        )

        self.subtitle(
            "Now consider a different pair. The first vector is one, two. The second is two, four.",
            duration=3.0,
        )

        # Line y = 2x, shown as the shared direction.
        line = Line(
            plane.c2p(-1.5, -3),
            plane.c2p(2.5, 5),
            color=GOLD,
            stroke_width=3,
        )

        self.play(
            Create(line),
            run_time=0.55,
        )

        w1 = self.make_arrow(
            plane,
            (1, 2),
            LIME,
            r"\vec{w}_1",
            UR,
        )

        w2 = self.make_arrow(
            plane,
            (2, 4),
            CORAL,
            r"\vec{w}_2",
            UR,
        )

        self.play(
            FadeIn(w1[0]),
            GrowArrow(w1[1]),
            FadeIn(w1[2]),
            run_time=0.7,
        )

        self.play(
            FadeIn(w2[0]),
            GrowArrow(w2[1]),
            FadeIn(w2[2]),
            run_time=0.8,
        )

        self.subtitle(
            "Look carefully. Both vectors lie on exactly the same line.",
            duration=2.5,
            emphasis=CORAL,
        )

        relation = MathTex(
            r"\vec{w}_2=2\vec{w}_1",
            color=CORAL,
            font_size=43,
        ).to_edge(RIGHT, buff=0.4).shift(UP * 1.25)

        self.play(
            Write(relation),
            run_time=0.6,
        )

        self.subtitle(
            "The second vector is simply twice the first. It does not introduce a new direction.",
            duration=3.0,
        )

        # Highlight the redundancy.
        redundant = Text(
            "NO NEW DIRECTION",
            font="DejaVu Sans",
            font_size=18,
            color=CORAL,
            weight=BOLD,
        ).next_to(relation, DOWN, buff=0.3)

        self.play(
            FadeIn(redundant, shift=UP * 0.12),
            run_time=0.45,
        )

        self.subtitle(
            "Even if we change both coefficients, every possible combination remains on this same line.",
            duration=3.2,
            emphasis=CORAL,
        )

        line_span = MathTex(
            r"\operatorname{span}\{\vec w_1,\vec w_2\}",
            color=GOLD,
            font_size=27,
        ).to_edge(RIGHT, buff=0.35).shift(DOWN * 0.65)

        self.play(
            FadeIn(line_span),
            run_time=0.5,
        )

        self.subtitle(
            "These vectors are linearly dependent because one can be expressed as a scalar multiple of the other.",
            duration=3.2,
        )

        self.clear_scene_objects(
            heading,
            plane,
            line,
            w1,
            w2,
            relation,
            redundant,
            line_span,
        )

    # ========================================================
    # ACT 4 — SIDE-BY-SIDE COMPARISON
    # ========================================================

    def geometric_comparison(self):

        heading = self.section_heading(
            "03",
            "ONE PLANE. TWO DIFFERENT SPANS.",
            GOLD,
        )

        self.play(
            FadeIn(heading),
            run_time=0.45,
        )

        left_title = Text(
            "INDEPENDENT",
            font="DejaVu Sans",
            font_size=22,
            color=LIME,
            weight=BOLD,
        )

        right_title = Text(
            "DEPENDENT",
            font="DejaVu Sans",
            font_size=22,
            color=CORAL,
            weight=BOLD,
        )

        left_plane = self.create_plane(
            x_range=(-2, 2),
            y_range=(-2, 2),
            width=4.3,
            height=3.2,
            position=LEFT * 3.0 + DOWN * 0.15,
        )

        right_plane = self.create_plane(
            x_range=(-2, 2),
            y_range=(-2, 2),
            width=4.3,
            height=3.2,
            position=RIGHT * 3.0 + DOWN * 0.15,
        )

        left_title.next_to(left_plane, UP, buff=0.25)
        right_title.next_to(right_plane, UP, buff=0.25)

        self.play(
            FadeIn(left_title),
            FadeIn(right_title),
            Create(left_plane),
            Create(right_plane),
            run_time=0.8,
        )

        # Independent pair.
        left_v1 = Arrow(
            left_plane.c2p(0, 0),
            left_plane.c2p(1, 1),
            buff=0,
            color=LIME,
            stroke_width=5,
        )

        left_v2 = Arrow(
            left_plane.c2p(0, 0),
            left_plane.c2p(1, -1),
            buff=0,
            color=CORAL,
            stroke_width=5,
        )

        # Dependent pair.
        right_line = Line(
            right_plane.c2p(-1.5, -1.5),
            right_plane.c2p(1.5, 1.5),
            color=GOLD,
            stroke_width=4,
        )

        right_v1 = Arrow(
            right_plane.c2p(0, 0),
            right_plane.c2p(0.7, 0.7),
            buff=0,
            color=LIME,
            stroke_width=5,
        )

        right_v2 = Arrow(
            right_plane.c2p(0, 0),
            right_plane.c2p(1.4, 1.4),
            buff=0,
            color=CORAL,
            stroke_width=5,
        )

        self.play(
            GrowArrow(left_v1),
            GrowArrow(left_v2),
            Create(right_line),
            GrowArrow(right_v1),
            GrowArrow(right_v2),
            run_time=0.85,
        )

        left_result = VGroup(
            MathTex(r"\mathbb{R}^2", color=LIME, font_size=34),
            Text("THE ENTIRE PLANE", font_size=16, color=CREAM),
        ).arrange(DOWN, buff=0.12)

        right_result = VGroup(
            MathTex(r"\text{a line}", color=CORAL, font_size=34),
            Text("ONLY ONE DIRECTION", font_size=16, color=CREAM),
        ).arrange(DOWN, buff=0.12)

        left_result.next_to(left_plane, DOWN, buff=0.3)
        right_result.next_to(right_plane, DOWN, buff=0.3)

        self.play(
            FadeIn(left_result, shift=UP * 0.1),
            FadeIn(right_result, shift=UP * 0.1),
            run_time=0.5,
        )

        self.subtitle(
            "In this two-dimensional example, independent vectors span the plane, while dependent vectors span only a line.",
            duration=3.5,
            emphasis=GOLD,
        )

        self.subtitle(
            "The difference is not the number of arrows. It is the number of genuinely independent directions.",
            duration=3.3,
        )

        self.clear_scene_objects(
            heading,
            left_title,
            right_title,
            left_plane,
            right_plane,
            left_v1,
            left_v2,
            right_line,
            right_v1,
            right_v2,
            left_result,
            right_result,
        )

    # ========================================================
    # ACT 5 — MATHEMATICAL CONCLUSION
    # ========================================================

    def mathematical_conclusion(self):

        heading = self.section_heading(
            "04",
            "THE IDEA BEHIND THE GEOMETRY",
            GOLD,
        )

        self.play(
            FadeIn(heading),
            run_time=0.4,
        )

        statement = Text(
            "INDEPENDENCE",
            font="DejaVu Sans",
            font_size=23,
            color=LIME,
            weight=BOLD,
        ).move_to(UP * 1.5)

        statement_two = Text(
            "No vector is redundant.",
            font="DejaVu Sans",
            font_size=28,
            color=CREAM,
        ).next_to(statement, DOWN, buff=0.25)

        divider = Line(
            LEFT * 3.5,
            RIGHT * 3.5,
            color=GREY,
            stroke_opacity=0.4,
        )

        divider.move_to(DOWN * 0.15)

        statement_three = Text(
            "DEPENDENCE",
            font="DejaVu Sans",
            font_size=23,
            color=CORAL,
            weight=BOLD,
        ).move_to(DOWN * 0.9)

        statement_four = Text(
            "At least one vector is redundant.",
            font="DejaVu Sans",
            font_size=28,
            color=CREAM,
        ).next_to(statement_three, DOWN, buff=0.25)

        self.play(
            FadeIn(statement),
            Write(statement_two),
            run_time=0.65,
        )

        self.subtitle(
            "Independence means that every vector contributes something that cannot be recreated from the others.",
            duration=3.4,
        )

        self.play(
            Create(divider),
            FadeIn(statement_three),
            Write(statement_four),
            run_time=0.75,
        )

        self.subtitle(
            "Dependence means that at least one vector can be built from the remaining vectors.",
            duration=3.3,
            emphasis=CORAL,
        )

        self.clear_scene_objects(
            heading,
            statement,
            statement_two,
            divider,
            statement_three,
            statement_four,
        )

    # ========================================================
    # ACT 6 — TRANSITION TO ALGEBRAIC PROOF
    # ========================================================

    def transition_to_proof(self):

        question = Text(
            "BUT HOW CAN WE PROVE IT?",
            font="DejaVu Sans",
            font_size=39,
            color=CREAM,
            weight=BOLD,
        )

        self.play(
            FadeIn(question, shift=UP * 0.2),
            run_time=0.65,
        )

        self.subtitle(
            "A diagram gives us intuition. But mathematics demands a proof.",
            duration=3.0,
            emphasis=GOLD,
        )

        equation = MathTex(
            r"c_1\vec v_1+c_2\vec v_2=\vec 0",
            color=CREAM,
            font_size=47,
        )

        equation.move_to(DOWN * 0.45)

        self.play(
            Write(equation),
            run_time=0.85,
        )

        self.subtitle(
            "We can test independence by asking whether a combination of the vectors can equal the zero vector.",
            duration=3.5,
        )

        key_phrase = Text(
            "THE ZERO-VECTOR TEST",
            font="DejaVu Sans",
            font_size=21,
            color=LIME,
            weight=BOLD,
        ).next_to(equation, DOWN, buff=0.4)

        self.play(
            FadeIn(key_phrase, shift=UP * 0.1),
            run_time=0.45,
        )

        self.subtitle(
            "The next step is to examine the coefficients and discover whether only the trivial solution is possible.",
            duration=3.5,
            emphasis=LIME,
        )

        self.play(
            FadeOut(VGroup(question, equation, key_phrase)),
            run_time=0.6,
        )

        end_title = Text(
            "GEOMETRY SHOWS US WHY.",
            font="DejaVu Sans",
            font_size=34,
            color=CREAM,
            weight=BOLD,
        )

        end_subtitle = Text(
            "ALGEBRA WILL SHOW US HOW.",
            font="DejaVu Sans",
            font_size=28,
            color=LIME,
            weight=BOLD,
        ).next_to(end_title, DOWN, buff=0.3)

        self.play(
            FadeIn(end_title),
            FadeIn(end_subtitle),
            run_time=0.65,
        )

        self.wait(1.5)

        self.play(
            FadeOut(VGroup(end_title, end_subtitle)),
            run_time=0.5,
        )
