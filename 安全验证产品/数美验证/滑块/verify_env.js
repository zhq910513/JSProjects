// -----------------------------------------------------   verify 环境  ------------------------------------------------

window = global;

window.opr = function () {};

// 2、补充 document 对象
document = {
    createElement: function (res) {
        console.log("当前执行 document 当中的 createElement 方法：", res);
    },
    getElementsByTagName: function (res) {
        console.log("当前执行 document 当中的 getElementsByTagName 方法：", res);
        if (res === "head"){
            return {}
        }
        console.log("当前执行 document 当中的 getElementsByTagName 方法  *缺失*：", res);
    },
    documentElement: {
        getAttribute: function (res) {
            console.log("当前执行 document 当中的 getAttribute 方法：", res);
        },
        doScroll: function (res) {
            console.log("当前执行 document 当中的 doScroll 方法：", res);
        },
    },
    addEventListener: function () {},
    attachEvent: function () {},
    readyState: "complete",
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
    "href": "https://www.ishumei.com/trial/captcha.html",
    "origin": "https://www.ishumei.com",
    "protocol": "https:",
    "host": "www.ishumei.com",
    "hostname": "www.ishumei.com",
    "port": "",
    "pathname": "/trial/captcha.html",
    "search": "",
    "hash": ""
};

// 5、补充 screen 对象
screen = {};


// ====================================================   代理吐环境   ===================================================
require("D:\\Projects\\逆向项目\\环境检测框架\\proxy吐环境")