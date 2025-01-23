# pyqt-hackrylic
Simulates, in a hacky way, the [acrylic window effect](https://learn.microsoft.com/en-us/windows/apps/design/style/acrylic) by using screenshots with a blur effect as the window's background.

## Screenshots
### Empty
![Example](https://github.com/andrew-bedford/pyqt-hackrylic/blob/main/Example.jpg)

### Application
![re/log](https://github.com/andrew-bedford/pyqt-hackrylic/blob/main/QWebEngine.jpg)

## Why?
I like the look and wanted to make it optionally available in [re/apps](https://github.com/andrew-bedford/re-app) in a cross-platform way. I tried some of the existing solutions, like [PyQt-Frameless-Window](https://github.com/zhiyiYo/PyQt-Frameless-Window) and [qtacrylic](https://github.com/blitpxl/qtacrylic), however they had significant performance issues and/or didn't work on my current compositor ([mutter](https://github.com/GNOME/mutter)) as it doesn't currently support this feature.

## Limitations
It takes screenshots before showing the window the first time, and whenever it goes from minimized to visible. As a result, the background that it shows may not always reflect what's actually behind the window. There may also be a delay before it updates the background.

**Note**: This is just an experiment, I wouldn't recommend using it in production as is.