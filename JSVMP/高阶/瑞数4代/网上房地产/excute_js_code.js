let content = "meta_content";

// 1、补充 window 对象
window = global;

// 网站会检测 "__filename"/"__dirname" 关键字是否可用，来判断是否为真实的浏览器环境
delete __filename;
delete __dirname;

// 补充 window 对象下其他需要的环境
null_function = function (){
    console.log("--- args ---", ...arguments)
}
setTimeout = null_function;
setInterval = null_function;
window.top = window;
window.addEventListener = function (res1, res2, res3) {
    console.log("当前执行 window 当中的 addEventListener 方法：", res1, res2, res3);
};
window.attachEvent = function (res1, res2) {
    console.log("当前执行 window 当中的 attachEvent 方法：", res1, res2);
};

// 2、补充 document 对象
div = {
    getElementsByTagName: function (res) {
        console.log("当前执行 div 当中的 getElementsByTagName 方法：", res);
        if (res === "i") {
            return {}
        }
    }
};
meta = [
    {
        getAttribute: function (res) {
            console.log("当前执行 meta 当中的 getAttribute 方法：", res);
            if (res === "r") {
                return "m"
            }
        },
        content: content,
        parentNode: {
            removeChild: function (res) {
                console.log("当前执行 meta 当中的 removeChild 方法：", res);
            }
        }
    }
];
script = [
    {
        type: "text/javascript",
        getAttribute: function (res) {
            console.log("当前执行 script 当中的 getAttribute 方法：", res);
            if (res === "r") {
                return "m"
            }

            console.log("当前执行 script 当中的 getAttribute 方法  *缺失*：", res);
        },
        parentElement: {
            removeChild: function (res) {
                console.log("当前执行 script 当中父节点的 removeChild 方法：", res);
            }
        }
    }
];
document = {
    createElement: function (res) {
        console.log("当前执行 document 当中的 createElement 方法：", res);
        if (res === "div") {
            return div;
        }
    },
    getElementsByTagName: function (res) {
        console.log("当前执行 document 当中的 getElementsByTagName 方法：", res);
        if (res === "meta") {
            return meta
        }
        if (res === "script") {
            return script
        }
        console.log("当前执行 document 当中的 getElementsByTagName *** 缺失方法 ***：", res);
    },
    addEventListener: function (res1, res2, res3) {
        console.log("当前执行 window 当中的 addEventListener 方法：", res1, res2, res3);
    },
    attachEvent: function (res1, res2) {
        console.log("当前执行 window 当中的 attachEvent 方法：", res1, res2);
    },
};

// 3、补充 navigator 对象
navigator = {
    appCodeName: "Mozilla",
    appName: "Netscape",
    appVersion: "5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    userAgent: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
}

// 4、补充 location 对象
location = {
    "ancestorOrigins": {},
    "href": "http://www.fangdi.com.cn/index.html",
    "origin": "http://www.fangdi.com.cn",
    "protocol": "http:",
    "host": "www.fangdi.com.cn",
    "hostname": "www.fangdi.com.cn",
    "port": "",
    "pathname": "/index.html",
    "search": "",
    "hash": ""
};

// 5、补充 screen 对象

// 6、补充 localStorage 对象



// 待写入的第一段 JS 代码
"ts_code_1"



// 待写入的第二段 JS 代码
"ts_code_2"



function get_80T() {
    let cookie = document.cookie.split(";")[0].split("=")[1];
    console.log(cookie.length)
    return cookie;
}