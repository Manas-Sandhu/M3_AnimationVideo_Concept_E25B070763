
from manim import *
import numpy as np

# ============================================================
# BEYOND THE ARROWS
# VECTOR STORIES / STUDIO EDITION
#
# SCENE 05 — THE MATHEMATICS OF SOUND
#
# Application of linear dependence to a simplified
# four-sample signal model.
#
# Design: Charcoal / Ivory / Lime / Coral / Gold
# Estimated duration: 75–90 seconds
# ============================================================

BG = "#20201E"
CREAM = "#F2EBDD"
LIME = "#C6F277"
CORAL = "#FF765E"
GOLD = "#F2BE69"
GREY = "#A8A69F"
PANEL = "#30302C"
GRID = "#77776F"


class BeyondTheArrowsSound(Scene):

    def construct(self):

        self.camera.background_color = BG
        self.create_background()

        self.opening()
        self.signal_representation()
        self.component_addition()
        self.dependence_test()
        self.real_world_meaning()
        self.closing()

    # ========================================================
    # BACKGROUND
    # ========================================================

    def create_background(self):

        grid = NumberPlane(
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

        header = Text(
            "VECTOR STORIES   /   STUDIO EDITION",
            font="DejaVu Sans",
            font_size=15,
            color=GREY,
        ).to_corner(UL, buff=0.35)

        label = Text(
            "05  —  AN APPLICATION",
            font="DejaVu Sans",
            font_size=14,
            color=LIME,
        ).to_corner(UR, buff=0.35)

        self.add(grid, header, label)

    # ========================================================
    # SUBTITLES
    # ========================================================

    def subtitle(self, dialogue, duration=2.8, color=CREAM):

        panel = RoundedRectangle(
            corner_radius=0.12,
            width=12,
            height=0.85,
            fill_color=PANEL,
            fill_opacity=0.98,
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

        num = Text(
            number,
            font="DejaVu Sans",
            font_size=18,
            color=color,
            weight=BOLD,
        )

        text = Text(
            title,
            font="DejaVu Sans",
            font_size=25,
            color=CREAM,
            weight=BOLD,
        )

        group = VGroup(num, text)
        group.arrange(RIGHT, buff=0.22)
        group.to_corner(UL, buff=0.55)
        group.shift(DOWN * 0.48)

        return group

    def clear_objects(self, *objects):

        self.play(
            *[FadeOut(obj) for obj in objects],
            run_time=0.45,
        )

    # ========================================================
    # SIGNAL VISUALISATION
    # ========================================================

    def make_signal_row(self, name, values, color, y_position):

        """
        Each signal is shown as four sample values.

        The small bars represent positive and negative
        sample amplitudes. This is a teaching visualisation,
        not a waveform recording.
        """

        label = MathTex(
            name,
            color=color,
            font_size=33,
        ).move_to(LEFT * 5.35 + UP * y_position)

        cells = VGroup()

        start_x = -3.75
        cell_width = 1.62
        gap = 0.16

        for i, value in enumerate(values):

            x = start_x + i * (cell_width + gap)

            cell = RoundedRectangle(
                corner_radius=0.08,
                width=cell_width,
                height=0.92,
                fill_color=PANEL,
                fill_opacity=1,
                stroke_color=GREY,
                stroke_opacity=0.25,
                stroke_width=1,
            )

            cell.move_to([x, y_position, 0])

            baseline_y = y_position - 0.12

            baseline = Line(
                [x - 0.48, baseline_y, 0],
                [x + 0.48, baseline_y, 0],
                color=GREY,
                stroke_width=1,
                stroke_opacity=0.7,
            )

            if value != 0:

                height = abs(value) * 0.20

                bar = Rectangle(
                    width=0.30,
                    height=height,
                    fill_color=color,
                    fill_opacity=1,
                    stroke_width=0,
                )

                if value > 0:
                    bar.move_to(
                        [x, baseline_y + height / 2, 0]
                    )
                else:
                    bar.move_to(
                        [x, baseline_y - height / 2, 0]
                    )

            else:

                bar = Dot(
                    [x, baseline_y, 0],
                    radius=0.055,
                    color=color,
                )

            number = MathTex(
                str(value),
                color=CREAM,
                font_size=25,
            ).move_to([x, y_position + 0.29, 0])

            cell_group = VGroup(
                cell,
                baseline,
                bar,
                number,
            )

            cells.add(cell_group)

        row = VGroup(label, cells)

        return row

    # ========================================================
    # ACT 1 — OPENING
    # ========================================================

    def opening(self):

        title = Text(
            "CAN MATHEMATICS HEAR SOUND?",
            font="DejaVu Sans",
            font_size=39,
            color=CREAM,
            weight=BOLD,
        )

        title.move_to(UP * 0.65)

        accent = Text(
            "A SIGNAL. A VECTOR. A CONNECTION.",
            font="DejaVu Sans",
            font_size=22,
            color=LIME,
            weight=BOLD,
        ).next_to(title, DOWN, buff=0.35)

        self.play(
            FadeIn(title, shift=UP * 0.2),
            run_time=0.6,
        )

        self.play(
            FadeIn(accent),
            run_time=0.5,
        )

        self.subtitle(
            "Sound may seem like something we simply hear. But computers process it using numbers.",
            duration=3.1,
        )

        self.subtitle(
            "And those numbers can be organised into vectors.",
            duration=2.5,
            color=LIME,
        )

        self.play(
            FadeOut(VGroup(title, accent)),
            run_time=0.45,
        )

    # ========================================================
    # ACT 2 — SIGNAL REPRESENTATION
    # ========================================================

    def signal_representation(self):

        heading = self.heading(
            "01",
            "TURNING A SIGNAL INTO A VECTOR",
            LIME,
        )

        self.play(
            FadeIn(heading),
            run_time=0.4,
        )

        intro = Text(
            "A SIMPLIFIED FOUR-SAMPLE MODEL",
            font="DejaVu Sans",
            font_size=17,
            color=GOLD,
            weight=BOLD,
        ).move_to(UP * 2.0)

        self.play(
            FadeIn(intro),
            run_time=0.4,
        )

        row1 = self.make_signal_row(
            r"\vec{s}_1",
            [1, 0, 1, -1],
            LIME,
            1.0,
        )

        row2 = self.make_signal_row(
            r"\vec{s}_2",
            [0, 1, 1, 0],
            CORAL,
            -0.15,
        )

        row3 = self.make_signal_row(
            r"\vec{s}_3",
            [1, 1, 2, -1],
            GOLD,
            -1.3,
        )

        self.play(
            FadeIn(row1, shift=RIGHT * 0.2),
            run_time=0.65,
        )

        self.subtitle(
            "Imagine that we represent a signal using four numerical samples.",
            duration=2.8,
        )

        self.play(
            FadeIn(row2, shift=RIGHT * 0.2),
            run_time=0.65,
        )

        self.subtitle(
            "Each position records the value of the signal at a particular sample.",
            duration=2.8,
        )

        self.play(
            FadeIn(row3, shift=RIGHT * 0.2),
            run_time=0.65,
        )

        self.subtitle(
            "These three rows are three vectors in a four-dimensional vector space.",
            duration=3.0,
            color=GOLD,
        )

        note = Text(
            "FOUR SAMPLES  =  FOUR COMPONENTS",
            font="DejaVu Sans",
            font_size=18,
            color=GREY,
        ).move_to(DOWN * 2.35)

        self.play(
            FadeIn(note),
            run_time=0.4,
        )

        self.subtitle(
            "The values are simplified for learning. They are not a recording of an actual sound.",
            duration=3.0,
            color=GOLD,
        )

        self.clear_objects(
            heading,
            intro,
            row1,
            row2,
            row3,
            note,
        )

    # ========================================================
    # ACT 3 — COMPONENT-WISE ADDITION
    #
    # s1 = (1,0,1,-1)
    # s2 = (0,1,1,0)
    # s3 = (1,1,2,-1)
    #
    # s1 + s2 = s3
    # ========================================================

    def component_addition(self):

        heading = self.heading(
            "02",
            "WHEN TWO SIGNALS COMBINE",
            GOLD,
        )

        self.play(
            FadeIn(heading),
            run_time=0.4,
        )

        equation1 = MathTex(
            r"\vec{s}_1+\vec{s}_2=\vec{s}_3",
            color=CREAM,
            font_size=47,
        ).move_to(UP * 1.8)

        self.play(
            Write(equation1),
            run_time=0.8,
        )

        self.subtitle(
            "Now look at what happens when we add the first two signal vectors.",
            duration=2.8,
        )

        component_equation = MathTex(
            r"(1,0,1,-1)+(0,1,1,0)",
            color=GOLD,
            font_size=34,
        ).move_to(UP * 0.55)

        self.play(
            Write(component_equation),
            run_time=0.8,
        )

        self.subtitle(
            "We add corresponding components, one position at a time.",
            duration=2.7,
            color=GOLD,
        )

        result = MathTex(
            r"=(1,1,2,-1)",
            color=LIME,
            font_size=40,
        ).next_to(component_equation, DOWN, buff=0.45)

        self.play(
            Write(result),
            run_time=0.65,
        )

        self.subtitle(
            "One plus zero gives one. Zero plus one gives one. One plus one gives two. Minus one plus zero stays minus one.",
            duration=4.0,
        )

        final_identity = MathTex(
            r"\boxed{\vec{s}_1+\vec{s}_2=\vec{s}_3}",
            color=LIME,
            font_size=47,
        ).move_to(DOWN * 1.55)

        self.play(
            Transform(
                VGroup(equation1, component_equation, result),
                final_identity,
            ),
            run_time=0.8,
        )

        self.subtitle(
            "The sum of the first two vectors exactly reproduces the third vector.",
            duration=3.0,
            color=LIME,
        )

        self.clear_objects(
            heading,
            VGroup(equation1, component_equation, result),
        )

    # ========================================================
    # ACT 4 — THE DEPENDENCE TEST
    #
    # s1 + s2 - s3 = 0
    #
    # Coefficients: 1, 1, -1
    # Not all zero.
    # Therefore dependent.
    # ========================================================

    def dependence_test(self):

        heading = self.heading(
            "03",
            "THE HIDDEN DEPENDENCE",
            CORAL,
        )

        self.play(
            FadeIn(heading),
            run_time=0.4,
        )

        relation = MathTex(
            r"\vec{s}_1+\vec{s}_2=\vec{s}_3",
            color=CREAM,
            font_size=43,
        ).move_to(UP * 1.65)

        self.play(
            Write(relation),
            run_time=0.7,
        )

        self.subtitle(
            "We have discovered a relationship between the three vectors. But what does it tell us?",
            duration=3.0,
        )

        zero_test = MathTex(
            r"\vec{s}_1+\vec{s}_2-\vec{s}_3=\vec{0}",
            color=GOLD,
            font_size=42,
        ).move_to(UP * 0.25)

        self.play(
            Write(zero_test),
            run_time=0.8,
        )

        self.subtitle(
            "Move the third vector to the left. Now their combination equals the zero vector.",
            duration=3.0,
            color=GOLD,
        )

        coefficients = MathTex(
            r"1\vec{s}_1+1\vec{s}_2+(-1)\vec{s}_3=\vec{0}",
            color=CREAM,
            font_size=33,
        ).move_to(DOWN * 0.9)

        self.play(
            Write(coefficients),
            run_time=0.8,
        )

        self.subtitle(
            "The coefficients are one, one and minus one. They are clearly not all zero.",
            duration=3.0,
        )

        verdict = Text(
            "NON-TRIVIAL SOLUTION",
            font="DejaVu Sans",
            font_size=24,
            color=CORAL,
            weight=BOLD,
        ).move_to(DOWN * 1.95)

        self.play(
            FadeIn(verdict, shift=UP * 0.1),
            run_time=0.5,
        )

        self.subtitle(
            "That means a non-trivial solution exists. Therefore, these three vectors are linearly dependent.",
            duration=3.4,
            color=CORAL,
        )

        conclusion = MathTex(
            r"\boxed{\{\vec{s}_1,\vec{s}_2,\vec{s}_3\}\text{ is dependent}}",
            color=LIME,
            font_size=35,
        ).move_to(DOWN * 2.65)

        self.play(
            Write(conclusion),
            run_time=0.7,
        )

        self.clear_objects(
            heading,
            relation,
            zero_test,
            coefficients,
            verdict,
            conclusion,
        )

    # ========================================================
    # ACT 5 — REAL WORLD MEANING
    # ========================================================

    def real_world_meaning(self):

        heading = self.heading(
            "04",
            "WHY DOES THIS MATTER?",
            GOLD,
        )

        self.play(
            FadeIn(heading),
            run_time=0.4,
        )

        statement1 = Text(
            "THREE VECTORS",
            font="DejaVu Sans",
            font_size=22,
            color=CREAM,
            weight=BOLD,
        ).move_to(UP * 1.55)

        statement2 = Text(
            "ONLY TWO ARE NEEDED",
            font="DejaVu Sans",
            font_size=34,
            color=LIME,
            weight=BOLD,
        ).next_to(statement1, DOWN, buff=0.35)

        statement3 = Text(
            "The third is already their sum.",
            font="DejaVu Sans",
            font_size=23,
            color=CREAM,
        ).next_to(statement2, DOWN, buff=0.35)

        self.play(
            FadeIn(statement1),
            run_time=0.45,
        )

        self.play(
            FadeIn(statement2, shift=UP * 0.1),
            run_time=0.6,
        )

        self.play(
            FadeIn(statement3),
            run_time=0.5,
        )

        self.subtitle(
            "In this example, the third vector contains no new information beyond the first two.",
            duration=3.2,
        )

        self.subtitle(
            "This is the mathematical idea behind redundancy: one vector can be reconstructed from the others.",
            duration=3.2,
            color=GOLD,
        )

        self.subtitle(
            "The same kind of reasoning is useful when studying signal representations and data.",
            duration=3.0,
        )

        self.clear_objects(
            heading,
            statement1,
            statement2,
            statement3,
        )

    # ========================================================
    # ACT 6 — CLOSING
    # ========================================================

    def closing(self):

        title = Text(
            "DEPENDENCE IS REDUNDANCY.",
            font="DejaVu Sans",
            font_size=37,
            color=CREAM,
            weight=BOLD,
        )

        subtitle_text = Text(
            "THE ZERO-VECTOR TEST REVEALS IT.",
            font="DejaVu Sans",
            font_size=26,
            color=LIME,
            weight=BOLD,
        ).next_to(title, DOWN, buff=0.35)

        self.play(
            FadeIn(title, shift=UP * 0.15),
            FadeIn(subtitle_text, shift=UP * 0.15),
            run_time=0.7,
        )

        self.subtitle(
            "From arrows in a plane to numerical signals, the same mathematical principle connects them all.",
            duration=3.5,
        )

        self.wait(0.5)

        self.play(
            FadeOut(VGroup(title, subtitle_text)),
            run_time=0.5,
        )
