---
name: typography_layout
description: 应用现代网页排版原则、字体处理和整体结构布局技巧，确保绝佳的可读性。
---

# 现代排版与布局规划 (Typography & Layout Constraints)

一流的UI设计有一半取决于排版和布局。执行布局任务时请参考以下准则。

## 1. 字体配置 (Font Configuration)
- **使用系统或高级无衬线字体 (Sans-Serif)**: 如果没有特别要求，使用如 `Inter`, `Roboto`, `SF Pro Display`, `Outfit` 等现代字体。
- **多级字号字重 (Hierarchy)**:
  - 标题 `h1`, `h2`: 字体加粗 (`font-weight: 700` 或 `800`)，使用更紧凑的字间距 (`letter-spacing: -0.025em`)。
  - 正文 `p`: 保持可读性，行高建议为 `1.6` 到 `1.8` (`line-height: 1.6;`)。
- **颜色层级**: 正文不要使用纯黑 (`#000000`)。标题可以使用 `#111827` 或 `#1e293b`，正文使用 `#4b5563` 或 `#64748b` 以降低对比，护眼且优雅。

## 2. 响应式布局 (Responsive Layouts)
- **Flexbox & CSS Grid**: 不要使用浮动（float）。全面使用现代 Flex 或者 Grid 系统来实现居中、对齐和网格分布。
- **内容容器 (Constrained Container)**: 为页面核心内容设置最大宽度（例如 `max-width: 1200px; margin: 0 auto;`），避免文字行在超大屏幕上过长（可读性最佳长度是单行 60-80 字符）。

## 3. 分割与对比 (Delimiters and Contrast)
- 避免使用粗重的和深色的实体边框。
- 进行视觉分割时，优先考虑利用背景色彩差异（如灰白交替层）或者极淡的细线 (`border-bottom: 1px solid #e2e8f0;`)。

## 4. 行动指南 (Action Item)
配置基本 CSS 时，先在 `:root` 也就是 `html` / `body` 层面上设置并统一下字体族、基础行高、字体颜色，然后再处理个别组件库。
