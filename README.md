# pyqt-hackrylic
Simulates the acrylic window effect by using screenshot with a blur effect as you window's background.

## Why?
I like how it looks and wanted to make it optionally available in re/apps in a cross-platform way. I tried some of the existing solutions ([PyQt-Frameless-Window](https://github.com/zhiyiYo/PyQt-Frameless-Window) and [qtacrylic](https://github.com/blitpxl/qtacrylic), however they had significant performance issues and didn't work on my current compositor (GNOME's mutter) as it doesn't support this feature.

## Limitations
It takes screenshots before showing the window the first time, and whenever it goes from minimized to visible. As a result, the background that it shows may not always reflect what's actually behind the window.
