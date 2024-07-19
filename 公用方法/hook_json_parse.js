(function () {
    var parse = JSON.parse;
    JSON.parse = function (params) {
        console.log("Hook JSON.parse:::", params);

        // 条件断点
        if (params.indexOf("result")){
            debugger;
        }

        // 无差别断点
        // debugger;

        return parse(params);
    }
})();