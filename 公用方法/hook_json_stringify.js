// 技巧：post请求参数可以浏览器 atob(加密内容) 解码

(function () {
    var stringify = JSON.stringify;
    JSON.stringify = function (params) {
        console.log("Hook JSON.stringify:::", params);

        // 条件断点
        if (params["payload"]){
            debugger;
        }

        // 无差别断点
        // debugger;

        return stringify(params);
    }
})();