from pymol import cmd

VERSION = "v5"


# ============================================================
# Splash / Help
# ============================================================
def _splash():
    print(rf"""
============================================================
   ____        __  ___                 
  |  _ \ _   _|  \/  | ___ _ __ __ ___  __
  | |_) | | | | |\/| |/ _ \ '__/ _` \ \/ /
  |  __/| |_| | |  | |  __/ | | (_| |>  <
  |_|    \__, |_|  |_|\___|_|  \__,_/_/\_\
          |___/

            PyMeraX {VERSION}
     PyMOL pretending to be ChimeraX
============================================================

AVAILABLE COMMANDS
------------------
pymerax()
pymerax("cartoon")
pymerax("surface")
pymerax("publication")
pymerax("ligand")
pymerax_help()

RENDER
------
ray 3000,3000
png figure.png, dpi=300
============================================================
""")


def pymerax_help():
    _splash()


# ============================================================
# Shared base
# ============================================================
def _set_bg():
    cmd.set_color("pymerax_bg", [0.84, 0.84, 0.84])
    cmd.bg_color("pymerax_bg")


def _base():
    settings = {
        "orthoscopic": 1,
        "antialias": 2,
        "ray_trace_mode": 0,
        "ray_trace_gain": 0.12,
        "ray_trace_fog": 0,
        "ray_opaque_background": 0,
        "depth_cue": 0,
        "hash_max": 300,
    }

    for k, v in settings.items():
        cmd.set(k, v)


def _lights():
    settings = {
        "ambient": 0.40,
        "direct": 0.40,
        "reflect": 0.20,
        "specular": 0.08,
        "shininess": 8,
        "spec_direct": 0,
        "light_count": 8,
    }

    for k, v in settings.items():
        cmd.set(k, v)

    # Manual lights
    cmd.set("light", (-0.4, -0.3, -1.0))
    cmd.set("light2", (-0.8, -0.2, 0.2))
    cmd.set("light3", (0.6, -0.7, -0.1))


# ============================================================
# Ambient Occlusion
# ============================================================
def _ao_cartoon():
    try:
        cmd.set("ambient_occlusion_mode", 1)
        cmd.set("ambient_occlusion_scale", 10)
        cmd.set("ambient_occlusion_smooth", 8)
    except:
        pass


def _ao_surface():
    try:
        cmd.set("ambient_occlusion_mode", 2)
        cmd.set("ambient_occlusion_scale", 14)
        cmd.set("ambient_occlusion_smooth", 14)
    except:
        pass


# ============================================================
# Modes
# ============================================================
def _cartoon():
    settings = {
        "cartoon_fancy_helices": 1,
        "cartoon_oval_length": 1.2,
        "cartoon_oval_width": 1.1,
        "cartoon_sampling": 20,
        "cartoon_smooth_loops": 1,
        "cartoon_flat_sheets": 0,
        "cartoon_highlight_color": -1,
    }

    for k, v in settings.items():
        cmd.set(k, v)

    _ao_cartoon()


def _surface():
    settings = {
        "surface_quality": 1,
        "surface_smooth_edges": 1,
        "surface_solvent": 0,
        "transparency": 0,
        "transparency_mode": 2,
        "two_sided_lighting": 1,

        # Lighting (less extreme)
        "ambient": 0.46,
        "direct": 0.30,
        "reflect": 0.34,

        "specular": 0.02,
        "shininess": 2,

        "ray_shadows": 1,
        "ray_shadow_decay_factor": 0.08,
        "ray_shadow_decay_range": 4.5,
        
    }
    cmd.set("surface_quality", 2)
    cmd.set("surface_smooth_edges", 1)

    for k, v in settings.items():
        cmd.set(k, v)

    # Better grazing-angle lights for surfaces
    cmd.set("light", (-0.3, -0.2, -1.0))
    cmd.set("light2", (-1.0, 0.0, 0.4))
    cmd.set("light3", (0.8, -0.5, 0.2))

    _ao_surface()


def _ligand():
    settings = {
        "stick_radius": 0.18,
        "stick_ball": 1,
        "stick_ball_ratio": 1.5,
        "valence": 1,
        "specular": 0.20,
        "shininess": 18,
    }

    for k, v in settings.items():
        cmd.set(k, v)


# ============================================================
# Main
# ============================================================
def pymerax(mode="cartoon"):
    cmd.reinitialize("settings")

    mode = mode.lower().strip()

    _set_bg()
    _base()
    _lights()

    if mode == "cartoon":
        _cartoon()

    elif mode == "surface":
        _surface()

    elif mode == "publication":
        _cartoon()
        cmd.bg_color("white")
        cmd.set("ray_trace_mode", 1)
        cmd.set("ray_trace_gain", 0.04)

    elif mode == "ligand":
        _cartoon()
        _ligand()

    else:
        print("Modes: cartoon, surface, publication, ligand")
        return

    print(f"PyMeraX {VERSION} loaded [{mode}]")
    print("Run 'ray' for full quality.")


cmd.extend("pymerax", pymerax)
cmd.extend("pymerax_help", pymerax_help)

_splash()