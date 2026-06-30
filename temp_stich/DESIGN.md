---
name: Pythonic Cinematic
colors:
  surface: '#111415'
  surface-dim: '#111415'
  surface-bright: '#373a3b'
  surface-container-lowest: '#0c0f10'
  surface-container-low: '#191c1d'
  surface-container: '#1d2021'
  surface-container-high: '#282a2b'
  surface-container-highest: '#323536'
  on-surface: '#e1e3e4'
  on-surface-variant: '#c1c7d0'
  inverse-surface: '#e1e3e4'
  inverse-on-surface: '#2e3132'
  outline: '#8b919a'
  outline-variant: '#41474f'
  surface-tint: '#98cbff'
  primary: '#98cbff'
  on-primary: '#003354'
  primary-container: '#3776ab'
  on-primary-container: '#f5f8ff'
  inverse-primary: '#1d6296'
  secondary: '#efc52b'
  on-secondary: '#3c2f00'
  secondary-container: '#d1aa00'
  on-secondary-container: '#504000'
  tertiary: '#c3c6cf'
  on-tertiary: '#2d3137'
  tertiary-container: '#6e727a'
  on-tertiary-container: '#f6f8ff'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#cfe5ff'
  primary-fixed-dim: '#98cbff'
  on-primary-fixed: '#001d33'
  on-primary-fixed-variant: '#004a77'
  secondary-fixed: '#ffe082'
  secondary-fixed-dim: '#ecc228'
  on-secondary-fixed: '#231b00'
  on-secondary-fixed-variant: '#564500'
  tertiary-fixed: '#dfe2eb'
  tertiary-fixed-dim: '#c3c6cf'
  on-tertiary-fixed: '#181c22'
  on-tertiary-fixed-variant: '#43474e'
  background: '#111415'
  on-background: '#e1e3e4'
  surface-variant: '#323536'
typography:
  display-lg:
    fontFamily: Sora
    fontSize: 72px
    fontWeight: '700'
    lineHeight: 80px
    letterSpacing: -0.04em
  headline-lg:
    fontFamily: Sora
    fontSize: 40px
    fontWeight: '600'
    lineHeight: 48px
    letterSpacing: -0.02em
  headline-lg-mobile:
    fontFamily: Sora
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
    letterSpacing: -0.02em
  body-md:
    fontFamily: Manrope
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
    letterSpacing: 0em
  code-sm:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '500'
    lineHeight: 20px
    letterSpacing: 0.05em
  label-caps:
    fontFamily: Sora
    fontSize: 12px
    fontWeight: '800'
    lineHeight: 16px
    letterSpacing: 0.15em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 8px
  container-max: 1280px
  gutter: 24px
  margin-desktop: 64px
  margin-mobile: 20px
  section-gap: 120px
---

## Brand & Style

The design system is engineered for a premium, high-tech audience that values the intersection of developer culture and cinematic excellence. The brand personality is powerful yet refined, echoing the precision of clean code and the high-energy output of an elite performance product.

The visual direction blends **Minimalism** with **Glassmorphism** and **Metallic accents**. It utilizes heavy whitespace to create a "gallery" feel, where every element has room to breathe. Inspired by high-end hardware marketing, the interface uses subtle background blurs, hairline borders, and soft glows to simulate depth and light refraction, as seen on brushed aluminum or frosted glass. The emotional response is one of sophisticated focus, professional reliability, and futuristic energy.

## Colors

This design system utilizes a dark-mode-first palette to emphasize the "Cinematic Tech" aesthetic. 

- **Primary (Python Blue):** Used for primary actions, subtle glows, and highlighting key technical paths.
- **Secondary (Python Yellow):** Reserved for high-energy accents, status indicators, and tactical "sparks" of information.
- **Background (Dark Navy/Black):** A deep, rich `#0D1117` or pure black creates a canvas for metallic highlights.
- **Surface (Metallic/Glass):** Semi-transparent variants of dark navy combined with white hairline borders create the "Metallic" UI look.
- **Typography:** High-contrast White for primary headers and muted Grays for secondary body text to maintain visual hierarchy.

## Typography

Typography is a primary vehicle for the "Premium Tech" feel. 

**Sora** provides a geometric, futuristic weight to headlines, feeling engineered and bold. **Manrope** is used for body text to ensure readability with a modern, balanced sans-serif structure. **JetBrains Mono** is strategically integrated for labels, tags, and technical metadata to pay homage to the Python developer environment.

Key principles:
- **Tight Kerning:** On large display headers to create a cinematic impact.
- **Aggressive Leading:** High line-height on body text to maximize whitespace.
- **Uppercase Labels:** Used for utility text to mimic high-end technical spec sheets.

## Layout & Spacing

The layout philosophy follows a **Fixed Grid** model for maximum control over cinematic composition. On desktop, a 12-column grid with generous 64px side margins is used to center content and focus the eye.

Spacing is expansive. Sections are separated by large vertical gaps (120px+) to ensure no two major ideas compete for attention. Component spacing follows a strict 8px base unit, ensuring technical precision. Elements should feel "placed" on a canvas rather than "poured" into a container. For mobile, margins tighten, and content collapses into a single-column stack, maintaining the signature white (or black) space between blocks.

## Elevation & Depth

Hierarchy is achieved through **Glassmorphism** and **Tonal Layering** rather than traditional drop shadows.

- **Background:** Deepest layer, often a subtle radial gradient of Dark Navy to Black.
- **Glass Surfaces:** Semi-transparent layers (10-20% opacity) with a `24px` backdrop blur. These surfaces feature a `0.5px` inner border of white at 15% opacity to simulate a light-catching "metallic" edge.
- **Soft Glows:** High-priority elements use "Ambient Glows"—extra-diffused shadows tinted with Python Blue (`#3776AB`) with a blur radius of 40px+ and low opacity (10-15%). This mimics light emitting from a high-tech screen or hardware component.
- **Flat Overlays:** No shadows on text or buttons; depth is communicated solely through color contrast and background blur.

## Shapes

The shape language balances industrial precision with approachability. 

The standard **Rounded (0.5rem)** corner radius is applied to cards and containers. However, for interactive elements like buttons or chips, a more geometric and "engineered" feel is desired. Hairline borders are essential—never exceeding 1px—to maintain the premium, high-resolution aesthetic. Icons should be thin-stroke, linear, and strictly geometric.

## Components

### Buttons
Primary buttons use a "Metallic" gradient of Python Blue or a solid high-contrast white. They feature a slight outer glow on hover. Secondary buttons are "Ghost" style with a 1px metallic border and no fill until interaction.

### Cards
Cards utilize the glassmorphism treatment: 15% opacity background, 24px backdrop blur, and a subtle white hairline border. Content inside cards should have generous padding (32px+).

### Inputs
Search and text inputs are minimalist underlays or fully transparent glass containers. The active state is indicated by the bottom border turning Python Yellow or Blue with a soft glow.

### Chips & Tags
Technical tags (e.g., "v3.12") use **JetBrains Mono** in all-caps, with a dark background and a subtle tint of the primary color. They are small and sharp, appearing like printed labels on hardware.

### Progress Indicators
Linear bars should be ultra-thin (2px - 4px) using Python Yellow to represent "Energy" or "Power" flow, often accompanied by a trailing glow effect to suggest movement.