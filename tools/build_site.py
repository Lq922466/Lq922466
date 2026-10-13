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
 'back': t('返回分类','Back to category','Volver a la categoría'), 'updated': t('资料核对：2026-10-13','Sources checked: 2026-10-13','Fuentes revisadas: 2026-10-13'),
 'planned': t('计划中 · 尚未实现','Planned · not implemented','Planificado · sin implementar'),
 'languages': t('语言','Language','Idioma'), 'source': t('网站源码','Website source','Código del sitio')
}
cats = {
 'featured': {'title':t('精选','Featured','Destacados'), 'sub':t('更大的想法','The big ideas','Las grandes ideas'), 'desc':t('原有精选文档尚未选定项目。这里保留这个状态，你可以从其他分类了解已有作品。','The original featured document has no selected projects yet. This status is preserved; explore the other categories for documented work.','El documento original aún no tiene proyectos seleccionados. Se conserva ese estado; explora las otras categorías para conocer el trabajo documentado.')},
 'infra-security': {'title':t('基础设施与安全','Infra & Security','Infraestructura y seguridad'), 'sub':t('技术实验','The technical stuff','Los experimentos técnicos'), 'desc':t('系统管理、基础设施与安全实验。已完成的实验与未来计划分开呈现。','Systems administration, infrastructure and security labs. Completed lab work is separated from future plans.','Laboratorios de administración, infraestructura y seguridad. El trabajo completado se distingue de los planes futuros.')},
 'games': {'title':t('游戏','Games','Juegos'), 'sub':t('有趣的作品','The fun stuff','Las cosas divertidas'), 'desc':t('Flutter / Dart 游戏。公开仓库提供介绍与真实界面；游戏源码保持私有。','Flutter / Dart games. Public repositories share presentations and real interfaces; game source code remains private.','Juegos en Flutter / Dart. Los repositorios públicos ofrecen presentaciones e interfaces reales; el código de los juegos permanece privado.')},
 'robots-iot': {'title':t('机器人与物联网','Robots & IoT','Robots e IoT'), 'sub':t('小小的发明','The little inventions','Los pequeños inventos'), 'desc':t('ESP32-C3 纸板陪伴机器人：V1 历史记录、V2 集成固件与实物演示，以及 V3 未来计划。','ESP32-C3 cardboard companion: V1 history, V2 integrated firmware and real demo, and V3 future plans.','Robot de cartón ESP32-C3: historia V1, firmware integrado V2 y demo real, y planes V3.')}
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
  'cat':'robots-iot', 'title':t('PaperRobot V2 · ESP32 纸板机器人','PaperRobot V2 · ESP32 cardboard robot','PaperRobot V2 · Robot ESP32 de cartón'),
  'status':t('V2 实物演示已公开 · 逐项测试待记录','V2 build demo published · test log pending','Demo física V2 publicada · pruebas pendientes'),
  'tech':'ESP32-C3 SuperMini / SSD1306 / 2× SG90 / 2× IR / TTP223 / Arduino C++',
  'summary':t('从 V1 静态 OLED 页面更新到已公开的 V2 集成固件与实物演示：表情、红外互动、转头与触摸点头。','Updated from the static V1 OLED page to published V2 integrated firmware and a real build demo: expressions, IR interaction, yaw and touch nod.','Del OLED estático V1 al firmware integrado V2 publicado y una demo real: expresiones, interacción IR, giro y asentimiento táctil.'),
  'body':t('源码包含六种面孔数据、眨眼和平滑过渡。左右红外使整张脸横移并控制转头；两侧同时触发时回中。触摸触发开心表情与一次点头，45 秒无活动后进入睡眠表情。2026-10-13 的仓库报告记录 11 个程序编译通过。用户表示实物已完成并提供约 74 秒演示；视频未与确切烧录固件哈希绑定。','Source contains six face designs, blinking and smooth transitions. Left/right IR shifts the whole face and controls yaw; both inputs center it. Touch triggers happiness and one nod; 45 seconds of inactivity selects sleep. The repository records 11 successful sketch compilations on 2026-10-13. The owner reports a completed build and supplied a roughly 74-second demo; the flashed firmware hash is unconfirmed.','El código contiene seis diseños de cara, parpadeo y transiciones suaves. IR desplaza toda la cara y controla el giro; ambas entradas la centran. El tacto activa alegría y un asentimiento; tras 45 segundos sin actividad aparece sueño. El repositorio registra 11 compilaciones correctas el 2026-10-13. El propietario comunica un montaje terminado y aporta una demo de unos 74 segundos; falta confirmar el hash del firmware grabado.'),
  'limit':t('编译与演示不等于完整硬件验收：逐项实测、持续运行、最终供电接法、零件精确额定值、制作照片与尺寸仍待补充。没有摄像头、语音、联网或 AI 对话功能。V1 历史代码和文档保留；当前 V2 仍是参考改编，不宣称独立原创。','Compilation and a demo do not establish a full hardware acceptance test: per-test observations, sustained operation, final power arrangement, exact part ratings, assembly photos and dimensions remain pending. No camera, voice, networking or AI dialogue is implemented. V1 source and documentation are preserved; current V2 remains an inspired adaptation.','La compilación y la demo no equivalen a una validación completa: faltan resultados por prueba, funcionamiento prolongado, alimentación final, especificaciones exactas, fotos de montaje y medidas. No hay cámara, voz, red ni diálogo IA. Se conservan V1 y su documentación; V2 sigue siendo una adaptación inspirada.'),
  'image':'media/demo-preview.jpg', 'caption':t('用户提供的实物演示视频第 5 秒截帧，非独立成品照片。','Frame at 5 seconds from the owner’s real demo, not a separate product photograph.','Fotograma a los 5 segundos de la demo real del propietario, no una foto de producto independiente.'),
  'doc':{'zh':'README.zh-CN.md','en':'README.md','es':'README.es.md'}
 }

}
plans = [t('Linux 与 Docker 家庭实验室','Linux & Docker Homelab','Laboratorio doméstico Linux y Docker'),t('网络基础设施实验','Network Infrastructure Lab','Laboratorio de infraestructura de red'),t('网络安全 SOC 实验','Cybersecurity SOC Lab','Laboratorio SOC de ciberseguridad'),t('AI 系统管理助手','AI SysAdmin Assistant','Asistente de administración con IA')]


def robot_details(lang):
 sections=[
  (t('实际硬件与接线','Hardware and wiring','Hardware y cableado'),t('ESP32-C3 SuperMini ×1；SSD1306 128×64 I²C OLED ×1（0x3C，SDA 0 / SCL 1）；SG90 ×2（转头 GPIO4，俯仰 GPIO5）；红外模块 ×2（GPIO6/7）；TTP223 ×1（GPIO10）。5V UBEC 给舵机供电并共地；12V 只接 UBEC 输入。现有大面包板与手工测量裁切的 3mm 瓦楞纸板外壳，无裁切模板。','One ESP32-C3 SuperMini; one SSD1306 128×64 I²C OLED (0x3C, SDA 0 / SCL 1); two SG90 servos (yaw GPIO4, pitch GPIO5); two IR modules (GPIO6/7); one TTP223 (GPIO10). A 5V UBEC powers servos with common ground; 12V goes only to its input. Existing large breadboard and hand-measured 3mm corrugated cardboard shell; no cutting template.','Un ESP32-C3 SuperMini; OLED SSD1306 128×64 I²C (0x3C, SDA 0 / SCL 1); dos SG90 (giro GPIO4, inclinación GPIO5); dos IR (GPIO6/7); TTP223 (GPIO10). UBEC de 5V para servos con masa común; 12V solo a su entrada. Placa de pruebas grande existente y carcasa de cartón corrugado de 3mm medida a mano, sin plantilla.')),
  (t('组装与调试路径','Assembly and diagnostics','Montaje y diagnóstico'),t('文档建议：先独立测试 USB、OLED、IR、触摸与舵机；按实际零件裁切纸板；拆舵盘回中 90°，断电后安装；预留检修口和线缆余量。确认供电与共地后空载上传 V2，再逐步加载。Arduino 选择 ESP32C3 Dev Module，串口 115200。此为仓库重建指南，制作照片与真实步骤记录尚待补充。','Documented sequence: test USB, OLED, IR, touch and servos separately; cut cardboard to measured parts; center at 90° without horns, then attach with power off; preserve service access and cable slack. Check power and grounding, upload V2 unloaded, then add load gradually. Arduino target ESP32C3 Dev Module, serial 115200. This is a reconstruction guide; assembly photos and the actual build log are pending.','Secuencia documentada: probar USB, OLED, IR, tacto y servos por separado; medir y cortar cartón; centrar a 90° sin brazos y montarlos sin corriente; reservar acceso y holgura. Revisar alimentación y masa, cargar V2 sin carga y añadirla gradualmente. Arduino: ESP32C3 Dev Module, serie 115200. Es una guía reconstruida; faltan fotos e historial real.')),
  (t('技术挑战','Technical challenges','Retos técnicos'),t('OLED ACK 仅代表总线响应，不能证明可见像素：先扫描地址，再做独立显示测试。输入使用 40ms 去抖，触摸需释放后重触并等待 2200ms 冷却。舵机每 20ms 最多走 1°，默认转头 80–100°、俯仰 82–98°；软件限位不保证机械安全。抖动或重启需排查供电压降、共地、接触与机械堵转。','OLED ACK proves a bus response, not visible pixels: scan the address, then test the display separately. Inputs use 40ms debounce; touch requires release/re-touch and a 2200ms cooldown. Servos move at most 1° per 20ms, with yaw 80–100° and pitch 82–98° defaults; software limits do not establish mechanical safety. Jitter or resets require checks for voltage droop, grounding, contacts and stalls.','ACK del OLED confirma respuesta del bus, no píxeles visibles: escanear y probar pantalla aparte. Entradas con antirrebote de 40ms; tacto requiere soltar y volver a tocar tras 2200ms. Servos: máximo 1° cada 20ms, giro 80–100° e inclinación 82–98°; los límites no garantizan seguridad mecánica. Revisar caídas de tensión, masa, contactos y bloqueos ante vibración o reinicios.'))]
 result=''.join(f'<h2>{heading[lang]}</h2><p>{text[lang]}</p>' for heading,text in sections)
 result+='<p class="attribution">'+t('感谢 Made by Z 的纸板机器人制作思路；V1 与 V2 均保留参考致谢。作者身份、原始代码和复用许可未独立核实。','Thanks to Made by Z for the cardboard-robot inspiration; V1 and V2 retain this credit. Creator identity, original code and reuse permissions are not independently verified.','Gracias a Made by Z por la inspiración; V1 y V2 conservan el crédito. Identidad, código original y permisos no verificados independientemente.')[lang]+' <a href="https://xhslink.cn/m/5y0F9KIVkvd">'+t('原始参考','Original reference','Referencia original')[lang]+'</a></p>'
 result+=f'<h2>{ui["roadmap"][lang]}</h2><p>V3 · {ui["planned"][lang]}</p>'
 docroot={'zh':'docs/zh-CN/','en':'docs/','es':'docs/es/'}[lang]
 result+='<ul class="resource-list">'
 for file,label in [('BOM',t('硬件清单','Bill of materials','Materiales')),('WIRING',t('接线与供电','Wiring and power','Cableado y alimentación')),('ASSEMBLY',t('组装指南','Assembly guide','Guía de montaje')),('COMPONENT-TESTS',t('独立零件测试','Component tests','Pruebas de componentes')),('FIRMWARE',t('固件与上传','Firmware and upload','Firmware y carga')),('TROUBLESHOOTING',t('故障排查','Troubleshooting','Solución de problemas')),('TESTING',t('编译与测试证据','Compilation and test evidence','Compilación y pruebas')),('ATTRIBUTION',t('来源致谢与差异','Credits and differences','Créditos y diferencias'))]:
  result+=f'<li><a href="{G}esp32-companion-v1/blob/main/{docroot}{file}.md">{label[lang]} ↗</a></li>'
 result+=f'<li><a href="{G}esp32-companion-v1/commits/main/">'+t('提交记录','Commit history','Historial de cambios')[lang]+'</a></li></ul>'
 return result

def card(pid, lang):
 p=projects[pid]
 return f'<a class="project-card" href="projects/{pid}.html"><span class="status">{esc(p["status"][lang])}</span><h2>{esc(p["title"][lang])}</h2><p>{esc(p["summary"][lang])}</p><small>{esc(p["tech"])}</small><span class="card-action">{ui["detail"][lang]} <span aria-hidden="true">↗</span></span></a>'

def shell(lang, page, title, body, depth=0):
 prefix='../'*depth
 links=''.join(f'<a href="{prefix}{slug}.html"'+(' aria-current="page"' if page==slug else '')+f'>{c["title"][lang]}</a>' for slug,c in cats.items())
 languages=''.join(f'<a lang="{k}" hreflang="{k}" href="{prefix}../{k}/{page}.html"'+(' aria-current="true"' if lang==k else '')+f'>{label}</a>' for k,label in [('zh','中文'),('en','EN'),('es','ES')])
 description=projects[page.split('/')[-1]]['summary'][lang] if page.startswith('projects/') else cats[page]['desc'][lang] if page in cats else ui['intro'][lang]
 canonical='https://lq922466.github.io/Lq922466/'+lang+'/'+page+'.html'
 alternates=''.join(f'<link rel="alternate" hreflang="{k if k!="zh" else "zh-CN"}" href="https://lq922466.github.io/Lq922466/{k}/{page}.html">' for k in L)
 opts=''.join(f'<option value="{key}">{ui[key][lang]}</option>' for key in ['system','light','dark'])
 return f'''<!doctype html>
<html lang="{'zh-CN' if lang=='zh' else lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="color-scheme" content="light dark"><meta name="description" content="{esc(description)}"><title>{esc(title)} · INNNX.</title><link rel="canonical" href="{canonical}">{alternates}<link rel="alternate" hreflang="x-default" href="https://lq922466.github.io/Lq922466/"><meta property="og:type" content="website"><meta property="og:site_name" content="INNNX."><meta property="og:title" content="{esc(title)} · INNNX."><meta property="og:description" content="{esc(description)}"><meta property="og:url" content="{canonical}"><meta property="og:image" content="https://lq922466.github.io/Lq922466/assets/social-preview.png"><meta property="og:locale" content="{dict(zh='zh_CN',en='en_US',es='es_ES')[lang]}"><meta name="twitter:title" content="{esc(title)} · INNNX."><meta name="twitter:description" content="{esc(description)}"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:image" content="https://lq922466.github.io/Lq922466/assets/social-preview.png"><link rel="stylesheet" href="{prefix}../assets/site.css"><script src="{prefix}../assets/site.js" defer></script></head>
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
  if slug=='robots-iot': body+=f'<section class="plans"><h2>{ui["roadmap"][lang]}</h2><ul><li><strong>V3</strong><span>{ui["planned"][lang]}</span></li></ul></section>'
  body+=f'<p class="source-link"><a href="{G}Lq922466/blob/main/portfolio/{slug}.md">{ui["docs"][lang]} ↗</a></p>'
  (d/f'{slug}.html').write_text(shell(lang,slug,c['title'][lang],body),encoding='utf-8')
 for pid,p in projects.items():
  body=f'<a class="back" href="../{p["cat"]}.html">← {ui["back"][lang]}</a><div class="page-heading"><p class="eyebrow">{cats[p["cat"]]["title"][lang]}</p><h1>{p["title"][lang]}</h1><span class="status">{p["status"][lang]}</span><p class="lead">{p["summary"][lang]}</p><p class="tech">{p["tech"]}</p></div><div class="detail-grid"><article><p>{p["body"][lang]}</p><h2>{ui["scope"][lang]}</h2><p>{p["limit"][lang]}</p>'
  if pid=='esp32-companion-v1':
   body+=robot_details(lang)
  body+=f'<h2>{ui["evidence"][lang]}</h2><ul class="resource-list"><li><a href="{G}{pid}">{ui["repo"][lang]} ↗</a></li><li><a href="{G}{pid}/blob/main/{p["doc"][lang]}">'+t('项目介绍','Project documentation','Documentación del proyecto')[lang]+' ↗</a></li>'
  if 'release' in p: body+=f'<li><a href="{p["release"]}">'+t('Android v1.0.0 试玩发布与校验文件','Android v1.0.0 demo release & checksums','Demo Android v1.0.0 y sumas de verificación')[lang]+' ↗</a></li>'
  if pid=='esp32-companion-v1': body+=f'<li><a href="{G}{pid}/blob/main/firmware/PaperRobotV2/PaperRobotV2.ino">PaperRobot V2 Arduino / C++ ↗</a></li>'
  body+='</ul></article>'
  if 'image' in p:
   img=p['image'].format(lang=lang)
   url=f'https://raw.githubusercontent.com/Lq922466/{pid}/main/{img}'
   if pid=='esp32-companion-v1': url='../../assets/robot-demo.jpg'
   body+=f'<figure><a href="{G}{pid}/blob/main/{img}"><img class="evidence-image" src="{url}" alt="{esc(p["caption"][lang])}" loading="lazy" decoding="async"></a><figcaption>{p["caption"][lang]}</figcaption></figure>'
  if pid=='esp32-companion-v1':
   video='https://github.com/Lq922466/esp32-companion-v1/raw/refs/heads/main/media/PaperRobotV2-demo.mp4'
   body+=f'<section class="demo"><h2>'+t('实物演示 · 约 74 秒','Real build demo · about 74 seconds','Demo real · unos 74 segundos')[lang]+f'</h2><p>'+t('视频包含原始音轨，尚无字幕或完整文字转录。播放或下载原始公开演示：','The video retains original audio; captions and a full transcript are not available. Play or download the published demo:','El vídeo conserva el audio original; no hay subtítulos ni transcripción completa. Reproducir o descargar:')[lang]+f'</p><a href="{video}">'+t('打开演示视频','Open demo video','Abrir vídeo de demostración')[lang]+'</a><video controls playsinline preload="none" width="1080" height="608" poster="../../assets/robot-demo.jpg" aria-label="'+t('机器人实物演示','Real robot demonstration','Demostración real del robot')[lang]+f'"><source src="{video}" type="video/mp4"></video></section>'
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

base='https://lq922466.github.io/Lq922466/'
urls=[base]+[base+str(f.relative_to(OUT)).replace('\\','/') for f in sorted(OUT.rglob('*.html')) if f.name!='404.html' and f!=OUT/'index.html']
(OUT/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join('<url><loc>'+esc(u)+'</loc></url>' for u in urls)+'</urlset>',encoding='utf-8')
(OUT/'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: '+base+'sitemap.xml\n',encoding='utf-8')

entry=OUT/'index.html'
entry.write_text(entry.read_text(encoding='utf-8').replace('<title>', '<meta name="description" content="INNNX. · Code, games, robots and security. 中文 · English · Español"><link rel="canonical" href="'+base+'"><meta property="og:title" content="INNNX. — Making Stuff Just Because."><meta property="og:type" content="website"><meta property="og:url" content="'+base+'"><meta property="og:description" content="Code, games, robots and security."><meta property="og:image" content="'+base+'assets/social-preview.png"><meta name="twitter:card" content="summary_large_image">'+''.join('<link rel="alternate" hreflang="'+('zh-CN' if k=='zh' else k)+'" href="'+base+k+'/index.html">' for k in L)+'<link rel="alternate" hreflang="x-default" href="'+base+'"><title>'),encoding='utf-8')
(OUT/'404.html').write_text('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex"><title>404 · INNNX.</title><link rel="stylesheet" href="/Lq922466/assets/site.css"></head><body><main class="canvas error-page"><h1>404 · INNNX.</h1><p><span lang="zh-CN">页面不存在，请选择首页继续浏览。</span><br>Page not found. Choose a home page to keep exploring.<br><span lang="es">Página no encontrada. Elige un inicio para continuar.</span></p><nav class="languages" aria-label="Home language"><a lang="zh-CN" href="/Lq922466/zh/index.html">中文首页</a><a href="/Lq922466/en/index.html">English home</a><a lang="es" href="/Lq922466/es/index.html">Inicio en español</a></nav><p><a href="https://github.com/Lq922466">GitHub ↗</a></p></main></body></html>',encoding='utf-8')
