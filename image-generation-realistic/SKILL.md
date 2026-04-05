---
name: Realistic Image Generation
description: Generate hyper-realistic, highly-controlled images using parameterized JSON prompting via Gemini API. Trigger when the user says "realistic image", "photo generation", "generate image", "realistic photo", or wants a photorealistic AI image.
---

# Realistic Image Generation

## Goal
Generate hyper-realistic images by enforcing structured JSON prompts that neutralize AI model biases (over-smoothing, dataset-averaging, "plastic" styling) and produce raw, unretouched outputs.

## Prerequisites
- `GEMINI_API_KEY` set as environment variable or in workspace `.env`
- `scripts/generate_image.py` present in workspace

## Core Schema Structure

```json
{
  "task": "string - High-level goal (e.g., 'sports_selfie_collage', 'single_macro_portrait')",

  "output": {
    "type": "string - e.g., 'single_image', '4-panel_collage'",
    "layout": "string - e.g., '1x1', '2x2_grid', 'side-by-side'",
    "aspect_ratio": "string - e.g., '3:4', '16:9', '4:5'",
    "camera_style": "string - e.g., 'smartphone_front_camera', 'professional_dslr'"
  },

  "image_quality_simulation": {
    "sharpness": "string",
    "noise": "string",
    "compression_artifacts": "boolean",
    "dynamic_range": "string",
    "white_balance": "string",
    "lens_imperfections": ["array of strings"]
  },

  "subject": {
    "type": "string - e.g., 'human_portrait', 'nature_macro'",
    "human_details": {
      "identity": "string",
      "appearance": "string - Extremely specific (e.g., visible pores, mild redness)",
      "outfit": "string"
    },
    "object_or_nature_details": {
      "material_or_texture": "string",
      "wear_and_tear": "string",
      "typography": "string"
    }
  },

  "environment": {
    "location": "string",
    "background": "string",
    "lighting": {
      "type": "string",
      "quality": "string"
    }
  },

  "explicit_restrictions": {
    "no_professional_retouching": true,
    "no_studio_lighting": true,
    "no_ai_beauty_filters": true
  },

  "negative_prompt": {
    "forbidden_elements": [
      "anatomy normalization, body proportion averaging, skin smoothing, plastic skin, airbrushed texture, stylized realism, beautification filters, editorial fashion proportions"
    ]
  }
}
```

## Dense Narrative Format (for Gemini API)

```json
{
  "prompt": "string - A dense, ultra-descriptive narrative. Use specific camera math (85mm lens, f/1.8, ISO 200), explicit flaws (visible pores, mild redness, subtle freckles), lighting behavior (direct on-camera flash creating sharp highlights), and direct negative commands (Do not beautify or alter facial features).",
  "negative_prompt": "string - Comma-separated list of realism blockers (no plastic skin, no CGI).",
  "image_input": ["array of strings (URLs) - Optional reference images"],
  "api_parameters": {
    "aspect_ratio": "string - e.g., '16:9', '4:5'"
  },
  "settings": {
    "style": "string - e.g., 'documentary realism'",
    "lighting": "string - e.g., 'direct on-camera flash'",
    "camera_angle": "string",
    "depth_of_field": "string",
    "quality": "string - e.g., 'high detail, unretouched skin'"
  }
}
```

## Best Practices

1. **Camera Mathematics:** Always define exact focal length, aperture, and ISO (e.g., `85mm lens, f/2.0, ISO 200`).
2. **Explicit Imperfections:** Dictate flaws: `mild redness`, `subtle freckles`, `light acne marks`.
3. **Direct Commands:** Use imperative negative commands inside the positive prompt: `Do not beautify or alter facial features.`
4. **Lighting Behavior:** Name what light does: `direct flash photography, creating sharp highlights on skin.`
5. **Non-Human Materials:** Replace skin logic with material physics: `micro-scratches on anodized aluminum`.
6. **Mandatory Negative Stack:** Always forbid `skin smoothing`, `anatomy normalization`, `plastic skin`.
7. **Avoid Over-Degradation:** Keep ISO below 800. Rely on physical subject imperfections over camera noise.

## Execution

1. Construct the JSON prompt following the schema above.
2. Save prompt to `prompts/images/[category]/[name].json`.
3. Run: `python3 scripts/generate_image.py prompts/images/[category]/[name].json outputs/images/[category]/[name].png "4:5"`
4. Play chime: `afplay /System/Library/Sounds/Glass.aiff`

## How to use this skill
When a user asks for a realistic or photographic image, construct the prompt as JSON, save it, and execute via the generate script. Never use the brand or infographic skill for photorealistic work.
