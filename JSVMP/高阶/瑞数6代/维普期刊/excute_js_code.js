// ---------------------------------------------------  cookie 生成环境  -------------------------------------------------
let content = "meta_content";

// 1、补充 window 对象
window = global;

// 网站会检测 "__filename"/"__dirname" 关键字是否可用，来判断是否为真实的浏览器环境
delete __filename;
delete __dirname;
null_function = function (){
    console.log("--- args ---", ...arguments)
}

// 补充 window 对象下其他需要的环境
window.top = window;
setTimeout = null_function;
setInterval = null_function;
window.addEventListener = function (res1, res2, res3) {
    console.log("当前执行 window 当中的 addEventListener 方法：", res1, res2, res3);
};
window.attachEvent = function (res1, res2) {
    console.log("当前执行 window 当中的 attachEvent 方法：", res1, res2);
};

window.ActiveXObject = function (res) {
    console.log("当前执行 window 当中的 ActiveXObject 方法：", res);
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
meta = [
    {
        getAttribute: function (res) {
            console.log("当前执行 meta 当中的 getAttribute 方法：", res);
            if (res === "r"){
                return "m"
            }
        },
        http_equiv: "Content-Type",
        content: "text/html; charset=utf-8",
    },
    {
        getAttribute: function (res) {
            console.log("当前执行 meta 当中的 getAttribute 方法：", res);
            if (res === "r"){
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
        if (res === "base") {
            return {}
        }
        console.log("当前执行 document 当中的 getElementsByTagName *** 缺失方法 ***：", res);
    },
    addEventListener: function (res1, res2, res3) {
        console.log("当前执行 window 当中的 addEventListener 方法：", res1, res2, res3);
    },
    attachEvent: function (res1, res2) {
        console.log("当前执行 window 当中的 attachEvent 方法：", res1, res2);
    },

    getElementById: function (res) {
        console.log("当前执行 document 当中的 getElementById 方法：", res);
    },
};

// 3、补充 navigator 对象
navigator = {
    appCodeName: "Mozilla",
    appName: "Netscape",
    appVersion: "5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    userAgent: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
};

// 4、补充 location 对象
location = {
    "href": "http://zxgk.court.gov.cn/",
    "protocol": "http:",
    "host": "zxgk.court.gov.cn",
    "hostname": "zxgk.court.gov.cn",
};

// 5、补充 screen 对象

// 6、补充 localStorage 对象



// ------------------------------------------------  cookie _ts 代码段 一  -----------------------------------------------
"ts_code_1"



// ------------------------------------------------  cookie _ts 代码段 二  -----------------------------------------------
"ts_code_2"



// ----------------------------------------------------  cookie 返回  ---------------------------------------------------
function get_ZuT() {
    let cookie = document.cookie.split(";")[0].split("=")[1];
    console.log(cookie.length)
    return cookie;
}
