var _eval = eval;

eval = function (src) {
    console.log("eval 截断开始...");
    debugger;
    _eval.apply(this, src);
    console.log("eval 截断结束！");
}
