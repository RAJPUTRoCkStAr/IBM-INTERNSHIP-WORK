# Chrome Extension Guide

This guide will walk you through the steps to create a basic Chrome Extension.

## Table of Contents

1. [Introduction](#introduction)
2. [Prerequisites](#prerequisites)
3. [Setting Up](#setting-up)
4. [Folder Structure](#Folder Structure)
5. [Manifest File](#manifest-file)
6. [Testing Your Extension](#testing-your-extension)
7. [Packaging Your Extension](#packaging-your-extension)
8. [Conclusion](#conclusion)

## Introduction

A Chrome extension is a small software program that customizes the browsing experience. It can add new features or modify the behavior of web pages. In this guide, you will learn how to create a simple Chrome extension.

## Prerequisites

Before you start, make sure you have:

- Basic knowledge of HTML, CSS, and JavaScript.
- A text editor (e.g., Visual Studio Code).
- Google Chrome installed.

## Setting Up

1. **Create a project folder**: Create a new folder on your computer where you will store all the files related to your extension.

2. **Create the following files inside the folder**:
   - `manifest.json`
   - `background.js`
   - `content.js`
   - `popup.html`
   - `popup.js`
   - `styles.css`

## Folder Structure
Your project folder should look like this:
```plaintext
chrome-extension/
│
├── icons/
│   ├── icon16.png
│   ├── icon48.png
│   └── icon128.png
│
├── background.js
├── content.js
├── manifest.json
├── popup.html
├── popup.js
├── styles.css
└── README.md
```
## Manifest File

The `manifest.json` file is the blueprint of your Chrome extension. It tells Chrome what your extension does, and what files it needs to run.

```json
{
  "manifest_version": 3,
  "name": "My Chrome Extension",
  "version": "1.0",
  "description": "A simple Chrome extension",
  "action": {
    "default_popup": "popup.html",
    "default_icon": {
      "16": "icons/icon16.png",
      "48": "icons/icon48.png",
      "128": "icons/icon128.png"
    }
  },
  "background": {
    "service_worker": "background.js"
  },
  "content_scripts": [
    {
      "matches": ["<all_urls>"],
      "js": ["content.js"]
    }
  ],
  "permissions": ["activeTab"]
}
```
## Testing Your Extension
** Open Chrome and go to chrome://extensions/.
** Enable Developer mode by toggling the switch in the top right corner.
** Click "Load unpacked" and select your project folder.
** Your extension should now be loaded. Click on the extension icon to see your popup.
## Packaging Your Extension
* Go to chrome://extensions/.
* Make sure Developer mode is enabled.
* Click "Pack extension".
* Select your extension’s folder and click "Pack Extension".
* A .crx file will be created, which you can distribute.
## Conclusion
You have successfully created a basic Chrome extension! From here, you can expand your extension by adding more features, using Chrome's APIs, and customizing the UI.