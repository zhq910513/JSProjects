// 去除无限debugger   只包含: debugger;

Function.prototype.__constructor_back = Function.prototype.constructor;
Function.prototype.constructor = function () {
    if(arguments && typeof arguments[0] === "string"){
        if("debugger" === arguments[0]) {
            return
        }
    }
    return Function.prototype.__constructor_back.apply(this.arguments);
};