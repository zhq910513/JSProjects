// --------------------------------------------- hot board 接口 / 参数 _signature --------------------------------------------
// 导入已处理的环境
require("./hotboard_env")
require("./hotboard_signature_source")


// 测试接口
function get_signature(o, cookie) {
    document.cookie = cookie;
    return window.byted_acrawler.sign(o)
}

// result = get_signature(_cookie)
//
// if (result.length === 147) {
//     console.log("成功获取解密结果:::", result);
// } else {
//     console.log("解密结果获取失败!!!", result);
// }