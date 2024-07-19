// --------------------------------------------- homefeed 接口 / headers x-s --------------------------------------------
// 导入已处理的环境
require("./homefeed_env")

// 导入扣下的JS源码
require("./homefeed_x_s_source")

// 测试接口
function get_x_s(c, i) {
    const result = window._webmsxyw(c, i);
    if (result["X-s"].length === 604) {
        console.log("成功获取解密结果:::", result);
        return result["X-s"]
    } else {
        console.log("解密结果获取失败!!!", result);
        return ""
    }
}

