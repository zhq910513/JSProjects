(function () {
    'use strict'
    var _cookie = "";
    Object.defineProperty(document, "cookie", {
        set: function (val) {
            console.log("设置了 Cooke:::", val);
            debugger;
            _cookie = val;
            return _cookie;
        },
        get: function () {
            return _cookie;
        },
    })
})()
