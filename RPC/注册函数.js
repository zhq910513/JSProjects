// 目标函数 Decrypt
demo.regAction("getData", function (resolve,param) {
    //这里还是param参数 param里面的key 是先这里写，但到时候传接口就必须对应的上
    var result = Decrypt(param["param_1_name"],param["param_2_name"])
    resolve(result);
})