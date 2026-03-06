---
name: "responsive-layout"
description: "Creates responsive website layouts that adapt to different screen sizes. Invoke when user needs help designing layouts that work across devices."
---

# Responsive Layout Designer

## Overview

This skill helps create responsive website layouts that adapt seamlessly to different screen sizes, from mobile devices to desktop computers. It provides layout strategies, breakpoints, and implementation techniques for modern responsive design.

## Features

- **Layout Strategies**: Generate fluid grids, flexible containers, and adaptive layouts
- **Breakpoint Management**: Define optimal breakpoints for different device sizes
- **Responsive Typography**: Create text that scales appropriately across devices
- **Media Queries**: Generate CSS media queries for different viewport sizes
- **Mobile-First Approach**: Implement mobile-first design principles
- **Layout Patterns**: Provide common responsive layout patterns and solutions

## Usage

### Basic Usage

When designing a new website or optimizing an existing one for responsiveness, invoke this skill to generate responsive layout solutions. The skill will provide:

1. **Layout Structure**: HTML structure optimized for responsiveness
2. **CSS Framework**: Responsive CSS with media queries and flexible grids
3. **Breakpoint Strategy**: Recommended breakpoints for different device sizes
4. **Responsive Components**: Components that adapt to different screen sizes
5. **Testing Guidelines**: How to test responsiveness across devices

### Example Prompt

```
Create a responsive layout for a portfolio website with a hero section, project grid, and contact form. Include breakpoints for mobile, tablet, and desktop.
```

## Layout Strategies

### Mobile-First Approach

- Start with mobile design and progressively enhance for larger screens
- Use relative units (rem, em, vh, vw) instead of fixed pixels
- Implement flexible grids that adapt to container width
- Prioritize content for smaller screens

### Breakpoint Strategy

Recommended breakpoints:

- **Mobile**: 320px - 767px
- **Tablet**: 768px - 1023px
- **Desktop**: 1024px - 1439px
- **Large Desktop**: 1440px and above

### Layout Patterns

- **Fluid Grid**: Flexible grid system that adapts to screen width
- **Column Drop**: Columns stack vertically on smaller screens
- **Layout Shifter**: Major layout changes at different breakpoints
- **Off-Canvas**: Navigation menu that slides in from the side on mobile
- **Flexbox Layout**: Modern CSS flexbox for flexible layouts
- **CSS Grid Layout**: Two-dimensional grid system for complex layouts

## Implementation

### HTML Structure

- Use semantic HTML5 elements for better accessibility
- Implement a container system for consistent spacing
- Use appropriate heading hierarchy
- Include viewport meta tag for mobile devices

### CSS Techniques

- Use CSS variables for consistent spacing and sizing
- Implement media queries for different breakpoints
- Use flexbox and grid for layout management
- Implement responsive typography using relative units
- Optimize images for different screen sizes

### Testing

- Test across multiple devices and screen sizes
- Use browser developer tools for responsive testing
- Check for touch-friendly elements on mobile devices
- Ensure text readability across all screen sizes
- Test performance on slower connections

## Best Practices

- Keep layout changes minimal between breakpoints
- Maintain visual consistency across devices
- Prioritize content based on screen size
- Optimize for touch interactions on mobile devices
- Ensure accessibility across all screen sizes
- Test performance on different devices

## Integration

The responsive layouts can be integrated with:

- Frontend frameworks (React, Vue, Angular)
- CSS frameworks (Bootstrap, Tailwind CSS, Foundation)
- Static site generators (Jekyll, Hugo, Gatsby)
- Content management systems (WordPress, Drupal, Joomla)