![PF-team_name_handler](https://socialify.git.ci/XueK66/PF-team_name_handler/image?issues=1&language=1&name=1&stargazers=1&theme=Light)
# Team Name Handler for MCDReforged

[![仓库大小](https://img.shields.io/github/repo-size/XueK66/PF-team_name_handle?style=flat-square&label=仓库占用)](/)
[![最新版](https://img.shields.io/github/v/release/XueK66/PF-team_name_handle?style=flat-square&label=最新版)](https://github.com/XueK66/PF-team_name_handler/releases/latest)
[![总下载量](https://img.shields.io/github/downloads/XueK66/PF-team_name_handle/total?style=flat-square&label=下载量)](https://github.com/XueK66/PF-team_name_handler/releases)
[![最新发布下载量](https://img.shields.io/github/downloads/XueK66/PF-team_name_handle/latest/total?style=flat-square&label=最新版本下载量)](https://github.com/XueK66/PF-team_name_handler/releases/latest)

#### 插件简介
**Team Name Handler** 是一款为 MCDReforged (MCDR) 开发的信息处理器，用于正确解析带队伍名前缀的玩家名称。

#### 功能

- **多格式配置支持**: 支持多种日志格式解析，确保不同场景下都能正确提取队伍信息。

#### 安装与配置
1. **安装**: 将插件文件放入 MCDReforged 的 `plugins` 目录中，启动服务器。
2. **配置**: 插件会自动生成一个 `config.json` 配置文件。文件格式如下：
  - `skip_name_check`: 是否跳过玩家名称校验。如果设置为 `true`，插件将允许使用不符合规范的玩家名称（如特殊字符或格式），适用于部分特殊需求场景。
  - `regular_expression`: 用于解析日志中玩家名称和消息的正则表达式。可根据实际日志格式进行自定义修改。

```json
{
  "skip_name_check": false,
  "regular_expression": "<(?:\\[[^\\[\\]]+\\])?(?P<name>[^>\\[\\]]+)> (?P<message>.*)"
}
```

### 贡献
如果发现问题，或希望贡献代码，欢迎在 GitHub 提交 Issue 或 Pull Request。

- 技术支持: 雪开（[XueK66](https://github.com/XueK66)）
- 文档编写: 雪开（[XueK66](https://github.com/XueK66)）

---

#### 未来计划
- 暂无

欢迎提建议！
