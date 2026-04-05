---
name: Brand Visuals Generation
description: Generate crisp, minimalist logos, app icons, and flat-vector brand illustrations via Gemini API. Trigger when the user says "logo", "brand visual", "app icon", "illustration", or wants flat vector graphic design output.
---

# Brand Visuals Generator

## Goal
Generate UI elements, logos, and flat brand illustrations by enforcing structured JSON prompts focused on graphic design principles (spacing, typography, geometry, color palettes). Prevents unwanted photorealism, 3D artifacts, complex lighting, or messy backgrounds.

## Prerequisites
- `GEMINI_API_KEY` set as environment variable or in workspace `.env`
- `scripts/generate_image.py` present in workspace

## Core Schema Structure

```json
{
  "task": "string - e.g., 'primary_wordmark_logo', 'daily_app_icon', 'minimalist_website_illustration'",

  "output_specs": {
    "type": "string - e.g., 'svg_feel_vector', 'flat_geometric_art', 'monoline_logo'",
    "layout": "string - e.g., '1x1_icon', '16:9_hero_illustration'",
    "background": "string - e.g., 'solid warm peach (#FFDAB9)', 'pure white, isolated'"
  },

  "brand_identity": {
    "industry_context": "string - e.g., 'calming therapy app'",
    "mood_and_personality": "string - e.g., 'calm, flowing, organic'",
    "color_palette": {
      "primary": "string",
      "secondary": "string",
      "avoid_colors": "string"
    }
  },

  "design_elements": {
    "imagery_and_symbols": "string - Explicit geometric instructions",
    "composition": "string - e.g., 'perfectly centered, balanced negative space, strictly 2D'",
    "typography": "string - Describe fonts or specify 'pure icon/symbol, NO text'"
  },

  "explicit_restrictions": {
    "no_photorealism": true,
    "no_lighting_artifacts": true,
    "no_humans_or_faces": true,
    "no_3d_rendering": true
  },

  "negative_prompt": {
    "forbidden_elements": [
      "3d render, drop shadows, gradients, complex messy backgrounds, human figures, faces, noise, film grain, blur, depth of field, photo realism, glowing light effects, bevels, embossing, cgi"
    ]
  }
}
```

## Dense Narrative Format (for Gemini API)

```json
{
  "prompt": "string - Dense narrative of the graphic design.",
  "negative_prompt": "string - Comma-separated realism blockers.",
  "api_parameters": {
    "aspect_ratio": "string - '1:1', '16:9', etc."
  },
  "settings": {
    "style": "minimalist flat vector graphics",
    "lighting": "flat graphic",
    "camera_angle": "straight on 2d",
    "depth_of_field": "flat",
    "quality": "crisp vector style perfectly rendered"
  }
}
```

## Best Practices

1. **Describe the Geometry:** "A continuous single line forming an abstract S curve with perfectly rounded caps" — not "a cool logo."
2. **Color Codes & Specific Names:** "sage green, sand beige, and soft peach (#FFDAB9)." Call out forbidden colors.
3. **Flat Lighting:** Always specify "flat color, 2D vector style, straight-on composition."
4. **Emphasize Typography:** Specify "sans-serif, lowercase, slightly rounded edges, clean spacing."
5. **Robust Negative Prompting:** Must include: `3d render, drop shadow, bevel, gradient, realistic lighting, photorealism, noise`.

## Execution

1. Construct the JSON prompt following the schema above.
2. Save prompt to `prompts/images/[category]/[name].json`.
3. Run: `python3 scripts/generate_image.py prompts/images/[category]/[name].json outputs/images/[category]/[name].png`
4. Play chime: `afplay /System/Library/Sounds/Glass.aiff`

## How to use this skill
When a user asks for a logo, app icon, or brand visual, construct the prompt as JSON, save it, and execute via the generate script. Never use the realistic photography skill for branding exercises.
