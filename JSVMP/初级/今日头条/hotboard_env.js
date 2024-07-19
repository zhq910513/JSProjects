// --------------------------------------------------   _signature 环境  -------------------------------------------------

// 1、补充 window 对象
window = global;

// 部分网站会检测 "global"/"Buffer" 关键字是否可用，来判断是否为真实的浏览器环境
delete global;

// 拼多多检测
delete Buffer;

window._$jsvmprt = function () {
};


// 2、补充 document 对象
document = {
    cookie: "",
    referrer: "https://www.toutiao.com/",
    createElement: function (res) {
        console.log("当前执行 document 当中的 createElement 方法：", res);
    },
    createEvent: function (res) {
        console.log("当前执行 document 当中的 createEvent 方法：", res);
    },
};


// 3、补充 location 对象
location = {
    "ancestorOrigins": {},
    "href": "https://www.toutiao.com/",
    "origin": "https://www.toutiao.com",
    "protocol": "https:",
    "host": "www.toutiao.com",
    "hostname": "www.toutiao.com",
    "port": "",
    "pathname": "/",
    "search": "",
    "hash": ""
};


// 4、补充 navigator 对象
navigator = {
    appCodeName: "Mozilla",
    appName: "Netscape",
    appVersion: "5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    userAgent: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
};


// 5、补充 screen 对象
screen = {
    availHeight: 912,
    availLeft: 0,
    availTop: 0,
    availWidth: 1440,
    colorDepth: 24,
    height: 960,
    pixelDepth:24,
    width:1440,
};

// 6、补充 sessionStorage 对象
sessionStorage = {
    getItem: function () {
    },
};

// 7、补充 localStorage 对象
localStorage = {
    getItem: function () {
    },
};


// ====================================================   代理吐环境   ===================================================
require("D:\\Projects\\逆向项目\\环境检测框架\\proxy吐环境")