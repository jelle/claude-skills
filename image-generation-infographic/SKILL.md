---
name: Infographic Generation
description: Generate clean, professional infographics — flowcharts, process diagrams, step-by-step visuals, comparison charts, and data layouts via Gemini API. Trigger when the user says "infographic", "flowchart", "process diagram", "step-by-step", "comparison chart", "workflow diagram", or wants a visual explanation of a concept or process.
---

# Infographic Generator

## Goal
Generate high-quality, professional infographics: process flows, step-by-step diagrams, comparison layouts, and data visualizations with consistent visual language — pastel color-coded cards, simple line-art icons, clear typography, and logical flow indicators.

## Prerequisites
- `GEMINI_API_KEY` set as environment variable or in workspace `.env`
- `scripts/generate_image.py` present in workspace

## When to Use This Skill (NOT the others)
- **Use this** for: flowcharts, process diagrams, step-by-step explanations, comparison charts, timeline graphics, concept maps.
- **Use Realistic** for: photorealistic images, product shots, portraits.
- **Use Brand** for: logos, app icons, abstract brand marks without structured content.

## Infographic Design Principles

1. **Text legibility is king.** Every word must be perfectly readable. Short phrases only (3-8 words per card).
2. **Structural clarity.** Viewer must instantly understand the flow/hierarchy.
3. **Color-coding communicates grouping.** Each card/step gets a distinct pastel shade.
4. **Icons are simple line-art.** Single-weight stroke icons (Phosphor, Lucide, Feather style).
5. **Whitespace is structural.** Generous padding inside cards and between elements.

## Core Schema Structure

```json
{
  "task": "string - e.g., 'process_flowchart', 'comparison_chart', 'step_by_step_guide'",

  "output_specs": {
    "type": "string - e.g., 'infographic', 'process_diagram', 'flowchart'",
    "layout": "string - e.g., 'horizontal_flow', 'vertical_flow', '2x3_grid'",
    "aspect_ratio": "string - e.g., '16:9', '9:16', '4:3', '1:1'",
    "background": "string - e.g., 'clean white (#FFFFFF)', 'very light warm gray (#F8F8F6)'"
  },

  "content_structure": {
    "title": "string - Main heading at top",
    "subtitle": "string (optional)",
    "total_steps_or_items": "number",
    "flow_direction": "string - 'left_to_right', 'top_to_bottom', 'radial', 'zigzag'",
    "connectors": "string - 'arrows', 'dotted_lines', 'numbered_sequence', 'chevrons'",
    "items": [
      {
        "position": "string - e.g., 'step_1'",
        "icon_description": "string - Simple line-art icon",
        "card_color": "string - Pastel hex (e.g., '#E8D5F5')",
        "heading": "string - Short label (2-5 words)",
        "body_text": "string - Brief description (5-15 words)"
      }
    ]
  },

  "visual_style": {
    "card_shape": "string - e.g., 'rounded_rectangle'",
    "icon_style": "string - e.g., 'simple_line_art_single_weight'",
    "icon_placement": "string - e.g., 'above_heading'",
    "typography": {
      "title_font": "string - e.g., 'bold sans-serif, similar to Inter'",
      "text_color": "string - e.g., 'dark charcoal (#333333)'"
    },
    "color_palette": {
      "colors": ["#E8D5F5", "#D4F1E8", "#FFE4CC", "#DBEAFE", "#FDE8E8", "#FEF3C7", "#D1FAE5"],
      "accent_color": "string - For arrows (e.g., '#888888')"
    }
  },

  "explicit_restrictions": {
    "no_photorealism": true,
    "no_3d_rendering": true,
    "no_gradients_on_cards": true,
    "no_decorative_backgrounds": true,
    "text_must_be_perfectly_legible": true,
    "icons_must_be_simple_not_detailed": true
  },

  "negative_prompt": {
    "forbidden_elements": [
      "3d render, photorealism, complex detailed illustrations, gradient backgrounds, busy patterns, clip art, blurry text, illegible text, overlapping elements, cluttered layout, dark backgrounds, neon colors, glossy effects, hand-drawn sketch style, watercolor, perspective distortion, depth of field, noise, compression artifacts"
    ]
  }
}
```

## Dense Narrative Format (for Gemini API)

```json
{
  "prompt": "string - Dense description of the infographic with exact text for every card.",
  "negative_prompt": "string - 3d render, photorealism, complex illustrations, gradient backgrounds, busy patterns, clip art, blurry text, illegible text, cluttered layout, dark backgrounds, neon colors, glossy effects, hand-drawn style, watercolor, perspective distortion, depth of field, noise",
  "api_parameters": {
    "aspect_ratio": "16:9"
  },
  "settings": {
    "style": "clean flat infographic, modern SaaS marketing style",
    "lighting": "flat, even, no directional light",
    "camera_angle": "straight on, perfectly flat 2D",
    "depth_of_field": "none, perfectly flat",
    "quality": "crisp, high contrast text, perfectly legible typography"
  }
}
```

## Prompt Engineering Best Practices

1. **Text Content Must Be Explicit:** Spell out EVERY word that should appear. The model won't invent good copy.
2. **Describe Layout Geometrically:** "Seven rounded rectangle cards in a single horizontal row, connected by thin right-pointing arrows."
3. **Color-Code with Hex Values:** Lavender (#E8D5F5), mint (#D4F1E8), peach (#FFE4CC), sky blue (#DBEAFE), soft pink (#FDE8E8), pale yellow (#FEF3C7), sage green (#D1FAE5).
4. **Icons Must Be Dead Simple:** "A triangle play button inside a rounded rectangle" — not "a detailed media player."
5. **Enforce Text Legibility:** Always include "All text must be perfectly legible, crisp, and high contrast."
6. **Whitespace Is Mandatory:** "Generous padding inside each card" and "even spacing between cards."
7. **Flat = Non-negotiable:** "Perfectly flat 2D, no perspective, no shadows, no gradients, no 3D effects."
8. **Aspect Ratio Guide:**
   - Horizontal flows: 16:9
   - Vertical flows: 9:16 or 2:3
   - Grid layouts: 4:3 or 1:1
   - Wide single-row: 21:9 or 3:1

## Layout Templates

| Type | Layout | Best For | Aspect |
|------|--------|----------|--------|
| Horizontal Flow | Cards left-to-right with arrows | 4-8 step processes | 16:9 |
| Vertical Steps | Cards stacked with numbered circles | Tutorials, instructions | 9:16 |
| Grid Comparison | 2x2, 2x3, 3x3 grid | Feature comparisons, pros/cons | 4:3 |
| Hub-and-Spoke | Central node with radiating connections | Concept maps, ecosystems | 1:1 |
| Timeline | Line with branching event cards | Project timelines, roadmaps | 16:9 |

## Execution

1. Clarify the content (steps, items, text for each card).
2. Choose the appropriate layout template.
3. Construct the JSON prompt.
4. Save prompt to `prompts/images/infographics/[name].json`.
5. Run: `python3 scripts/generate_image.py prompts/images/infographics/[name].json outputs/images/infographics/[name].png "16:9"`
6. Play chime: `afplay /System/Library/Sounds/Glass.aiff`

## How to use this skill
When a user asks for an infographic, flowchart, or process diagram, construct the prompt as JSON, save it, and execute via the generate script. Never use the realistic or brand skill for infographic work.
