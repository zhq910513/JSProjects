// -----------------------------------------------------   x-s 环境  ----------------------------------------------------

// 1、补充 window 对象
window = global;

// 部分网站会检测 "global"/"Buffer" 关键字是否可用，来判断是否为真实的浏览器环境
delete global;

// 拼多多检测
delete Buffer;

// 补充 window 对象下其他需要的环境
window.CanvasRenderingContext2D = {};
window.HTMLCanvasElement = {};
window.devicePixelRatio = 1.5;
window.AudioContext = function () {};

canvas = {
    getContext: function (res) {
        console.log("当前执行 document 当中的 getContext 方法：", res);
    }
}

// 2、补充 document 对象
document = {
    createElement: function (res) {
        console.log("当前执行 document 当中的 createEvent 方法：", res);
        if (res === "canvas") {
            return canvas
        } else if (res === "div") {
            return "div"
        }
        console.log("当前执行 document 当中的 createElement 方法  *缺失*：", res);
    },
    documentElement: function (res) {
        console.log("当前执行 document 当中的 documentElement 方法：", res);
    },
    cookie: 'abRequestId=0b6dbe190547857cdafdb403cf2cae21; a1=18edb3cedecsru1wqpkagnqm8to45yb8wt46a25if50000213178; webId=047f355453a1b18da1796624246d1d8e; gid=yYdfDqSiJqEDyYdfDqSdf9J2dSMF7yEAUT0k43iIA6Y9lK2842vDY0888JyqyWY80yJyJqfJ; xsecappid=xhs-pc-web; webBuild=4.24.2; websectiga=cf46039d1971c7b9a650d87269f31ac8fe3bf71d61ebf9d9a0a87efb414b816c; sec_poison_id=5effc910-e9f4-4a33-b007-e330ef1b2b3e'
};

// 3、补充 navigator 对象
navigator = {
    appCodeName: "Mozilla",
    appName: "Netscape",
    appVersion: "5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    userAgent: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
};

// 4、补充 location 对象
location = {
    "ancestorOrigins": {},
    "href": "https://www.xiaohongshu.com/explore?channel_id=homefeed.food_v3",
    "origin": "https://www.xiaohongshu.com",
    "protocol": "https:",
    "host": "www.xiaohongshu.com",
    "hostname": "www.xiaohongshu.com",
    "port": "",
    "pathname": "/explore",
    "search": "?channel_id=homefeed.food_v3",
    "hash": ""
};

// 5、补充 screen 对象
screen = {};

// 6、补充 localStorage 对象
localStorage = {
    getItem: function () {

    },
};


// ====================================================   代理吐环境   ===================================================
require("../../../环境检测框架/proxy吐环境")