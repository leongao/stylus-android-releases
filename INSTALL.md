# 安装与更新

## 首次安装

1. 打开 [最新 Release](https://github.com/leongao/stylus-android-releases/releases/latest)。
2. 下载 `Stylus-0.2.0-universal.apk`。不要选择 GitHub 自动生成的 Source code 压缩包。
3. 在 Android 上打开 APK。如系统要求，允许当前使用的浏览器或文件管理器安装此 APK。
4. 安装后打开 **Stylus**。无需登录；笔记保存在设备本地。

要求 Android 10（API 29）或更高版本。此 APK 已包含四种 CPU 架构和所需笔刷、封面、字体资源，无需另装 APK 分包。

## 更新与旧测试版

- 从本仓库安装的正式版，后续直接安装同一发布签名的新版本即可；不要先卸载。
- Checks / Stylus Checks 使用独立包名，原有数据保留，不会自动复制到正式版。
- 早期叫作 Stylus 的调试包可能也使用 `com.leon.still`，但签名不同。Android 会拒绝覆盖安装并提示冲突。这种情况不要卸载有笔记的旧应用；先保留原应用，并联系维护者讨论数据迁移。
- 不建议降级。新版本保存的数据可能无法被旧版本完整读取。
- 本版没有整本可编辑笔记的备份导出功能。PNG 导出只保存页面图像，不能替代可编辑笔记备份。清除数据 / 卸载会移除本地笔记。

## 下载校验

同一 Release 附带 `SHA256SUMS`。将它与 APK 放在同一目录后，可使用以下命令核对下载完整性：

```sh
# macOS
shasum -a 256 -c SHA256SUMS
# Linux
sha256sum -c SHA256SUMS
```

Windows PowerShell：

```powershell
Get-FileHash .\Stylus-0.2.0-universal.apk -Algorithm SHA256
```

将结果与 `SHA256SUMS` 对应行比较。校验和也包含 `build-info.json`；执行批量校验前请一并下载。

正式版签名证书 SHA-256：

```text
9d390abd726a7711bb1d5d31b69dc31c4377d47fc9128ca695fc9a1e696314be
```

开发者可以使用 Android SDK 的 `apksigner verify --verbose --print-certs` 检查 APK 签名。本仓库只发布证书指纹，不包含私钥或签名密码。
