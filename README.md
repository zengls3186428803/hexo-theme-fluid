- [all in one script for archlinux](#all-in-one-script-for-archlinux)
- [快速开始](#快速开始)
    - [搭建 Hexo 博客](#搭建-hexo-博客)
    - [获取主题最新版本](#获取主题最新版本)
    - [指定主题](#指定主题)
    - [latex 数学公式支持](#latex-数学公式支持)
    - [创建「关于页」](#创建关于页)
- [更新主题](#更新主题)
- [功能特性](#功能特性)

## all in one script for archlinux

**note** :如果想一步到位，请先确保已经在一个 python3 和 pip 的环境里。

```bash
set -e
hexo init blog
cd blog
npm install --save hexo-theme-fluid
wget https://raw.githubusercontent.com/zengls3186428803/hexo-theme-fluid/refs/heads/master/_config.yml -O _config.fluid.yml
pip install ruamel.yaml fire
wget https://raw.githubusercontent.com/zengls3186428803/hexo-theme-fluid/refs/heads/master/yaml_utils.py -O yaml_utils.py
python yaml_utils.py _config.yml theme "fluid"
python yaml_utils.py _config.yml language "zh-CN"
python yaml_utils.py _config.fluid.yml post.math.enable True
yay -S pandoc-cli --noconfirm
npm uninstall hexo-renderer-marked --save
npm install hexo-renderer-pandoc --save
```

## 快速开始

#### 搭建 Hexo 博客

如果你还没有 Hexo 博客，请按照 [Hexo 官方文档](https://hexo.io/zh-cn/docs/) 进行安装、建站。

#### 获取主题最新版本

**方式一：**

Hexo 5.0.0 版本以上，推荐通过 npm 直接安装，进入博客目录执行命令：

```bash
npm install --save hexo-theme-fluid
```

然后在博客目录下创建 `_config.fluid.yml`，将主题的 [\_config.yml](https://github.com/zengls3186428803/hexo-theme-fluid/blob/master/_config.yml) 内容复制进去。

```bash
wget https://github.com/zengls3186428803/hexo-theme-fluid/blob/master/_config.yml -O _config.fluid.yml
```

**方式二：**

下载 [最新 release 版本](https://github.com/fluid-dev/hexo-theme-fluid/releases) 解压到 themes 目录，并将解压出的文件夹重命名为 `fluid`。

#### 指定主题

如下修改 Hexo 博客目录中的 `_config.yml`：

```yaml
theme: fluid # 指定主题

language: zh-CN # 指定语言，会影响主题显示的语言，按需修改
```

#### [latex 数学公式支持](https://fluid-dev.github.io/hexo-fluid-docs/en/guide/#math)

If you want to use LaTeX (opens new window)math, you should finish follow steps:

1. theme config
   ```
   post:
    math:
      enable: true
      specific: false
      engine: mathjax
   ```
   if specific: true，you should add math: true into front-matter (opens new window), and then the typesetting will be display on post page, and it can improve the speed of page load.
2. Change Markdown engine

Because the default engine of hexo doesn't support math typesetting, it should be changed by other better engine.

engine: engine for typesetting, mathjax or katex is supported.

```bash
# mathjax
npm uninstall hexo-renderer-marked --save
npm install hexo-renderer-pandoc --save
```

使用 hexo-renderer-pandoc 这个引擎需要安装 pandoc 包

```bash
# archlinux
yay -S pandoc-cli
```

#### 创建「关于页」

首次使用主题的「关于页」需要手动创建：

```bash
hexo new page about
```

创建成功后，编辑博客目录下 `/source/about/index.md`，添加 `layout` 属性。

修改后的文件示例如下：

```yaml
---
title: about
layout: about
---
这里写关于页的正文，支持 Markdown, HTML
```

## 更新主题

更新主题的方式[参照这里](https://hexo.fluid-dev.com/docs/start/#更新主题)。

## 功能特性

- [x] 无比详实的[用户文档](https://hexo.fluid-dev.com/docs/)
- [x] 页面组件懒加载
- [x] 多种代码高亮方案
- [x] 多语言配置
- [x] 内置多款评论插件
- [x] 内置网页访问统计
- [x] 内置文章本地搜索
- [x] 支持暗色模式
- [x] 支持脚注语法
- [x] 支持 LaTeX 数学公式
- [x] 支持 mermaid 流程图
