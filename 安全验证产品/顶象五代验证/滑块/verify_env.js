// -----------------------------------------------------   ac 环境  ----------------------------------------------------

// 1、补充 window 对象
window = global;
global.self = global;
global.top = global;
// 部分网站会检测 "global"/"Buffer" 关键字是否可用，来判断是否为真实的浏览器环境
delete global;

// 拼多多检测
delete Buffer;

// 补充 window 对象下其他需要的环境
window.addEventListener = function () {
};
window.attachEvent = function () {
};

window.outerHeight = 912;
window.outerWidth = 1440;
window.innerHeight = 912;
window.innerWidth = 1440;
window.screenTop = 0;
window.screenLeft = 0;

// 2、补充 document 对象
document = {
    referrer: "https://www.dingxiang-inc.com/",
    createElement: function (tagName) {
        // 创建元素的逻辑
        return {
            tagName: tagName.toUpperCase(),
            setAttribute: function (name, value) {
                // 设置属性的逻辑
            },
            appendChild: function (child) {
                // 添加子元素的逻辑
            },
            innerHTML: ""
        };
    },
    documentElement: {
        getAttribute: function () {},
        doScroll: function () {},
    },
    addEventListener: function (type, listener, options) {
        // 添加事件监听器的逻辑
    },
    attachEvent: function (event, listener) {
        // 附加事件监听器的逻辑
    },

    readyState: "complete",
    getElementsByTagName: function (tagName) {
        // 获取指定标签名的元素列表
        var elements = [];
        // 示例：这里可以添加一些模拟元素
        if (tagName.toLowerCase() === "p") {
            elements.push({
                tagName: "P",
                innerText: "Example paragraph"
            });
        }
        return elements;
    },
    getElementById: function (id) {
        // 获取指定 ID 的元素
        return {
            id: id,
            tagName: "DIV",
            getElementsByTagName: function (tagName) {
                // 获取该元素内的指定标签名的元素列表
                var elements = [];
                if (tagName.toLowerCase() === "p") {
                    elements.push({
                        tagName: "P",
                        innerText: "Example paragraph inside element with ID"
                    });
                }
                return elements;
            },
            appendChild: function (child) {
                // 添加子元素的逻辑
            },
            innerHTML: ""
        };
    },
    title: "Document Title",
    body: {
        tagName: "BODY",
        appendChild: function (child) {
            // 添加子元素的逻辑
        },
        innerHTML: ""
    },
    head: {
        tagName: "HEAD",
        appendChild: function (child) {
            // 添加子元素的逻辑
        },
        innerHTML: ""
    }
};

// 3、补充 navigator 对象
navigator = {
    webdriver: false,
    appCodeName: "Mozilla",
    appName: "Netscape",
    appVersion: "5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    userAgent: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    platform: "Win32",
    language: "en-US",
    languages: ["en-US", "en"],
    online: true,
    javaEnabled: function () {
        return false;
    },
    cookieEnabled: true,
    doNotTrack: null,
    geolocation: {
        getCurrentPosition: function (successCallback, errorCallback, options) {
            // 模拟位置
            var position = {
                coords: {
                    latitude: 37.7749,
                    longitude: -122.4194,
                    altitude: null,
                    accuracy: 100,
                    altitudeAccuracy: null,
                    heading: null,
                    speed: null
                },
                timestamp: Date.now()
            };
            successCallback(position);
        },
        watchPosition: function (successCallback, errorCallback, options) {
            // 这里可以实现一个简单的模拟
            return setInterval(function () {
                var position = {
                    coords: {
                        latitude: 37.7749,
                        longitude: -122.4194,
                        altitude: null,
                        accuracy: 100,
                        altitudeAccuracy: null,
                        heading: null,
                        speed: null
                    },
                    timestamp: Date.now()
                };
                successCallback(position);
            }, 1000);
        },
        clearWatch: function (watchId) {
            clearInterval(watchId);
        }
    }
};

// 4、补充 location 对象
location = {
    "ancestorOrigins": {},
    "href": "https://www.dingxiang-inc.com/business/captcha",
    "origin": "https://www.dingxiang-inc.com",
    "protocol": "https:",
    "host": "www.dingxiang-inc.com",
    "hostname": "www.dingxiang-inc.com",
    "port": "",
    "pathname": "/business/captcha",
    "search": "",
    "hash": ""
};

// 5、补充 screen 对象
screen = {
    width: 1920,
    height: 1080,
    availHeight: 912,
    availWidth: 1440,
};

// 6、补充 localStorage 对象
// localStorage = {
// };


// ====================================================   代理吐环境   ===================================================
require("D:\\Projects\\逆向项目\\环境检测框架\\proxy吐环境")