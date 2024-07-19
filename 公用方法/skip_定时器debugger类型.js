// 处理debugger   包含: var a = new Date();

var _Function = Function

Function = function (s) {
    if (s === "debugger") {
        console.log(s);
        return null;
    }
    return _Function(s);
}