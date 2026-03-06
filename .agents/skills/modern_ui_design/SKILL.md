---
name: modern_ui_design
description: 用于在构建或修改网页时实施现代、高级感、精美的UI设计规范，包括玻璃拟态、渐变色、阴影等。
---

# 现代网页UI设计规范 (Modern UI Design Guidelines)

当你被要求美化网页或应用现代UI设计时，请严格遵守以下规则：

## 1. 核心视觉原则 (Core Visual Principles)
- **拒绝默认样式**: 永远不要使用浏览器默认的按钮、输入框、边框样式。必须重置默认样式并应用自定义设计。
- **高级感配色**: 不要使用纯红、纯蓝、纯绿（如 #FF0000, #00FF00, #0000FF）。使用低饱和度、高明度或深色模式下的沉稳色系，推荐使用 HSL 调整颜色。
- **微妙的渐变 (Subtle Gradients)**: 使用柔和的线性或径向渐变作为背景或强调色，避免过度强烈的对比。

## 2. 质感与空间 (Texture and Space)
- **大圆角 (Large Border Radiuses)**: 卡片元素和按钮使用适当的圆角（如 `8px` 到 `16px` 或 `border-radius: 1rem`），让人感觉友好且现代。
- **弥散阴影 (Soft Box Shadows)**: 避免生硬的黑色黑色阴影。使用多层极淡的阴影，例如 `box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);`。
- **留白 (Whitespace/Negative Space)**: 在组件之间和组件内部给予充足的 `padding` 和 `margin`。现代设计中，空间也是一种设计元素。

## 3. 玻璃拟态 (Glassmorphism)
对于浮动面板、头部导航或模态框，可以适当使用玻璃拟态：
- 背景设置为半透明，例如 `background: rgba(255, 255, 255, 0.7);`（如果是深色模式则是 `rgba(17, 24, 39, 0.7)`）
- 背景模糊：`backdrop-filter: blur(10px);`
- 边缘高光：`border: 1px solid rgba(255, 255, 255, 0.3);`

## 4. 行动指南 (Action Item)
每当你进行UI改善时，首先检查以上元素是否被合理运用，并在你的 CSS 文件中添加对应的全局变量（CSS Variables）来管理这些色彩和阴影。
