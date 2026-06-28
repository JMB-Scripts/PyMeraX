# PyMeraX

**PyMeraX** is a small PyMOL script that makes PyMOL rendering look closer to ChimeraX by applying improved lighting, softer shadows, ambient occlusion, and cleaner cartoon/surface presets.

Can be use in parralell with MolNympheas 
(https://github.com/JMB-Scripts/MolNympheas)

---

## Features

- Improved global lighting
- Softer shadows with better depth perception
- Ambient occlusion for enhanced volume
- ChimeraX-like surface rendering
- Cleaner cartoon representation
- Publication-ready rendering presets
- Ligand-focused visualization mode

---

## Installation

1. Save the script as:

```bash
pymerax.py
```

2. Load it inside PyMOL:

```python
run pymerax.py
```

Or from command line:

```bash
pymol pymerax.py
```

---

## Usage

Available commands:

```python
pymerax()
pymerax("cartoon")
pymerax("surface")
pymerax("publication")
pymerax("ligand")
pymerax_help()
```

Default mode:

```python
pymerax()
```

Equivalent to:

```python
pymerax("cartoon")
```

---

## Rendering Modes

### Cartoon

Best for proteins, domains, and structural overviews.

```python
pymerax("cartoon")
```

# Without PyMeraX

<img width="325" height="391" alt="image" src="https://github.com/user-attachments/assets/d7bd9357-d69e-4b58-bfcd-76a814cb636b" />



# With PyMeraX

<img width="336" height="385" alt="image" src="https://github.com/user-attachments/assets/6e92719c-f04b-46e4-a22d-db65cc64abdc" />


Features:
- Smooth helices
- Rounded ribbons
- Better depth
- Soft AO shading

---

### Surface

Best for molecular surfaces and cryo-EM-like visualization.

```python
pymerax("surface")
```

Features:
- Improved grazing-angle lighting
- Stronger shadowing
- Enhanced surface curvature perception
- Better cavity visibility


# Without PyMeraX

<img width="446" height="460" alt="image" src="https://github.com/user-attachments/assets/d0fff1db-a781-47ba-818a-e72d5cee6e8e" />




# With PyMeraX

<img width="452" height="460" alt="image" src="https://github.com/user-attachments/assets/71c01aad-d51d-4f94-b8e5-4f25bed39b41" />


---

### Publication

Clean white background for figures.

```python
pymerax("publication")
```

Features:
- White background
- Balanced contrast
- High-quality ray tracing

---

### Ligand

Optimized for protein–ligand complexes.

```python
pymerax("ligand")
```

Features:
- Improved stick rendering
- Better specular highlights
- Enhanced ligand visibility

---

## Notes

PyMeraX modifies PyMOL settings globally using:

```python
cmd.reinitialize("settings")
```

This resets rendering settings before applying a preset.

---

## Compatibility

Tested with:

- PyMOL 3.x+
- Open-source PyMOL
- Incentive PyMOL (partial AO support depending on version)

Ambient occlusion parameters may be ignored in older PyMOL builds.

---

## License

Do whatever you want with the scripts and keep in mind that it has been code by a stupid biochemist (for that matter me).
