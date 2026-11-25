
from manim import *

# ============================================================
# BEYOND THE ARROWS
# VECTOR STORIES / STUDIO EDITION
#
# SCENE 06 — THE COMPLETE PICTURE
#
# Final synthesis, formal definition, credits and disclosure.
# ============================================================

BG = "#20201E"
CREAM = "#F2EBDD"
LIME = "#C6F277"
CORAL = "#FF765E"
GOLD = "#F2BE69"
GREY = "#A8A69F"
PANEL = "#30302C"
GRID = "#77776F"


class BeyondTheArrowsFinal(Scene):

    def construct(self):

        self.camera.background_color = BG
        self.create_background()

        self.recap()
        self.formal_definition()
        self.final_message()
        self.credits()

    # --------------------------------------------------------
    # BACKGROUND
    # --------------------------------------------------------

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
            "06  —  FINAL SYNTHESIS",
            font="DejaVu Sans",
            font_size=14,
            color=LIME,
        ).to_corner(UR, buff=0.35)

        self.add(grid, header, label)

    # --------------------------------------------------------
    # SUBTITLE SYSTEM
    # --------------------------------------------------------

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

    # --------------------------------------------------------
    # ACT 1 — RECAP
    # --------------------------------------------------------

    def recap(self):

        title = Text(
            "THE COMPLETE PICTURE",
            font="DejaVu Sans",
            font_size=42,
            color=CREAM,
            weight=BOLD,
        )

        title.move_to(UP * 1.65)

        self.play(
            FadeIn(title, shift=UP * 0.2),
            run_time=0.65,
        )

        self.subtitle(
            "We began with a simple question: can one vector be recreated using the others?",
            duration=3.1,
        )

        concepts = VGroup(
            Text(
                "LINEAR COMBINATIONS",
                font="DejaVu Sans",
                font_size=23,
                color=LIME,
                weight=BOLD,
            ),
            Text(
                "GEOMETRIC INTERPRETATION",
                font="DejaVu Sans",
                font_size=23,
                color=GOLD,
                weight=BOLD,
            ),
            Text(
                "ALGEBRAIC PROOF",
                font="DejaVu Sans",
                font_size=23,
                color=CORAL,
                weight=BOLD,
            ),
            Text(
                "SIGNAL APPLICATION",
                font="DejaVu Sans",
                font_size=23,
                color=CREAM,
                weight=BOLD,
            ),
        ).arrange(DOWN, buff=0.35)

        concepts.move_to(DOWN * 0.35)

        for concept in concepts:

            self.play(
                FadeIn(concept, shift=RIGHT * 0.15),
                run_time=0.4,
            )

        self.subtitle(
            "We explored the idea through combinations, geometry, equations and a simplified signal model.",
            duration=3.2,
        )

        self.play(
            FadeOut(VGroup(title, concepts)),
            run_time=0.5,
        )

    # --------------------------------------------------------
    # ACT 2 — FORMAL DEFINITION
    # --------------------------------------------------------

    def formal_definition(self):

        heading = Text(
            "THE MATHEMATICAL DEFINITION",
            font="DejaVu Sans",
            font_size=29,
            color=GOLD,
            weight=BOLD,
        ).move_to(UP * 2.0)

        self.play(
            FadeIn(heading),
            run_time=0.5,
        )

        general_equation = MathTex(
            r"c_1\vec v_1+c_2\vec v_2+\cdots+c_n\vec v_n=\vec 0",
            color=CREAM,
            font_size=39,
        ).move_to(UP * 0.85)

        self.play(
            Write(general_equation),
            run_time=0.9,
        )

        self.subtitle(
            "A set of vectors is dependent if a non-trivial combination of them equals the zero vector.",
            duration=3.5,
            color=CORAL,
        )

        dependent_label = Text(
            "LINEARLY DEPENDENT",
            font="DejaVu Sans",
            font_size=22,
            color=CORAL,
            weight=BOLD,
        ).move_to(DOWN * 0.15)

        dependent_condition = MathTex(
            r"\text{At least one }c_i\neq 0",
            color=CORAL,
            font_size=33,
        ).next_to(dependent_label, DOWN, buff=0.25)

        self.play(
            FadeIn(dependent_label),
            Write(dependent_condition),
            run_time=0.65,
        )

        self.subtitle(
            "It is independent when the only possible solution is the trivial one: every coefficient is zero.",
            duration=3.5,
            color=LIME,
        )

        independent_label = Text(
            "LINEARLY INDEPENDENT",
            font="DejaVu Sans",
            font_size=22,
            color=LIME,
            weight=BOLD,
        ).move_to(DOWN * 1.75)

        independent_condition = MathTex(
            r"c_1=c_2=\cdots=c_n=0",
            color=LIME,
            font_size=34,
        ).next_to(independent_label, DOWN, buff=0.25)

        self.play(
            FadeIn(independent_label),
            Write(independent_condition),
            run_time=0.65,
        )

        self.subtitle(
            "This is the central test that connects every part of our exploration.",
            duration=2.8,
        )

        self.play(
            FadeOut(
                VGroup(
                    heading,
                    general_equation,
                    dependent_label,
                    dependent_condition,
                    independent_label,
                    independent_condition,
                )
            ),
            run_time=0.5,
        )

    # --------------------------------------------------------
    # ACT 3 — FINAL MESSAGE
    # --------------------------------------------------------

    def final_message(self):

        first = Text(
            "INDEPENDENCE IS ABOUT",
            font="DejaVu Sans",
            font_size=29,
            color=CREAM,
            weight=BOLD,
        )

        second = Text(
            "UNIQUE CONTRIBUTION.",
            font="DejaVu Sans",
            font_size=43,
            color=LIME,
            weight=BOLD,
        ).next_to(first, DOWN, buff=0.3)

        third = Text(
            "DEPENDENCE IS ABOUT REDUNDANCY.",
            font="DejaVu Sans",
            font_size=27,
            color=CORAL,
            weight=BOLD,
        ).next_to(second, DOWN, buff=0.55)

        self.play(
            FadeIn(first, shift=UP * 0.15),
            run_time=0.55,
        )

        self.play(
            Write(second),
            run_time=0.8,
        )

        self.play(
            FadeIn(third, shift=UP * 0.15),
            run_time=0.65,
        )

        self.subtitle(
            "Understanding this difference helps us recognise the structure hidden inside vectors and the spaces they generate.",
            duration=3.6,
        )

        self.wait(0.8)

        self.play(
            FadeOut(VGroup(first, second, third)),
            run_time=0.5,
        )

    # --------------------------------------------------------
    # ACT 4 — CREDITS AND AI DISCLOSURE
    # --------------------------------------------------------

    def credits(self):

        project = Text(
            "BEYOND THE ARROWS",
            font="DejaVu Sans",
            font_size=38,
            color=CREAM,
            weight=BOLD,
        ).move_to(UP * 1.65)

        subtitle_text = Text(
            "THE HIDDEN LOGIC OF LINEAR INDEPENDENCE",
            font="DejaVu Sans",
            font_size=19,
            color=LIME,
        ).next_to(project, DOWN, buff=0.3)

        divider = Line(
            LEFT * 3.8,
            RIGHT * 3.8,
            color=GREY,
            stroke_opacity=0.45,
        ).move_to(DOWN * 0.05)

        organiser = Text(
            "PRESENTED BY  PALAK",
            font="DejaVu Sans",
            font_size=21,
            color=CREAM,
            weight=BOLD,
        ).move_to(DOWN * 0.65)

        institution = Text(
            "NEWTON SCHOOL OF TECHNOLOGY",
            font="DejaVu Sans",
            font_size=17,
            color=GREY,
        ).next_to(organiser, DOWN, buff=0.25)

        disclosure = Text(
            "AI tools were used for assistance in animation coding and development.",
            font="DejaVu Sans",
            font_size=14,
            color=GREY,
        ).move_to(DOWN * 2.05)

        self.play(
            FadeIn(project),
            FadeIn(subtitle_text),
            Create(divider),
            run_time=0.9,
        )

        self.play(
            FadeIn(organiser),
            FadeIn(institution),
            run_time=0.7,
        )

        self.subtitle(
            "Thank you for exploring the mathematics of linear independence and dependence.",
            duration=3.2,
            color=LIME,
        )

        self.play(
            FadeIn(disclosure),
            run_time=0.5,
        )

        self.wait(2.0)

        self.play(
            FadeOut(
                VGroup(
                    project,
                    subtitle_text,
                    divider,
                    organiser,
                    institution,
                    disclosure,
                )
            ),
            run_time=1.0,
        )
