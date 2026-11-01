import * as path from 'node:path';
import { defineConfig } from '@rspress/core';
import sidebar from './sidebar.json';

export default defineConfig({
  root: path.join(__dirname, 'docs'),
  base: '/miaoshou-api-docs/',
  lang: 'zh',
  title: '妙手开放平台 API 文档',
  icon: '/rspress-icon.png',
  themeConfig: {
    nav: [
      { text: '总览', link: '/overview' },
      { text: '商品', link: '/product/' },
      { text: 'SHEIN', link: '/shein' },
    ],
    sidebar: { '/': sidebar as any },
    socialLinks: [{ icon: 'github', mode: 'link', content: 'https://github.com/MeesuMaes/miaoshou-api-docs' }],
  },
});
