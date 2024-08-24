---
abbrlink: 5a8a6c8d
ai:
- 本教程介绍了如何在博客中安装基于Hexo主题的安知鱼主题，并提供了安装、应用主题、修改配置文件、本地启动等详细步骤及技术支持方式。教程的内容针对最新的主题版本进行更新，如果你是旧版本教程会有出入。
categories: []
cover: https://pic.chino.my.to/i/2024/08/23/460580.webp
date: '2024-07-31T11:25:00+08:00'
tags:
- api
title: API文档
updated: '2024-08-23T09:45:36.982+08:00'
---

# 1.前言

本文是对于[luohAPI](https://api.luoh.my.to/New)的文档介绍，便于更方便的使用

---

# 2.介绍

## 2.1 InfoHub

### 2.1.1 HistoryToday

{% folding blue open, 历史上的今天 %}
**接口地址**  <span id="HistoryToday" onclick="CopyApiLink()"><code class="API">`https://api.luoh.my.to/New/InfoHub/HistoryToday/`</code></span>
**请求方法** `GET` <br>
**请求参数说明**

| 名称 | 必填 | 类型 | 说明 |
| :-: | :-: | :-: | :-: |
| date | 否 | string | `{month}{day}` <br> 例如 `1010` 及表示 `十月十日`的历史 <br> `0101` 即表示 `一月一日` 的历史 <br> 不填写时默认为今日日期 |

<br>

**返回示例**

```json
{
    "year": "1731",
    "title": "英国化学家和物理学家 卡文迪许 出生",
    "festival": "辛亥革命纪念日",
    "type": "诞生",
    "desc": "卡文迪许是英国化学家和物理学家。他出生贵族，继承了叔伯和父亲的遗产后成为英国巨富之一。但他生活简朴，全心投身于科学研究，在物理化学领域获得了杰出成就，硝酸就是他发现的。",
    "cover": true,
    "recommed": true,
    "pic_caledar": "http://baike.bdimg.com/cms/rc/r/image/2014-08-31/c83fa196d6f0d95fbd1292d0ecd11e22_80_80.jpg",
    "pic_share": "http://baike.bdimg.com/cms/rc/r/image/2014-08-31/a04b2298b06e097a216d053b888c10fe_360_212.jpg",
    "pic_idex": "http://baike.bdimg.com/cms/rc/r/image/2014-08-31/23c0660eb476f5e8ac614f9dea4a048c_134_100.jpg",
    "baike": "http://baike.baidu.com/subview/19638/14698117.htm"
}
```

<br>

**返回参数说明**

| 名称 | 类型 | 说明 |
| :-: | :-: | :-: |
| year | string | 年份 |
| title | string | 该历史精简概括 |
| festival | string | 节日 |
| type | string | 历史类型 |
| desc | string | 详细介绍 |
| cover | boolean | 是否有图片 |
| recommed | boolean | 是否推荐 |
| baike | string | 百科链接 |

<br>

**请求示例** 
<br> <span id="HistoryToday" onclick="CopyApiLink()"><code class="API">`https://api.luoh.my.to/New/InfoHub/HistoryToday/`</code></span>

 {% endfolding %}


### 2.1.2 Horoscope

{% folding blue open, 星座运势 %}
**接口地址**  <span id="Horoscope" onclick="CopyApiLink()"><code class="API">`https://api.luoh.my.to/New/InfoHub/Horoscope/`</code></span>
**请求方法** `GET` <br>
**请求参数说明**

| 名称 | 必填 | 类型 | 说明 |
| :-: | :-: | :-: | :-: |
| msg | 是 | string | 需要查询的星座 <br> 例如 `白羊` `双子座` <br>` 座` 可加可不加 |

<br>

**返回示例**

```json
{
  "status": 200,
  "data": {
    "星座": "白羊",
    "贵人方位": "东北方向",
    "贵人星座": "金牛座",
    "幸运数字": "0",
    "幸运颜色": "猪肝紫",
    "爱情运势": "容易结识谈天说地的异性朋友，有时也会向你诉苦，这让你有种被需要的快乐感。",
    "财富运势": "花钱如流水，不懂得节省。\\n",
    "事业运势": "善用你良好的人际关系，将会让今天要处理的事情更为顺利，也有机会结识兴趣相投的伙伴。",
    "整体运势": "感性的一面突显，非常在意另一半的一言一行，有不合意会引起你的不悦，学会收敛情绪，小心爱情悄悄远离。花钱欲望强烈，支出较多，甚至会买回一堆无用的东西，造成浪费。",
    "提示": "发展态势良好，生活中会小有惊喜。"
  }
}
```

<br>

**返回参数说明**

| 名称 | 类型 | 说明 |
| :-: | :-: | :-: |
| status | int | 状态码 |
| data | object | 该星座运势详细内容 |

*其余不作解释*

<br>

**请求示例**
<span id="Horoscope" onclick="CopyApiLink()"><code class="API">`https://api.luoh.my.to/New/InfoHub/Horoscope/?msg=白羊`</code></span>

 {% endfolding %}


## 2.2 PicLibrary

### 2.2.1 AnimeImage

{% folding blue open, 动漫趋向图片 %}
**接口地址**  <span id="AnimeImage" onclick="CopyApiLink()"><code class="API">`https://api.luoh.my.to/New/PicLibrary/AnimeImage/`</code></span>
**请求方法** `GET` <br>
**请求参数说明**

| 名称 | 必填 | 类型 | 说明 |
| :-: | :-: | :-: | :-: |
| t | 是 | string | 获取哪一类的图片 <br> 详情查看 [此处](#) |
| r | 否 | string | 返回格式 <br> 可选择 `json` `images` <br> 默认为 `image` |

<br>

**返回示例**

```json
{
  "status": "200",
  "url": "https://new-api-2.pages.dev/image/ecy/anime/first/85a1dd13bc908d1c.webp"
}
```

<br>

**返回参数说明**

| 名称 | 类型 | 说明 |
| :-: | :-: | :-: |
| status | int | 状态码 |
| url | string | 图片链接 |

<br>

**请求示例**
<span id="AnimeImage" onclick="CopyApiLink()"><code class="API">`https://api.luoh.my.to/New/PicLibrary/AnimeImage/?t=anime/first&r=image`</code></span>
![AnimeImage](https://api.luoh.my.to/New/PicLibrary/AnimeImage/?t=anime/first&r=image)

 {% endfolding %}


### 2.2.2 Emoticon

{% folding blue open, 动漫趋向图片 %}
**接口地址**  <span id="Emoticon" onclick="CopyApiLink()"><code class="API">`https://api.luoh.my.to/New/PicLibrary/Emoticon/`</code></span>
**请求方法** `GET` <br>
**请求参数说明**

| 名称 | 必填 | 类型 | 说明 |
| :-: | :-: | :-: | :-: |
| t | 是 | string | 获取哪一类的图片 <br> 详情查看 [此处](#) |
| r | 否 | string | 返回格式 <br> 可选择 `json` `images` <br> 默认为 `image` |

<br>

**返回示例**

```json
{
  "status": "200",
  "url": "https://new-api-1.pages.dev/image/emoticon/capoo/cc9ee90088ddab18.png"
}
```

<br>

**返回参数说明**

| 名称 | 类型 | 说明 |
| :-: | :-: | :-: |
| status | int | 状态码 |
| url | string | 图片链接 |

<br>

**请求示例**
<span id="Emoticon" onclick="CopyApiLink()"><code class="API">`https://api.luoh.my.to/New/PicLibrary/Emoticon/?t=capoo&r=image`</code></span>
![Emoticon](https://api.luoh.my.to/New/PicLibrary/Emoticon/?t=capoo&r=image)

 {% endfolding %}


### 2.2.3 Other

{% folding blue open, 未做分类的图片 %}
**接口地址**  <span id="Other" onclick="CopyApiLink()"><code class="API">`https://api.luoh.my.to/New/PicLibrary/Other/`</code></span>
**请求方法** `GET` <br>
**请求参数说明**

| 名称 | 必填 | 类型 | 说明 |
| :-: | :-: | :-: | :-: |
| r | 否 | string | 返回格式 <br> 可选择 `json` `images` <br> 默认为 `image` |

<br>

**返回示例**

```json
{
  "status": 200,
  "url": "https://new-api-1.pages.dev/image/other/dbd3e84f51b4da63.webp"
}
```

<br>

**返回参数说明**

| 名称 | 类型 | 说明 |
| :-: | :-: | :-: |
| status | int | 状态码 |
| url | string | 图片链接 |

<br>

**请求示例**
<span id="Other" onclick="CopyApiLink()"><code class="API">`https://api.luoh.my.to/New/PicLibrary/Other/?r=image`</code></span>
![Other](https://api.luoh.my.to/New/PicLibrary/Other/?r=image)

 {% endfolding %}


### 2.2.4 RealImage

{% folding blue open, 现实趋向图片 %}
**接口地址**  <span id="RealImage" onclick="CopyApiLink()"><code class="API">`https://api.luoh.my.to/New/PicLibrary/RealImage/`</code></span>
**请求方法** `GET` <br>
**请求参数说明**

| 名称 | 必填 | 类型 | 说明 |
| :-: | :-: | :-: | :-: |
| t | 是 | string | 获取哪一类的图片 <br> 详情查看 [此处](#) |
| r | 否 | string | 返回格式 <br> 可选择 `json` `images` <br> 默认为 `image` |

<br>

**返回示例**

```json
{
  "status": "200",
  "url": "https://new-api-1.pages.dev/image/scy/cat/da8a76f0fa575444.png"
}
```

<br>

**返回参数说明**

| 名称 | 类型 | 说明 |
| :-: | :-: | :-: |
| status | int | 状态码 |
| url | string | 图片链接 |

<br>

**请求示例**
<span id="RealImage" onclick="CopyApiLink()"><code class="API">`https://api.luoh.my.to/New/PicLibrary/RealImage/?t=cat&r=image`</code></span>
![RealImage](https://api.luoh.my.to/New/PicLibrary/RealImage/?t=cat&r=image)

 {% endfolding %}


## 2.3 RiLitools

### 2.3.1 DateImage

{% folding blue open, 每日一签图片 %}
**接口地址**  <span id="DateImage" onclick="CopyApiLink()"><code class="API">`https://api.luoh.my.to/New/RiliTools/DateImage/`</code></span>
**请求方法** `GET` <br>

<br>

**请求示例**
<span id="DateImage" onclick="CopyApiLink()"><code class="API">`https://api.luoh.my.to/New/RiliTools/DateImage/`</code></span>
![DateImage](https://api.luoh.my.to/New/RiliTools/DateImage/)

 {% endfolding %}


### 2.3.2 DateInfo

{% folding blue open, 每日日期信息 %}
**接口地址**  <span id="DateInfo" onclick="CopyApiLink()"><code class="API">`https://api.luoh.my.to/New/RiliTools/DateInfo/`</code></span>
**请求方法** `GET` <br>
**请求参数说明**

| 名称 | 必填 | 类型 | 说明 |
| :-: | :-: | :-: | :-: |
| date | 否 | string | `Y-m-d` <br> 例如 `2024-08-24` |
<br>

**返回示例**

```json
{
    "date": "2024年08月24日",
    "dateD": "24",
    "dateM": "08",
    "dateMC": "8",
    "dateY": "2024",
    "week": "星期六",
    "lunardate": "2024年07月21日",
    "hseb": "甲辰年 壬申月 庚申日",
    "text": "野店垂杨步，荒祠苦竹丛。"
}
```

<br>

**返回参数说明**

| 名称 | 类型 | 说明 |
| :-: | :-: | :-: |
| date | string | 阳历日期 |
| dateD | int | 阳历日期-日 |
| dateM | int | 阳历日期-月 |
| dateY | int | 阳历日期-年 |
| week | string | 星期 |
| lunardate | string | 天支地干型日期 |
| text | string | 随机诗词 |

<br>

**请求示例**
<span id="DateInfo" onclick="CopyApiLink()"><code class="API">`https://api.luoh.my.to/New/RiliTools/DateInfo/`</code></span>

 {% endfolding %}


### 2.3.2 GetTime

{% folding blue open, 时区时间 %}
**接口地址**  <span id="GetTime" onclick="CopyApiLink()"><code class="API">`https://api.luoh.my.to/New/RiliTools/GetTime/`</code></span>
**请求方法** `GET` <br>
**请求参数说明**

| 名称 | 必填 | 类型 | 说明 |
| :-: | :-: | :-: | :-: |
| timezone | 否 | string | `时区` <br> 例如 `America/New_York` <br> 默认为 `Asia/Shanghai` <br> 时区总汇可查看[此处](https://www.php.net/manual/zh/timezones.php) <br> 不可识别 UTC类型 |

<br>

**返回示例**

```json
{
  "date": "2024-08-24",
  "year": "2024",
  "month": "08",
  "day": "24",
  "hour": "11",
  "minute": "07",
  "second": "20",
  "timezone": "Asia/Shanghai",
  "timestamp": 1724468840
}
```

<br>

**返回参数说明**

| 名称 | 类型 | 说明 |
| :-: | :-: | :-: |
| date | string | 日期 |
| year | int | 年 |
| month | int | 月 |
| day | int | 日 |
| hour | string | 小时 |
| minute | string | 分钟 |
| second | string | 秒 |
| timezone | string | 当前时区 |
| timestamp| int | Unix 时间戳 |

<br>

**请求示例**
<span id="GetTime" onclick="CopyApiLink()"><code class="API">`https://api.luoh.my.to/New/RiliTools/GetTime/`</code></span>

 {% endfolding %}


## 2.4 ToolBox

### 2.4.1 GetIP

{% folding blue open, IP地址 %}
**接口地址**  <span id="GetIP" onclick="CopyApiLink()"><code class="API">`https://api.luoh.my.to/New/ToolBox/GetIP/`</code></span>
**请求方法** `GET` <br>

<br>

**返回示例**

```json
{
  "code": 200,
  "data": {
    "ip": "************",
    "city": "*********"
  }
}
```

<br>

**返回参数说明**

| 名称 | 类型 | 说明 |
| :-: | :-: | :-: |
| code | int | 状态码 |
| data | object | 数据 |
| ip | string | IP 地址 |
| city | string | 所在地 |

<br>

**请求示例**
<span id="GetIP" onclick="CopyApiLink()"><code class="API">`https://api.luoh.my.to/New/RiliTools/GetIP/`</code></span>

 {% endfolding %}

<script>
function CopyApiLink() {
    var element = event.target;
    var textarea = document.createElement('textarea');
    textarea.value = element.textContent;
    document.body.appendChild(textarea);
    textarea.select();
    document.execCommand('copy');0
    document.body.removeChild(textarea);
}
</script>
<style>
.API {
  display: block;
  white-space: nowrap;
  overflow-x: auto;
  -ms-overflow-style: none;
  scrollbar-width: none;
}
.API::-webkit-scrollbar {
  display: none;
}
</style>