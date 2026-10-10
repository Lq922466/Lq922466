const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');
const assert = require('assert');
const root = path.resolve(__dirname, '../docs');
const pages = fs.readdirSync(root).filter(x => ['zh','en','es'].includes(x)).flatMap(lang => [
  ...fs.readdirSync(path.join(root,lang)).filter(x=>x.endsWith('.html')).map(x=>`${lang}/${x}`),
  ...fs.readdirSync(path.join(root,lang,'projects')).map(x=>`${lang}/projects/${x}`)
]);
(async()=>{
  const browser = await chromium.launch({headless:true,channel:'msedge'});
  let checks = 0;
  for (const width of [360,390,768,1440]) {
    const context = await browser.newContext({viewport:{width,height:1000}});
    const page = await context.newPage();
    for (const url of pages) {
      const errors=[];
      const handler = e=>errors.push(e.message);
      page.on('pageerror',handler);
      const response = await page.goto('http://127.0.0.1:8765/'+url);
      assert.equal(response.status(),200,url);
      await page.evaluate(()=>document.fonts.ready);
      const result = await page.evaluate(()=>({
        overflow:document.documentElement.scrollWidth>innerWidth,
        h1:document.querySelectorAll('h1').length,
        main:!!document.querySelector('main#main'),
        broken:[...document.querySelectorAll('a[href],link[href],script[src],img[src]')].map(el=>el.href||el.src).filter(url=>url.startsWith(location.origin)).map(url=>new URL(url).pathname),
        alts:[...document.images].every(img=>img.hasAttribute('alt')),
        lang:document.documentElement.lang
      }));
      assert(!result.overflow,`Overflow ${width} ${url}`);
      assert.equal(result.h1,1,url);
      assert(result.main&&result.alts,url);
      assert(!errors.length,errors.join(';'));
      for(const pathname of result.broken) assert(fs.existsSync(path.join(root,decodeURIComponent(pathname))),`Broken ${pathname}`);
      // Switch language and preserve the same category or project.
      const target = url.replace(/^(zh|en|es)/,url.startsWith('en')?'es':'en');
      const href = await page.locator('.languages a').filter({hasText:url.startsWith('en')?'ES':'EN'}).getAttribute('href');
      assert.equal(new URL(href,page.url()).pathname,'/'+target);
      page.removeListener('pageerror',handler);
      checks++;
    }
    await page.goto('http://127.0.0.1:8765/en/index.html');
    assert.equal(await page.locator('.category-grid').evaluate(el=>getComputedStyle(el).gridTemplateColumns.split(' ').length),width<=760?1:2);
    await page.locator('#theme').selectOption('dark');
    assert.equal(await page.locator('html').getAttribute('data-theme'),'dark');
    await page.screenshot({path:path.join(__dirname,`../../innnx-${width}-dark.png`),fullPage:true});
    await page.locator('#theme').selectOption('light');
    await page.reload();
    assert.equal(await page.locator('html').getAttribute('data-theme'),'light');
    await page.screenshot({path:path.join(__dirname,`../../innnx-${width}-light.png`),fullPage:true});
    await page.keyboard.press('Tab');
    assert.equal(await page.evaluate(()=>document.activeElement.className),'skip');
    await context.close();
  }
  const context=await browser.newContext({javaScriptEnabled:false});
  const page=await context.newPage();
  await page.goto('http://127.0.0.1:8765/zh/projects/esp32-companion-v1.html');
  assert.equal(await page.locator('a[href="https://xhslink.cn/m/5y0F9KIVkvd"]').count(),1);
  await page.goto('http://127.0.0.1:8765/');
  assert.equal(await page.locator('.languages a').count(),3);
  await browser.close();
  console.log(`PASS: ${checks} page/viewport combinations; internal links, language continuity, headings, alt attributes, theme persistence, keyboard skip link, no-JS navigation.`);
})().catch(e=>{console.error(e);process.exit(1)});
