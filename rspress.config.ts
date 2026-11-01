import * as path from 'node:path';
import { defineConfig } from '@rspress/core';
import { pluginLlms } from '@rspress/plugin-llms';
import sidebar from './sidebar.json';

export default defineConfig({
  root: path.join(__dirname, 'docs'),
  base: '/miaoshou-api-docs/',
  lang: 'zh',
  llms: false,
  plugins: [pluginLlms()],
  title: '妙手开放平台 API 文档',
  icon: '/rspress-icon.png',
  themeConfig: {
    llmsUI: true,
    nav: [
      { text: '快速接入', link: '/quick-start' },
      { text: '商品', link: '/product/' },
      { text: 'SHEIN', link: '/shein' },
    ],
    sidebar: { '/': sidebar as any },
    socialLinks: [{ icon: 'github', mode: 'link', content: 'https://github.com/MeesuMaes/miaoshou-api-docs' }],
  },
});
