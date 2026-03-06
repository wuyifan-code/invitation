---
name: "color-scheme-generator"
description: "Generates professional color schemes for UI design with hex, RGB, and HSL values. Invoke when user needs color palettes for websites or applications."
---

# Color Scheme Generator

## Overview

This skill creates professional color schemes for UI design, including primary, secondary, and accent colors, as well as neutral tones. It provides color values in hex, RGB, and HSL formats, along with usage guidelines for different design elements.

## Features

- **Color Palettes**: Generate comprehensive color schemes with primary, secondary, and accent colors
- **Color Formats**: Provide color values in hex, RGB, and HSL formats
- **Color Psychology**: Include information on color psychology and emotional impact
- **Accessibility**: Ensure color combinations meet accessibility standards
- **Usage Guidelines**: Provide recommendations for using colors in different UI elements
- **Theme Variations**: Generate light and dark theme variations
- **Color Harmonies**: Create color schemes based on different harmony rules (complementary, analogous, triadic, etc.)

## Usage

### Basic Usage

When designing a new website or application, invoke this skill to generate a professional color scheme. The skill will provide:

1. **Primary Colors**: Main brand colors
2. **Secondary Colors**: Supporting colors for accents and highlights
3. **Neutral Colors**: Grayscale colors for text, backgrounds, and UI elements
4. **Color Formats**: Values in hex, RGB, and HSL formats
5. **Usage Guidelines**: Recommendations for applying colors to different UI elements
6. **Accessibility Check**: Verification that color combinations meet WCAG standards

### Example Prompt

```
Create a color scheme for a modern tech startup website with a professional and innovative feel. Include primary, secondary, accent, and neutral colors with usage guidelines.
```

## Color Schemes

### Monochromatic

- **Description**: Variations of a single hue
- **Best For**: Clean, minimalist designs
- **Example**: Different shades and tints of blue

### Complementary

- **Description**: Colors opposite each other on the color wheel
- **Best For**: High contrast, vibrant designs
- **Example**: Blue and orange

### Analogous

- **Description**: Colors adjacent to each other on the color wheel
- **Best For**: Harmonious, cohesive designs
- **Example**: Blue, blue-green, and green

### Triadic

- **Description**: Three colors evenly spaced on the color wheel
- **Best For**: Balanced, dynamic designs
- **Example**: Red, yellow, and blue

### Tetradic

- **Description**: Four colors forming a rectangle on the color wheel
- **Best For**: Rich, complex designs
- **Example**: Blue, orange, green, and red

### Split Complementary

- **Description**: A base color plus the two colors adjacent to its complement
- **Best For**: High contrast without clashing
- **Example**: Blue, red-orange, and yellow-orange

## Color Psychology

### Warm Colors

- **Red**: Passion, energy, urgency
- **Orange**: Creativity, enthusiasm, warmth
- **Yellow**: Happiness, optimism, attention

### Cool Colors

- **Blue**: Trust, stability, professionalism
- **Green**: Growth, health, harmony
- **Purple**: Creativity, luxury, wisdom

### Neutral Colors

- **White**: Purity, simplicity, space
- **Gray**: Neutrality, sophistication, balance
- **Black**: Elegance, authority, drama

## Accessibility

### WCAG Guidelines

- **Contrast Ratio**: Ensure sufficient contrast between text and background
- **Normal Text**: Minimum contrast ratio of 4.5:1
- **Large Text**: Minimum contrast ratio of 3:1
- **UI Elements**: Ensure interactive elements have sufficient contrast

### Testing Tools

- **Contrast Checkers**: Tools to verify contrast ratios
- **Color Blindness Simulators**: Test how colors appear to users with color vision deficiencies
- **Accessibility Validators**: Tools to check overall accessibility compliance

## Usage Guidelines

### Primary Colors

- **Branding**: Logo, main navigation, primary buttons
- **Accents**: Important highlights and call-to-action elements
- **Consistency**: Use consistently across the application

### Secondary Colors

- **Supporting Elements**: Secondary buttons, icons, and highlights
- **Categorization**: Different sections or features
- **Visual Hierarchy**: Create depth and visual interest

### Neutral Colors

- **Text**: Primary and secondary text
- **Backgrounds**: Page backgrounds and card surfaces
- **Borders**: Dividers and UI element boundaries
- **Shadows**: Depth and dimensionality

### Dark Themes

- **Background**: Darker neutral colors
- **Text**: Lighter neutral colors
- **Accents**: Same primary and secondary colors
- **Contrast**: Maintain sufficient contrast ratios

## Implementation

### CSS Variables

```css
:root {
  /* Primary Colors */
  --primary-50: #f0f9ff;
  --primary-100: #e0f2fe;
  --primary-200: #bae6fd;
  --primary-300: #7dd3fc;
  --primary-400: #38bdf8;
  --primary-500: #0ea5e9;
  --primary-600: #0284c7;
  --primary-700: #0369a1;
  --primary-800: #075985;
  --primary-900: #0c4a6e;
  
  /* Secondary Colors */
  --secondary-50: #fdf2f8;
  --secondary-100: #fce7f3;
  --secondary-200: #fbcfe8;
  --secondary-300: #f9a8d4;
  --secondary-400: #f472b6;
  --secondary-500: #ec4899;
  --secondary-600: #db2777;
  --secondary-700: #be185d;
  --secondary-800: #9d174d;
  --secondary-900: #831843;
  
  /* Neutral Colors */
  --neutral-50: #f9fafb;
  --neutral-100: #f3f4f6;
  --neutral-200: #e5e7eb;
  --neutral-300: #d1d5db;
  --neutral-400: #9ca3af;
  --neutral-500: #6b7280;
  --neutral-600: #4b5563;
  --neutral-700: #374151;
  --neutral-800: #1f2937;
  --neutral-900: #111827;
}
```

### Design Tools Integration

- **Figma**: Import color palettes as styles
- **Sketch**: Create color swatches
- **Adobe XD**: Define color assets
- **Photoshop**: Create color swatches
- **InDesign**: Define color libraries

## Best Practices

- **Limit Palette Size**: Keep color schemes to 3-5 main colors
- **Consistency**: Use the same color scheme across the entire application
- **Accessibility**: Ensure all color combinations meet WCAG standards
- **Context**: Consider the context and purpose of the design
- **Testing**: Test colors across different devices and lighting conditions
- **Flexibility**: Create color schemes that work in both light and dark modes

## Industry-Specific Color Schemes

### Technology

- **Best Colors**: Blue, teal, purple
- **Psychology**: Trust, innovation, professionalism
- **Example**: Google, Microsoft, IBM

### Healthcare

- **Best Colors**: Blue, green, white
- **Psychology**: Trust, health, cleanliness
- **Example**: Mayo Clinic, Kaiser Permanente

### Finance

- **Best Colors**: Blue, gold, green
- **Psychology**: Trust, wealth, stability
- **Example**: Chase, Bank of America

### Food & Beverage

- **Best Colors**: Red, orange, green
- **Psychology**: Appetite, energy, freshness
- **Example**: McDonald's, Starbucks

### Fashion

- **Best Colors**: Black, white, gray, accent colors
- **Psychology**: Elegance, sophistication, style
- **Example**: Chanel, Gucci