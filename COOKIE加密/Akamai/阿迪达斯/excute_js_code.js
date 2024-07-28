// 环境检测点
_window = {
    addEventListener: true,
    XMLHttpRequest: true,
    XDomainRequest: true,
    emit: true,
    DeviceOrientationEvent: true,
    DeviceMotionEvent: true,
    TouchEvent: true,
    spawn: true,
    chrome: {
        webstore: undefined,
    },
    Buffer: true,
    PointerEvent: true,
    innerWidth: true,
    outerWidth: true,
    HTMLElement: true,
    RTCPeerConnection: true,
    webkitRTCPeerConnection: true,
    FileReader: true,

    callPhantom: false,
    ActiveXObject: false,
    mozRTCPeerConnection: false,

    opera: undefined,
    mozInnerScreenY: false,

};
_Function = {
    prototype: {
        bind: true
    }
};
_document = {
    documentMode: undefined,

};
_navigator = {
    onLine: true,
    vibrate: true,
    getBattery: true,

};
_InstallTrigger = false;
_Array = {
    prototype: {
        forEach: true,
    }
};

// 固定变量
YH = [
    148,
    380,
    446,
    996,
    487,
    343,
    723,
    343,
    388
];
LS = [
    300000,
    4095,
    1,
    9,
    0,
    2,
    4,
    5,
    10,
    14,
    16,
    18,
    8888888,
    7777777,
    8,
    3,
    1000,
    4294967296,
    999999,
    12,
    3600000,
    65535,
    65793,
    8388607,
    4282663,
    32,
    92,
    4294967295,
    4064256,
    2048,
    3540,
    100
];
AS = 388;
fW = 23;
Oh = 6;
ZL = 7;
dh = 8;
xH = 9;
mT = 10;
DT = 11;
JK = 12;
Tg = 13;
md = 0;
Ss = 0;
d3 = 28;
vG = 1000;

// 变化变量
start_time = Date.now();

// 公用方法
function mH(a, b) {
    return a > b;
}

function gr(a, b) {
    return a / b;
}

function XQ(a, b) {
    return a + b;
}

function Cr(a, b) {
    return a * b;
}

// 数组值
function array_1() {
    var CZ = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36";
    var wZ = "8106";
    var JZ = gr(start_time, 2);
    var BZ = -1;
    var tZ = -1;
    var AZ = -1;
    var VZ = -1;
    var xZ = -1;
    var MZ = -1;
    var PZ = -1;
    var HZ = -1;
    try {
        var gZ = [
            148,
            380,
            446,
            996,
            487,
            343,
            723,
            343,
            388
        ];
        HZ = 1;
    } catch (rZ) {
    }
    try {
        var LZ = [
            148,
            380,
            446,
            996,
            487,
            343,
            723,
            343,
            388
        ];
        BZ = 1440;
    } catch (TZ) {
    }
    try {
        var SZ = [
            148,
            380,
            446,
            996,
            487,
            343,
            723,
            343,
            388
        ];
        tZ = 912;
    } catch (vZ) {
    }
    try {
        var fZ = [
            148,
            380,
            446,
            996,
            487,
            343,
            723,
            343,
            388
        ];
        AZ = 1440;
    } catch (lZ) {
    }
    try {
        var WZ = [
            148,
            380,
            446,
            996,
            487,
            343,
            723,
            343,
            388
        ];
        VZ = 960;
    } catch (FZ) {
    }
    try {
        var bZ = [
            148,
            380,
            446,
            996,
            487,
            343,
            723,
            343,
            388
        ];
        xZ = 791;
    } catch (cZ) {
    }
    try {
        var IZ = [
            148,
            380,
            446,
            996,
            487,
            343,
            723,
            343,
            388
        ];
        MZ = 1440;
    } catch (ZZ) {
    }
    try {
        var dZ = [
            148,
            380,
            446,
            996,
            487,
            343,
            723,
            343,
            388
        ];
        PZ = 1440;
    } catch (mZ) {
    }
    var Ed = parseInt(gr(start_time, LS[d3]), mT);
    var Dd = Math.random();
    console.log(Dd);
    var Yd = ''.concat(Dd);
    console.log(Yd);
    var jd = parseInt(gr(Cr(vG, Dd), 2), mT);
    Yd = XQ(Yd.slice(0, DT), jd);
    console.log(Yd, Yd.length);
    var Ud = "20030107";
    var Od = "zh-CN";
    var Nd = "Gecko";
    var Cd = 5;
    var wd = 0;
    var Bd = 0;
    var Ad = 0;

    return (((((((((((((((((((((((''.concat(CZ, ',uaend,'))['concat'](
        12147, ','))['concat'](Ud, ','))['concat'](Od, ','))['concat'](Nd, ','))['concat'](Cd, ','))['concat'](wd, ','))['concat'](Bd, ','))['concat'](Ad, ','))['concat'](Ed, ','))['concat'](md, ','))['concat'](BZ, ','))['concat'](tZ, ','))['concat'](AZ, ','))['concat'](VZ, ','))['concat'](MZ, ','))['concat'](xZ, ','))['concat'](PZ, ','))['concat'](function EX() {
        var DX = [];
        DX.push(',cpen:'.concat(_window.callPhantom ? 1 : 0));
        DX.push('i1:'.concat(_window.ActiveXObject ? 1 : 0));
        DX.push('dm:'.concat(_document.documentMode ? 1 : 0));
        DX.push('cwen:'.concat(_window.chrome && _window.chrome.webstore ? 1 : 0));
        DX.push('non:'.concat(_navigator.onLine ? 1 : 0));
        DX.push('opc:'.concat(_window.opera ? 1 : 0));
        DX.push('fc:'.concat(_InstallTrigger ? 1 : 0));
        DX.push('sc:'.concat(_window.HTMLElement && mH(-1, 0) ? 1 : 0));
        DX.push('wrc:'.concat(_window.RTCPeerConnection || _window.mozRTCPeerConnection || _window.webkitRTCPeerConnection ? 1 : 0));
        DX.push('isc:'.concat(_window.mozInnerScreenY ? 1 : 0));
        DX.push('vib:'.concat(_navigator.vibrate ? 1 : 0));
        DX.push('bat:'.concat(_navigator.getBattery ? 1 : 0));
        DX.push('x11:'.concat(_Array.prototype.forEach ? 0 : 1));
        DX.push('x12:'.concat(_window.FileReader ? 1 : 0));

        return DX['join'](',');
    }(), ','))['concat'](wZ, ','))['concat'](Yd, ','))['concat'](JZ, ','))['concat'](Ss, ','))['concat'](HZ, ',loc:');
}

console.log(array_1())