// 处理debugger   包含: debugger;_$db(17153426617510)

var _constructor = Function.prototype.constructor;

Function.prototype.constructor = function (s) {
    if (s === "debugger") {
        console.log(s);
        return function() {}; // 返回一个空函数
    }
    return _constructor.call(this, s);
};
