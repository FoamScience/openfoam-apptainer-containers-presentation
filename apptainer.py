from manim import *
from manim_slides import Slide
from manim.utils import color
from manim.utils.color import interpolate_color
from numpy.random import RandomState
import numpy as np
import pandas as pd

rng = RandomState(0)
MAIN_COLOR = color.TEAL_A
BACKGROUND_COLOR = color.GRAY_E
TEXT_COLOR = color.WHITE
GRAPH_COLOR = color.BLUE_B
WARN_COLOR= color.YELLOW_C
DOT_COLOR = color.RED_C
ITEM_ICON = "•"
BOX_BUFF = 0.3
very_small_size = 12.0
small_size = 16
mid_size = 20
big_size = 25
N = 6
Text.set_default(font="Comic Code Ligatures", color=TEXT_COLOR, font_size=small_size)
Code.set_default(font="Comic Code Ligatures", font_size=small_size, style="manni", background="window", tab_width=4, line_spacing=0.65)
Tex.set_default(color=TEXT_COLOR, font_size=small_size)
Dot.set_default(radius=0.07, color=DOT_COLOR)


def replace_nth_line(string, n, repl):
    lines = string.splitlines()
    if 0 <= n-1 < len(lines):
        lines[n-1] = repl
    return "\n".join(lines)

def keep_only_objects(slide, grp):
    slide.clear()
    for _ in grp:
        slide.add(_)

class Apptainer(Slide):

    def itemize(self, items, anchor, distance, stepwise, **kwargs):
        anims = []
        mobjs = []
        for i in range(len(items)):
            mobjs.append(Text(f"{i+1}{ITEM_ICON} {items[i]}", font_size=small_size, **kwargs))
            if i == 0:
                mobjs[i].next_to(anchor, DOWN*distance).align_to(anchor, LEFT)
            else:
                mobjs[i].next_to(mobjs[i-1], DOWN).align_to(mobjs[i-1], LEFT)
        anims = [FadeIn(mobjs[i]) for i in range(len(items))]
        if stepwise:
            for a in anims:
                self.play(a)
        else:
            self.play(AnimationGroup(*anims))
        return mobjs[-1]

    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        # Title page
        layout = Group()
        title = Text(f"Apptainer containers for OpenFOAM", font_size=big_size)#.to_edge(UP+LEFT)
        footer = Text("Research Software Engineering SIG Meeting", t2w={"NHR4CES": BOLD}, font_size=very_small_size).to_edge(DOWN+RIGHT)
        author = Text("Mohammed Elwardi Fadeli, Oct. 2024", font_size=very_small_size).to_edge(DOWN+LEFT)
        logo = ImageMobject("./images/nhr-tu-logo.png").next_to(title, UP).scale(0.6)#.to_edge(UP+RIGHT)
        layout.add(title, footer, author, logo)
        self.play(FadeIn(layout))
        self.next_slide()

        c1 = Text(f"Write Code")
        b1 = SurroundingRectangle(c1, color=MAIN_COLOR, buff=BOX_BUFF)
        bg1 = BackgroundRectangle(c1, color=MAIN_COLOR, fill_opacity=0.3, buff=BOX_BUFF)
        vg1 = VGroup(c1, b1, bg1).to_edge(LEFT+UP).shift(0.5*RIGHT)
        anims =[
            Transform(title, vg1),
            Transform(logo, logo.copy().scale(0.5).to_edge(UP+RIGHT)),
        ]
        self.play(AnimationGroup(*anims))
        self.next_slide()

        c2 = Text(f"Build")
        b2 = SurroundingRectangle(c2, color=MAIN_COLOR, buff=BOX_BUFF)
        bg2 = BackgroundRectangle(c2, color=MAIN_COLOR, fill_opacity=0.3, buff=BOX_BUFF)
        vg2 = VGroup(c2, b2, bg2).next_to(vg1, 5*RIGHT)
        anims =[
            Create(Arrow(vg1.get_right(), vg2.get_left(), color=MAIN_COLOR, buff=0.1)),
            FadeIn(vg2)
        ]
        self.play(AnimationGroup(*anims))
        self.next_slide()

        c3 = Text(f"Test")
        b3 = SurroundingRectangle(c3, color=MAIN_COLOR, buff=BOX_BUFF)
        bg3 = BackgroundRectangle(c3, color=MAIN_COLOR, fill_opacity=0.3, buff=BOX_BUFF)
        vg3 = VGroup(c3, b3, bg3).next_to(vg2, 3*DOWN)
        anims =[
            Create(Arrow(vg2.get_bottom(), vg3.get_top(), color=MAIN_COLOR, buff=0.1)),
            FadeIn(vg3)
        ]
        self.play(AnimationGroup(*anims))
        self.next_slide()

        c4 = Text(f"Push to Version Control")
        b4 = SurroundingRectangle(c4, color=MAIN_COLOR, buff=BOX_BUFF)
        bg4 = BackgroundRectangle(c4, color=MAIN_COLOR, fill_opacity=0.3, buff=BOX_BUFF)
        vg4 = VGroup(c4, b4, bg4).next_to(vg3, 4*RIGHT)
        anims =[
            Create(Arrow(vg3.get_right(), vg4.get_left(), color=MAIN_COLOR, buff=0.1)),
            FadeIn(vg4)
        ]
        self.play(AnimationGroup(*anims))
        self.next_slide()

        c5 = Text(f"Trigger CI")
        b5 = SurroundingRectangle(c5, color=DOT_COLOR, buff=BOX_BUFF)
        bg5 = BackgroundRectangle(c5, color=DOT_COLOR, fill_opacity=0.3, buff=BOX_BUFF)
        vg5 = VGroup(c5, b5, bg5).next_to(vg4, 4*RIGHT)
        anims =[
            Create(Arrow(vg4.get_right(), vg5.get_left(), color=DOT_COLOR, buff=0.1)),
            FadeIn(vg5)
        ]
        self.play(AnimationGroup(*anims))
        self.next_slide()

        vg6 = vg2.copy().set(color=DOT_COLOR).next_to(vg5, 4*DOWN)
        vg6[0].set(color=WHITE)
        anims =[
            Create(Arrow(vg5.get_bottom(), vg6.get_top(), color=DOT_COLOR, buff=0.1)),
            FadeIn(vg6)
        ]
        self.play(AnimationGroup(*anims))
        self.next_slide()

        vg7 = vg3.copy().set(color=DOT_COLOR).next_to(vg6, 4*DOWN)
        vg7[0].set(color=WHITE)
        anims =[
            Create(Arrow(vg6.get_bottom(), vg7.get_top(), color=DOT_COLOR, buff=0.1)),
            FadeIn(vg7)
        ]
        self.play(AnimationGroup(*anims))
        self.next_slide()

        c8 = Text(f"Deploy/Release")
        b8 = SurroundingRectangle(c8, color=DOT_COLOR, buff=BOX_BUFF)
        bg8 = BackgroundRectangle(c8, color=DOT_COLOR, fill_opacity=0.3, buff=BOX_BUFF)
        vg8 = VGroup(c8, b8, bg8).next_to(vg7, 4*LEFT)
        anims =[
            Create(Arrow(vg7.get_left(), vg8.get_right(), color=DOT_COLOR, buff=0.1)),
            FadeIn(vg8)
        ]
        self.play(AnimationGroup(*anims))
        self.next_slide()

        c9 = Text(f"Fetch Code")
        b9 = SurroundingRectangle(c9, color=GREEN, buff=BOX_BUFF)
        bg9 = BackgroundRectangle(c9, color=GREEN, fill_opacity=0.3, buff=BOX_BUFF)
        vg9 = VGroup(c9, b9, bg9).next_to(vg3, 6.1*DOWN).shift(1.1*RIGHT)
        anims =[
            Create(CurvedArrow(vg4.get_bottom()+LEFT, vg9.get_right(), color=GREEN, angle=-TAU/4)),
            FadeIn(vg9)
        ]
        self.play(AnimationGroup(*anims))
        self.next_slide()

        c10 = Text(f"Run")
        b10 = SurroundingRectangle(c10, color=GREEN, buff=BOX_BUFF)
        bg10 = BackgroundRectangle(c10, color=GREEN, fill_opacity=0.3, buff=BOX_BUFF)
        vg10 = VGroup(c10, b10, bg10).next_to(vg9, 2*(LEFT+DOWN))
        anims =[
            Create(CurvedArrow(vg9.get_bottom(), vg10.get_right(), color=GREEN, angle=-TAU/4)),
            FadeIn(vg10)
        ]
        self.play(AnimationGroup(*anims))
        self.next_slide()

        c11 = Text(f"Analyze results")
        b11 = SurroundingRectangle(c11, color=GREEN, buff=BOX_BUFF)
        bg11 = BackgroundRectangle(c11, color=GREEN, fill_opacity=0.3, buff=BOX_BUFF)
        vg11 = VGroup(c11, b11, bg11).next_to(vg1, 10*DOWN)
        anims =[
            Create(CurvedArrow(vg10.get_left(), vg11.get_bottom(), color=GREEN, angle=-TAU/6)),
            FadeIn(vg11)
        ]
        self.play(AnimationGroup(*anims))
        self.next_slide()

        self.play(
            Create(Arrow(vg11.get_top(), vg1.get_bottom(), color=MAIN_COLOR, buff=0.1)),
        )
        self.next_slide()

        bg12 = BackgroundRectangle(Group(vg2,vg3), color=YELLOW, fill_opacity=0.15, buff=BOX_BUFF/2)
        ttx = Text(f"containerize local dev.", color=YELLOW).next_to(bg12, 0.5*DOWN)
        self.play(FadeIn(bg12), Create(ttx))
        self.next_slide()

        bg13 = BackgroundRectangle(Group(vg6,vg7,vg8), color=YELLOW, fill_opacity=0.15, buff=BOX_BUFF/2)
        ttx = Text(f"containerize CI/CD", color=YELLOW).next_to(bg13, 0.5*UP).shift(LEFT)
        self.play(FadeIn(bg13), Create(ttx))
        self.next_slide()

        bg14 = BackgroundRectangle(Group(vg9,vg10,vg11), color=YELLOW, fill_opacity=0.15, buff=BOX_BUFF/2)
        ttx = Text(f"containerize on HPC", color=YELLOW).next_to(bg14, 0.5*DOWN).shift(1.5*RIGHT)
        arr = Arrow(bg13.get_left(), bg14.get_right(), color=YELLOW, buff=0.1)
        self.play(FadeIn(bg14), Create(ttx), Create(arr))
        self.next_slide()

        t00 = Text(f"0.0 Benefits of containerization...", t2w={"0.0": BOLD}, font_size=big_size).to_edge(UP+LEFT)
        keep_only_objects(self, Group(layout))
        self.play(Transform(title, t00))
        self.next_slide()

        objs = Text("- Containers:", font_size=mid_size).next_to(title, DOWN*2).align_to(title, LEFT)
        self.play(Create(objs))
        items = [
            "Controled versionning of dependencies.",
            "Consistency across environments.",
            "Lightweight, uses host's Kernel.",
            "Partial isolation from host machine."
        ]
        last = self.itemize(items, objs, 1.5, False,
            t2w={f"1{ITEM_ICON}": BOLD, f"2{ITEM_ICON}": BOLD, f"3{ITEM_ICON}": BOLD, f"4{ITEM_ICON}": BOLD},
            t2c={f"1{ITEM_ICON}": MAIN_COLOR, f"2{ITEM_ICON}": MAIN_COLOR, f"3{ITEM_ICON}": MAIN_COLOR, f"4{ITEM_ICON}": MAIN_COLOR})
        self.next_slide()

        objs = Text("- Virtual Machines?", font_size=mid_size).next_to(title, DOWN*14).align_to(title, LEFT)
        self.play(Create(objs))
        items = [
            "Better control over dedicated resources.",
            "Full isolation from host machine.",
            "Higher provisionning overhead.",
        ]
        last = self.itemize(items, objs, 1.5, False,
            t2w={f"1{ITEM_ICON}": BOLD, f"2{ITEM_ICON}": BOLD, f"3{ITEM_ICON}": BOLD, f"4{ITEM_ICON}": BOLD},
            t2c={f"1{ITEM_ICON}": MAIN_COLOR, f"2{ITEM_ICON}": MAIN_COLOR, f"3{ITEM_ICON}": MAIN_COLOR, f"4{ITEM_ICON}": MAIN_COLOR})
        self.next_slide()

        t01 = Text(f"0.1 Use case insights", t2w={"0.1": BOLD}, font_size=big_size).to_edge(UP+LEFT)
        keep_only_objects(self, Group(layout))
        self.play(Transform(title, t01))
        self.next_slide()

        objs = Text("- Image creation and administration:", font_size=mid_size).next_to(title, DOWN*2).align_to(title, LEFT)
        self.play(Create(objs))
        items = [
            "Get images from HUBs or build from definition files.",
            "What image formats to support?",
            "Can CI/CD build container images? When?",
            "Should images be suitable for local development?"
        ]
        last = self.itemize(items, objs, 1.5, False,
            t2w={f"1{ITEM_ICON}": BOLD, f"2{ITEM_ICON}": BOLD, f"3{ITEM_ICON}": BOLD, f"4{ITEM_ICON}": BOLD},
            t2c={f"1{ITEM_ICON}": MAIN_COLOR, f"2{ITEM_ICON}": MAIN_COLOR, f"3{ITEM_ICON}": MAIN_COLOR, f"4{ITEM_ICON}": MAIN_COLOR})
        self.next_slide()

        objs = Text("- Container runs:", font_size=mid_size).next_to(title, DOWN*14).align_to(title, LEFT)
        self.play(Create(objs))
        items = [
            "HPC: MPI/Slurm compatibility is a must.",
            "Integration with load balancers, accelerators, parallel FSs ... etc.",
            "User convenience even with minial training.",
            "Security: Oh no! -> next slide"
        ]
        last = self.itemize(items, objs, 1.5, False,
            t2w={f"1{ITEM_ICON}": BOLD, f"2{ITEM_ICON}": BOLD, f"3{ITEM_ICON}": BOLD, f"4{ITEM_ICON}": BOLD},
            t2c={f"1{ITEM_ICON}": MAIN_COLOR, f"2{ITEM_ICON}": MAIN_COLOR, f"3{ITEM_ICON}": MAIN_COLOR, f"4{ITEM_ICON}": MAIN_COLOR})
        self.next_slide()

        t02 = Text(f"0.2 Cluster admins and container tech", t2w={"0.2": BOLD}, font_size=big_size).to_edge(UP+LEFT)
        keep_only_objects(self, Group(layout))
        self.play(Transform(title, t02))
        self.next_slide()

        c1 = Text(f"Docker Daemon")
        b1 = SurroundingRectangle(c1, color=DOT_COLOR, buff=BOX_BUFF)
        bg1 = BackgroundRectangle(c1, color=DOT_COLOR, fill_opacity=0.3, buff=BOX_BUFF)
        vg1 = VGroup(c1, b1, bg1).shift(2*LEFT)
        sep = Line(UP*2.5, DOWN*2.5, stroke_width=3, color=GRAPH_COLOR)
        tx1 = Text(f"Daemon runs as a service, owned by root", font_size=mid_size).next_to(sep, RIGHT).shift(2*UP)
        self.play(FadeIn(vg1, sep, tx1))
        self.next_slide()


        c2 = Text(f"Image building")
        b2 = SurroundingRectangle(c2, color=MAIN_COLOR, buff=BOX_BUFF)
        bg2 = BackgroundRectangle(c2, color=MAIN_COLOR, fill_opacity=0.3, buff=BOX_BUFF)
        vg2 = VGroup(c2, b2, bg2).next_to(vg1, 3*LEFT)
        anims =[
            Create(Arrow(vg1.get_left(), vg2.get_right(), color=MAIN_COLOR, buff=0.1)),
            FadeIn(vg2)
        ]
        tx2 = Text(f"", font_size=mid_size).next_to(sep, 0.5*RIGHT).shift(2*UP)
        self.play(AnimationGroup(*anims))
        self.next_slide()

        c3 = Text(f"Container exec")
        b3 = SurroundingRectangle(c3, color=MAIN_COLOR, buff=BOX_BUFF)
        bg3 = BackgroundRectangle(c3, color=MAIN_COLOR, fill_opacity=0.3, buff=BOX_BUFF)
        vg3 = VGroup(c3, b3, bg3).next_to(vg1, 3*(DOWN+LEFT))
        anims =[
            Create(Arrow(
                np.array([vg1.get_left()[0],vg1.get_bottom()[1], 0]),
                np.array([vg3.get_right()[0], vg3.get_top()[1], 0]),
                color=MAIN_COLOR, buff=0.1)),
            FadeIn(vg3)
        ]
        self.play(AnimationGroup(*anims))
        self.next_slide()


        c4 = Text(f"Kernel")
        b4 = SurroundingRectangle(c4, color=YELLOW, buff=BOX_BUFF)
        bg4 = BackgroundRectangle(c4, color=YELLOW, fill_opacity=0.3, buff=BOX_BUFF)
        vg4 = VGroup(c4, b4, bg4).next_to(vg1, 3*DOWN)
        anims =[
            Create(Arrow(vg1.get_bottom(), vg4.get_top(), color=YELLOW, buff=0.1)),
            FadeIn(vg4)
        ]
        self.play(AnimationGroup(*anims))
        self.next_slide()

        c5 = Text(f"user:docker")
        b5 = SurroundingRectangle(c5, color=YELLOW, buff=BOX_BUFF)
        bg5 = BackgroundRectangle(c5, color=YELLOW, fill_opacity=0.3, buff=BOX_BUFF)
        vg5 = VGroup(c5, b5, bg5).next_to(vg1, 3*(UP+LEFT))
        tx2 = Text(f"docker grp can easily escalate privileges", font_size=mid_size).next_to(sep, RIGHT).shift(UP)
        anims =[
            Create(CurvedArrow(vg5.get_right(), vg1.get_top(), color=YELLOW, angle=-TAU/4)),
            FadeIn(vg5, tx2)
        ]
        self.play(AnimationGroup(*anims))
        self.next_slide()

        tx3 = Text(f"Hard to mount volumes with correct perms", font_size=mid_size).next_to(sep, RIGHT)
        tx4 = Text(f"Manage resource contention???", font_size=mid_size).next_to(sep, RIGHT).shift(DOWN)
        tx5 = Text(f"Orchestration within HPC is not trivial", font_size=mid_size).next_to(sep, RIGHT).shift(2*DOWN)
        self.play(FadeIn(tx3, tx4, tx5))
        self.next_slide()

        t03 = Text(f"0.3 Any more container tech?", t2w={"0.3": BOLD}, font_size=big_size).to_edge(UP+LEFT)
        keep_only_objects(self, Group(layout))
        def container_infrastructure(logo, msg, direction=DOWN):
            imlg = SVGMobject(logo, height=1.5)
            txt = Text(msg, font_size=small_size).next_to(imlg, direction, buff=0.2)
            return VGroup(imlg, txt)
        docker = container_infrastructure("./images/Docker.svg", f"Most popular.")
        podman = container_infrastructure("./images/Podman.svg", f"avoids Docker's daemon.").next_to(docker, 0.5*UR)
        sarus = container_infrastructure("./images/Sarus.svg", f"HPC focused, not popular.").next_to(docker, 0.1*DOWN+0.7*RIGHT)
        singularity = container_infrastructure("./images/Singularity.svg", f"single process execution.").shift(4*LEFT+DOWN)
        apptainer = container_infrastructure("./images/Apptainer.svg", f"Modernized Singularity fork.").next_to(singularity, UP)
        self.play(
            Transform(title, t03),
            FadeIn(docker),
            FadeIn(podman),
            FadeIn(sarus),
            FadeIn(singularity),
            FadeIn(apptainer),
        )
        self.next_slide()

        t11 = Text(f"1.0 Is Apptainer any better?", t2w={"1.0": BOLD}, font_size=big_size).to_edge(UP+LEFT)
        self.play(Transform(apptainer, title))
        keep_only_objects(self, Group(layout))
        self.play(Transform(title, t11))
        self.next_slide()

        objs = Text("- Some things are better:", font_size=mid_size).next_to(title, DOWN*3).align_to(title, LEFT)
        self.play(Create(objs))
        items = [
            "No daemon.",
            "No user mapping.",
            "Rootless mode with user namespaces.",
            "Single process execution.",
        ]
        last = self.itemize(items, objs, 1.5, False,
            t2w={f"1{ITEM_ICON}": BOLD, f"2{ITEM_ICON}": BOLD, f"3{ITEM_ICON}": BOLD, f"4{ITEM_ICON}": BOLD},
            t2c={f"1{ITEM_ICON}": MAIN_COLOR, f"2{ITEM_ICON}": MAIN_COLOR, f"3{ITEM_ICON}": MAIN_COLOR, f"4{ITEM_ICON}": MAIN_COLOR})
        self.next_slide()

        objs = Text("- Single process execution?", font_size=mid_size).next_to(last, DOWN*2).align_to(title, LEFT)
        self.play(Create(objs))
        items = [
            "Apptainer process launches.",
            "User namespaces get checked.",
            "Replace apptainer process code with user app.",
        ]
        last = self.itemize(items, objs, 1.5, False,
            t2w={f"1{ITEM_ICON}": BOLD, f"2{ITEM_ICON}": BOLD, f"3{ITEM_ICON}": BOLD, f"4{ITEM_ICON}": BOLD},
            t2c={f"1{ITEM_ICON}": MAIN_COLOR, f"2{ITEM_ICON}": MAIN_COLOR, f"3{ITEM_ICON}": MAIN_COLOR, f"4{ITEM_ICON}": MAIN_COLOR})
        self.next_slide()

        objs = Text("- But still using setuid bins:", font_size=mid_size).next_to(title, DOWN*3).align_to(title, LEFT).shift(8*RIGHT)
        self.play(Create(objs))
        items = [
            "Image mounting.",
            "Namespace creation in the kernel.",
            "Path Binding to container.",
        ]
        last = self.itemize(items, objs, 1.5, False,
            t2w={f"1{ITEM_ICON}": BOLD, f"2{ITEM_ICON}": BOLD, f"3{ITEM_ICON}": BOLD, f"4{ITEM_ICON}": BOLD},
            t2c={f"1{ITEM_ICON}": MAIN_COLOR, f"2{ITEM_ICON}": MAIN_COLOR, f"3{ITEM_ICON}": MAIN_COLOR, f"4{ITEM_ICON}": MAIN_COLOR})
        self.next_slide()

        t12 = Text(f"1.1 Apptainer containers for OpenFOAM", t2w={"1.1": BOLD}, font_size=big_size).to_edge(UP+LEFT)
        keep_only_objects(self, Group(layout))
        self.play(Transform(title, t12))
        self.next_slide()

        code_t = """git clone https://github.com/FoamScience/openfoam-apptainer-packaging
cd openfoam-apptainer-packaging
pip install ansible
ansible-playbook build.yaml \\
    --extra-vars "original_dir=$PWD" \\
    --extra-vars "@config.yaml" 
   
"""
        code = Code(code=code_t, language="shell", insert_line_no=False)
        tx1 = Text(f"Convenient building of apptainer images:", font_size=mid_size).next_to(code, UP)
        self.play(FadeIn(code), FadeIn(tx1))
        self.next_slide()

        keep_only_objects(self, layout)

        code_yaml1 = """containers:
  basic:
    opencfd-openfoam:
      os:
        distro: ubuntu
        version: 24.04
      mpi:
        implementation: openmpi
        version: 4.1.5
      framework:
        definition: com-openfoam
        version: 2312
"""
        code_yaml2 = """projects:
  test:
    base_container: opencfd-openfoam
    definition: projects/test.def
    build_args:
      branch:
        - master"""
        code1 = Code(code=code_yaml1, language="yaml").to_edge(LEFT)
        code2 = Code(code=code_yaml2, language="yaml", background="rectangle", line_no_from=13).to_edge(RIGHT).align_to(code1, UP)
        tx1 = Text(f"A config file is all you need:", font_size=mid_size).next_to(code1, UP)
        self.play(FadeIn(code1), FadeIn(code2), FadeIn(tx1))
        self.next_slide()

        t13 = Text(f"1.2 Quick feature run-down", t2w={"1.2": BOLD}, font_size=big_size).to_edge(UP+LEFT)
        keep_only_objects(self, Group(layout))
        self.play(Transform(title, t13))
        self.next_slide()

        objs = Text("- Base containers:", font_size=mid_size).next_to(title, DOWN*2).align_to(title, LEFT)
        self.play(Create(objs))
        items = [
            "MPI setup is a 1st class citizen.",
            "Pulls images instead of building if they are already there.",
            "Custom base containers!! Eg. Switch to spack-based images.",
            "Control over container metadata, at build-time."
        ]
        last = self.itemize(items, objs, 1.5, False,
            t2w={f"1{ITEM_ICON}": BOLD, f"2{ITEM_ICON}": BOLD, f"3{ITEM_ICON}": BOLD, f"4{ITEM_ICON}": BOLD},
            t2c={f"1{ITEM_ICON}": MAIN_COLOR, f"2{ITEM_ICON}": MAIN_COLOR, f"3{ITEM_ICON}": MAIN_COLOR, f"4{ITEM_ICON}": MAIN_COLOR})
        self.next_slide()

        objs = Text("- Project containers:", font_size=mid_size).next_to(last, DOWN*2).align_to(title, LEFT)
        self.play(Create(objs))
        items = [
            "Provide your definition files for your own projects.",
            "Supporting arbitrary build arguments.",
            "Continuous Development -> Persistent Overlays.",
        ]
        last = self.itemize(items, objs, 1.5, False,
            t2w={f"1{ITEM_ICON}": BOLD, f"2{ITEM_ICON}": BOLD, f"3{ITEM_ICON}": BOLD, f"4{ITEM_ICON}": BOLD},
            t2c={f"1{ITEM_ICON}": MAIN_COLOR, f"2{ITEM_ICON}": MAIN_COLOR, f"3{ITEM_ICON}": MAIN_COLOR, f"4{ITEM_ICON}": MAIN_COLOR})
        self.next_slide()

        t20 = Text(f"2.0 Container usage - Querry the metadata", t2w={"2.0": BOLD}, font_size=big_size).to_edge(UP+LEFT)
        keep_only_objects(self, Group(layout))
        self.play(Transform(title, t20))
        self.next_slide()

        code_t = """apptainer run containers/projects/test-master.sif "jq '.' /apps.json" """
        res_t = """{
  "openmpi": { "version": "4.1.5" },
  "openfoam": {
    "fork": "com-openfoam", "branch": "default",
    "commit": "default", "version": "2312"
  },
  "test": {
    "ompi_test_bin": "/opt/OMPIFoam/ompiTest",
    "foam_test_bin": "/opt/OMPIFoam/testOMPIFoam",
    "branch": "master"
  }
}"""
        code = Code(code=code_t, language="shell").shift(2*UP)
        res = Code(code=res_t, language="json", background="rectangle").next_to(code, DOWN)
        self.play(FadeIn(res, code))
        self.next_slide()

        t21 = Text(f"2.1 Container usage - Run with SLURM", t2w={"2.1": BOLD}, font_size=big_size).to_edge(UP+LEFT)
        keep_only_objects(self, Group(layout))
        self.play(Transform(title, t21))
        self.next_slide()

        code_t1 = """mpirun apptainer run --sharens containers/projects/test-master.sif \\
    '/opt/OMPIFoam/testOMPIFoam -parallel' """
        code1 = Code(code=code_t1, language="shell").shift(UP)
        txt1 = Text(f"These should 'just work' all the same:").next_to(code1,UP)
        code_t2 = """apptainer run -C containers/projects/test-master.sif \\
    'mpirun /opt/OMPIFoam/testOMPIFoam -parallel' """
        code2 = Code(code=code_t2, language="shell").next_to(code1, 1.5*DOWN)
        self.play(FadeIn(code2, code1, txt1))
        self.next_slide()

        t22 = Text(f"2.2 Container usage - Typical case runs", t2w={"2.2": BOLD}, font_size=big_size).to_edge(UP+LEFT)
        keep_only_objects(self, Group(layout))
        self.play(Transform(title, t22))
        self.next_slide()

        code_t1 = """cd /path/to/openfoam/case/on/host/machine
apptainer run -C container.sif "./Allclean"
apptainer run -C container.sif "./Allrun.prepare"
mpirun -n 16 apptainer run --sharens container.sif \\
    "containerSolver -parallel"
"""
        code1 = Code(code=code_t1, language="shell")
        self.play(FadeIn(code1))
        self.next_slide()

        t23 = Text(f"2.3 Container usage - Continuous development", t2w={"2.3": BOLD}, font_size=big_size).to_edge(UP+LEFT)
        keep_only_objects(self, Group(layout))
        self.play(Transform(title, t23))

        code_t = """apptainer overlay create --size 1024 overlay.img
apptainer run --overlay overlay.img container.sif"""
        code = Code(code=code_t, language="shell")
        txt = Text(f"Containers are immutable by default; for CD:").next_to(code, UP)
        self.play(FadeIn(txt, code))
        self.next_slide()

        t24 = Text(f"2.4 Container usage - Load custom bases", t2w={"2.4": BOLD}, font_size=big_size).to_edge(UP+LEFT)
        keep_only_objects(self, Group(layout))
        self.play(Transform(title, t24))

        code_t = """containers:
  extra_basics: https://github.com/FoamScience/spack-apptainer-containers
  basic:
    spack_openfoam:
      os:
        distro: spack_ubuntu-bionic
        version: latest
      mpi:
        implementation: spack_openmpi
        version: 4.1.5
      framework:
        definition: spack_openfoam
        version: 2312"""
        code = Code(code=code_t, language="yaml")
        self.play(FadeIn(code))
        self.next_slide()

        t25 = Text(f"2.5 Container usage - Debugging and CVEs", t2w={"2.5": BOLD}, font_size=big_size).to_edge(UP+LEFT)
        keep_only_objects(self, Group(layout))
        self.play(Transform(title, t25))
        code_t = """# Convert SIF to sandbox dir.
apptainer build --sandbox my-container container.sif
# Compare to base docker image
docker scout compare fs://my-container --to ubuntu:24.04
# Quick scan for vulnerabilities
docker scout quickview fs://my-container
# More details on CVEs
docker scout cves fs://my-container"""
        code = Code(code=code_t, language="shell")
        self.play(FadeIn(code))
        self.next_slide()

        t31 = Text(f"3.1 Use cases - Optimization on HPC", t2w={"3.1": BOLD}, font_size=big_size).to_edge(UP+LEFT)
        keep_only_objects(self, Group(layout))
        self.play(Transform(title, t31))
        self.next_slide()

        objs = Text("- Optimize OpenFOAM cases without installing/compiling OpenFOAM on host:", font_size=mid_size).next_to(title, DOWN*2).align_to(title, LEFT)
        self.play(Create(objs))

        items = [
            "foamBO: A Python-based optimization framework set up with virtual envs.",
            "For local trial completion tests, foamBO checks on PIDs.",
            "For SLURM trial completion tests, foamBO asks SLURM.",
            "This 'just works' with Apptainer containers because of single-process execution.",
            "Great for heavily customized builds of OpenFOAM..."
        ]
        last = self.itemize(items, objs, 1.5, False,
            t2w={f"1{ITEM_ICON}": BOLD, f"2{ITEM_ICON}": BOLD, f"3{ITEM_ICON}": BOLD, f"4{ITEM_ICON}": BOLD, f"5{ITEM_ICON}": BOLD},
            t2c={f"1{ITEM_ICON}": GREEN, f"2{ITEM_ICON}": GREEN, f"3{ITEM_ICON}": GREEN, f"4{ITEM_ICON}": GREEN, f"5{ITEM_ICON}": GREEN})

        txt = Text("** Build arguments allow for specialized HPC containers vs. CD containers", font_size=mid_size, color=GRAPH_COLOR).next_to(last, DOWN*2).align_to(title, LEFT)
        self.play(Create(txt))
        self.next_slide()

        t32 = Text(f"3.2 Use cases - OpenFOAM Reflections", t2w={"3.2": BOLD}, font_size=big_size).to_edge(UP+LEFT)
        keep_only_objects(self, Group(layout))
        self.play(Transform(title, t32))
        self.next_slide()

        code_t = """git clone https://github.com/FoamScience/openfoam-apptainer-packaging /tmp/of_tainers
git clone https://github.com/FoamScience/openfoam-reflections 
cd openfoam-reflections # <- only to use definition files
# BTW, you host the container configuration in your own repo...
# Hence the build/config.yaml reference
ansible-playbook /tmp/of_tainers/build.yaml \\
    --extra-vars="original_dir=$PWD" --extra-vars="@build/config.yaml"
# In one terminal, open a JSON endpoint for OpenFOAM classes
apptainer run containers/projects/reflections.sif \\
    "/opt/openfoam-reflections/endpoint"
# In another terminal (and choose one of the options), Either
apptainer run containers/projects/reflections.sif \\
    "npm start --prefix /opt/openfoam-reflections/reflect-json-app"
# Then check localhost:3000 in a web browser, Or
apptainer run containers/projects/reflections.sif \\
    "/opt/openfoam-reflections/TUI/tui"
# Notice the seamless networking and reduced dependencies frustration
"""
        code = Code(code=code_t, language="shell", insert_line_no=False)
        self.play(FadeIn(code))
        self.next_slide()

        tf = Text(f"THANK YOU", t2w={"THANK YOU": BOLD} ,font_size=big_size*2)
        keep_only_objects(self, Group(layout))
        self.play(Transform(title, tf))
        self.next_slide()
