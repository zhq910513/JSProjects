// function _0x2d350e() {
//     var _0x49a2b0 = _0x247065
//       , _0x1163e8 = ''
//       , _0x40ad39 = _0x49a2b0(0x42a)
//       , _0x3531f2 = _0x40ad39['length'];
//     for (var _0x235133 = -0x149e + -0x231d * 0x1 + -0x37bb * -0x1; _0x235133 < -0x2214 + 0xd * 0x223 + 0xe9 * 0x7; _0x235133++) {
//         _0x1163e8 += _0x40ad39['charAt'](Math[_0x49a2b0(0x2c6)](Math[_0x49a2b0(0x134)]() * _0x3531f2));
//     }
//     return _0x529f28[_0x49a2b0(0x294)](this[_0x49a2b0(0x232)](), _0x1163e8);
// }

// 单步调试后代码
// _0x49a2b0 是个方法对象  直接取到所用方法后可以删除，不需要加载全部方法
// _0x49a2b0(0x42a) = "ABCDEFGHJKMNPQRSTWXYZabcdefhijkmnprstwxyz2345678"  重命名为 salt
// _0x40ad39['length'] = 48  重命名为 salt_length
// -0x149e + -0x231d * 0x1 + -0x37bb * -0x1 = 0
// _0x235133 设置成 i
// -0x2214 + 0xd * 0x223 + 0xe9 * 0x7 = 18
// _0x1163e8 设置成 result_str
// _0x49a2b0(0x2c6) = "floor"
// _0x49a2b0(0x134) = "random"
// _0x49a2b0(0x294) = "RILLV"
// _0x49a2b0(0x232) = "generateTimeFormat"

// generateTimeFormat  找到方法
// function generateTimeFormat() {
//     var _0x22a162 = _0x247065
//       , _0x17a50d = {
//         'quGfF': function(_0x4a7d31, _0x590206) {
//             var _0x15591b = _0x1f0d;
//             return _0x529f28[_0x15591b(0x38c)](_0x4a7d31, _0x590206);
//         },
//         'CJGuh': function(_0xc09495, _0x4ee56d) {
//             var _0x58a401 = _0x1f0d;
//             return _0x529f28[_0x58a401(0x5d6)](_0xc09495, _0x4ee56d);
//         }
//     }
//       , _0x1b3e3d = new Date()
//       , _0x2170bf = function _0x1b206b(_0x27ca65) {
//         var _0x4fd5cc = _0x1f0d;
//         return _0x17a50d['quGfF'](+_0x27ca65, 0x9f9 * 0x2 + 0x13c8 * 0x1 + -0x27b0) ? _0x17a50d[_0x4fd5cc(0x329)]('0', _0x27ca65) : _0x27ca65[_0x4fd5cc(0x423)]();
//     };
//     return _0x529f28[_0x22a162(0x5d6)](_0x529f28[_0x22a162(0x5d6)](_0x529f28[_0x22a162(0x44f)](_0x529f28[_0x22a162(0x16d)](_0x529f28[_0x22a162(0x1ea)](_0x1b3e3d[_0x22a162(0x341)]()[_0x22a162(0x423)](), _0x529f28[_0x22a162(0x24a)](_0x2170bf, _0x529f28[_0x22a162(0x294)](_0x1b3e3d[_0x22a162(0x628)](), -0x5c + -0x8f * -0xc + -0x3 * 0x21d))), _0x2170bf(_0x1b3e3d[_0x22a162(0x22d)]())), _0x529f28[_0x22a162(0x27e)](_0x2170bf, _0x1b3e3d['getHours']())), _0x2170bf(_0x1b3e3d[_0x22a162(0x10b)]())), _0x2170bf(_0x1b3e3d[_0x22a162(0x486)]()));
// }
// _0x22a162(0x5d6) = "obmuT"
// _0x22a162(0x44f) = "rZQOM"
// _0x22a162(0x16d) = "BqJvQ"
// _0x22a162(0x1ea) = "ddKQQ"
// _0x22a162(0x341) = "getFullYear"
// _0x22a162(0x423) = "toString"
// _0x22a162(0x24a) = "Lfobh"
// _0x22a162(0x294) = "RILLV"
// _0x22a162(0x628) = "getMonth"
// -0x5c + -0x8f * -0xc + -0x3 * 0x21d = 1
// _0x22a162(0x22d) = "getDate"
// _0x22a162(0x27e) = "iJKAu"
// _0x22a162(0x10b) = "getMinutes"
// _0x22a162(0x486) = "getSeconds"
// 里面有很多方法体一样但是命名不一样的函数  简化后保留 add 和 RILLV， 替换上方 return后面代码

function add(a, b) {
    return a + b;
}

function RILLV(a, b) {
    return a + b;
}

// this["generateTimeFormat"]() 改成调整后函数 generateTimeFormat
function generateTimeFormat() {
    var date_obj = new Date();
    return add(
            add(
                add(
                    add(
                        add(
                            date_obj.getFullYear().toString(),
                            RILLV(date_obj.getMonth(), 1)
                        ),
                        date_obj.getDate()
                    ),
                    date_obj.getHours()
                ),
                date_obj.getMinutes()
            ),
            date_obj.getSeconds()
        )
}

function getCaptchaUuid() {
    var result_str = ''
        , salt = "ABCDEFGHJKMNPQRSTWXYZabcdefhijkmnprstwxyz2345678"
        , salt_length = 48;
    for (var i = 0; i < 18; i++) {
        result_str += salt['charAt'](Math["floor"](Math["random"]() * salt_length));
    }
    return RILLV(generateTimeFormat(), result_str);
}

console.log(getCaptchaUuid())
