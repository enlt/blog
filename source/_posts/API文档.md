---
title: API文档
cover: 'https://i1.wp.com/new-api-2.pages.dev/image/ecy/wallpaper/db59776fed7be1c5.webp'
tags: api
abbrlink: 5a8a6c8d
date: 2024-07-31 11:25:00
---

# 前言
本文是对于[luohAPI](https://api.luoh.my.to/)的文档介绍，便于更方便的使用

---

# 介绍

---

## 图片类

### 动漫图
{% folding blue, 获取随机的动漫类图片 %}
**接口地址**  <span id="animePHP" onclick="CopyApiLink()">`https://api.luoh.my.to/anime.php`</span> <br>
**请求方法** `GET` <br>
**返回格式** `image` `json` <br>
**请求参数说明**
| 名称 | 必填 | 类型 | 说明 |
|:-------:|:-------:|:-------:|:-------:|
| type | 是 | string | 需要获取的图片类型 可选为: <br> `first` `second` `third` `genshin` `mobile` <br> 其中后二者为 <br> `原神类` `手机尺寸类` |
| return | 否 | string | 指定返回类型，可选为: <br> `image` `json` | 

<br>

**返回示例**
```json
直接返回图片
----------
{ "status": "200", "imageurl": "https://i1.wp.com/new-api-2.pages.dev/image/ecy/anime/first/7d7494e0413c29f5.webp" }
```
<br>

**返回参数说明**
| 名称 | 类型 |  | 说明 |
|:-------:|:-------:|:-------:|:-------:|
| status | string | 状态码 |
| imageurl | string | 图片链接 或 错误信息 | 

<br>

**请求示例** <span id="animePHPE" onclick="CopyApiLink()">`https://api.luoh.my.to/anime.php?type=first&return=image`</span> <br>
![anime.webp](https://api.luoh.my.to/anime.php?type=first&return=image)

 {% endfolding %}

---


### 头像
{% folding cyan, 获取随机的头像类图片 %}
**接口地址**  <span id="avatarPHP" onclick="CopyApiLink()">`https://api.luoh.my.to/avatar.php`</span> <br>
**请求方法** `GET` <br>
**返回格式** `image` `json` <br>
**请求参数说明**
| 名称 | 必填 | 类型 | 说明 |
|:-------:|:-------:|:-------:|:-------:|
| type | 是 | string | 需要获取的图片类型 可选为: <br> `dm` `gf` `kt` `ka` `random` <br> 其分别对应 <br> `动漫` `古风` `卡通` `可爱` `随机` |
| return | 否 | string | 指定返回类型，可选为: <br> `image` `json` | 

<br>

**返回示例**
```json
直接返回图片
----------
{ "status": "200", "imageurl": "https://i1.wp.com/new-api-2.pages.dev/二次元/avatar/dongman/90d635bd248701e4.webp" }
```
<br>

**返回参数说明**
| 名称 | 类型 |  | 说明 |
|:-------:|:-------:|:-------:|:-------:|
| status | 是 | string | 状态码 |
| imageurl | 是 | string | 图片链接 | 

<br>

**请求示例** <span id="avatarPHPE" onclick="CopyApiLink()">`https://api.luoh.my.to/avatar.php?type=dm&return=image`</span> <br>
![avatar.webp](https://api.luoh.my.to/avatar.php?type=dm&return=image)

 {% endfolding %}

---


### 三次元
{% folding green, 获取随机的三次元类图片 %}
**接口地址**  <span id="scyPHP" onclick="CopyApiLink()">`https://api.luoh.my.to/scy.php`</span> <br>
**请求方法** `GET` <br>
**返回格式** `image` `json` <br>
**请求参数说明**
| 名称 | 必填 | 类型 | 说明 |
|:-------:|:-------:|:-------:|:-------:|
| type | 是 | string | 需要获取的图片类型 可选为 <br> `cat` `fj` <br> 其分别为 <br> `猫` `风景`
| return | 否 | string | 指定返回类型，可选为: <br> `image` `json` | 

<br>

**返回示例**
```json
直接返回图片
----------
{ "status": 200, "imageurl": "https://i1.wp.com/new-api-1.pages.dev/image/三次元/cat/ea78b37bce6ac049.png" }
```
<br>

**返回参数说明**
| 名称 | 类型 |  | 说明 |
|:-------:|:-------:|:-------:|:-------:|
| status | 是 | string | 状态码 |
| imageurl | 是 | string | 图片链接 | 

<br>

**请求示例** <span id="scyPHPE" onclick="CopyApiLink()">`https://api.luoh.my.to/scy.php?type=cat&return=image`</span> <br>
![cat.webp](https://api.luoh.my.to/scy.php?type=cat&return=image)

 {% endfolding %}

---


### 表情包
{% folding yellow, 获取随机的表情包类图片 %}
**接口地址**  <span id="emoticonPHP" onclick="CopyApiLink()">`https://api.luoh.my.to/emoticon.php`</span> <br>
**请求方法** `GET` <br>
**返回格式** `image` `json` <br>
**请求参数说明**
| 名称 | 必填 | 类型 | 说明 |
|:-------:|:-------:|:-------:|:-------:|
| type | 是 | string | 需要获取的图片类型 可选为：<br> `scymm` `ecybqb` `sej` `sxly` `sxlyhb` `cjm` `hj` `xmt` `mmckb` `gcmm` `lx` `lt` <br> 其分别为 <br> `三次元猫猫` `二次元表情包` `兽耳酱` `塞西莉娅` `塞西莉娅黑白` `柴郡猫` `滑稽` `熊猫头` `猫猫虫咖波` `甘城猫猫` `罗翔` `龙图` |
| return | 是 | string | 指定返回类型，可选为: <br> `image` `json` | 

<br>

**返回示例**
```json
直接返回图片
----------
{ "status": "200", "imageurl": "https://i1.wp.com/new-api-1.pages.dev/image/bqb/cjm/12ab959dfb54797b.png" }
```
<br>

**返回参数说明**
| 名称 | 类型 |  | 说明 |
|:-------:|:-------:|:-------:|:-------:|
| status | 是 | string | 状态码 |
| imageurl | 是 | string | 图片链接 | 

<br>

**请求示例** <span id="emoticonPHPE" onclick="CopyApiLink()">`https://api.luoh.my.to/emoticon.php?type=cjm&return=image`</span> <br>
![emoticon.webp](https://api.luoh.my.to/emoticon.php?type=cjm&return=image)

 {% endfolding %}

<script>
function CopyApiLink() {
    var element = event.target;
    var textarea = document.createElement('textarea');
    textarea.value = element.textContent;
    document.body.appendChild(textarea);
    textarea.select();
    document.execCommand('copy');
    document.body.removeChild(textarea);
}
</script>