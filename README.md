<p align="center"><img src="assets/app-icon.png" width="144" alt="Stylus app icon"></p>

# Stylus for Android

为 Android 平板和手写笔打造的本地笔记与绘画应用。用不同的笔触书写、画图，在自己的笔记本中整理灵感。

**[下载最新 APK](https://github.com/leongao/stylus-android-releases/releases/latest)** · [安装与更新](INSTALL.md) · [更新记录](CHANGELOG.md) · [隐私说明](PRIVACY.md)

## 当前版本

**0.3.0 · build 11**。下载 Release 中的 **`Stylus-0.3.0-universal.apk`**，无需分包安装或额外素材下载。GitHub 自动生成的 Source code 压缩包是本仓库的文档，不是安装包。

- Android 10 或更高版本；面向平板和主动式手写笔优化。
- 同一个 APK 包含 arm64-v8a、armeabi-v7a、x86、x86_64。
- 开发与此前书写体验验证基于小米 Pad 7 Ultra + Xiaomi Focus Pen；其他设备的压感、倾角和系统手势支持可能不同。
- Android 13 及以上使用曲面玻璃效果，较早版本使用兼容效果。Android 10–12 的本次正式包尚未完成设备验证。

## 可以做什么

- 多笔记本、多页面与 3D 封面；笔记在设备本地保存。
- 钢笔、水笔、铅笔和两种马克笔，支持笔宽、颜色和透明度调整。
- 钢笔默认透明度 60%，水笔 70%；铅笔支持压感、纹理和倾斜侧锋。
- 局部 / 整笔橡皮、套索、撤销与重做，以及画布缩放和平移。
- 拖拽调整笔盒中的画笔和自定义颜色顺序；色板横向分页，笔盒内直接调 HSL。
- 添加图片，移动、等比缩放、删除与撤销；导入后保存在应用内。
- 沉浸书写、自适应胶囊控件，以及折射、色散可调的曲面玻璃面板。
- 玻璃上方的文字与图标随背景明暗调整，提升对比度。
- 通过系统文件选择器导出 PNG。

## 开始使用

1. 安装 APK 后打开 **Stylus**，在书库中新建笔记本。
2. 点笔记本进入页面，用手写笔书写；双指移动或缩放纸面。
3. 点画笔选择工具，再点当前画笔调整设置；在色盘上直接选色，下方滑条调明度。
4. 点笔盒的添加图片按钮选择图片；置入后用选择工具移动，拖动右下角等比缩放。
5. 在页面菜单中导出 PNG。PNG 是图片，不是可继续编辑的笔记本备份。

## 数据与更新

正式版包名为 `com.leon.still`。它与 **Checks / Stylus Checks** (`com.leon.still.validation`) 独立安装，数据互不迁移，安装本 APK 不会删除 Checks 中的笔记。

后续正式版使用同一专用发布签名，可以覆盖更新并保留应用数据。若系统提示与已有应用的签名冲突，请先阅读 [安装说明](INSTALL.md)，不要为了安装而删除有笔记的旧应用。

当前没有云同步或整本可编辑笔记的导入 / 导出入口。卸载或清除应用数据会删除本地笔记；系统自动备份也已关闭。

## 反馈

请在 [Issues](https://github.com/leongao/stylus-android-releases/issues) 提供应用版本、设备、Android / HyperOS 版本及复现步骤。截图或录屏请先遮挡私人笔记。

本仓库用于分发 APK、版本记录与使用文档；应用源代码未在此发布。第三方组件及其许可证见 [licenses](licenses/THIRD_PARTY_NOTICES.md)。
