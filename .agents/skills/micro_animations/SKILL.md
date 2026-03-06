---
name: micro_animations
description: 为网页元素添加微交互、平滑过渡动画和反馈，让网页感觉敏捷且“栩栩如生”。
---

# 网页微交互与动画规范 (Micro-animations and Transitions)

为了提升用户体验并让网页具有高级感，你需要应用以下动画和过渡效果。

## 1. 交互过渡 (Interaction Transitions)
- **全局过渡 (Global Transitions)**: 对于所有可交互元素（按钮、链接、卡片），必须为其常规和 hover/active 状态添加过渡效果。
- **最佳实践**: `transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);` 或者仅仅过渡需要改变的属性（如 `background-color, transform, box-shadow`）。

## 2. 悬停效果 (Hover Effects)
- **按压与浮动**: 
  - 按钮/卡片在悬停时轻微上浮：`transform: translateY(-2px);` 或 `scale(1.02);`。
  - 点击时下压：`transform: scale(0.97);`。
- **阴影变化**: 悬停时加深且扩大阴影：`box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);`
- **颜色突显**: 背景颜色微调或者边框发光。

## 3. 入场与加载动画 (Entrance and Loading)
- **淡入上浮 (Fade In Up)**: 页面核心内容加载时，不要突然闪现。使用从底部微移并淡入的动画：
```css
@keyframes fadeInUp {
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
}
.animate-fade-in { animation: fadeInUp 0.6s ease-out forwards; }
```
- **错开加载 (Staggered Loading)**: 如果存在列表或网格项，可以为每个子项目添加递增的 `animation-delay`。

## 4. 行动指南 (Action Item)
在添加任何交互组件之前，问问自己：“它能响应用户的操作吗？” 为此编写专门的 CSS 类或关键帧，并在 HTML 中应用它。
