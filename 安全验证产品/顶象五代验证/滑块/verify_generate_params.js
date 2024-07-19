// --------------------------------------------- homefeed 接口 / headers x-s --------------------------------------------
// 导入已处理的环境
require("./verify_env")

// 导入扣下的JS源码
require("./verify_ac_source_1")

console.log(window)

function get_ac(sid, tarck_list, x, y) {
    let n = {
        "token": sid
    };

    let w_xpath = "/html/body/div[11]";

    let UA = window._dx.UA.init(n);
    // console.log("UA:::", UA.ua.length)

    // TODO 找不到生成处，为什么要这么写？
    // 加入轨迹
    for (let index = 0; index < tarck_list.length; index++) {
        // console.log(UA.__proto__.tm)
        UA.__proto__.tm = new Date().getTime() - tarck_list[index][2]
        UA.recordSA({"pageX": tarck_list[index][0], "pageY": tarck_list[index][1]})
    }

    // 经过验证 sendSA   sendTemp   经过这两个方法 ua 会拼接长度变长
    UA.sendSA()
    UA.sendTemp({
        "xpath": w_xpath,
        "x": x,
        "y": y
    })
    // w_xpath为空，sendTemp则走下面
    // UA.sendTemp("x=" + x + "&y=" + y)

    const ac = UA.getUA();
    console.log("ac:::", ac.length)

    return UA.getUA()
}

tcck = [[0, 2, 0], [7, 3, 97], [22, 2, 185], [30, 2, 271], [45, 5, 358], [60, 1, 441], [80, -4, 528], [81, -2, 625], [97, -2, 727], [110, 2, 838], [130, 0, 929], [137, -2, 1011], [148, -1, 1120], [164, 1, 1233], [178, 3, 1343], [194, -1, 1431], [200, -5, 1531], [208, 2, 1643], [215, -2, 1759], [227, -3, 1869], [237, 2, 1968], [245, -2, 2056], [252, -4, 2152], [263, 2, 2234], [264, -1, 2335], [276, -4, 2437], [277, -2, 2545], [277, 2, 2664]];

console.log(get_ac("77389d615a8554eddcf66492bc3dba88", tcck, 277, 37))
