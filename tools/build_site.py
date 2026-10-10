"""Build the INNNX. portfolio. Only public, reviewed material belongs here."""
from pathlib import Path
import html, re, json

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'docs'
OUT.mkdir(exist_ok=True)
G = 'https://github.com/Lq922466/'
L = ['zh', 'en', 'es']
def t(zh, en, es): return dict(zip(L, [zh, en, es]))
def esc(s): return html.escape(s, quote=True)

ui = {
 'home': t('首页','Home','Inicio'), 'tag': t('把随机想法变成真实作品。','Making Stuff Just Because.','Convertir ideas en cosas reales.'),
 'intro': t('嗨，我是 INNNX。探索代码、游戏、机器人与安全，一次实现一个想法。','Hey! I’m INNNX. Exploring code, games, robots and security, one idea at a time.','¡Hola! Soy INNNX. Exploro código, juegos, robots y seguridad, una idea a la vez.'),
 'made': t('已制作，或正在制作','Things I’ve made (or am making)','Lo que he creado (o estoy creando)'),
 'theme': t('外观','Theme','Apariencia'), 'system': t('跟随系统','System','Sistema'), 'light': t('浅色','Light','Claro'), 'dark': t('深色','Dark','Oscuro'),
 'skip': t('跳到正文','Skip to content','Saltar al contenido'), 'detail': t('查看项目','Explore project','Ver proyecto'),
 'docs': t('原始分类文档','Original category document','Documento original de categoría'),
 'repo': t('公开仓库','Public repository','Repositorio público'), 'evidence': t('资料与证据','Documentation & evidence','Documentación y pruebas'),
 'scope': t('当前范围与限制','Current scope & limitations','Alcance actual y límites'),
 'roadmap': t('未来计划','Future plans','Planes futuros'), 'footer': t('仍在不断尝试。公开资料是项目状态的依据。','Currently experimenting with everything. Public documentation grounds every project status.','Sigo experimentando con todo. La documentación pública sustenta el estado de cada proyecto.'),
 'back': t('返回分类','Back to category','Volver a la categoría'), 'updated': t('资料核对：2026-10-10','Sources checked: 2026-10-10','Fuentes revisadas: 2026-10-10'),
 'planned': t('计划中 · 尚未实现','Planned · not implemented','Planificado · sin implementar'),
 'languages': t('语言','Language','Idioma'), 'source': t('网站源码','Website source','Código del sitio')
}
cats = {
 'featured': {'title':t('精选','Featured','Destacados'), 'sub':t('更大的想法','The big ideas','Las grandes ideas'), 'desc':t('原有精选文档尚未选定项目。这里保留这个状态，你可以从其他分类了解已有作品。','The original featured document has no selected projects yet. This status is preserved; explore the other categories for documented work.','El documento original aún no tiene proyectos seleccionados. Se conserva ese estado; explora las otras categorías para conocer el trabajo documentado.')},
 'infra-security': {'title':t('基础设施与安全','Infra & Security','Infraestructura y seguridad'), 'sub':t('技术实验','The technical stuff','Los experimentos técnicos'), 'desc':t('系统管理、基础设施与安全实验。已完成的实验与未来计划分开呈现。','Systems administration, infrastructure and security labs. Completed lab work is separated from future plans.','Laboratorios de administración, infraestructura y seguridad. El trabajo completado se distingue de los planes futuros.')},
 'games': {'title':t('游戏','Games','Juegos'), 'sub':t('有趣的作品','The fun stuff','Las cosas divertidas'), 'desc':t('Flutter / Dart 游戏。公开仓库提供介绍与真实界面；游戏源码保持私有。','Flutter / Dart games. Public repositories share presentations and real interfaces; game source code remains private.','Juegos en Flutter / Dart. Los repositorios públicos ofrecen presentaciones e interfaces reales; el código de los juegos permanece privado.')},
 'robots-iot': {'title':t('机器人与物联网','Robots & IoT','Robots e IoT'), 'sub':t('小小的发明','The little inventions','Los pequeños inventos'), 'desc':t('从 OLED 表情显示代码开始的硬件探索。V1 是受启发原型，V2/V3 是未来独立开发计划。','Hardware exploration starting with OLED facial-display code. V1 is an inspired prototype; V2/V3 are future independent development plans.','Exploración de hardware a partir del código de expresión OLED. V1 es un prototipo inspirado; V2/V3 son planes de desarrollo independiente.')}
}
projects = {
 'linux-server-hardening': {
  'cat':'infra-security', 'title':t('Linux 服务器加固','Linux Server Hardening','Refuerzo de servidor Linux'), 'status':t('已完成 · 文档所述实验范围','Completed · documented lab scope','Completado · alcance del laboratorio documentado'),
  'tech':'Ubuntu Server / VirtualBox / OpenSSH / UFW / Fail2ban',
  'summary':t('在虚拟 Ubuntu 服务器上完成 SSH 密钥认证、UFW 防火墙和 Fail2ban 手动封禁集成实验。','A virtual Ubuntu server lab covering SSH key authentication, UFW firewall rules and manual Fail2ban integration.','Un laboratorio de Ubuntu virtual con autenticación SSH por claves, reglas UFW e integración manual de Fail2ban.'),
  'body':t('创建 sudo 管理员，配置 Ed25519 登录，禁用 root 与密码登录，并检查有效 SSH 设置。UFW 使用默认拒绝入站、允许出站规则，保留 SSH 访问。手动封禁与解封验证了 Fail2ban 到 UFW 的集成。','Created a sudo administrator, configured Ed25519 access, disabled root and password login, and checked effective SSH settings. UFW denies incoming traffic by default while allowing outgoing traffic and SSH. Manual ban/unban verified Fail2ban-to-UFW integration.','Se creó un administrador sudo, se configuró Ed25519, se desactivaron el acceso root y las contraseñas y se comprobó la configuración SSH efectiva. UFW rechaza entradas por defecto y permite salidas y SSH. El bloqueo y desbloqueo manual verificaron la integración Fail2ban–UFW.'),
  'limit':t('未直接测试自动检测登录失败。报告发现待安装更新，未证明全部更新已安装。“已完成”仅指记录的实验范围。','Automatic failed-login detection was not directly tested. Pending updates were identified; the report does not establish that all were installed. “Completed” refers only to the recorded lab scope.','No se probó directamente la detección automática de accesos fallidos. Se identificaron actualizaciones pendientes sin demostrar su instalación completa. “Completado” se refiere al alcance registrado.'),
  'image':'screenshots/ufw-final-status.png', 'caption':t('仓库中已有的 UFW 最终状态截图。','Existing repository screenshot of final UFW status.','Captura existente del estado final de UFW.'),
  'doc': {'zh':'README.md','en':'README.md','es':'README.es.md'}
 },
 'party-games': {
  'cat':'games', 'title':t('PASS / Party Games','PASS / Party Games','PASS / Party Games'), 'status':t('开发中 · Android 预发布试玩版','In development · Android pre-release demo','En desarrollo · demo preliminar Android'), 'tech':'Flutter / Dart / Android',
  'summary':t('一部手机，大家一起玩。集合提问、挑战、随机玩家选择与倒计时回答的聚会游戏。','One phone. Everyone plays. A collection of questions, challenges, random player selection and timed answers.','Un teléfono. Todos juegan. Una colección de preguntas, retos, selección aleatoria de jugadores y respuestas cronometradas.'),
  'body':t('九个入口包括真心话大冒险、数字炸弹、谁最可能、我从来没有、五秒挑战、生日派对、真心话、大冒险与混合模式。应用提供中英西三语界面；核心题目可离线使用。','Nine entries include Truth or Dare, Number Bomb, Most Likely To, Never Have I Ever, 5 Second Challenge, Birthday Party, Truth, Dare and Mix Mode. The app has Chinese, English and Spanish interfaces; core prompts work offline.','Las nueve entradas incluyen Verdad o reto, Bomba numérica, Quién es más probable, Yo nunca, Reto de 5 segundos, Fiesta de cumpleaños, Verdad, Reto y Modo mixto. La app ofrece chino, inglés y español; las preguntas principales funcionan sin conexión.'),
  'limit':t('GitHub Releases 已提供 v1.0.0 Android 试玩包，要求 Android 7.0+。这是预发布 Demo，尚未正式上架 Google Play；仅使用 Google 测试广告。源码、题库与签名材料保持私有。iOS 运行状态未确认。','GitHub Releases provides the v1.0.0 Android demo, requiring Android 7.0+. This is a pre-release demo, not an official Google Play release, and uses Google test ads only. Source, prompt libraries and signing materials remain private. iOS operation is unconfirmed.','GitHub Releases ofrece la demo Android v1.0.0 para Android 7.0+. Es una demo preliminar, aún sin publicación oficial en Google Play, con anuncios de prueba de Google. El código, las preguntas y las firmas permanecen privados. El funcionamiento en iOS no está confirmado.'),
  'image':'screenshots/home-{lang}.png', 'caption':t('已有 Android 界面捕获拼接的完整滚动首页。','Full scrolling home preview stitched from existing Android UI captures.','Vista completa del inicio compuesta de capturas Android existentes.'),
  'doc':{k:f'README.{k}.md' for k in L}, 'release':'https://github.com/Lq922466/party-games/releases/tag/v1.0.0'
 },
 'blockslayer': {
  'cat':'games', 'title':t('BlockSlayer','BlockSlayer','BlockSlayer'), 'status':t('开发中 · 早期原型','In development · early prototype','En desarrollo · prototipo inicial'), 'tech':'Flutter / Dart / Provider / SharedPreferences',
  'summary':t('将方块消除与史莱姆战斗结合的原型：摆放方块、清除行列，并为战斗保留空间。','A prototype combining block clearing and slime combat: place pieces, clear lines and preserve space for battle.','Un prototipo de bloques y combate contra slimes: coloca piezas, elimina líneas y conserva espacio para combatir.'),
  'body':t('公开介绍记录了 8×8 棋盘、经典模式与限时模式。后续战斗实现包含敌人生命值、消行攻击及按成功放置次数推进的敌人回合。这些描述来自代码检查，未在此次工作中验证运行。','Public documentation describes an 8×8 board, Classic Mode and Time Attack. Later combat implementation includes enemy health, line-clear attacks and enemy turns counted by successful placements. These descriptions come from code inspection, without runtime validation in this work.','La documentación describe un tablero 8×8, modo clásico y contrarreloj. La implementación posterior incluye vida enemiga, ataques por líneas y turnos contados por colocaciones correctas. Las descripciones proceden de revisar el código, sin validación de ejecución en este trabajo.'),
  'limit':t('没有公开安装包。现有界面仍显示 BLOCK CRUSH，使用英语。原始 README 致谢 Md Rounaq Ali 的 block-crush-game 项目；上游链接、许可证、素材权限与改动范围仍待核实。不能把全部上游工作归于 INNNX。源码保持私有。','No installer is public. The existing interface still says BLOCK CRUSH and uses English. The original README credited Md Rounaq Ali’s block-crush-game project; upstream URL, license, asset permissions and modification scope still require verification. Not all upstream work is attributed to INNNX. Source remains private.','No hay instalador público. La interfaz conserva BLOCK CRUSH y está en inglés. El README original agradecía el proyecto block-crush-game de Md Rounaq Ali; faltan por verificar URL, licencia, permisos y alcance de cambios. No se atribuye todo el trabajo original a INNNX. El código sigue privado.'),
  'image':'screenshots/home.png', 'caption':t('真实的现有英语首页，仍显示 BLOCK CRUSH。','Authentic existing English home, still displaying BLOCK CRUSH.','Inicio real existente en inglés, todavía con BLOCK CRUSH.'), 'doc':{k:f'README.{k}.md' for k in L}
 },
 'esp32-companion-v1': {
  'cat':'robots-iot', 'title':t('ESP32 陪伴机器人 V1','ESP32 Companion Robot V1','Robot de compañía ESP32 V1'), 'status':t('开发中 · 受启发原型','In development · inspired prototype','En desarrollo · prototipo inspirado'), 'tech':'ESP32 / Arduino C++ / I²C / SSD1306',
  'summary':t('已公开 OLED 表情显示代码。当前是静态面孔模块，尚未确认硬件验证。','Published OLED facial-display code. Currently a static-face module; hardware validation is unconfirmed.','Código de expresión facial OLED publicado. Actualmente es un módulo de cara estática; la validación física no está confirmada.'),
  'body':t('代码初始化 I²C 和 128×64 SSD1306，绘制眼睛与嘴巴并提交显示缓冲区。loop() 为空。V1 灵感来自小红书原作者的公开机器人制作思路，并根据需求调整部分硬件材料与配置。','The code initializes I²C and a 128×64 SSD1306, draws eyes and a mouth, and submits the display buffer. loop() is empty. V1 is inspired by the original Xiaohongshu creator’s public robot-building approach, with some hardware materials and configuration adapted to personal needs.','El código inicializa I²C y una SSD1306 de 128×64, dibuja ojos y boca y envía el búfer. loop() está vacío. V1 se inspira en el enfoque público del creador original de Xiaohongshu, adaptando algunos materiales y configuraciones a necesidades personales.'),
  'limit':t('硬件未在此次工作中连接或测试。动画、联网、语音、对话、运动与自主行为均未实现。V1 不是完全独立原创设计；原作者名称与代码来源未独立核实，保留原始致谢链接。','No hardware was connected or tested in this work. Animation, networking, voice, conversation, motion and autonomy are not implemented. V1 is not a wholly independent original design; the creator’s name and code provenance are not independently verified. The original attribution link is retained.','No se conectó ni probó hardware en este trabajo. No hay animación, red, voz, conversación, movimiento ni autonomía implementados. V1 no es un diseño totalmente independiente; el nombre del creador y el origen del código no se verificaron de forma independiente. Se conserva el enlace de atribución.'),
  'doc':{'zh':'docs/README.zh-CN.md','en':'docs/README.en.md','es':'docs/README.es.md'}
 }
}
plans = [t('Linux 与 Docker 家庭实验室','Linux & Docker Homelab','Laboratorio doméstico Linux y Docker'),t('网络基础设施实验','Network Infrastructure Lab','Laboratorio de infraestructura de red'),t('网络安全 SOC 实验','Cybersecurity SOC Lab','Laboratorio SOC de ciberseguridad'),t('AI 系统管理助手','AI SysAdmin Assistant','Asistente de administración con IA')]

def card(pid, lang):
 p=projects[pid]
 return f'<a class="project-card" href="projects/{pid}.html"><span class="status">{esc(p["status"][lang])}</span><h2>{esc(p["title"][lang])}</h2><p>{esc(p["summary"][lang])}</p><small>{esc(p["tech"])}</small><span class="card-action">{ui["detail"][lang]} <span aria-hidden="true">↗</span></span></a>'

def shell(lang, page, title, body, depth=0):
 prefix='../'*depth
 links=''.join(f'<a href="{prefix}{slug}.html"'+(' aria-current="page"' if page==slug else '')+f'>{c["title"][lang]}</a>' for slug,c in cats.items())
 languages=''.join(f'<a lang="{k}" hreflang="{k}" href="{prefix}../{k}/{page}.html"'+(' aria-current="true"' if lang==k else '')+f'>{label}</a>' for k,label in [('zh','中文'),('en','EN'),('es','ES')])
 opts=''.join(f'<option value="{key}">{ui[key][lang]}</option>' for key in ['system','light','dark'])
 return f'''<!doctype html>
<html lang="{'zh-CN' if lang=='zh' else lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="color-scheme" content="light dark"><meta name="description" content="{esc(title+' · '+ui['intro'][lang])}"><title>{esc(title)} · INNNX.</title><link rel="stylesheet" href="{prefix}../assets/site.css"><script src="{prefix}../assets/site.js" defer></script></head>
<body><a class="skip" href="#main">{ui['skip'][lang]}</a><div class="canvas"><header><a class="wordmark" href="{prefix}index.html">innnx’s playground <span aria-hidden="true">✳</span></a><span class="est">est. 2026</span></header>
<div class="controls"><nav class="languages" aria-label="{ui['languages'][lang]}">{languages}</nav><label>{ui['theme'][lang]} <select id="theme">{opts}</select></label><a class="github" href="{G[:-1]}">GitHub ↗</a></div>
<nav class="main-nav" aria-label="{ui['home'][lang]}"><a href="{prefix}index.html"{' aria-current="page"' if page=='index' else ''}>{ui['home'][lang]}</a>{links}</nav>
<main id="main">{body}</main><footer><p>{ui['footer'][lang]}</p><div><span>{ui['updated'][lang]}</span><a href="{G}Lq922466">{ui['source'][lang]} ↗</a></div></footer></div></body></html>'''

for lang in L:
 d=OUT/lang
 (d/'projects').mkdir(parents=True,exist_ok=True)
 grid=''.join(f'<a class="category category-{i}" href="{slug}.html"><span class="number">0{i+1} /</span><h3>{c["title"][lang]}</h3><p>— {c["sub"][lang]}</p><span class="arrow" aria-hidden="true">↗</span></a>' for i,(slug,c) in enumerate(cats.items()))
 body=f'<section class="hero"><div><h1>INNNX.</h1><p class="tagline">{ui["tag"][lang]}</p><p class="intro">{ui["intro"][lang]}</p><p class="topics">✳ code　✳ games　✳ robots　✳ security</p></div><img class="city" src="../assets/city.svg" alt="" width="250" height="220"></section><section class="home-categories"><h2>{ui["made"][lang]}</h2><div class="category-grid">{grid}</div></section>'
 (d/'index.html').write_text(shell(lang,'index',ui['home'][lang],body),encoding='utf-8')
 for slug,c in cats.items():
  body=f'<div class="page-heading"><p class="eyebrow">INNNX. / 0{list(cats).index(slug)+1}</p><h1>{c["title"][lang]}</h1><p class="lead">{c["desc"][lang]}</p></div>'
  if slug=='featured':
   body+=f'<div class="category-grid">'+''.join(f'<a class="category" href="{s}.html"><h2>{cc["title"][lang]}</h2><p>{cc["sub"][lang]} ↗</p></a>' for s,cc in cats.items() if s!='featured')+'</div>'
  else: body+='<div class="project-grid">'+''.join(card(pid,lang) for pid,p in projects.items() if p['cat']==slug)+'</div>'
  if slug=='infra-security': body+=f'<section class="plans"><h2>{ui["roadmap"][lang]}</h2><ul>'+''.join(f'<li><strong>{p[lang]}</strong><span>{ui["planned"][lang]}</span></li>' for p in plans)+'</ul></section>'
  if slug=='robots-iot': body+=f'<section class="plans"><h2>{ui["roadmap"][lang]}</h2><ul><li><strong>V2 · '+t('独立设计','Independent design','Diseño independiente')[lang]+f'</strong><span>{ui["planned"][lang]}</span></li><li><strong>V3 · '+t('未来独立开发','Future independent development','Desarrollo independiente futuro')[lang]+f'</strong><span>{ui["planned"][lang]}</span></li></ul></section>'
  body+=f'<p class="source-link"><a href="{G}Lq922466/blob/main/portfolio/{slug}.md">{ui["docs"][lang]} ↗</a></p>'
  (d/f'{slug}.html').write_text(shell(lang,slug,c['title'][lang],body),encoding='utf-8')
 for pid,p in projects.items():
  body=f'<a class="back" href="../{p["cat"]}.html">← {ui["back"][lang]}</a><div class="page-heading"><p class="eyebrow">{cats[p["cat"]]["title"][lang]}</p><h1>{p["title"][lang]}</h1><span class="status">{p["status"][lang]}</span><p class="lead">{p["summary"][lang]}</p><p class="tech">{p["tech"]}</p></div><div class="detail-grid"><article><p>{p["body"][lang]}</p><h2>{ui["scope"][lang]}</h2><p>{p["limit"][lang]}</p>'
  if pid=='esp32-companion-v1':
   body+=f'<p class="attribution"><a href="https://xhslink.cn/m/5y0F9KIVkvd">'+t('V1 灵感来源：小红书原作者','V1 inspiration: original Xiaohongshu creator','Inspiración V1: creador original de Xiaohongshu')[lang]+'</a></p><h2>'+ui['roadmap'][lang]+'</h2><p>'+t('V2：独立设计；V3：未来独立开发。两者均处于计划阶段，没有已完成的版本或已验证功能。','V2: independent design; V3: future independent development. Both are plans only, with no completed versions or verified features.','V2: diseño independiente; V3: desarrollo independiente futuro. Ambos son planes, sin versiones completadas ni funciones verificadas.')[lang]+'</p>'
  body+=f'<h2>{ui["evidence"][lang]}</h2><ul class="resource-list"><li><a href="{G}{pid}">{ui["repo"][lang]} ↗</a></li><li><a href="{G}{pid}/blob/main/{p["doc"][lang]}">'+t('项目介绍','Project documentation','Documentación del proyecto')[lang]+' ↗</a></li>'
  if 'release' in p: body+=f'<li><a href="{p["release"]}">'+t('Android v1.0.0 试玩发布与校验文件','Android v1.0.0 demo release & checksums','Demo Android v1.0.0 y sumas de verificación')[lang]+' ↗</a></li>'
  if pid=='esp32-companion-v1': body+=f'<li><a href="{G}{pid}/blob/main/firmware/oled-face/oled-face.ino">OLED Arduino / C++ ↗</a></li>'
  body+='</ul></article>'
  if 'image' in p:
   img=p['image'].format(lang=lang)
   url=f'https://raw.githubusercontent.com/Lq922466/{pid}/main/{img}'
   body+=f'<figure><a href="{G}{pid}/blob/main/{img}"><img class="evidence-image" src="{url}" alt="{esc(p["caption"][lang])}" loading="lazy"></a><figcaption>{p["caption"][lang]}</figcaption></figure>'
  body+='</div>'
  (d/'projects'/f'{pid}.html').write_text(shell(lang,'projects/'+pid,p['title'][lang],body,1),encoding='utf-8')

assets=OUT/'assets'
assets.mkdir(exist_ok=True)
svg=(ROOT/'assets/playground.svg').read_text(encoding='utf-8')
city=re.search(r'<g id="city".*?</g>\s*</g>',svg,re.S).group(0)
city=city.replace('translate(900 184)','translate(7 10)')
(assets/'city.svg').write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 250 220">'+city+'</svg>',encoding='utf-8')
(OUT/'index.html').write_text('''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>INNNX. — Choose your language</title><link rel="stylesheet" href="assets/site.css"></head><body><main class="canvas language-entry"><h1>INNNX.</h1><p>选择语言 · Choose your language · Elige tu idioma</p><nav class="languages"><a href="zh/index.html" lang="zh-CN">简体中文</a><a href="en/index.html" lang="en">English</a><a href="es/index.html" lang="es">Español</a></nav></main><script>try{const saved=localStorage.getItem('innnx-language');const lang=saved||((navigator.language||'en').startsWith('zh')?'zh':(navigator.language||'en').startsWith('es')?'es':'en');if(['zh','en','es'].includes(lang))location.replace(lang+'/index.html')}catch(e){}</script></body></html>''',encoding='utf-8')
(OUT/'404.html').write_text('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>404 · INNNX.</title></head><body><h1>404 · INNNX.</h1><p>页面不存在 · Page not found · Página no encontrada</p><a href="/Lq922466/">首页 · Home · Inicio</a></body></html>',encoding='utf-8')
(OUT/'.nojekyll').touch()
print('Built 27 translated pages plus language entry and 404. Existing profile and documents untouched.')
