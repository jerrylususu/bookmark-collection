- [我做系统架构的一些原则 | 酷 壳 - CoolShell](https://coolshell.cn/articles/21672.html) #infra
- [软考资源目录](https://pan.htm.fun/%E8%BD%AF%E8%80%83%E7%9B%AE%E5%BD%95) #resource
- [“n个球放到m个盒子”问题整理(Twelvefold way) - RioTian - 博客园](https://www.cnblogs.com/RioTian/p/15188528.html) 数论 #math#hack
- [Deterministic variants of the Miller-Rabin primality test. Miller-Rabin SPRP bases records](https://miller-rabin.appspot.com/) Miller-Rabin 质数判定的确定性根 #hack
- [米勒-拉宾素性检验 - 维基百科，自由的百科全书](https://zh.wikipedia.org/wiki/%E7%B1%B3%E5%8B%92-%E6%8B%89%E5%AE%BE%E6%A3%80%E9%AA%8C) 随机化素数判定算法 #hack
- [Various ways to include comments on your static site](https://darekkay.com/blog/static-site-comments/) 各种给静态网页加评论功能的方式总结 #read#frontend
- [Instantly parse JSON in any language | quicktype](https://app.quicktype.io/) 根据 JSON 生成对应语言的对象和解析器 #tools
- [余光中：怎样改进英式中文？- 论中文的常态与变态 | LeanCloud 开放资源](https://open.leancloud.cn/improve-chinese/) #read
- [Lossless Image Compression in O(n) Time](https://phoboslab.org/log/2021/11/qoi-fast-lossless-image-compression) QOI，一个简单的图片无损压缩格式，和 PNG 压缩比类似但速度更快 #tools
- [分布式系统下的认证与授权](https://www.bmpi.dev/dev/authentication-and-authorization-in-a-distributed-system/) #backend#distributed#security
- [工作性价比计算器](https://jfstone.cn/salary/) #tools
- [In C, how do you know if the dynamic allocation succeeded?](https://lemire.me/blog/2021/10/27/in-c-how-do-you-know-if-the-dynamic-allocation-succeeded/) 因为 Linux 下 Overcommit 机制的存在，malloc 可能会容许分配大内存，但实际使用的时候出错 #tips#linux
- [My Logging Best Practices – Thomas Uhrig](https://tuhrig.de/my-logging-best-practices/) INFO for business, DEBUG for code #tips#backend
- [条分缕析分布式：到底什么是一致性？ - 铁蕾的个人博客](http://zhangtielei.com/posts/blog-distributed-consistency.html) 原子提交问题并不是一般的共识问题，而是要求更高的 uniform consensus 问题 #distributed
- [多路复用、非阻塞、线程与协程 - 御坂研究所](https://www.nosuchfield.com/2019/01/09/Multiplex-and-non-blocking-and-threading-and-coroutine/) #backend#arch#blog
- [A visual guide on troubleshooting Kubernetes deployments](https://learnk8s.io/troubleshooting-deployments) #backend#distributed
- [Generators - The Final Frontier](http://www.dabeaz.com/finalgenerator/) Python Generator & Coroutine 三部曲之三，介绍 context manager, asyncio, 简单编译器和实现调用栈 #course#py#backend
- [A Curious Course on Coroutines and Concurrency](http://www.dabeaz.com/coroutines/) Python Generator & Coroutine 三部曲之二，介绍基于 yield 的 coroutine 实现，reactor model，以及如何用 coroutine 模拟一个简单的 OS #course#py#backend
- [Generator Tricks for Systems Programmers](http://www.dabeaz.com/generators/) Python Generator & Coroutine 三部曲之一，介绍 generator 与 data pipeline #course#py#backend
- [All possible notations of IPv4 address](https://lucb1e.com/randomprojects/php/funnip.php?ip=8.8.8.8&link) URL 中的 IP 地址，数字部分可以用不同的进制 (dec, hex, oct) 表示，从而构造相同 IP 的诸多不同表示方法 #web#hack
- [EtherDream/http-server-online: Start a local HTTP server without any tools, just open a web page.](https://github.com/EtherDream/http-server-online) 在浏览器里直接预览本地静态网站，原理是用 Service Worker 拦截请求 URL，然后用 FileSystem API 读取本地资源 #tools
- [Spending $5k to learn how database indexes work](https://briananglin.me/posts/spending-5k-to-learn-how-database-indexes-work/) 如果没加索引，limit 最坏情况下也会全表读（但是如果读够了就不会再读了） #database
- [Netlify Drop | Netlify](https://app.netlify.com/drop) 拖放静态网站文件，直接得到公网地址 #tools
- [Timing With Curl - Susam's Maze](https://susam.in/maze/timing-with-curl.html) 让 curl 显示连接用时 #tips
- [My VS Code Playground - Pawel Cislo](https://pawelcislo.com/2021/11/14/my-vs-code-playground/) VS Code 配置指北 #tips
- [It's Now Possible To Sign Arbitrary Data With Your SSH Keys](https://www.agwa.name/blog/post/ssh_signatures) 用 SSH key 给文件签名 #tips
- [DNS doesn't "propagate"](https://jvns.ca/blog/2021/12/06/dns-doesn-t-propagate/) 对 DNS 的更好类比是 CDN，以及关于为什么 DNS 记录修改生效需要很久的讨论（negative DNS caching） #backend#web
- [GPU选购指南：训练ML模型，我必须买RTX3080吗？-InfoQ](https://www.infoq.cn/article/yujetuzzjhlnvjwrfo5s) 适合于不同深度学习场景的 GPU 选购（2020 版） #tips
- [nip.io - wildcard DNS for any IP Address](https://nip.io/) 解析到指定 IP 的域名服务 #tools
- [automerge/automerge: A JSON-like data structure (a CRDT) that can be modified concurrently by different users, and merged again automatically.](https://github.com/automerge/automerge) 支持自动解决冲突（Collision-Resolve）的类 JSON 数据结构 #tools
- [Uninitialized Stack Variables](https://www.netmeister.org/blog/stack-vars.html) C 中没有用 memset 手动初始化栈上变量导致了诡异的 Bug #c#backend
- [Ciphey/Ciphey: ⚡ Automatically decrypt encryptions without knowing the key or cipher, decode encodings, and crack hashes ⚡](https://github.com/Ciphey/Ciphey) 自动对复杂编码串 decode 的工具 #tools
- [Performance - Stack Exchange](https://stackexchange.com/performance) Stack Overflow 的网站架构 #backend
- [Distributed Systems lecture series](https://www.youtube.com/playlist?list=PLeKd45zvjcDFUEv_ohr_HdUFe97RItdiB) DDIA 作者的分布式系统课程 #video#distributed
- [如何学习一门技术](https://www.bmpi.dev/dev/how-to-learn-tech/) 是否要学、怎么学、如何用 #tips#blog
- [Command line text processing with GNU Coreutils](https://learnbyexample.github.io/cli_text_processing_coreutils/cover.html) #books
- [wg/wrk: Modern HTTP benchmarking tool](https://github.com/wg/wrk) 单机 HTTP 压力测试工具 #tools
- [ROAPI: An API Server for Static Datasets](https://tech.marksblogg.com/roapi-rust-data-api.html) #blog#tools
- [roapi/roapi: Create full-fledged APIs for static datasets without writing a single line of code.](https://github.com/roapi/roapi) 直接从 JSON/CSV 文件生成 query API #tools#data
- [Building a full stack application with Cloudflare Pages](http://blog.cloudflare.com/building-full-stack-with-pages/) Cloudflare Pages 增加了通过 js 文件在静态网页内增加动态内容的功能，甚至还额外提供了 KV，持久存储和中间件支持 #frontend
- [How We Made Bracket Pair Colorization 10,000x Faster In Visual Studio Code](https://code.visualstudio.com/blogs/2021/09/29/bracket-pair-colorization) (2,3)-trees, recursion-free tree-traversal, bit-arithmetic, incremental parsing #algo
- [Why Your Website Should Use Dithered Images | endtimes.dev](https://endtimes.dev/why-you-should-dither-images/) 与直接压缩原始真彩色图片相比，dithered image 能有更好的压缩比率，在非重要场合下很合适 #frontend#hack
- [Javascript Anti Debugging — Some Next Level Sh*t (Part 2— Abusing Chromium Devtools Scope Pane)](https://gist.github.com/b21c71187fcbf138aec341021e0e4e30) 细化到行级的 chrome devtool debugging 检测 #frontend#hack
- [There is no 'printf'.](https://www.netmeister.org/blog/return-printf.html) gcc 在满足 heuristic 的时候，会用 puts 替代 printf，导致 printf 作为 main 中最后一次调用时返回值不符合预期 #c
- [Debugging a weird 'file not found' error](https://jvns.ca/blog/2021/11/17/debugging-a-weird--file-not-found--error/) 生成的 Go 二进制文件不是 static linked 的；ELF 可执行文件可以请求一个 interpreter 来执行自身，如果这个 interpreter 不存在，会导致文件存在但是无法被运行 #hack#tips
- [Home : Hypothesis](https://web.hypothes.is/) 网页荧光笔 #tools
- [Some notes on using esbuild](https://jvns.ca/blog/2021/11/15/esbuild-vue/) 一个相对简单的前端构建方案：用 import 导入库，用 esbuild 生成单体 js #frontend
- [How we built a forever-free serverless SQL database](https://www.cockroachlabs.com/blog/how-we-built-cockroachdb-serverless/) 构造 serverless SQL DB：用 KV 作为 SQL DB 的底层存储，把 SQL 执行层无状态化 #arch#database
- [软件开发|扩展一个 GraphQL 网站](https://linux.cn/article-13983-1.html) 调整 GraphQL API 和网页构造，使其更易于缓存 #read#blog#frontend#backend
- [Modern SQL: A lot has changed since SQL-92](https://modern-sql.com/) 展示现代 SQL 的一些写法（递归，over，system_time...） #books#backend#database
- [SQL Indexing and Tuning e-Book for developers: Use The Index, Luke covers Oracle, MySQL, PostgreSQL, SQL Server, ...](https://use-the-index-luke.com/) 解释 SQL 索引如何工作的电子书 #books#read#database#backend
- [Understanding AWK](https://earthly.dev/blog/awk-examples/) 简明 awk 教程 #read
- [bobwen-dev/htpdate: a tool to synchronize system time with web servers, for linux, windows and macos.](https://github.com/bobwen-dev/htpdate) 利用 Web Server 的响应时间戳作为时间源同步时间 #tools
- [SQLime — Online SQLite playground](https://sqlime.org/) 在线 SQLite 环境，基于 sql.js #tools
- [Cloudcraft – Draw AWS diagrams](https://www.cloudcraft.co/) 不仅是画架构图，还能把架构图和实际环境同步起来 #arch#tools
- [A catalog of wealth-creation mechanisms](http://blog.rongarret.info/2009/10/catalog-of-wealth-creation-mechanisms.html) 生成财富的九种方式，以及对信息时代生成财富方式的细分 #life
- [Mechanical sympathy for QR codes: making NSW check-in better](https://huonw.github.io/blog/2021/10/nsw-covid-qr/) 简化二维码（QR Code）中的 URL：参数编码、域名长度、纠错等级 #hack
- [Composerize](https://www.composerize.com/?utm_source=appinn.com) 把复杂的 docker 命令转换成 docker-compose.yml #tools#backend#infra
- [Darts, Dice, and Coins](https://www.keithschwarz.com/darts-dice-coins/) 非均衡抽样方法（抽奖算法），以及 O(1) 时间的 Alias Method（空间换时间，避免了查询随机数所在的区间） #algo
- [Red Blob Games: Hexagonal Grids](https://www.redblobgames.com/grids/hexagons/) 如何设计和实现六边形网格系统 #game#design
- [K8S 云原生应用开发小记](https://www.bmpi.dev/dev/guide-to-k8s-cloud-native/) 从设计到建构的全过程 #infra#backend
- [The Billion Pi Challenge](https://nullprogram.com/blog/2014/09/18/) 如何在 pi 的前 1B 小数位中搜寻一个特定的数字序列？空间换时间 #hack#backend#c
- [为 PDF 增加目录 - 少数派](https://sspai.com/post/69601) （pdf.tocgen）先根据已有的标题提取出标题对应的格式信息，然后用格式信息匹配所有标题，最后构造目录 #hack
- [Introducing WebContainers: Run Node.js natively in your browser](https://blog.stackblitz.com/posts/introducing-webcontainers/) 用WASM写了个极小的OS，然后在这个OS上跑node.js，通过把OS里的虚拟TCP层关联到浏览器的service worker，就可以在本地浏览器里完全实现一个node.js开发环境了，用的时候只需要浏览器本身，并不需要任何其他配置 #frontend#hack
- [My Top 10 Money Rules](https://jonpauluritis.com/articles/my-top-10-money-rules/) 关于金钱的一些感悟 #lifehack
- [Motion One: The Web Animations API for everyone](https://motion.dev/) 高性能的前端 JavaScript 动画库 #frontend#visual
- [Injecting environment variables into static websites using NGINX](https://www.innoq.com/de/blog/nginx-ssi-env/) Server Side Include，往网页里注入环境变量 #backend#hack
- [DIY Single Sign-On for SSH](https://smallstep.com/blog/diy-single-sign-on-for-ssh/) SSH + Single Sign On，自己配置 CA 和认证服务 #tips#hack#backend
- [Don’t Build A General Purpose API To Power Your Own Front End - Max Chernyak](https://max.engineer/server-informed-ui?utm_source=pocket_mylist) 对自有的前端，可以提供一套更自由、独立演化的内部 API，而不用痛苦的修改对外 API 以适应业务需求 #backend#api#tips
- [Regret Minimization | Samvit Jain](http://www.samvitjain.com/blog/regret/?utm_source=pocket_mylist) 「最小化后悔」可能不是决策的最好方式，「寻找不变量」可能更适合 #life#tips
- [Git飞行规则(Flight Rules)](https://github.com/k88hudson/git-flight-rules/blob/master/README_zh-CN.md) Git 出现问题之后如何应对 #tips
- [Linearizability & CAP](https://mwhittaker.github.io/consistency_in_distributed_systems/2_cap.html) 一个很赞的线性一致性可视化 #visual#distributed#read
- [Category:Programming Tasks - Rosetta Code](http://rosettacode.org/wiki/Category:Programming_Tasks) 相同算法的不同语言实现 #tools
- [How to get useful answers to your questions](https://jvns.ca/blog/2021/10/21/how-to-get-useful-answers-to-your-questions/) 问 Yes/No，展示自己当前的理解，愿意打断 #tips
- [A future for SQL on the web](https://jlongster.com/future-sql-web) 浏览器自带的 IndexedDB 太慢，用 WASM 版的 SQLite 替代，然后把 IndexedDB 作为单纯的存储后端（Filesystem 抽象） #frontend#database#read
- [GitHub stars won't pay your rent](https://kitze.io/posts/github-stars-wont-pay-your-rent) 从开源项目到 Startup #read#startup
- [How I made $50K in 3 days with NFTs](https://paulstamatiou.com/how-i-made-50k-in-3-days-with-NFTs/) #blockchain#nft
- [前言 | HZFE - 剑指前端 Offer](https://febook.hzfe.org/awesome-interview/) 前端面试书籍 #books#interview#frontend
- [Go go-to guide](https://yourbasic.org/golang/) #golang
- [Goroutine Leak和解决之道](https://hoverzheng.github.io/post/technology-blog/go/goroutine-leak%E5%92%8C%E8%A7%A3%E5%86%B3%E4%B9%8B%E9%81%93/) #golang
- [tianmingyun/MasterBitcoin2CN: 《精通比特币》第二版  区块链研习社 云天明联合出品。本书更名《精通区块链编程第二版》已由机械工业出版社出版，京东有售。](https://github.com/tianmingyun/MasterBitcoin2CN) #books#distributed
- [golang101/golang101: Go语言101 : 一本侧重于Go语言语法和语义的编程解释和指导书](https://github.com/golang101/golang101) #books#golang
- [pow-captcha](https://git.sequentialread.com/forest/pow-captcha) 基于 Proof of Work 的验证码方案 #tools
- [Persistent Data Structure](http://fuzhe1989.github.io/2017/11/07/persistent-data-structure/) 可持久化数据结构（修改后旧版本依然可用） #data#blog
- [白板编程浅谈——Why, What, How](http://lucida.me/404/) #career#job
- [mviereck/x11docker: Run GUI applications and desktops in docker and podman containers. Focus on security.](https://github.com/mviereck/x11docker) 容器化的 X Server，可以在容器里跑 GUI #tools
- [BornToBeRoot/NETworkManager: A powerful tool for managing networks and troubleshoot network problems!](https://github.com/BornToBeRoot/NETworkManager) Windows 下的高级网络管理工具 #tools
- [Working From Orbit](https://blog.immersed.team/working-from-orbit-39bf95a6d385) 完全在 VR 世界中工作 #read#visual
- [CapRover · Free and Open Source PaaS!](https://caprover.com/) self-host PaaS #infra#tools
- [Evan's Awesome A/B Tools - sample size calculator, A/B test results, and more](https://www.evanmiller.org/ab-testing/) AB测试计算器 #tools#data
- [Understanding How Facebook Disappeared from the Internet](https://blog.cloudflare.com/october-2021-facebook-outage/) Cloudflare 的 Facebook BGP 事件外部记录 #infra
- [Mind-bending metaclasses - adding function overloads to Python - YouTube](https://www.youtube.com/watch?v=yWzMiaqnpkI) #hack
- [devongovett/regexgen: Generate regular expressions that match a set of strings](https://github.com/devongovett/regexgen) #tools#frontend
- [笔记文档一把梭——MkDocs 快速上手指南 ｜ 少数派会员  π+Prime](https://sspai.com/prime/story/mkdocs-primer) #tools
- [Overview - Dropbox Engineering Career Framework](https://dropbox.github.io/dbx-career-framework/overview.html) #career#grow
- [How to tell what level of developer you are, junior to senior](https://jg.gg/2020/11/22/how-to-tell-what-level-of-developer-you-are/) #read#grow
- [Raft | The Secret Lives of Data](http://thesecretlivesofdata.com/raft/) 最好的 Raft 交互式可视化 #distributed#visual
- [「图解Raft」让一致性算法变得更简单](https://zinglix.xyz/2020/06/25/raft/) Raft 图解 #algo#distributed#read
- [肘后备急方 - Miao Yu | 于淼](https://yufree.cn/cn/2021/09/26/first-aid/) #read#lifehack
- [Windows 更新设计、类型、步骤及常见问题 - 少数派](https://sspai.com/post/68959) #read
- [A Constructive Look At TempleOS](http://www.codersnotes.com/notes/a-constructive-look-at-templeos/) #blog#read
- [hadolint/hadolint: Dockerfile linter, validate inline bash, written in Haskell](https://github.com/hadolint/hadolint) Dockerfile 的 Linter #tools#docker#infra
- [Automating a software company with GitHub Actions - PostHog](https://posthog.com/blog/automating-a-software-company-with-github-actions) Github Actions 在软件开发各个阶段的使用示例 #blog#read#infra
- [GNU nano is my editor of choice – Ariadne's Space](https://ariadne.space/2021/08/13/gnu-nano-is-my-editor-of-choice/) 配置 nano 支持语法高亮 #blog#read#editor
- [Mito](https://trymito.io/) 给 Jupyter 增加类 Excel 的可视化数据处理工具 #tools#data
- [Tutorial - Write a Shell in C - Stephen Brennan](https://brennan.io/2015/01/16/write-a-shell-in-c/) 如何用 C 写一个 Shell #blog#read
- [发现 GNOME 上的最佳应用 – GNOME 上的应用](https://apps.gnome.org/zh-CN/) #tools
- [DataStation | The Data IDE for Developers](https://datastation.multiprocess.io/) 一站式数据分析，将数据库 SQL 查询、脚本编程、数据可视化结合在一起。 #tools#data
- [calganaygun/MDcat: A super simple script which uses the GitHub API to convert your markdown files to GitHub styled HTML site.](https://github.com/calganaygun/MDcat) Github 自带的 Markdown 转 HTML 示例 #tools
- [Gaphor | Modeling for Everyone](https://gaphor.org/) 跨平台 UML 工具  #tools
- [allanrbo/filesremote: An SSH file manager that lets you edit files like they are local](https://github.com/allanrbo/filesremote) SSH 文件管理工具 #tools
- [容器与云|容器的四大基础技术](https://linux.cn/article-13792-1.html) namespace, cgroup, seccomp, SELinux #backend#security#container
- [One does not simply calculate the absolute value](https://habr.com/en/post/574082/) 浮点数与绝对值里的坑 #backend#java#blog#trick#hole
- [go实现无限缓存的channel](https://colobu.com/2021/05/11/unbounded-channel-in-go/) #backend#blog#golang
- [Accidentally Quadratic](https://accidentallyquadratic.tumblr.com) 不小心用了二次算法的经验 #blog#programming
- [Visualizing Concurrency in Go ·  divan's blog](https://divan.dev/posts/go_concurrency_visualize/) #blog#visual
- [Go 语言设计与实现](https://draveness.me/golang/) #books#backend
- [Elm - delightful language for reliable web applications](https://elm-lang.org/) #frontend
- [Elm at Rakuten | Rakuten Engineering Blog](https://engineering.rakuten.today/post/elm-at-rakuten/) #blog
- [Technical Interview Guide for Busy Engineers | Tech Interview Handbook](https://techinterviewhandbook.org/) #books
- [Interactive Linear Algebra](http://textbooks.math.gatech.edu/ila/index.html) #books
- [Go by Example](https://gobyexample.com/) #books
- [LearnShare/learn-VRA: Let's learn Vue/React/Angular together.](https://github.com/LearnShare/learn-VRA) Vue、React 和 Angular 一起学怎么样？ #read#frontend
- [Mastering Web Scraping in Python: Crawling from Scratch - ZenRows](https://www.zenrows.com/blog/mastering-web-scraping-in-python-crawling-from-scratch) #blog#read
- [Amazon Web Services In Plain English](https://expeditedsecurity.com/aws-in-plain-english/) #tools#infra
- [anuraghazra/github-readme-stats: Dynamically generated stats for your github readmes](https://github.com/anuraghazra/github-readme-stats) 生成关于 Github 使用情况的 badge #tools
- [When One-Way Latency Doesn’t Matter](http://twistedoakstudios.com/blog/Post2353_when-one-way-latency-doesnt-matter) 无法准确测量 one-way latency #blog#read#network
- [A Collection of O'rly book Covers | Ben E. C. Boyter](https://boyter.org/2016/04/collection-orly-book-covers/) #blog
- [doocs/source-code-hunter: 😱 从源码层面，剖析挖掘互联网行业主流技术的底层实现原理，为广大开发者 “提升技术深度” 提供便利。目前开放 Spring 全家桶，Mybatis、Netty、Dubbo 框架，及 Redis、Tomcat 中间件等](https://github.com/doocs/source-code-hunter) #core
- [Developer-Y/cs-video-courses: List of Computer Science courses with video lectures.](https://github.com/Developer-Y/cs-video-courses) #list#course
- [Long.bitCount() 解析 | 吴俊笔记本](https://wujun234.github.io/01%20%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84%E4%B8%8E%E7%AE%97%E6%B3%95/Long.bitCount()%20%E8%A7%A3%E6%9E%90/) JDK 中计算为 1 的比特位的神奇方法 #read#blog#java#hack
- [吴俊笔记本](https://wujun234.github.io/) #books#read
- [labuladong 的算法小抄](https://labuladong.gitbook.io/algo/) #books#read
- [Java 全栈知识体系](https://www.pdai.tech/) 包含: Java 基础, Java 部分源码, JVM, Spring, Spring Boot, Spring Cloud, 数据库原理, MySQL, ElasticSearch, MongoDB, Docker, k8s, CI&CD, Linux, DevOps, 分布式, 中间件, 开发工具, Git, IDE, 源码阅读，读书笔记, 开源项目... #read#books
- [Why are hyperlinks blue? | The Mozilla Blog](https://blog.mozilla.org/en/internet-culture/deep-dives/why-are-hyperlinks-blue/) #blog#read
- [The Logfile Navigator](https://lnav.org/) 一个强大的命令行日志查看器，支持彩色、SQL、时间线 #tools
- [RAWGraphs](https://rawgraphs.io/) CSV 数据可视化，前端实现 #tools#visual
- [云开发 Webify | 云开发 Webify](https://webify.cloudbase.net/) 腾讯云的 netify 山寨版 #tools
- [如何愉快地写个小parser](https://zhuanlan.zhihu.com/p/20178871) #read
- [自己动手写编译器 — 自己动手写编译器](https://pandolia.net/tinyc/index.html) tinyc #books
- [Systemizer - A system design tool](https://honzaap.github.io/Systemizer/) 画系统架构图 #tools#visual
- [Calligrapher.ai: Realistic computer-generated handwriting](https://www.calligrapher.ai/) 生成手写
- [New in Git: switch and restore](https://www.banterly.net/2021/07/31/new-in-git-switch-and-restore/) switch 切换分支，restore 恢复内容 #blog#read
- [How I built a business that lets me live on the beach full time](https://www.expatsoftware.com/Articles/guy-on-the-beach-with-a-laptop.html) #blog
- [How to improve your Docker containers security - [cheat sheet]](https://blog.gitguardian.com/how-to-improve-your-docker-containers-security-cheat-sheet/) Docker 容器安全性 #backend#infra#blog#read
- [How MDN’s autocomplete search works – Mozilla Hacks - the Web developer blog](https://hacks.mozilla.org/2021/08/mdns-autocomplete-search/) #frontend#blog#read
- [速度与压缩比如何兼得？压缩算法在构建部署中的优化](https://tech.meituan.com/2021/01/07/pack-gzip-zstd-lz4.html) #blog
- [Founders Guide: Complex Projects 101](https://vadimkravcenko.com/en/dealing-with-complex-projects/) #read
- [Postgres Full-Text Search: A Search Engine in a Database](https://blog.crunchydata.com/blog/postgres-full-text-search-a-search-engine-in-a-database) Postgres 自带的英文全文搜索 #tools#db#backend
- [Hora | Hora Search Everywhere](https://horasearch.com/) 搜索相似 #tools
- [yifeikong/interview: solutions to all kinds of questions for an interview](https://github.com/yifeikong/interview) 常见面试算法题突击手册 #interview#tips
- [yifeikong/reverse-interview-zh: 技术面试最后反问面试官的话](https://github.com/yifeikong/reverse-interview-zh) #interview#tips
- [Introduction to Information Retrieval](https://nlp.stanford.edu/IR-book/) #books
- [Introduction - Rust and WebAssembly](https://rustwasm.github.io/docs/book/introduction.html) #books
- [Webhook Infrastructure and Tooling - Hookdeck](https://hookdeck.com/) #tools#backend
- [Using CSS without HTML · Mathias Bynens](https://mathiasbynens.be/notes/css-without-html) #blog#read#frontend#css
- [Dark Mode in One Line of Code!](https://davidwalsh.name/dark-mode-invert-filter) html filter invert(1) #frontend
- [Modeling mutual friendship](https://minimalmodeling.substack.com/p/modeling-mutual-friendship) Two-row model vs. One-row model #blog#read#backend#db
- [如何优化 node 项目的 docker 镜像（像老板压榨员工一样压榨镜像）](https://juejin.cn/post/6991689670027542564) #blog#read#backend
- [当你想来一把数独](https://me.guanghechen.com/post/game/sudoku/) 如何生成一个数独 #read#blog
- [Best Pitch Decks](https://www.pitchdeckhunt.com/best-pitch-decks) Startup Pitch Examples #tools
- [Feed me up, Scotty!](https://feed-me-up-scotty.vincenttunru.com/) CSS selector based RSS Generator #tools
- [10 Predictions for the Future of Computing or; the Inane Ramblings of our Chief Scientist](https://blog.container-solutions.com/10-predictions-for-the-future-of-computing) #blog#read
- [arogozhnikov/einops: Deep learning operations reinvented (for pytorch, tensorflow, jax and others)](https://github.com/arogozhnikov/einops) #tools#dl
- [从一个Emoji字符说起](https://blog.xuwei.fun/2020/09/07/characterset/) Unicode 漫谈 #read
- [The Twelve-Factor App （简体中文）](https://12factor.net/zh_cn/) SaaS 应用方法论 #arch#read
- [HTTPie – command-line HTTP client for the API era](https://httpie.io/) #tools
- [.bashrc generator: create your .bashrc PS1 with a drag and drop interface](http://bashrcgenerator.com/) Generate Bash Prefix tooltips #tools
- [yozora/README-zh.md at main · yozorajs/yozora](https://github.com/yozorajs/yozora) Markdown MST Generation #tools
- [Scimago Graphica | A new way to explore, visually communicate and make sense of data](https://graphica.app/) visualization tools #visual#tools
- [Let’s build our own ‘nodemon’ in under 10 minutes!](https://blog.pankajtanwar.in/have-you-ever-thought-how-nodemon-works-internally-lets-build-our-own-nodemon-in-under-10-minutes) #node#backend
- [The (too) many pitfalls of VLA in C](https://blog.joren.ga/programming/vla-bad) #c
- [PostgreSQL的数据变化捕获和实时通知——基于Listen-Notify和Server-Sent Events](http://kaifeiji.cc/post/change-data-capture-and-instant-notification-on-postgresql-via-listen-notify-and-server-sent-events/) #db
- [一日一技 | 集中管理与备份 Windows 分散各处的应用配置文件 - 少数派](https://sspai.com/post/67829) #tips#windows
- [程序员可能必读书单推荐（一） - 面向信仰编程](https:/draveness.me/books-1) #books
- [Utopia: Design and Code on one platform](https://utopia.app/) React Drag-Drop Editor #frontend#tools
- [Git: An Interactive History](https://git-history.jpalmer.dev/) #ui#read
- [How to Measure Execution Time of a Program](https://serhack.me/articles/measure-execution-time-program/) #read
- [15 Tips for Better Signup / Login UX](https://learnui.design/blog/tips-signup-login-ux.html) #ui#frontend
- [Tesla AI chief explains why self-driving cars don’t need lidar](https://venturebeat.com/2021/07/03/tesla-ai-chief-explains-why-self-driving-cars-dont-need-lidar/)
- [重新認識 Pixel、DPI / PPI 以及像素密度 | INFOLINK Blog](https://blog.infolink.com.tw/2021/rediscover-pixel-dpi-ppi-and-pixel-density/)
- [理解VirtualBox网络](https://www.junmajinlong.com/virtual/network/virtualbox_net/) #misc
- [B站高可用用架构实践 - 云+社区 - 腾讯云](https://cloud.tencent.com/developer/article/1618923) #infra
- [Elevator Saga - help and API documentation](http://play.elevatorsaga.com/documentation.html#docs) 一个写电梯逻辑的游戏 #game
- [Linux IO模式及 select、poll、epoll详解](https://segmentfault.com/a/1190000003063859) #backend#kernel
- [Avoiding complexity with systemd](https://mgdm.net/weblog/systemd/) 用 systemd 自启服务 #linux
- [Nuitka/Nuitka](https://github.com/Nuitka/Nuitka) a Python compiler written in Python #tools
- [SQL queries don't start with SELECT](https://jvns.ca/blog/2019/10/03/sql-queries-don-t-start-with-select/) #db
- [How to circumvent Sci-Hub ISP block](https://fragile-credences.github.io/scihub-proxy/) using manually crafted PAC files
- [Java: Formatting byte size to human readable format | Programming.Guide](https://programming.guide/java/formatting-byte-size-to-human-readable-format.html)
- [The most copied StackOverflow snippet of all time is flawed! | Programming.Guide](https://programming.guide/worlds-most-copied-so-snippet.html)
- [Hosting SQLite databases on Github Pages - (or any static file hoster) - phiresky's blog](https://phiresky.github.io/blog/2021/hosting-sqlite-databases-on-github-pages/) #frontend
- [M.I.T. 6.004 Computation Structures](https://computationstructures.org/index.html) #course
- [Image Filtering - Lode's Computer Graphics Tutorial](https://lodev.org/cgtutor/filtering.html) 卷积里用的 filter 是如何构造的 #dl
- [Deep JavaScript: Theory and techniques](https://exploringjs.com/deep-js/index.html) #books
- [热重载 C - CJ Ting's Blog](https://cjting.me/2021/06/10/hot-reload-c/) #c#hack
- [sorenisanerd/gotty](https://github.com/sorenisanerd/gotty) Share your terminal as a web application #tools
- [cs01/termpair](https://github.com/cs01/termpair) View and control terminals from your browser with end-to-end encryption 🔒 #tools
- [Representing SHA-256 Hashes As Avatars](https://francoisbest.com/posts/2021/hashvatars) #visual
- [Polyomino Solver](https://cemulate.github.io/polyomino-solver/) Solves the calendar puzzle #tools
- [VOSK Offline Speech Recognition API](https://alphacephei.com/vosk/) #api
- [Introducing WebContainers: Run Node.js natively in your browser](https://blog.stackblitz.com/posts/introducing-webcontainers/) #framework#frontend
- [Web 中文字体应用指南 · Ruby China](https://ruby-china.org/topics/14005) #frontend
- [使用正则表达式匹配 3 的倍数](https://zhuanlan.zhihu.com/p/39022144) #regex
- [Experiences working with an Outsourced Dev Shop](https://software.rajivprab.com/2021/04/26/experiences-working-with-an-outsourced-dev-shop/)
- [Why do database columns have a character length of 191?](https://www.grouparoo.com/blog/varchar-191) #db#backend
- [Be more productive with use of your BASH history · cyb.org.uk](https://cyb.org.uk/2021/05/03/bash-productivity.html) #cli
- [Compose for Web UI Framework | JetBrains: Developer Tools for Professionals and Teams](https://compose-web.ui.pages.jetbrains.team/) #web#framework
- [Compose for Web UI Framework | JetBrains: Developer Tools for Professionals and Teams](https://compose-web.ui.pages.jetbrains.team/) #web
- [narakeet - From Markdown to Video](https://www.narakeet.com/docs/script/) #video#tools
- [you-dont-need/You-Dont-Need-GUI](https://github.com/you-dont-need/You-Dont-Need-GUI) #cli
- [arogozhnikov/einops](https://github.com/arogozhnikov/einops) 魔改 tensor 操作库 #ml#tensor
- [凤凰架构：构筑可靠的大型分布式系统 | 凤凰架构](http://icyfenix.cn/) 一本讲分布式的开源书籍 #books#backend#distributed
- [Learn CSS](https://web.dev/learn/css/) Google 的 CSS 教程 #css#frontend
- [Magician](http://magician-io.com/) 异步非阻塞的网络协议解析包 #tools#network#java

# About

- This file is auto-generated by [osmos::memo](https://github.com/osmoscraft/osmosmemo).
- New content will appear on top when you click "save" button in the tool.
- To search use <kbd>Ctrl</kbd> + <kbd>F</kbd>, or <kbd>Command</kbd> + <kbd>F</kbd> on Mac.
