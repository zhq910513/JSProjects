// ----------------------------------------------------- cookie _ts ----------------------------------------------------
// 导入已处理的环境
require("./cookie_env")

// 导入扣下的JS源码
require("./cookie_ts_source_part_1")
require("./cookie_ts_source_part_2")


function get_80T() {
    let cookie = document.cookie.split(";")[0].split("=")[1];
    console.log(cookie.length)
    return cookie;
}

console.log(get_80T())

