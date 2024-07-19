// ----------------------------------------------------- cookie _ts ----------------------------------------------------
// 导入已处理的环境
require("./cookie_env")

// 导入扣下的JS源码
require("./cookie_ts_source_part_1")
require("./cookie_ts_source_part_2")
// require("./code")

function get_ywP() {
    let cookie = document.cookie.split(";")[0].split("=")[1];
    console.log(cookie.length)
    return cookie;
}

console.log(get_ywP())

// 服务器返回Cookie
// acw_tc=276aedc317211043867113493e231d396da8447bbd63d7a4859a2840dafc84;
// NfBCSins2OywO=60ujYD50sNgqq5qIkHIt2Bg9ndlEp9CzYVd3GLI1M0QfMRbgRww_ornSehTs0WaUgBOtaOtMwQXl6ap8QVte26uA;

// 返回 JS 代码生成  长度
// NfBCSins2OywP=056AJ9mFDBpFkjtNQmbtIfLUwdmG6tAtUk4O
// .ZBVYGw_oZiMDqdjnUHYW2_cHLzJON9UtGVWGaGj96bfQrtg5kcxMzB2RZx_za2z4qVfiBuDFQSV3W3SgcogxtlYIbT6lD
// .ssGlmwYY8lSLy8oR1CfUKhDXNE_njXy411PRjixzZZ.m3XQGGUqJmb2RVdKI2pwXaHLinZun9d91uN0KvK0wo3dwrlc1lKSYArS6OrVmg

// 生成 cookie 长度
// 236   364   428
// 257   385   449
